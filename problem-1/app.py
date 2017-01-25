def is_multiple_of_3_or_5(number_):
    return number_ % 3 == 0 or number_ % 5 == 0


number = 1
sum = 0
while number < 1000:
    if is_multiple_of_3_or_5(number):
        print(number, 'is')
        sum += number
    number += 1


print sum