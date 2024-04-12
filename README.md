# Destiny 2 Mod Optimizer 
An application to help provide Destiny 2 players with selecting the best mods for their subclass and current activity. With over 100 different mods and each armor having unique mods it can be a bit overwhelming. This app is designed for individuals who do not have the time to do research on which combination is the best. 

## Table of Contents
- [__pycache__] (#__pycache__)
- [static] (#static)
- [templates] (#templates)
- [.env] (#.env)
- [.gitignore] (#.gitignore)
- [app.py] (#app.py)
- [database.db] (#database.db)
- [init_db.py] (#init_db.py)
- [db_test.py] (db_test.py)
- [LICENSE] (#license)
- [schema.sql] (#schema.spl)
- [destiny2.xlsx] (#destiny2.xlsx)

## __pycache__
Standard cache file that is created when pip is installed and stores data when the pythond scripts run. This file will be listed in the gitignore.

## static
Static images of the Destiny 2 Logo is saved here along with the CSS file to format the web app for organizational purposes. The main.css is used to format the index.html file within the subfolder [templates].

Reference for the Destiny 2 Logo is below:
Destiny 2 Logo. Retrieved from https://cdn.pu.nl/article/destiny2logo.png. 

## templates 
Subfolder holds the index.html used for the web application and is linked to the main.css located in the [static] subfolder in the head section of the html. The html file is also linked to the Destiny 2 Logo in the body of the html. The body also includes the data entry section of the application. The data that the user will enter is the followlist below (for more samples of the following for marking purposes please see the destiny2.xlmx file):

1. Activity - The current game mode the user is playing. Common game modes would be Strikes, Gambit, Trials.

2. Subclass - The current class/subclass you are playing example: Solar Hunter.

3. Primary Weapon - Users can enter in the exact weapon (example Hawkmoon) or the type of weapon (example Handcannon). 

4. Primary Perks - The perks that are assigned to the Primary Weapon.

5. Secondary Weapon - Users can enter in the exact weapon (example Sunfire) or the type of weapon (example Scout Rifle). 

6. Secondary Perks - The perks that are assigned to the Secondary Weapon.

7. Heavy Weapon - Users can enter in the exact weapon (example Ghallyhorn) or the type of weapon (example sword). 

8. Heavy Perks - The perks that are assigned to the Heavy Weapon.

After the request is sent to Chatgpt, a suggestion will be returned below the data entry section for what mods the user should use for each armor slot. 

## .env
Enviroment file which has API key used to conntect the application to the Chatgpt which is not uploaded to github as it will destory the key.

## .gitignore 
To ignore the [pycache] and [.env], pycache is not important and the .env holds the API key that should not be shared.

## app.py
This is the application file that sends infomation to Chatgpt. The file imports python libraries os, sqlite3, flask and openai. 

OpenAi will pull the key used to connec to Chatgpt from the [.env] file.
App is assigned to Flask in order to run the app in flask.
The application connects to the sql database.
App pulls the data entry data with GET POST and assigns the data to the appropriate variable. In order for the message to Chatgpt to be successful, all the variables assigned with data needs to be combined into one variable "message_content" (sending each variable in the "content" does not works and gives a internal server error!). 

When all varibles are assigned to message_contents the app then creates a variable response. It connects to Chatgpt 3.5 turbo, creates a messages variable and tells Chatgpt what task needs to complete with the data that was provided by the user.

The response is then saved into a variable msg, and the app reconnects to the database and writes the data entry infomations to their following fields in the database. 

The msg variable is then stored to result which is printed back to the web app in the index.html file. 

## databade.db
[app.py] writes the data to this database file thats was entered by the used for Activity, Subclass, Primary Weapon, Primary Perks, Secondary Weapon, Secondary Perks, Heavy Weapon, and the Heavy Perks.

## init_db.py 
Imports the sqlite3 library. Connects to the [database.db] file and opens the schema.sql file, inserts the following prompts 'Test Activity', 'Test Subclass', 'Test Primary', 'Test Primary Perk','Test Seconday', 'Test Secondary Perk', 'Test Heavy', 'Test Heavy Perk' to set up the database.db file. If database.db does not exist, the line in the code connection = sqlite3.connect('database.db') will create the [datebase.db] file. This code needs to be run to set up the database, should be ran before the app is being used. 

## db_test.py
Imports the sqlite3 library. Connects to the database.db file and prints all the prompts that were assigned, closes database.db. Basically to see if the [init_db.py] file worked. 

## LICENSE
Use the MIT Licenses as Github makes you assign a licence. Anyone can use this software. 

## schema.sql
Creates the table if they do not exist for the data entry date to be saved to. 

## Destiny2.xlsx
A cheat sheet used to help marking if you are not familar with the Destiny 2 game modes, classes/subclasses, weapons. This is not a complele list but provide some examples of what each field could be. 
