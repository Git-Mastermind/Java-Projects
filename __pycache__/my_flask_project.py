from flask import Flask, render_template, request, redirect, url_for, session
import mysql.connector
app = Flask(__name__)

app.secret_key = 'supersecret'
db = mysql.connector.connect(
    host = 'localhost',
    user = 'eshanjha', 
    password = 'ILovebooks!@#123',
    database = 'enu_db'
)
cursor = db.cursor()
@app.route('/')

def home():
    return render_template("home.html")

@app.route("/apartments")

def list_apartments():
    cursor.execute('SELECT apartment_number, bedrooms, bathrooms, rent_amount FROM apartments')
    apartments = cursor.fetchall()
    return render_template("apartments.html", apartments=apartments)

if __name__ == "__main__":
    app.run(debug=True)




    