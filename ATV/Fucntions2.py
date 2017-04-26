def create_record(name, telephone, address):
    """Create Record"""
    record = {
        'name': name ,
        'phone': telephone,
        'address': address,
    }
    return record

user1 = create_record("vasya", "1232345456", "lviv")
user2 = create_record("Pety", "23452345", "Turka")

print(user1)
print(user2)

def give_award(medal, *persons): # велика кількість персон
    for person in persons:
        print("Frend "+ person.title()+ " have a medal" + medal)
give_award("Za Lviv", "vasya", "Pery")
give_award("za London", 'pety', 'alecander', 'valintin')


