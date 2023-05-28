def basic ():
    for i in range(150):
        print(i)
# basic()
def multiples_of_five ():
    for i in range(5,1000):
        if not i%5 :
            print (i)
# multiples_of_five()
def dojo_way():
    for i in range(100):
        if not i%5 :
            print ("Dojo")
        else :
            print (i)
# dojo_way()
def huge():
    x=0
    for i in range(500000):
        x+=i
    print(x)
# huge()
def countdown():
    for i in range(2018,-1,-4):
        print(i)
# countdown()
def flexible(low_num,hi_num,mult):
    hi_num+=1
    while low_num%mult :
        low_num+=1
    for i in range(low_num,hi_num,mult):
        print(i)
flexible (2,9,3)
