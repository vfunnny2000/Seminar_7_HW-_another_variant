import add_contact as ac
import find_contact as fc
import user_interface
import logger

def start():
    button = user_interface.choice()
    if button == 1:
        print('Adding new contact')
        contact = ac.add_contact()
        logger.log_to_file(contact)
        print()
    if button == 2:
        print('\nFind contact\n')
        contact = fc.find()
        logger.reading_file(contact)
        print()
    if button == 3:
        print('Lookthrough the PH')
        logger.reading_all()
        print()
    if button == 4:
        print('Finish')
        exit
        