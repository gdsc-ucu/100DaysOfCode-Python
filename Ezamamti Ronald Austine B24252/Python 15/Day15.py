def find_max_min(numbers):
    if  not  numbers:
        return None, 
    max_value = numbers[0]
    min_value = numbers[0]

    for num in numbers:
        if num > max_value:
            max_value = num
        if num < min_value:
            min_value = num

    return max_value, min_value

numbers = [1,2,3,4,5,6,7]
max_num, min_num = find_max_min(numbers)
print("Maximum value:", max_num)
print("Minimum value:", min_num)