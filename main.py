import os
import random
import traceback


class File:
    def __init__(self, filename, creation_time):
        self.name = filename
        self.creation_time = creation_time


def task_1():
    print('Task 1')
    folder_path = input('Enter the path to the folder: ')
    file_extension = input('Enter the file extension: ')

    files = []
    try:
        for file in os.listdir(folder_path):
            if file.endswith('.' + file_extension):
                needed_file = File(os.path.join(file), os.path.getctime(folder_path + file))
                files.append(needed_file)
    except FileNotFoundError:
        print('Error:\n', traceback.format_exc())
        return

    try:
        if len(files) == 1:
            print('Most recent file:', files[0].name)
        else:
            files.sort(key=lambda x: x.creation_time, reverse=True)
            most_recent_creation_time = files[0].creation_time

            recent_files_by_creation_date = []
            for file in files:
                if file.creation_time > most_recent_creation_time - 10:
                    recent_files_by_creation_date.append(file.name)

            print('A list of the most recent files with a difference of no more than 10 seconds:',
                  recent_files_by_creation_date)
    except IndexError:
        print('Error:\n', traceback.format_exc())
        return


def get_result_with_collections_via_indexes(array_1, array_2):
    array_result = []

    i = 0
    while i < len(array_1):
        exist = False
        j = 0
        while j < len(array_2):
            if array_1[i] == array_2[j]:
                exist = True
            j += 1
        if not exist:
            array_result.append(array_1[i])
        i += 1
    return array_result


def get_result_with_collections(array_1, array_2):
    array_result = list(set(array_1).difference(set(array_2)))
    return array_result


def task_2():
    print('\nTask 2')
    array_1 = ["Alex", "Dima", "Kate", "Galina", "Ivan"]
    array_2 = ["Dima", "Ivan", "Kate"]

    array_result = get_result_with_collections_via_indexes(array_1, array_2)
    print('Result with collections via indexes:', array_result)

    array_result = get_result_with_collections(array_1, array_2)
    print('Result with collections:', array_result)


def select_cases(filepath, lines_number=10):
    result_filepath = filepath[: -4] + '_res' + filepath[-4:]
    try:
        lines = open(filepath).readlines()
    except FileNotFoundError:
        print('Error:\n', traceback.format_exc())
        return

    table_header = lines[0]
    lines.pop(0)

    result_file = open(result_filepath, 'w+')
    result_file.write(table_header)
    i = 0
    while i < lines_number:
        try:
            random_line = random.randrange(len(lines))
        except ValueError:
            print('Error:\n', traceback.format_exc())
            return
        result_file.write(lines[random_line])
        lines.pop(random_line)
        i += 1
    result_file.close()

    file = open(filepath, 'w+')
    file.write(table_header)
    for line in lines:
        file.write(line)
    file.close()

    return result_filepath


def task_3():
    print('\nTask 3')
    filepath = input('Enter the path to the source file: ')
    lines_number = int(input("Enter the number of rows: "))

    resulting_file = select_cases(filepath, lines_number)
    print('Path to the resulting file:', resulting_file)


if __name__ == '__main__':
    task_1()
    task_2()
    task_3()
