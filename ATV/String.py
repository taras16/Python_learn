mystring = "Bla bla bla "
name = "vasya pupkin"

print(name.title())
print(name.upper())# всі зробити з великої букви
print(name.lower())

print("He string \nPrivet string 2\n\nString 3 ")
print("Message: \n\tMessage1 \n\tmessage2 \nEnd") # \t робить таб
print("Lover name" + name.lower())
print("--------------------\n\n\n")


a = '... hello works ...'
print(a)
print(a.rstrip()) # стирає пробіл вкінці
print(a.lstrip()) # ситрає на початку

a = a.strip(".")
a = a.strip()
print(a)