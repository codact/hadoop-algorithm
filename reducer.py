'''Reducer'''
import sys

# define initial values
digit = None
digit_to_count = {}


# loop through all the digits in the input
for i in sys.stdin:
    i = i.split('\t', 1)
    for digit in i:
        digit, count = digit.strip(), 1
        try:
            count = int(count)
        except ValueError:
            continue
        # hadoop map reducing
        try:
            digit_to_count[digit] = digit_to_count[digit]+count
        except BaseException:
            digit_to_count[digit] = count
for digit in digit_to_count.keys():
    # decrement the values of 1 acting as count values to get the actual count of 1
    if digit == '1':
        digit_to_count[digit] = digit_to_count[digit]-1002
    # print the reduced values
    print(f'{digit,digit_to_count[digit]}')


# maximum digit value
print(f'Maximum digit value {max(item for item in digit_to_count.values())}')

# minimum digit value
print(f'Minimum digit value {min(item for item in digit_to_count.values())}')


'''Calculation of the mean of all the values counted in the reducer'''
count = 0
_sum = 0
for key in digit_to_count:
    count += 1
    _sum += digit_to_count[key]

print('The mean is: ', _sum/count)
