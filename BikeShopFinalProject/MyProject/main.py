from flask import Flask, redirect, url_for
from flask import render_template
from flask import request
app = Flask(__name__)
import psycopg2
import random
import bcrypt
import re
from bs4 import BeautifulSoup

daddy=0

daddy2=0

daddy3 = []

activeuser = ''

salt = bcrypt.gensalt()

# connects to the database
def db_connect():
    conn = psycopg2.connect(## change this depending on OS/database name
        host = 'localhost',
        database = 'bicycle',
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
                    Name varchar(500),
                    price varchar(500),
                    usr varchar(500)
                    )""")
    conn.commit()
    cur.close()
    conn.close()

def custom_bike_db():
    conn = db_connect()
    cur = conn.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS CustomBike(
                    item varchar(500),
                    price varchar(500),
                    usr varchar(500)
                    )""")
    conn.commit()
    cur.close()
    conn.close()

def bicycle():
    conn = db_connect()
    cur = conn.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS bicycle (
                    id bigserial,
                    name varchar(255),
                    email varchar(255),
                    usr varchar(255),
                    pass varchar(255)
                    )""")
    conn.commit()
    cur.close()
    conn.close()

def accessories_db():
    conn = db_connect()
    cur = conn.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS accessories_db (
                    item varchar(255),
                    price varchar(255),
                    usr varchar(255),
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



# functiopn to work on after pull from cart is functional
def Cart_Counter():
    counter=0
    cart=('pass')
    for items in cart:
        counter+=1

def logout():
    global activeuser
    activeuser = ''
    return render_template('StorePage.html',activeuser=activeuser)

def cart1():
    global activeuser
    conn = db_connect()
    cur = conn.cursor()
    cur.execute('SELECT * FROM prebuild where usr = %s',[activeuser])
    test2=cur.fetchall()
    print(test2)
    conn.commit()
    cur.close()
    conn.close()
    return test2

def cart2():
    global activeuser
    conn = db_connect()
    cur = conn.cursor()
    cur.execute('SELECT * FROM CustomBike where usr = %s',[activeuser])
    test3=cur.fetchall()
    print(test3)
    conn.commit()
    cur.close()
    conn.close()
    return test3






def Randomize_Review():
    end()
    bike_db()
    prebuild_db()
    custom_bike_db()
    bicycle()
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
    global activeuser
    test=Randomize_Review()
    print(test)
    b=[]
    for i in test:
        b.append(i)
        print(b)
        print(i)
    ran=random.choice(b)
    ran=str(ran).strip("'()',")
    return render_template('StorePage.html',ran=ran,activeuser=activeuser)

@app.route('/AdminPage')
def AdminPage():
    return render_template('AdminPage.html',activeuser=activeuser)

@app.route('/accessories')
def accessories():
    global activeuser
    return render_template('AccessoryPage.html',activeuser=activeuser)

@app.route('/BMXbikes')
def BMXbikes():
    global activeuser
    return render_template('BMXbikes.html',activeuser=activeuser)

@app.route('/CustomizationBikePage')
def customization_bike():
    global activeuser
    return render_template('CustomizationBikePage.html',activeuser=activeuser)
    
@app.route('/KidsBikes')
def KidsBikes():
    global activeuser
    return render_template('KidsBikes.html',activeuser=activeuser)

@app.route('/MountainBikes')
def MountainBikes():
    global activeuser
    return render_template('MountainBikes.html',activeuser=activeuser)

@app.route('/Overview')
def OverviewPage():
    global activeuser
    test3=cart1()
    test4=cart2()
    parts = []
    prices = []
    sums = []
    for i in range(0, len(test3)):
        parts.append(test3[i][0])
        prices.append(test3[i][1])
    for i in range(0, len(test4)):
        parts.append(test4[i][0])
        prices.append(test4[i][1])
    for b in prices:
        sums.append(int(b))
    sums = sum(sums)


    return render_template('/OverviewPage.html',sums=sums,parts=parts,prices=prices,activeuser=activeuser)

    
@app.route('/PaymentPage')
def PaymentPage():
    global activeuser
    return render_template('PaymentPage.html',activeuser=activeuser)

@app.route('/Prebuild')
def Prebuild():
    global activeuser
    return render_template('PrebuildPage.html',activeuser=activeuser)

@app.route('/RoadBikes')
def RoadBikes():
    global activeuser
    return render_template('RoadBikes.html',activeuser=activeuser)

@app.route('/SignIn')
def SignIn():
    global activeuser
    activeuser = ''
    conn = db_connect()
    cur = conn.cursor()
    pasw = bytes('password', 'utf-8')
    hashed = bcrypt.hashpw(pasw, salt)
    hashed = hashed.decode('utf-8')
    cur.execute('TRUNCATE TABLE custombike')
    conn.commit()
    cur.execute('TRUNCATE TABLE prebuild')
    conn.commit()
    cur.execute('SELECT * FROM bicycle')
    info = cur.fetchall()
    for i in range(0,len(info) + 1):
        if i == len(info):
            cur.execute('INSERT INTO bicycle(name, pass) VALUES(%s, %s)', ('admin',hashed))
            break
        if info[i][3] == 'admin':
            break
    conn.commit()
    cur.close()
    conn.close()
    return render_template('Signin.html')

@app.route('/description')
def description():
    global activeuser
    return render_template('description.html',activeuser=activeuser)

@app.route('/Register')## base route for register and adds an admin login
def Register():
    return render_template('Register.html',activeuser=activeuser)

@app.route('/end')
def endpoint():
    global activeuser
    conn = db_connect()
    cur = conn.cursor()
    cur.execute('TRUNCATE TABLE custombike')
    conn.commit()
    cur.execute('TRUNCATE TABLE prebuild')
    conn.commit()
    cur.close()
    conn.close()
    return render_template('EndPointPage.html',activeuser=activeuser)

@app.route('/error')
def error():
    return render_template('error.html')
# connect to the end page and adds the review table for the end page

@app.route('/SignIn', methods=['POST'])
def login():
    if request.method == 'POST':
        conn = db_connect()
        cur = conn.cursor()
        cur.execute('SELECT * FROM bicycle')
        info = cur.fetchall()
        user = request.form['user']
        pasw = request.form['pasw']
        for i in range(0,len(info)):
            if info[i][3] == user:
                password = info[i][4] 
                password = bytes(password, 'utf-8')
                pasw = bytes(pasw, 'utf-8')
                if bcrypt.checkpw(pasw, password):
                    if user == 'admin':
                        cur.close()
                        conn.close()
                        return redirect(url_for('AdminPage'))
                    global activeuser
                    activeuser = info[i][1]
                    cur.close()
                    conn.close()
                    print('here')
                    return redirect(url_for('random_insertdb'))
                else:
                    error = "WRONG USERNAME OF PASSWORD"
                    cur.close()
                    conn.close()
                    print('here')
                    return render_template('SignIn.html', error = error)
        error = "WRONG USERNAME OF PASSWORD"
        cur.close()
        conn.close()
        return render_template('SignIn.html', error = error)

@app.route('/Register', methods=['POST'])
def registration():
    if request.method == 'POST':
        mail = request.form['mail']
        user = request.form['user']
        pasw = request.form['pasw']
        name = request.form['name']
        conn = db_connect()
        cur = conn.cursor()
        cur.execute('SELECT * FROM bicycle;')
        info = cur.fetchall()
        if mail == '' or user == '' or pasw == '' or name == '':
            error = 'Fields can not be left empty!'
            return render_template('Register.html', error = error)
        if not re.match("^(?=.{7,}$)(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*\W).*$",pasw):
            error = 'The password is not strong enough!'
            return render_template('Register.html', error = error)
        for i in range(0,len(info)):
            if info[i][3] == user:
                error = 'User already exists, try to login instead!'
                return render_template('Register.html', error = error)
        pasw = bytes(pasw, 'utf-8')
        hashed = bcrypt.hashpw(pasw, salt)
        hashed = hashed.decode('utf-8')
        print(hashed)
        cur.execute('INSERT INTO bicycle(name, email, usr, pass) VALUES(%s, %s, %s, %s)', (name,mail,user,hashed))
        global activedaddy
        activedaddy = name
        conn.commit()
        cur.close()
        conn.close()
        return redirect(url_for('SignIn'))


@app.route('/Prebuild',methods=['POST', 'GET'])
def PreBuild_Buy():
    global activeuser
    if request.method == 'POST':
        global activeuser
        # bikes=request.form['Road' or 'kids' or 'Mountain' or 'b'or 'Road1' or'Road2'or 'Road3' or 'Road4' ]
        bikes = request.form.to_dict()
        bikes = bikes.values()
        bikes = list(bikes)
        bikes = bikes[0]
        # kids=request.form['kids']
        # Mountain=request.form['Mountain']
        # b=request.form['b']
        if activeuser =='':
            error =  'need to be logged in'
            return render_template('PrebuildPage.html',error=error)
        else:
            if bikes =='Rfirst':
                conn = db_connect()
                cur = conn.cursor()
                desc = 'placeholder1'
                cur.execute('INSERT INTO prebuild (Name,price,usr) VALUES(%s,%s,%s)',('Road bike1',500,activeuser))
                conn.commit()
                cur.close()
                conn.close()
            elif bikes =='Rsecond':
                conn = db_connect() 
                cur = conn.cursor()
                desc = 'placeholder2'
                cur.execute('INSERT INTO prebuild (Name,price,usr) VALUES(%s,%s,%s)',('Road bike2',550,activeuser))
                conn.commit()
                cur.close()
                conn.close()
            elif bikes =='Rthird':
                conn = db_connect()
                cur = conn.cursor()
                desc = 'placeholder3'
                cur.execute('INSERT INTO prebuild (Name,price,usr) VALUES(%s,%s,%s)',('Road bike3',600,activeuser))
                conn.commit()
                cur.close()
                conn.close()
            elif bikes =='Rfourth':
                conn = db_connect()
                cur = conn.cursor()
                desc = 'placeholder4'
                cur.execute('INSERT INTO prebuild (Name,price,usr) VALUES(%s,%s,%s)',('Road bike4',650,activeuser))
                conn.commit()
                cur.close()
                conn.close()
            elif bikes =='Rfifth':
                conn = db_connect()
                cur = conn.cursor()
                desc = 'placeholder5'
                cur.execute('INSERT INTO prebuild (Name,price,usr) VALUES(%s,%s,%s)',('Road bike5',700,activeuser))
                conn.commit()
                cur.close()
                conn.close()
            elif bikes =='Kfirst':
                conn = db_connect()
                cur = conn.cursor()
                desc = 'placeholder6'
                cur.execute('INSERT INTO prebuild (Name,price,usr) VALUES(%s,%s,%s)',('kids bike1',500,activeuser))
                conn.commit()
                cur.close()
                conn.close()
            elif bikes =='Ksecond':
                conn = db_connect()
                cur = conn.cursor()
                desc = 'placeholder7'
                cur.execute('INSERT INTO prebuild (Name,price,usr) VALUES(%s,%s,%s)',('kids bike2',550,activeuser))
                conn.commit()
                cur.close()
                conn.close()
            elif bikes =='Kthird':
                conn = db_connect()
                cur = conn.cursor()
                desc = 'placeholder8'
                cur.execute('INSERT INTO prebuild (Name,price,usr) VALUES(%s,%s,%s)',('kids bike3',600,activeuser))
                conn.commit()
                cur.close()
                conn.close()
            elif bikes =='Kfourth':
                conn = db_connect()
                cur = conn.cursor()
                desc = 'placeholder9'
                cur.execute('INSERT INTO prebuild (Name,price,usr) VALUES(%s,%s,%s)',('kids bike4',650,activeuser))
                conn.commit()
                cur.close()
                conn.close()
            elif bikes =='Kfifth':
                conn = db_connect()
                cur = conn.cursor()
                desc = 'placeholder10'
                cur.execute('INSERT INTO prebuild (Name,price,usr) VALUES(%s,%s,%s)',('kids bike5',700,activeuser))
                conn.commit()
                cur.close()
                conn.close()
            elif bikes =='Mfirst':
                conn = db_connect()
                cur = conn.cursor()
                desc = 'placeholder11'
                cur.execute('INSERT INTO prebuild (Name,price,usr) VALUES(%s,%s,%s)',('Mountain Bike1',500,activeuser))
                conn.commit()
                cur.close()
                conn.close()
            elif bikes =='Msecond':
                conn = db_connect()
                cur = conn.cursor()
                desc = 'placeholder12'
                cur.execute('INSERT INTO prebuild (Name,price,usr) VALUES(%s,%s,%s)',('Mountain Bike2',550,activeuser))
                conn.commit()
                cur.close()
                conn.close()
            elif bikes =='Mthird':
                conn = db_connect()
                cur = conn.cursor()
                desc = 'placeholder13'
                cur.execute('INSERT INTO prebuild (Name,price,usr) VALUES(%s,%s,%s)',('Mountain Bike3',600,activeuser))
                conn.commit()
                cur.close()
                conn.close()
            elif bikes =='Mfourth':
                conn = db_connect()
                cur = conn.cursor()
                desc = 'placeholder14'
                cur.execute('INSERT INTO prebuild (Name,price,usr) VALUES(%s,%s,%s',('Mountain Bike4',650,activeuser))
                conn.commit()
                cur.close()
                conn.close()
            elif bikes =='Mfifth':
                conn = db_connect()
                cur = conn.cursor()
                desc = 'placeholder15'
                cur.execute('INSERT INTO prebuild (Name,price,usr) VALUES(%s,%s,%s',('Mountain Bike5',700,activeuser))
                conn.commit()
                cur.close()
                conn.close()
            elif bikes =='Bfirst':
                conn = db_connect()
                cur = conn.cursor()
                desc = 'placeholder16'
                cur.execute('INSERT INTO prebuild (Name,price,usr) VALUES(%s,%s,%s)',('BMX bike1',500,activeuser))
                conn.commit()
                cur.close()
                conn.close()
            elif bikes =='Bsecond':
                conn = db_connect()
                cur = conn.cursor()
                desc = 'placeholder17'
                cur.execute('INSERT INTO prebuild (Name,price,usr) VALUES(%s,%s,%s)',('BMX bike2',550,activeuser))
                conn.commit()
                cur.close()
                conn.close()
            elif bikes =='Bthird':
                conn = db_connect()
                cur = conn.cursor()
                desc = 'placeholder18'
                cur.execute('INSERT INTO prebuild (Name,price,usr) VALUES(%s,%s,%s)',('BMX bike3',600,activeuser))
                conn.commit()
                cur.close()
                conn.close()
            elif bikes =='Bfourth':
                conn = db_connect()
                cur = conn.cursor()
                desc = 'placeholder19'
                cur.execute('INSERT INTO prebuild (Name,price,usr) VALUES(%s,%s,%s)',('BMX bike4',650,activeuser))
                conn.commit()
                cur.close()
                conn.close()
            elif bikes =='Bfifth':
                conn = db_connect()
                cur = conn.cursor()
                desc = 'placeholder20'
                cur.execute('INSERT INTO prebuild (Name,price,usr) VALUES(%s,%s,%s)',('BMX bike5',700,activeuser))
                conn.commit()
                cur.close()
                conn.close()
            else:
                # pass
                return render_template('error.html')

        return render_template('description.html', desc=desc)


# function to pull info for cart from db
# @app.route('/Overview',methods=['POST', 'GET'])
# def insert_into_overview():
#     if request.method == 'POST':
#         bike=request.form('bike')
#         conn = db_connect()
#         cur = conn.cursor()
#         cur.execute('SELECT bike FROM prebuild')(bike)
#         bought = cur.fetchall()
#         conn.commit()
#         cur.close()
#         conn.close()
#         print('works')

    




@app.route('/end',methods=['POST', 'GET'])
def Review_db_Insert():
    random_insertdb()
    global activeuser
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

        return redirect(url_for('random_insertdb',ran = review,activeuser=activeuser))





@app.route('/KidsBikes',methods=['POST', 'GET'])
def custombike1():
    global activeuser
    
    if activeuser =='':
        error =  'need to be logged in'
        return render_template('KidsBikes.html',error=error)
    else:
        if request.method == 'POST':
            print('daddy')
            # global activeuser
            button=request.form['bike']
            bike=[{'name':'Seat1', 'price':50},{'name':'Seat2', 'price':50},{'name':'Seat3', 'price':60},{'name':'Seat4', 'price':65}
            ,{'name':'Seat5', 'price':70},{'name':'Pedal1', 'price':100},{'name':'Pedal2', 'price':150},{'name':'Pedal3', 'price':180}
            ,{'name':'Pedal4', 'price':195},{'name':'Pedal5', 'price':200},{'name':'Handlebar1', 'price':150},{'name':'Handlebar2', 'price':200},{'name':'Handlebar3', 'price':210}
            ,{'name':'Handlebar4', 'price':220},{'name':'Handlebar5', 'price':230},{'name':'Shifter1', 'price':200},{'name':'Shifter2', 'price':155},
            {'name':'Shifter3', 'price':160},{'name':'Shifter4', 'price':185},{'name':'Shifter5', 'price':300},
            {'name':'Chainring1', 'price':150},{'name':'Chainring2', 'price':155},{'name':'Chainring3', 'price':160},{'name':'Chainring4', 'price':170},{'name':'Chainring5', 'price':190},
            {'name':'Chain1', 'price':15},{'name':'Chain2', 'price':15},{'name':'Chain3', 'price':16},{'name':'Chain4', 'price':17},{'name':'Chain5', 'price':19},
            {'name':'Suspension1', 'price':15},{'name':'Suspension2', 'price':15},{'name':'Suspension3', 'price':16},{'name':'Suspension4', 'price':17},{'name':'Suspension5', 'price':19},
            {'name':'Tire1', 'price':1200},{'name':'Tire2', 'price':1500},{'name':'Tire3', 'price':16500},{'name':'Tire4', 'price':1700},{'name':'Tire5', 'price':1900},]
            for i in range(0,len(bike)):
                print(bike[i]['name'])
                print(bike[i]['price'])
                if bike[i]['name'] == button:
                    print('test')
                    value = bike[i]['price'] 
                    item=bike[i]['name']
                    conn = db_connect()
                    cur = conn.cursor()
                    cur.execute('INSERT INTO CustomBike (item,price,usr) VALUES(%s,%s,%s)',(item,value,activeuser))
                    conn.commit()
                    cur.close()
                    conn.close()
                else:
                    pass

            return redirect(url_for('KidsBikes',activeuser=activeuser))


@app.route('/MountainBikes',methods=['POST', 'GET'])
def custombike2():
    global activeuser
    
    if activeuser =='':
        error =  'need to be logged in'
        return render_template('MountainBikes.html',error=error,activeuser=activeuser)
    else:
        if request.method == 'POST':
            print('daddy')
            button=request.form['bike']
            bike=[{'name':'Seat1', 'price':50},{'name':'Seat2', 'price':50},{'name':'Seat3', 'price':60},{'name':'Seat4', 'price':65}
            ,{'name':'Seat5', 'price':70},{'name':'Pedal1', 'price':100},{'name':'Pedal2', 'price':150},{'name':'Pedal3', 'price':180}
            ,{'name':'Pedal4', 'price':195},{'name':'Pedal5', 'price':200},{'name':'Handlebar1', 'price':150},{'name':'Handlebar2', 'price':200},{'name':'Handlebar3', 'price':210}
            ,{'name':'Handlebar4', 'price':220},{'name':'Handlebar5', 'price':230},{'name':'Shifter1', 'price':200},{'name':'Shifter2', 'price':155},
            {'name':'Shifter3', 'price':160},{'name':'Shifter4', 'price':185},{'name':'Shifter5', 'price':300},
            {'name':'Chainring1', 'price':150},{'name':'Chainring2', 'price':155},{'name':'Chainring3', 'price':160},{'name':'Chainring4', 'price':170},{'name':'Chainring5', 'price':190},
            {'name':'Chain1', 'price':15},{'name':'Chain2', 'price':15},{'name':'Chain3', 'price':16},{'name':'Chain4', 'price':17},{'name':'Chain5', 'price':19},
            {'name':'Suspension1', 'price':15},{'name':'Suspension2', 'price':15},{'name':'Suspension3', 'price':16},{'name':'Suspension4', 'price':17},{'name':'Suspension5', 'price':19},
            {'name':'Tire1', 'price':1200},{'name':'Tire2', 'price':1500},{'name':'Tire3', 'price':16500},{'name':'Tire4', 'price':1700},{'name':'Tire5', 'price':1900},]
            for i in range(0,len(bike)):
                print(bike[i]['name'])
                print(bike[i]['price'])
                if bike[i]['name'] == button:
                    print('test')
                    value = bike[i]['price'] 
                    item=bike[i]['name']
                    conn = db_connect()
                    cur = conn.cursor()
                    cur.execute('INSERT INTO CustomBike (item,price,usr) VALUES(%s,%s,%s)',(item,value,activeuser))
                    conn.commit()
                    cur.close()
                    conn.close()
                else:
                    pass

                return redirect(url_for('MountainBikes',activeuser=activeuser))

@app.route('/BMXbikes',methods=['POST', 'GET'])
def custombike3():
    global activeuser
    
    if activeuser =='':
        error =  'need to be logged in'
        return render_template('BMXbikes.html',error=error,activeuser=activeuser)
    else:
        if request.method == 'POST':
            print('daddy')
            button=request.form['bike']
            bike=[{'name':'Seat1', 'price':50},{'name':'Seat2', 'price':50},{'name':'Seat3', 'price':60},{'name':'Seat4', 'price':65}
            ,{'name':'Seat5', 'price':70},{'name':'Pedal1', 'price':100},{'name':'Pedal2', 'price':150},{'name':'Pedal3', 'price':180}
            ,{'name':'Pedal4', 'price':195},{'name':'Pedal5', 'price':200},{'name':'Handlebar1', 'price':150},{'name':'Handlebar2', 'price':200},{'name':'Handlebar3', 'price':210}
            ,{'name':'Handlebar4', 'price':220},{'name':'Handlebar5', 'price':230},{'name':'Shifter1', 'price':200},{'name':'Shifter2', 'price':155},
            {'name':'Shifter3', 'price':160},{'name':'Shifter4', 'price':185},{'name':'Shifter5', 'price':300},
            {'name':'Chainring1', 'price':150},{'name':'Chainring2', 'price':155},{'name':'Chainring3', 'price':160},{'name':'Chainring4', 'price':170},{'name':'Chainring5', 'price':190},
            {'name':'Chain1', 'price':15},{'name':'Chain2', 'price':15},{'name':'Chain3', 'price':16},{'name':'Chain4', 'price':17},{'name':'Chain5', 'price':19},
            {'name':'Suspension1', 'price':15},{'name':'Suspension2', 'price':15},{'name':'Suspension3', 'price':16},{'name':'Suspension4', 'price':17},{'name':'Suspension5', 'price':19},
            {'name':'Tire1', 'price':1200},{'name':'Tire2', 'price':1500},{'name':'Tire3', 'price':16500},{'name':'Tire4', 'price':1700},{'name':'Tire5', 'price':1900},]
            for i in range(0,len(bike)):
                print(bike[i]['name'])
                print(bike[i]['price'])
                if bike[i]['name'] == button:
                    print('test')
                    value = bike[i]['price'] 
                    item=bike[i]['name']
                    conn = db_connect()
                    cur = conn.cursor()
                    cur.execute('INSERT INTO CustomBike (item,price,usr) VALUES(%s,%s,%s)',(item,value,activeuser))
                    conn.commit()
                    cur.close()
                    conn.close()
                else:
                    pass

            return redirect(url_for('BMXbikes',activeuser=activeuser))

@app.route('/RoadBikes',methods=['POST', 'GET'])
def custombike4():
    global activeuser
    
    if activeuser =='':
        error =  'need to be logged in'
        return render_template('RoadBikes.html',error=error,activeuser=activeuser)
    else:
        if request.method == 'POST':
            print('daddy')
            button=request.form['bike']
            bike=[{'name':'Seat1', 'price':50},{'name':'Seat2', 'price':50},{'name':'Seat3', 'price':60},{'name':'Seat4', 'price':65}
            ,{'name':'Seat5', 'price':70},{'name':'Pedal1', 'price':100},{'name':'Pedal2', 'price':150},{'name':'Pedal3', 'price':180}
            ,{'name':'Pedal4', 'price':195},{'name':'Pedal5', 'price':200},{'name':'Handlebar1', 'price':150},{'name':'Handlebar2', 'price':200},{'name':'Handlebar3', 'price':210}
            ,{'name':'Handlebar4', 'price':220},{'name':'Handlebar5', 'price':230},{'name':'Shifter1', 'price':200},{'name':'Shifter2', 'price':155},
            {'name':'Shifter3', 'price':160},{'name':'Shifter4', 'price':185},{'name':'Shifter5', 'price':300},
            {'name':'Chainring1', 'price':150},{'name':'Chainring2', 'price':155},{'name':'Chainring3', 'price':160},{'name':'Chainring4', 'price':170},{'name':'Chainring5', 'price':190},
            {'name':'Chain1', 'price':15},{'name':'Chain2', 'price':15},{'name':'Chain3', 'price':16},{'name':'Chain4', 'price':17},{'name':'Chain5', 'price':19},
            {'name':'Suspension1', 'price':15},{'name':'Suspension2', 'price':15},{'name':'Suspension3', 'price':16},{'name':'Suspension4', 'price':17},{'name':'Suspension5', 'price':19},
            {'name':'Tire1', 'price':1200},{'name':'Tire2', 'price':1500},{'name':'Tire3', 'price':16500},{'name':'Tire4', 'price':1700},{'name':'Tire5', 'price':1900},]
            for i in range(0,len(bike)):
                print(bike[i]['name'])
                print(bike[i]['price'])
                if bike[i]['name'] == button:
                    print('test')
                    value = bike[i]['price'] 
                    item=bike[i]['name']
                    conn = db_connect()
                    cur = conn.cursor()
                    cur.execute('INSERT INTO CustomBike (item,price,usr) VALUES(%s,%s,%s)',(item,value,activeuser))
                    conn.commit()
                    cur.close()
                    conn.close()
                else:
                    pass

            return redirect(url_for('RoadBikes',activeuser=activeuser))



@app.route('/accessories',methods=['POST', 'GET'])
def accessories_insert():
    global activeuser
    
    if activeuser =='':
        error =  'need to be logged in'
        return render_template('AccessoryPage.html',error=error,activeuser=activeuser)
    else:
        if request.method == 'POST':
            print('daddy')
            button=request.form['bike']
            bike=[{'name':'Helment1', 'price':50},{'name':'Helment2', 'price':50},{'name':'Helment3', 'price':50},
            {'name':'Helment4', 'price':50},{'name':'Helment5', 'price':50},
            {'name':'Bell1', 'price':50},{'name':'Bell2', 'price':50},{'name':'Bell3', 'price':50},
            {'name':'Bell4', 'price':50},{'name':'Bell5', 'price':50},
            {'name':'Light1', 'price':50},{'name':'Light2', 'price':50},{'name':'Light3', 'price':50},
            {'name':'Light4', 'price':50},{'name':'Light5', 'price':50},]
            for i in range(0,len(bike)):
                print(bike[i]['name'])
                print(bike[i]['price'])
                if bike[i]['name'] == button:
                    print('test')
                    value = bike[i]['price'] 
                    item=bike[i]['name']
                    conn = db_connect()
                    cur = conn.cursor()
                    cur.execute('INSERT INTO CustomBike (item,price,usr) VALUES(%s,%s,%s)',(item,value,activeuser))
                    conn.commit()
                    cur.close()
                    conn.close()
                else:
                    pass

            return redirect(url_for('accessories',activeuser=activeuser))







@app.route('/AdminPage', methods=['POST'])
def changes():
    global activeuser
    if request.method == 'POST':
        global daddy3
        conn = db_connect()
        cur = conn.cursor()
        image = request.form['image']
        descrip = request.form['desc']
        price = request.form['price']
        entry = request.form['entry']
        print(entry)
        if descrip == '' or price == '' or image == '':
            error = 'No fields can be empty'
            cur.close()
            conn.close()
            return render_template('AdminPage.html', error = error)
        elif image.endswith('jpg') == True or image.endswith('jpeg') == True or image.endswith('png') == True :
            for i in range(0, len(daddy3) + 1):
                if i == len(daddy3):
                    new_bike = {'name':descrip,'price':price}
                    daddy3.append(new_bike)
                    print(daddy3)
                    break
                if daddy3[i]['name'] == descrip:
                    daddy3[i]['price'] = price
                    break
            with open("/Users/williemdevenney/Desktop/BikeShopProject/BikeShopFinalProject/MyProject/Templates/PrebuildPage.html", 'r+') as fp:
                error = 'Changes saved'
                soup = BeautifulSoup(fp, 'html.parser')
                img = soup.find('img', {'id':entry})
                print(img)
                img['src'] = image
                desc = soup.find('p', {'id':entry})
                desc.string = descrip
                cost = soup.find('cost', {'id':entry})
                cost.string = price
                fp.truncate(0)
                fp.write(str(soup))
                return render_template('AdminPage.html', error = error,activeuser=activeuser)
        else:
            error = 'Not an acceptable link'
            cur.close()
            conn.close()
            return render_template('AdminPage.html', error = error,activeuser=activeuser)

def final_cart():
    
    pass

if __name__ == '__main__':
    app.run(debug=True)