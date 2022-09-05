"""*args and **kwargs in Python
In Python, we can pass a variable number of arguments to a function using special symbols. 
There are two special symbols:

-> *args (Non Keyword Arguments)
-> **kwargs (Keyword Arguments)"""

# Using *args to pass the variable length arguments to the function

def adder(*num):
    sum = 0

    for n in num:
        sum = sum + n

    print("Sum:", sum)


adder(3, 5)
adder(4, 5, 6, 7)
adder(1, 2, 3, 5, 6)


# Using **kwargs to pass the variable keyword arguments to the function 

def intro(**data):
    print("\nData type of argument:",type(data))

    for key, value in data.items():
        print("{} is {}".format(key,value))

intro(Firstname="Pramit", Lastname="Chandra", Age=20, Phone=1234567890)
intro(Firstname="Sukhit", Lastname="Joshi", Email="skjoshi@examplemail.com", Country="India", Age=22, Phone=9543433330)