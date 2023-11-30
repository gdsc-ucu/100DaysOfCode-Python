def max_min(number):
    maximum = number[0]
    minimum = number[0]

    for num in number:
        if num > maximum:
            maximum = num
        if num < minimum:
            minimum = num

    return(maximum, minimum)

print(max_min([1,2,3,4,5,6,7]))
print(max_min([-3,-1,2,4]))
print(max_min([6]))