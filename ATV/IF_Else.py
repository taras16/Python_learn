
x = 0
if x == 0:
    print("yes x = 25")
else:
    print("no no no ")
print("--------------------\n----------------")

age = 12

if age <=4:
    print("you are litle")
elif age>=12 and age <19:
    print("you are teenager")

elif (age >4 ) and (age <12):
    print("you are kids ")
else:
    print("you are old")
print("___end---------------------------------- ")

cars = ['bmw','wolwo','skoda','lada']
badcars = ['tiko','tiko2','tiko3']

if  'lada' in cars:
    print("yes lads is in the list")
else:
    print("Not in  the list ")


for xxx in cars:
    if xxx in badcars:
        print(xxx + " is badcar")
    else:
        print(xxx + " in not bad car")
