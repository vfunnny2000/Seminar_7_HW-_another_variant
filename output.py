import controller

def view():
    a = int(input('View data: \n\
        1 - CSV;\n\
        2 - TXT.\n\
        Your choice:'))
    return a



# def reading_all():
#     res == output.view()
#     if res == 1:
#         with open('CSV_book.csv', 'r') as file:
#             for i in range(0, len(file)):
#                 list = line.split(';')
#                 print(line)
                
#     if res == 2:
#         with open('TXT_book.txt', 'r') as file:
#             for line in file:
#                 print(line)