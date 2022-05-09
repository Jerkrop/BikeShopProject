from flask import Flask, redirect, url_for
from flask import render_template
from flask import request
app = Flask(__name__)
import psycopg2
import random

# connects to the database
def db_connect():
    conn = psycopg2.connect(
        host = 'localhost',
        database = 'FinalBike',
        user = 'postgres',
        password = 'Meegee12'
    )
    return conn

@app.route('/')
def end():
    conn = db_connect()
    cur = conn.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS Bikerev(
                    Five_star varchar(500),
                    Four_star varchar(500),
                    Three_star varchar(500),
                    Two_star varchar(500),
                    One_star varchar(500) 
                    )""")
    conn.commit()
    cur.close()
    conn.close()
    return render_template('StorePage.html')

@app.route('/')
def random_insertdb():
    conn = db_connect()
    cur = conn.cursor()
    cur.execute('INSERT INTO Bikerev VALUES(%s)',('This place is wonderful'))
    conn.commit()
    cur.close()
    conn.close()
    # conn = db_connect()
    # cur = conn.cursor()
    # cur.execute('INSERT INTO Bikerev (five_star) VALUES(%s)',('This place makes gerb look like a pimp'))
    # conn.commit()
    # cur.close()
    # conn.close()
    # conn = db_connect()
    # cur = conn.cursor()
    # cur.execute('INSERT INTO Bikerev (five_star) VALUES(%s)',('The Customer Service is amzing'))
    # conn.commit()
    # cur.close()
    # conn.close()
    return render_template('StorePage.html')


# connects to the mainpage
# @app.route('/') 
# def main():
#     return render_template('StorePage.html')

@app.route('/accessories')
def accessory():
    return render_template('AccessoryPage.html')

@app.route('/BMXbikes')
def bmx_bikes():
    return render_template('BMXbikes.html')

@app.route('/CustomizationBikePage')
def customization_bike():
    return render_template('CustomizationBikePage.html')
    
@app.route('/KidsBikes')
def kids_bike():
    return render_template('KidsBikes.html')

@app.route('/MountainBikes')
def MountainBikes():
    return render_template('/MountainBikes.html')

@app.route('/OverviewPage')
def OverviewPage():
    return render_template('/OverviewPage.html')

@app.route('/PaymentPage')
def PaymentPage():
    return render_template('PaymentPage.html')

@app.route('/Prebuild')
def Prebuild():
    return render_template('/PrebuildPage.html')

@app.route('/Roadbike')
def road_bike():
    return render_template('Roadbikes.html')
@app.route('/SignIn')
def SignIn  ():
    return render_template('Signin.html')
       
@app.route('/Register')
def Reg  ():
    return render_template('Register.html')
       

@app.route('/end')
def endpoint():
    return render_template('EndPointPage.html')
@app.route('/error')
def error():
    return render_template('error.html')
# connect to the end page and adds the review table for the end page





# Not yet done do not tocuh or remove this
@app.route('/end',methods=['POST', 'GET'])
def Review_db_Insert():
    if request.method == 'POST':
        review = request.form['review']
        five = request.form['five' or 'four' or 'three' or 'two' or 'one']
        print(five)
        # error=' '

        if review == "":
            return render_template('error.html')
        elif five =='five':
            conn = db_connect()
            cur = conn.cursor()
            cur.execute('INSERT INTO Bikerev (five_star,four_star,three_star,two_star,one_star) VALUES(%s,%s,%s,%s,%s)',(review,'na','na','na','na'))
            conn.commit()
            cur.close()
            conn.close()
        elif five =='four':
            conn = db_connect()
            cur = conn.cursor()
            cur.execute('INSERT INTO Bikerev (five_star,four_star,three_star,two_star,one_star) VALUES(%s,%s,%s,%s,%s)',('na',review,'na','na','na'))
            conn.commit()
            cur.close()
            conn.close()
        elif five=='three':
            conn = db_connect()
            cur = conn.cursor()
            cur.execute('INSERT INTO Bikerev (five_star,four_star,three_star,two_star,one_star) VALUES(%s,%s,%s,%s,%s)',('na','na',review,'na','na'))
            conn.commit()
            cur.close()
            conn.close()
        elif five =='two':
            conn = db_connect()
            cur = conn.cursor()
            cur.execute('INSERT INTO Bikerev (five_star,four_star,three_star,two_star,one_star) VALUES(%s,%s,%s,%s,%s)',('na','na','na',review,'na'))
            conn.commit()
            cur.close()
            conn.close()
        elif five =='one':

            conn = db_connect()
            cur = conn.cursor()
            cur.execute('INSERT INTO Bikerev (five_star,four_star,three_star,two_star,one_star) VALUES(%s,%s,%s,%s,%s)',('na','na','na','na',review,))
            conn.commit()
            cur.close()
            conn.close()
        
        else:
            # pass
            return render_template('error.html')
            
        return render_template('StorePage.html', review = review)

@app.route('/',methods=['POST', 'GET'])
def Review_Main():
    if request.method == 'GET':
        review = request.form['review']
        # five = request.form['five' or 'four' or 'three' or 'two' or 'one']
        conn = db_connect()
        cur = conn.cursor()
        cur.execute('SELECT * FROM Bikerev (five_star)'(review))
        cur.close()
        conn.close()
        
        return render_template('StorePage.html',review=review)


if __name__ == '__main__':
    app.run(debug=True)