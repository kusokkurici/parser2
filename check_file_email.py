import itertools

# def check_file(filename):
#
#     with open(filename, 'r') as file:
#         while True:
#             for line in file:
#                 parts = line.strip().split('|')
#
#                 print(parts[0])
#                 print(parts[1])
#
#
# filename = 'text_for_mail.txt'  # Замените на имя вашего файла
# check_file(filename)


def check_file(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()

    fields = []
    for line in lines:
        parts = line.strip().split('|')
        fields.append(parts)

    field_cycle = itertools.cycle(fields)

    while True:
        current_field = next(field_cycle)
        print(current_field[0])
        print(current_field[1])
        input('press enter')

filename = 'text_for_mail.txt'  # Замените на имя вашего файла
check_file(filename)
