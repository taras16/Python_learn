enemy = {'taras': 5 ,
        'taras2':50,
        'health': 2,
        'color':4,
        'name': 'taras',
         'awards':['image.jpg', 'image2.jpg']
         }

all_enemies=[]




for x in range(0,10):
    all_enemies.append(enemy.copy())
for enem in all_enemies:
    print(enem)

all_enemies[5]["color"]= 20
print(all_enemies)