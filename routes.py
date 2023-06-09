from flask import Flask, render_template

import sqlite3  # needed to make database connections and queries


# dunder name (double underscore)
app = Flask(__name__)


# route -list
@app.route("/") #trailing slash
def home():
    return render_template("home.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/all_plants")
def all_plants():
   conn = sqlite3.connect('plants.db')
   cur = conn.cursor()
   cur.execute("SELECT * FROM plant")
   results = cur.fetchall()
   print(results)
   return render_template("all_plants.html", results = results)

@app.route('/plant/<int:id>')
def plant(id):
    conn = sqlite3.connect("plants.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM plant WHERE id = ?",(id,))
    plant = cur.fetchone()
    cur.execute("SELECT intro FROM plant WHERE id = plant[4]",(id,))
    base = cur.fetchone()
    cur.execute("SELECT name FROM plant WHERE id IN(SELECT id FROM category WHERE id = ?)",(id,))
    category = cur.fetchone()
    return render_template ("all_plants.html", plant = plant, base = base, category = category)
   

#must be at bottom
if __name__ == "__main__": # run app from file directly
    app.run(debug= True) #remove debug at end


