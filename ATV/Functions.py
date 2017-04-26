def private(name):
    print("Congratulation ," +name+  " wish you all the best ")
    print("hello , hello")

def aaaa():
    print("AAAAA")

def summa(x,y):
    print(x+y)

def summa (x,y):
    s = x +y
    return s


#------------------------
print("-------------------")
private('vova')
private('taras')
aaaa()
summa(10,20)
x = summa(33,44)
private(str(x))
#=========================
print("=========================")

# 2! = 1*2  factor 2
# 3! = 1*2*3 factor 3
# 4! = 1*2*3*4 factor 4

def factorial(x):
    """Calculate Factorial of number X """
    otvet =1
    for i in range(1,x+1):
        otvet = otvet *i
    return otvet

print(factorial(5))

for i in range(1,10):
     print(str(i) +"!\t=" + str(factorial(i)))