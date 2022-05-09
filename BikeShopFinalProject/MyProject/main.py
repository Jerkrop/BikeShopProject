from flask import Flask, redirect, url_for
from flask import render_template
from flask import request
app = Flask(__name__)
import psycopg2
import random
daddy=0
daddy2=0
# connects to the database
def db_connect():
    conn = psycopg2.connect(
        host = 'localhost',
        database = 'FinalBike',
        # user = 'postgres',
        # password = 'Meegee12'
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
                    One_star varchar(500),
                    name varchar(500)
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
                    Kids varchar(500)
                    )""")
    conn.commit()
    cur.close()
    conn.close()


def prebuild_db():
    conn = db_connect()
    cur = conn.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS prebuild(
                    Mountain varchar(500),
                    BMX varchar(500),
                    Road varchar(500),
                    Kids varchar(500),
                    price varchar(500)
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
    prebuild_db()
    
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
    ran=str(ran).strip("'()',")
    return render_template('StorePage.html',ran=ran)

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

@app.route('/Overview')
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
def Register():
    return render_template('Register.html')

@app.route('/end')
def endpoint():
    return render_template('EndPointPage.html')
@app.route('/error')
def error():
    return render_template('error.html')
# connect to the end page and adds the review table for the end page







@app.route('/',methods=['POST', 'GET'])
def PreBuild_Buy():
    if request.method == 'POST':
        Road=request.form['Rfirst' or 'Rsecond' or 'Rthird' or 'Rfourth'or 'Rfifth']
        # kids=request.form['Kfirst'or 'Ksecond' or 'Kthird'or 'Kfourth'or 'Kfifth']
        # Mountain=request.form['Mfirst'or 'Msecond' or 'Mthird'or 'Mfourth' or'Mfifth']
        # b=request.form['Mfirst'or'Msecond'or 'Mthird'or'Mfourth' or 'Mfifth']
        # CREATE TABLE IF NOT EXISTS prebuild(
        #             Mountain varchar(500),
        #             BMX varchar(500),
        #             Road varchar(500),
        #             Kids varchar(500)
        #             price varchar(500)
        if Road =='Rfirst':
            conn = db_connect()
            cur = conn.cursor()
            cur.execute('INSERT INTO bike_db (Mountain,BMX,Road,kids,price) VALUES(%s,%s,%s,%s,%s)',('na','na',Road,'na',500))
            conn.commit()
            cur.close()
            conn.close()
        elif Road =='Rsecond':
            conn = db_connect()
            cur = conn.cursor()
            cur.execute('INSERT INTO bike_db (Mountain,BMX,Road,kids,price) VALUES(%s,%s,%s,%s,%s)',('na','na',Road,'na',500))
            conn.commit()
            cur.close()
            conn.close()
        # elif Road =='Rthird':
        #     pass
        # elif Road =='Rfourth':
        #     pass
        # elif Road =='Rfifth':
        #     pass
        # elif kids =='Kfirst':
        #     pass
        # elif kids =='Ksecond':
        #     pass
        # elif kids =='Kthird':
        #     pass
        # elif kids =='Kfourth':
        #     pass
        # elif kids =='Kfifth':
        #     pass
        # elif Mountain =='Mfirst':
        #     pass
        # elif Mountain =='Msecond':
        #     pass
        # elif Mountain =='Mthird':
        #     pass
        # elif Mountain =='Mfourth':
        #     pass
        # elif Mountain =='Mfifth':
        #     pass
        # elif b =='Mfirst':
        #     pass
        # elif b =='Msecond':
        #     pass
        # elif b =='Mthird':
        #     pass
        # elif b =='Mfourth':
        #     pass
        # elif b =='Mfifth':
        #     pass
        else:
            # pass
            return render_template('error.html')




    return redirect(url_for('OverviewPage'))



# Not yet done do not tocuh or remove this












@app.route('/end',methods=['POST', 'GET'])
def Review_db_Insert():
    random_insertdb()
    if request.method == 'POST':
        name = request.form['name']
        review = request.form['review']
        five = request.form['five' or 'four' or 'three' or 'two' or 'one']
        # print(five)
        # error=' '
        if review == "":
            return render_template('error.html')
        elif five =='five':
            conn = db_connect()
            cur = conn.cursor()
            cur.execute('INSERT INTO Bikerev (five_star,four_star,three_star,two_star,one_star,name) VALUES(%s,%s,%s,%s,%s,%s)',(review,'na','na','na','na',name))
            conn.commit()
            cur.close()
            conn.close()
        elif five =='four':
            conn = db_connect()
            cur = conn.cursor()
            cur.execute('INSERT INTO Bikerev (five_star,four_star,three_star,two_star,one_star,name) VALUES(%s,%s,%s,%s,%s,%s)',('na',review,'na','na','na',name))
            conn.commit()
            cur.close()
            conn.close()
        elif five=='three':
            conn = db_connect()
            cur = conn.cursor()
            cur.execute('INSERT INTO Bikerev (five_star,four_star,three_star,two_star,one_star,name) VALUES(%s,%s,%s,%s,%s,%s)',('na','na',review,'na','na',name))
            conn.commit()
            cur.close()
            conn.close()
        elif five =='two':
            conn = db_connect()
            cur = conn.cursor()
            cur.execute('INSERT INTO Bikerev (five_star,four_star,three_star,two_star,one_star,name) VALUES(%s,%s,%s,%s,%s,%s)',('na','na','na',review,'na',name))
            conn.commit()
            cur.close()
            conn.close()
        elif five =='one':

            conn = db_connect()
            cur = conn.cursor()
            cur.execute('INSERT INTO Bikerev (five_star,four_star,three_star,two_star,one_star,name) VALUES(%s,%s,%s,%s,%s,%s)',('na','na','na','na',review,name))
            conn.commit()
            cur.close()
            conn.close()
        
        else:
            # pass
            return render_template('error.html')
        global daddy2 
        daddy2 +=1

        return redirect(url_for('random_insertdb', ran = review))
















# @app.route('/',methods=['POST', 'GET'])
# def Review_Main():
#     # if request.method == 'GET':
#     #     review = request.form['review']
#     #     # five = request.form['five' or 'four' or 'three' or 'two' or 'one']
#     #     # conn = db_connect()
#     #     # cur = conn.cursor()
#     #     # cur.execute('SELECT * FROM Bikerev WHERE five_star = This place is wonderful (five_star)'(review))
#     #     # cur.close()
#     #     # conn.close()
        
#     #     return render_template('StorePage.html')
#     pass


if __name__ == '__main__':
    app.run(debug=True)