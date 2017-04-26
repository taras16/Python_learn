

#         item
#       key     value

enemy = {'taras': 5 ,
        'taras2':50,
        'health': 2,
        'color':4,
        'name': 'taras'
         }
print(enemy)

print("location x =" + str(enemy['taras']))
print("location y =" + str(enemy['health']))
print("his name is " +  enemy['name'])

enemy['name'] = 'admiral'
print(enemy)

del enemy['taras']
print(enemy)

enemy['taras2'] = enemy ['taras2']+ 40
enemy['health']=  enemy['health'] -20
if enemy ['health'] < 90:
    enemy['color'] = 'yellow'
print(enemy)

print(enemy.keys())
print(enemy.values())
