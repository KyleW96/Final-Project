import sqlite3

connection = sqlite3.connect('database.db')

cur = connection.cursor()

with open('schema.sql') as f:
    script = f.read()
    cur.executescript(script)

cur.execute("INSERT INTO prompts (Activity, Subclass, Primaryweapon, PrimaryPerks, Secondaryweapon, SecondaryPerks, Heavyweapon, HeavyPerks) VALUES (?, ?, ?, ?, ?, ?, ?, ?)", ('Test Activity', 'Test Subclass', 'Test Primary', 'Test Primary Perk','Test Seconday', 'Test Secondary Perk', 'Test Heavy', 'Test Heavy Perk'))


connection.commit()
connection.close()