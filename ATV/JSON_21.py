# javascript object notation

import json
filename = "/home/taras/Desktop/ADV_IT/txt/user_settint.txt"
myfile = open(filename, mode='w', encoding='utf_8') # open file


#дані пергого гравця та другого
player1= {
    'PlayerName': "Donald Trump",
    'Score': 345,
    'awards': ["OR", "NV", "NY"]


}

player2= {
    'PlayerName': "Clinton",
    'Score': 356,
    'awards': ["WI","TX", "MI"]

}

myplayers = []
myplayers.append(player1)
myplayers.append(player2)


#-------------SAVE by JSON------------- створили файл
json.dump(myplayers,myfile )  # що зберігаємо , і в який файл
myfile.close()                # close programm

# -----------------Load by JSON-------------- тепер читаємо файл
myfile = open(filename, mode="r", encoding='utf_8')
json_data = json.load(myfile)   # і звідки читати

for user in json_data:
    print("Player Name is:" + str(user['PlayerName']))# конвертуємо в строку
    print("Player Score is : " + str(user['Score']))
    print("Player Award N1 " + str(user['awards'][0]))
    print("Player Award N2 " + str(user['awards'][0]))
    print("Player Award N3 " + str(user['awards'][0]))
    print("------------------------------\n\n")# Початок з нуля
