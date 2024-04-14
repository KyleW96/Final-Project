import os, sqlite3

from flask import Flask, redirect, render_template, request, url_for
from openai import OpenAI
client = OpenAI(
    api_key=os.environ.get(".env"),
)

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        activity_selected = request.form["Activity"]
        subclass_selected = request.form["Subclass"]
        primary_weapon = request.form["Primaryweapon"]
        primary_perks = request.form["PrimaryPerks"]
        secondary_weapon = request.form["Secondaryweapon"]
        secondary_perks = request.form["SecondaryPerks"]
        heavy_weapon = request.form["Heavyweapon"]
        heavy_perks = request.form["HeavyPerks"]
        message_content = f"Activity: {activity_selected}\n" \
                  f"Subclass: {subclass_selected}\n" \
                  f"Primary Weapon: {primary_weapon}\n" \
                  f"Primary Perks: {primary_perks}\n" \
                  f"Secondary Weapon: {secondary_weapon}\n" \
                  f"Secondary Perks: {secondary_perks}\n" \
                  f"Heavy Weapon: {heavy_weapon}\n" \
                  f"Heavy Perks: {heavy_perks}"



        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system","content": "You will receive submission from a destiny 2 player. Your job is to take all weapon stats and armor stats into conditoration and provide the best mods for the current activity the user is participating in depending on the current subclass, listing what mods should be on each armor piece in under 500 word response. Assume that all armor and weapons are masterworked."},
                {"role": "user", "content": message_content}
            ]
        )
        msg = response.choices[0].message.content
        conn = get_db_connection()
        conn.execute("INSERT INTO prompts (Activity, Subclass, Primaryweapon, PrimaryPerks, Secondaryweapon, SecondaryPerks, Heavyweapon, HeavyPerks) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                     (activity_selected, subclass_selected, primary_weapon, primary_perks, secondary_weapon, secondary_perks, heavy_weapon, heavy_perks))
        conn.commit()
        conn.close()
        return redirect(url_for("index", result=msg))

    result = request.args.get("result")
    return render_template("index.html", result=result)