def is_even(number_):
    return number_ & 1 == 0


running_sum = 0
prev_number = 0
curr_number = 1
while curr_number < 4e6:
    curr_number, prev_number = prev_number + curr_number, curr_number
    if is_even(curr_number):
        running_sum += curr_number

print(running_sum)
