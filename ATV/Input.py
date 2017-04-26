name = input("Please enter Your name:")
print('Hello'+ name)

num1 = input("Enter X : ")
num2 = input("Enter Y:")

sum = int(num1) + int(num2)
print(sum)

# ----------------------
message = ''
while message != 'sekret':
    message = input("Enter Password")
    if message == 'sekret':
        break
    print(message +"Password not Correct")

#---------------------------------
mylist = []
mag = ''
while mag != 'stop'.upper():
    mag = input("Enter nwe item")
    mylist.append(mag)
print(mylist)