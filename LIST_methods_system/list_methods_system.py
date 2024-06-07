def display_menu():
    print("\nChoose a list operation:")
    print("1. Append")
    print("2. Extend")
    print("3. Insert")
    print("4. Remove")
    print("5. Pop")
    print("6. Clear")
    print("7. Index")
    print("8. Count")
    print("9. Sort")
    print("10. Reverse")
    print("11. Copy")
    print("12. Exit")



def handle_append(lst):
    """
    The append method is used to add item/s to the end of the list.
    """
    print()
    object_to_append = input('Please enter what you want to append to the list: ')
    lst.append(object_to_append)
    return lst


def handle_extend(lst):
    """
    The extend() method is used to add item/s from an iterable to the end of the list.
    """
    print()
    object_to_extend = input('Please enter with what you want to extend the list with(comma-separated): ')

    # strips to remove a whitespace after the comma
    stripped_object = []
    for item in object_to_extend.split(','):
        stripped_object.append(item.strip())

    lst.extend(stripped_object)

    return lst


def handle_insert(lst):

    help_method = 'Use the insert() method to add the value at the specified index'
    print()
    object_to_insert = input('Please enter the object to insert :')
    index = input('Index to insert at: ')

    lst.insert(int(index), object_to_insert)
    return lst


def handle_remove(lst):

    help_method = 'remove method removes the first occurrence of the given value'
    print()
    object_to_remove = input('Please enter the object you want to remove the first occurrence of: ')

    try:
        lst.remove(object_to_remove)
        return lst
    except ValueError:
        print(f'{object_to_remove} not found in the list')
        return lst


def handle_pop(lst):

    help_method = 'Use the pop() method to remove the item at the specified index or the last item if no index is provided'

    index_to_remove_item_from = input('Please specify index to pop or leave blank for last object: ')

    if index_to_remove_item_from == '':
        lst.pop()
        return lst

    try:
        lst.pop(int(index_to_remove_item_from))

    except ValueError:
        print(f'UNSUCCESSFUL! You should choose an index from 0 to {len(lst)-1} or leave blank for last object.')

    return lst

def handle_clear(lst):

    help_method = 'Use the clear() method to remove all items from the list'

    confirm = input('Are you sure you want to clear the list?(type "YES" to confirm): ')

    if confirm == 'YES':
        lst.clear()
        return lst
    else:
        print('Clearing the list aborted.')
    return lst


def handle_index(lst):

    help_method = 'Use the index() method to find the index of a given object'

    value_to_search = input('Please enter a value to search the index of: ')

    try:
        print()
        print(f'{value_to_search} can be found at index {lst.index(value_to_search)}.')
    except ValueError:
        print()
        print(f'{value_to_search} not found in the list.')

    return lst


def handle_count(lst):

    help_method = 'counts how many times the given object appears in the list'

    object_to_search_for = input('Please input the object to count the occurrence of: ')

    print(f'{object_to_search_for} can be found {lst.count(object_to_search_for)} times in the list')

    return lst


def handle_sort(lst):

    help_method = 'The sort() method sorts the list in ascending order'

    lst.sort()
    print()
    print(f'Sorting the list...')

    return lst


def handle_reverse(lst):

    help_method = 'reverse creates a reverse object of the give one'

    print(f'Reversing the list...')

    return lst


def handle_copy(lst):

    help_method = 'copy returns a shallow copy of the list'

    print(f'This is a shallow copy of the current state of the list: {lst.copy()}')

    return lst


def main():

    initial_values = input("Enter initial list values (comma-separated): ")
    lst = initial_values.split(',')

    while True:
        print()
        print(f'The current state of the list is: {lst}')
        display_menu()
        choice = input("Enter your choice (1-12): ")
        if choice == '1':
            handle_append(lst)
        elif choice == '2':
            handle_extend(lst)
        elif choice == '3':
            handle_insert(lst)
        elif choice == '4':
            handle_remove(lst)
        elif choice == '5':
            handle_pop(lst)
        elif choice == '6':
            handle_clear(lst)
        elif choice == '7':
            handle_index(lst)
        elif choice == '8':
            handle_count(lst)
        elif choice == '9':
            handle_sort(lst)
        elif choice == '10':
            handle_reverse(lst)
        elif choice == '11':
            handle_copy(lst)
        elif choice == '12':
            print("Exiting the application.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
