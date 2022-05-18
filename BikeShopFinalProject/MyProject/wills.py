from encodings import utf_8
import re
import psycopg2
import bcrypt
import base64
import os
from bs4 import BeautifulSoup
import requests
from flask import Flask, redirect, url_for, render_template, request

salt = bcrypt.gensalt()

daddy3 = []

activedaddy = ''

app = Flask(__name__)

def get_db_connection():
    conn = psycopg2.connect(
        host = 'localhost',
        database = 'FinalBike'
    )
    return conn

@app.route('/')
def start():
    return redirect(url_for('Register'))

@app.route('/Register')
def Register():
    conn = get_db_connection()
    cur = conn.cursor()
    pasw = bytes('password', 'utf-8')
    hashed = bcrypt.hashpw(pasw, salt)
    hashed = hashed.decode('utf-8')
    cur.execute('SELECT * FROM bicycle')
    info = cur.fetchall()
    for i in range(0,len(info) + 1):
        if i == len(info):
            cur.execute('INSERT INTO bicycle(usr, pass) VALUES(%s, %s)', ('admin',hashed))
            break
        if info[i][3] == 'admin':
            break
    conn.commit()
    cur.close()
    conn.close()
    return render_template('Register.html')

@app.route('/Register', methods=['POST'])
def registration():
    if request.method == 'POST':
        mail = request.form['mail']
        user = request.form['user']
        pasw = request.form['pasw']
        name = request.form['name']
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('SELECT * FROM bicycle;')
        info = cur.fetchall()
        if mail == '' or user == '' or pasw == '' or name == '':
            error = 'Fields can not be left empty!'
            return render_template('Register.html', error = error)
        if not re.match("^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$",pasw):
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

@app.route('/SignIn')
def SignIn():
    
    return render_template('SignIn.html')


@app.route('/SignIn', methods=['POST'])
def login():
    if request.method == 'POST':
        conn = get_db_connection()
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
                    return redirect(url_for('StorePage'))
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

@app.route('/StorePage')
def StorePage():
    return render_template('StorePage.html')

@app.route('/AdminPage')
def AdminPage():
    return render_template('AdminPage.html')

@app.route('/AdminPage', methods=['POST'])
def changes():
    if request.method == 'POST':
        global daddy3
        conn = get_db_connection()
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
                return render_template('AdminPage.html', error = error)
        else:
            error = 'Not an acceptable link'
            cur.close()
            conn.close()
            return render_template('AdminPage.html', error = error)

@app.route('/Prebuild')
def Prebuild():
    return render_template('PrebuildPage.html')

if __name__ == '__main__':
    app.run(debug = True)