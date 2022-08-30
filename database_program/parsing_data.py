import decimal
import colorama


def parsing_data(input_data, data):
    result = ''
    if input_data == '1':
        print('\033[35m Your result:\033[0m')
        for tup in data:
            result += f'\033[35m {tup[0]} - average grade {tup[1]} \n\033[0m'
        return result
    elif input_data == '2':
        print('\033[35m Your result:\033[0m')
        for tup in data:
            result += f'\033[35m subject: {tup[0]}, student\'s name: {tup[1]}, grade: {tup[2]}\n\033[0m'
        return result
    elif input_data == '3':
        print('\033[35m Your result:\033[0m')
        for tup in data:
            result += f'\033[35m group: {tup[0]}, subject: {tup[1]}, average grade in group {tup[2]}\n\033[0m'
        return result
    elif input_data == '4':
        print('\033[35m Your result:\033[0m')
        for tup in data:
            result += f'\033[35m teacher\'s name: {tup[0]}, subject: {tup[1]}\n\033[0m'
        return result
    elif input_data == '5':
        print('\033[35m Your result:\033[0m')
        for tup in data:
            result += f'\033[35m student\'s name: {tup[0]}, group: {tup[1]}\n\033[0m'
        return result
    elif input_data == '6':
        print('\033[35m Your result:\033[0m')
        for tup in data:
            result += f'\033[35m student\'s name: {tup[0]}, group: {tup[1]}, subject: {tup[2]}, grade: {tup[3]}\n\033[0m'
        return result
    elif input_data == '7':
        print('\033[35m Your result:\033[0m')
        for tup in data:
            result += f'\033[35m student\'s name: {tup[0]}, group: {tup[1]}, subject: {tup[2]}, grade: {tup[3]}, date: {tup[4]}\n\033[0m'
        return result
    elif input_data == '8':
        print('\033[35m Your result:\033[0m')
        for tup in data:
            result += f'\033[35m student\'s name: {tup[0]}, subject: {tup[1]}\n\033[0m'
        return result
    elif input_data == '9':
        print('\033[35m Your result:\033[0m')
        for tup in data:
            result += f'\033[35m teacher\'s name: {tup[0]}, subject: {tup[1]}, average grade: {tup[2]}\n\033[0m'
        return result
    elif input_data == '10':
        print('\033[35m Your result:\033[0m')
        for tup in data:
            result += f'\033[35m teacher\'s name:: {tup[0]}, average grade: {tup[1]}\n\033[0m'
        return result
