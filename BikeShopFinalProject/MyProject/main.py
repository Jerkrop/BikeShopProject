from flask import Flask, redirect, url_for
from flask import render_template
from flask import request
app = Flask(__name__)
import psycopg2
import random

daddy=0
# connects to the database
def db_connect():
    conn = psycopg2.connect(
    host = 'localhost',
    database = 'FinalBike',
    
    )
    return conn

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


def bike_db():
    conn = db_connect()
    cur = conn.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS Bike_Name(
                    Mountain varchar(500),
                    BMX varchar(500),
                    Road varchar(500),
                    Kids varchar(500),
                    Prebuilt varchar(500)
                    )""")
    conn.commit()
    cur.close()
    conn.close()

def Insert_Place_Rev():
    conn = db_connect()
    cur = conn.cursor()
    cur.execute('INSERT INTO Bikerev (five_star) VALUES(%s)',['This place is wonderful'] )
    conn.commit()
    cur.execute('INSERT INTO Bikerev (five_star) VALUES(%s)',['This place is unmatched'] )
    conn.commit()
    cur.execute('INSERT INTO Bikerev (five_star) VALUES(%s)',['All of these different options for the bikes is why I shop here!!'])
    conn.commit()
    cur.execute('INSERT INTO Bikerev (five_star) VALUES(%s)',['This place is totally gerb'] )
    conn.commit()
    cur.execute('INSERT INTO Bikerev (five_star) VALUES(%s)',['I finially have a bike to climb up any mountain thanks to this bike store'] )
    conn.commit()
    cur.close()
    conn.close()

def Randomize_Review():
    end()
    bike_db()
    global daddy
    run_one=0
    if daddy==0:
        if run_one ==0:
            Insert_Place_Rev()
            run_one=1
        elif run_one==1:
            pass
    else:
        pass
    conn = db_connect()
    cur = conn.cursor()
    cur.execute('SELECT Five_star FROM Bikerev')
    test = cur.fetchall()
    conn.commit()
    cur.close()
    conn.close()
    
    daddy+=1
    return test
    
@app.route('/')
def random_insertdb():
    test=Randomize_Review()
    print(test)
    b=[]
    for i in test:

        b.append(i)
        print(b)
        print(i)
    

    ran=random.choice(b)
    ran=str(ran).strip("()")
    
    return render_template('StorePage.html',ran=ran)


# connects to the mainpage
# @app.route('/') 
# def main():
#     return render_template('StorePage.html')

@app.route('/accessories')
def accessory():
    return render_template('Accessories.html')

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
    return render_template('/OverviewPage')

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
        # print(five)
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
    # if request.method == 'GET':
    #     review = request.form['review']
    #     # five = request.form['five' or 'four' or 'three' or 'two' or 'one']
    #     # conn = db_connect()
    #     # cur = conn.cursor()
    #     # cur.execute('SELECT * FROM Bikerev WHERE five_star = This place is wonderful (five_star)'(review))
    #     # cur.close()
    #     # conn.close()
        
    #     return render_template('StorePage.html')
    pass


if __name__ == '__main__':
    app.run(debug=True)