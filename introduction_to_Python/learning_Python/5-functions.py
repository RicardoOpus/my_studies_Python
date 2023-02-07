# FUNCTIONS

# get age:
import datetime
def age(name, birth_year):
    today = datetime.date.today()
    today_year = today.year
    return print(f'{name}, you are {today_year - birth_year } years old')
age('Ric', 2000)


# naming parameters
age(birth_year=1995, name='Ted')


# Is a multiple of 3?
def multiple(*n):
    result = []
    for input in n:
        if input == 0:
            result.append(f'{input} is NOT a multiple of 3')
        elif (input / 3).is_integer():
            result.append(f'{input} is a multiple of 3')
        else:
            result.append(f'{input} is NOT a multiple of 3')
    return print(result)
multiple(0,3,9,10)