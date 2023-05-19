# "variable declaration"
#primitive
num1 = 42 #initialize int
num2 = 2.3 #init float
boolean = True #initialize bool
string = 'Hello World' # init string
#composite
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives']# list
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} # dictionary
fruit = ('blueberry', 'strawberry', 'banana')# tuple
print(type(fruit))# type check
print(pizza_toppings[1])#log statement
pizza_toppings.append('Mushrooms')#list add value
print(person['name'])#access value
person['name'] = 'George'#dictionary change value
person['eye_color'] = 'blue'#add value dictionary
print(fruit[2])#tuple access value
#conditional
if num1 > 45:
    print("It's greater")#if
else:
    print("It's lower")#else

if len(string) < 5: #if
    print("It's a short word!")
elif len(string) > 15:#else if
    print("It's a long word!")
else:#else
    print("Just right!")

for x in range(5):#for loop
    print(x)
for x in range(2,5):
    print(x)
for x in range(2,10,3):
    print(x)
x = 0
while(x < 5):
    print(x)
    x += 1

pizza_toppings.pop()
pizza_toppings.pop(1)

print(person)
person.pop('eye_color')
print(person)

for topping in pizza_toppings:
    if topping == 'Pepperoni':
        continue
    print('After 1st if statement')
    if topping == 'Olives':
        break

def print_hello_ten_times():
    for num in range(10):
        print('Hello')

print_hello_ten_times()

def print_hello_x_times(x):
    for num in range(x):
        print('Hello')

print_hello_x_times(4)

def print_hello_x_or_ten_times(x = 10):
    for num in range(x):
        print('Hello')

print_hello_x_or_ten_times()
print_hello_x_or_ten_times(4)


"""
Bonus section
"""

# print(num3)
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)