inputfile = 'taras.txt'
outputfile = 'taras1.txt'

password_tolooffor = "len"


myfile1 = open(inputfile, mode='r', encoding='utf_8')
myfile2 = open(outputfile, mode="w", encoding='utf_8') # create file

"""for line in myfile:
    print("hello "+ line.strip())  # добаляє hello для кожної строки
    # line.strip - обріже всі пробіли"""


for num , line in enumerate(myfile1, 1): # me file , я якої цифри починати
    if password_tolooffor in line: # чи існує len в файлі то тоді вивести саме ту строку
        print("line namber "+ str(num)+ ":" + line.strip())
        myfile2.write("found world len" + line)

myfile1.close()
myfile2.close()
