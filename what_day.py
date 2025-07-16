'''

complete the function which returns the weekday according to the input numbers

1 return Monday
2 return Tuesday
3 return Wednesday
4 return Thursday
5 return Friday
6 return Saturday
7 return Sunday
otherwise returns 'wrong, please enter the number between 1 and 7'
'''




my_dictionary = {
'1' : 'Monday',
'2' : 'Tuesday',
'3' : 'Wednesday',
'4' : 'Thursday',
'5' :'friday',
'6' : 'Saturday',
'7' : 'Sunday'
}

user_input = (input('Enter the number from 1 to 7 : '))


def weekday ():
    '''
    function which returns the weekday according to the input numbers
    :return: string
    '''
    return my_dictionary.get(user_input,"wrong, please enter the number between 1 and 7")
print(weekday())

