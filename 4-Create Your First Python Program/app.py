
user_input = 'random'
data = []  # data user Will add


def show_menu():
    """
    Menu Option
    """
    print('MENU:')
    print('1. Add an item')
    print('2. Mark as Done ')
    print('3. VIew Items')
    print('4. Exit')


while user_input != '4':
    show_menu()
    user_input = input('Enter Your Choice : ')

    if user_input == '1':

        item = input('what is to be done ?')  # ask user to add item
        data.append(item)  # add item to data
        print('add item', item)

    elif user_input == '2':

        item = input('what is to be marked as done ?')

        if item in data:  # check item if in data
            data.remove(item)
            print('remove item', item)
        else:
            print('Item Dose Not Exist in the list')

    elif user_input == '3':

        print('list of to do item :')
        for item in data:
            print(item)

    elif user_input == '4':
        print('good Buy')
    else:
        print('please enter one of 1,2,3 or 4')
