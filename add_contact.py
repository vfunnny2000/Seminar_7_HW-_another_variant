def add_contact():
    contact = []
    name = input('Enter name: ')
    contact.append(name.title())
    surname = input('Enter surname/lastname : ')
    contact.append(surname.title())
    phone_number = input('Enter phone number: ')
    contact.append(phone_number)
    any_info = input('Your comment: ')
    contact.append(any_info.title())
    print('Contact has been added: ', contact)
    return contact
