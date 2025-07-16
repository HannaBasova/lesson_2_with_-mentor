'''

In this little assignment you are given a string of space separated numbers, and have to return the highest and lowest number.

Examples

high_and_low("1 2 3 4 5") # return "5 1"
high_and_low("1 2 -3 4 5") # return "5 -3"
high_and_low("1 9 3 4 -5") # return "9 -5"
Notes

All numbers are valid Int32, no need to validate them.
There will always be at least one number in the input string.
Output string must be two numbers separated by a single space, and highest number is first.
'''

string = '8 3 -5 42 -1 0 0 -9 4 7 4 -4'

#перше ми прибираємо пробіли

#function which return the highest and lowest number from string of space separated numbers
def high_and_low (string:str)-> str:
    new_string = string.split() #перше ми прибираємо пробіли
    max_number = int(new_string[0])
    min_number = int(new_string[0])
    for numbers in new_string:
        int_numbers = int(numbers)
        if int_numbers < min_number:
            min_number = int_numbers
        if int_numbers > max_number:
            max_number = int_numbers
    return f'{max_number} {min_number}'

#print(high_and_low(string))

def alternativa_high_and_low (string:str)-> str:
    new_string = string.split() #убираем с списка пробелі
    int_new_string = []
    for numbers in new_string:
        int_new_string.append(int(numbers))
    max_number = max(int_new_string)
    min_number = min(int_new_string)
    return f'{max_number} {min_number}'

print(alternativa_high_and_low(string))