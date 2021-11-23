def last_digit(lst):
    number = 1
#    if lst == []:
#        return number
    for n in lst[::-1]:
        number = n ** (number if number < 4 else number % 4 + 4)
    return number % 10
