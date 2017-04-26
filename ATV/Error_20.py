import sys

filename = "ADV_IT/txt/taras2.txt"
while True:
    try:
        print("inside Try")
        myfile = open(filename, mode='r', encoding='utf_8')

    except Exception:  # перехвадка помилки якщо не має такого файлу
            print("inside Except")
            print("Error Found")
            filename = input("Enter file name : ")
            print(sys.exc_info()[1])
    else:
            print("Inside Else")

            print(myfile.read())
            sys.exit()
    finally:           #завжди запускається навіть як що є помилка
            print("Inside FInally")


print("+++++++++++++++")