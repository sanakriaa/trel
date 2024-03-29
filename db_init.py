import sqlite3

from models.user import User

def make_dicts(cursor, row):
    return dict((cursor.description[idx][0], value)
                for idx, value in enumerate(row))

  
db = sqlite3.connect('.data/db.sqlite')
db.row_factory = make_dicts

cur = db.cursor()

User.create_table(cur)


users = [
    User("Ford","zda", "ford@betelgeuse.star", "12345"),
    User("Arthur","firero", "arthur@earth.planet", "12345"),
]

for user in users:
    user.insert(cur)


db.commit()

print("The following users has been inserted into the DB"
      " (all the passwords are 12345):")

for user in users:
    # uses the magic __repr__ method
    print("\t", user)
    
print()
