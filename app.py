from flask import Flask, render_template, request, redirect, url_for, session
import mysql.connector
app = Flask(__name__)

def hello_world():
    @app.route("/")

    def hello():
        return 'My first API!'

    if __name__ == "__main__":
        app.run(debug=True)

# hello_world()

def about_route():
    @app.route('/about')

    def about():
        return 'This is the about page! Made with flask 🐍🔥'
    
    if __name__ == '__main__':
        app.run(debug=True)

# about_route()

def flask_html_website():
    @app.route('/')

    def hello_html():
        return render_template('templates/home.html')
    
    if __name__ == '__main__':
        app.run(debug=True)

# flask_html_website()

def apartment_renter_management_flask():
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

apartment_renter_management_flask()
    



    
