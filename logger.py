import controller
import csv
from re import A
import output
import find_contact
import user_interface

def log_to_file(contact):

    with open('CSV_book.csv', 'a', encoding='UTF-8') as file:
        file.write(
            f'{contact[0]}; {contact[1]}; {contact[2]}; {contact[3]};\n')

    with open('TXT_book.txt', 'a', encoding='UTF-8') as file:
        file.write(
            f'{contact[0]}\n {contact[1]}\n {contact[2]}\n {contact[3]}\n\n')


def reading_file(param):
    b = output.view()
    if b == 1:
        with open('CSV_book.csv', 'r') as file:
            for line in file:
                if param in line:
                    print(line)

    if b == 2:
        line = []
        with open('TXT_book.txt', 'r') as file:  
            for line in file:
                if param in line:
                    # file.read()
                    line = line.split('\n')
                    print(f'{line[0]}\n{line[1]}\n{line[2]}\n{line[3]}\n')
                    # print(line)
            # for line in file:
                # if param in line:
                    # file.read(f'{line[0]}\n{line[1]}\n{line[2]}\n{line[3]}\n')
                    # file.readline()
                    # print(line)
                # line = file.readline()
                # while line:
                #     print(line, end="")
                #     line = file.readline

def reading_all():
    reading_all == output.view()
    if reading_all == 1:
        with open('CSV_book.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                print(row)
            # for i in range(0, len(file)):
            #     list = line.split(';')
            #     print(line)
                
    if reading_all == 2:
        # with open('TXT_book.txt', 'r') as file:
            # data = file.readlines()
            # for data in file.splitlines():
            # print(data)
            # f = open()
            # reader = txt.reader(file)
            # for line in file:
            #     print(line)
        file = open('TXT_book.txt')  
        print( file.read())     