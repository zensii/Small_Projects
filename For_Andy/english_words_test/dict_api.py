from decouple import config
import requests
from bs4 import BeautifulSoup
api_key = config('API_KEY')


def get_api_translation(word: str, lang='en') -> tuple[str, str]:

    url = f"https://api.pons.com/v1/dictionary?q={word}&l=bgen&in={lang}"
    headers = {
        'X-Secret': api_key
    }
    # Make the GET request to the API
    response = requests.get(url, headers=headers)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the response as JSON
        dictionaries = response.json()

        for dictionary in dictionaries:

            # get first translation only
            source = (dictionary['hits'][0]['roms'][0]['headword'])
            translation = (dictionary['hits'][0]['roms'][0]['arabs'][0]['translations'][0]['target'].split()[0])

            return source, translation
    else:
        return f'not_found', f'not_found'

def get_full_call(word: str, lang):
    url = f"https://api.pons.com/v1/dictionary?q={word}&l=bgen&in={lang}"
    headers = {
        'X-Secret': api_key
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:

        translations = response.json()
        for dictionary in translations:
            arabs = dictionary['hits'][0]['roms'][0]['arabs']

            for index, arab in enumerate(arabs):
                print(index + 1, ':', arab['translations'][0]['target'].split()[0])
                examples = arab['translations']

                for example in examples:
                    cleantext_source = BeautifulSoup(example['source'], "lxml").text
                    cleantext = BeautifulSoup(example['target'], "lxml").text
                    print(cleantext_source)
                    print(cleantext, '\n')





if __name__ == "__main__":
    pass