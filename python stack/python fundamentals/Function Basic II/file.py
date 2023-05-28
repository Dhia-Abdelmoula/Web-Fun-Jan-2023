def countdown(elm):
    count = []
    for number in range (0,elm+1):
        y = elm - number
        count.append(y)
    return count
print(countdown(5))

def print_and_return(elm):
    print(elm[0])
    return elm[1]
print(print_and_return([1,2]))

def first_plus_length(elm):
    sum = elm[0]+len(elm)
    return sum
print(first_plus_length([1,2,3,4,5]))

def values_greater_than_second(elm):
    list = []
    for x in range (0, len(elm)):
        print(x)
        if elm[x] > elm[1]:
            list.append(elm[x])
        print(elm[x])
    return list
print(values_greater_than_second([5,2,3,2,1,4]))

def length_and_value(elm1,elm2):
    list = []
    for x in range (0,elm1):
        list.append(elm2)
    return list
print(length_and_value(4,7))
