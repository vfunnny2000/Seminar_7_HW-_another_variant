def find():
    print('Choose how to find: \n\
            1 - Name;\n\
            2 - Surname;\n\
            3 - Phone number;\n\
            4 - Comment.\n')
    a = int(input('enter your choice: '))
    if a == 1:
        contact = input('Enter name: ').title()
    if a == 2:
        contact = input('Enter surname: ').title()
    if a == 3:
        contact = input('Enter phone number: ')
    if a == 4:
        contact = input('Enter comment: ').title()

    print('We will find: ', contact)
    return contact