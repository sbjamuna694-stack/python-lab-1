#simple function
def greet():
    print("Hello, world!")
greet()


#function with parameters
def add(a,b):
    return a+b
print(add(3,5))


#function with default arguments
def power(base, exp=2):
    return base**exp
print(power(4))  #default square
print(power(4,3))


#function returning multiple values
def stats(numbers):
    return min(numbers),max(numbers),sum(numbers)/len(numbers)
print(stats ([2,4,6,8]))


#lamda function
square=lambda x: x**2
print(square(7)) 
      

#Basic callback
def process(data,callback):
    result = data*2
    callback(result)
    def showoutput(value):
        print("processed:",value)
        process(5,showoutput)


#
    
