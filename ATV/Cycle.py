cars = ['bmw','wolwo','skoda','lada']

for car in cars:
    print(car.upper())
for car in range(1,6):
    print(car)

mynamber_list = list(range(0,10))
print(mynamber_list)
print("=====================================")

for car in mynamber_list:
    car = car * 2
    print(car)

c = mynamber_list.sort(reverse=True)
print(mynamber_list)

print("max number is : " + str(max(mynamber_list)))
print("min number is : " + str(min(mynamber_list)))
print("sum of list is : " + str(sum(mynamber_list)))

print("=====================================")


mycars = cars [1:3]
print(mycars)
mycars = cars[:3]
print(mycars)