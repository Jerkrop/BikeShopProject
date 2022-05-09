from encodings import utf_8
import re
import psycopg2
import bcrypt
import base64
import os
from bs4 import BeautifulSoup
import requests
from flask import Flask, redirect, url_for, render_template, request

bikes = [{'name':'Bike', 'price':'5'}]
salt = bcrypt.gensalt()


app = Flask(__name__)

def get_db_connection():
    conn = psycopg2.connect(
        host = 'localhost',
        database = 'bicycle'
    )
    return conn

@app.route('/')
def start():
    return redirect(url_for('AdminPage'))

@app.route('/Register')
def Register():
    conn = get_db_connection()
    cur = conn.cursor()
    pasw = bytes('password', 'utf-8')
    hashed = bcrypt.hashpw(pasw, salt)
    hashed = hashed.decode('utf-8')
    cur.execute('INSERT INTO bicycle(name, pass) VALUES(%s, %s)', ('admin',hashed))
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
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('SELECT * FROM bicycle;')
        info = cur.fetchall()
        if mail == '' or user == '' or pasw == '':
            error = 'Fields can not be left empty!'
            return render_template('Register.html', error = error)
        if not re.match('^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$',pasw):
            error = 'The password is not strong enough!'
            return render_template('Register.html', error = error)
        for i in range(0,len(info)):
            if info[i][1] == user:
                error = 'User already exists, Try login in instead!'
                return render_template('Register.html', error = error)
        pasw = bytes(pasw, 'utf-8')
        hashed = bcrypt.hashpw(pasw, salt)
        hashed = hashed.decode('utf-8')
        print(hashed)
        cur.execute('INSERT INTO bicycle(email, name, pass) VALUES(%s, %s, %s)', (mail,user,hashed))
        conn.commit()
        cur.close()
        conn.close()
        return redirect(url_for('Signin'))

@app.route('/Signin')
def Signin():
    return render_template('Signin.html')

@app.route('/Signin', methods=['POST'])
def login():
    if request.method == 'POST':
        print('here')
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('SELECT * FROM bicycle')
        info = cur.fetchall()
        user = request.form['user']
        pasw = request.form['pasw']
        for i in range(0,len(info)):
            if info[i][2] == user:
                password = info[i][3] 
                password = bytes(password, 'utf-8')
                pasw = bytes(pasw, 'utf-8')
                print(password)
                print(pasw)
                if bcrypt.checkpw(pasw, password):
                    if user == 'admin':
                        cur.close()
                        conn.close()
                        return redirect(url_for('AdminPage'))
                    cur.close()
                    conn.close()
                    print('here')
                    return redirect(url_for('StorePage'))
                else:
                    error = "WRONG USERNAME OF PASSWORD"
                    cur.close()
                    conn.close()
                    print('here')
                    return render_template('Signin.html', error = error)
        error = "WRONG USERNAME OF PASSWORD"
        cur.close()
        conn.close()
        print('here')
        return render_template('Signin.html', error = error)

@app.route('/StorePage')
def StorePage():
    return render_template('StorePage.html')

@app.route('/AdminPage')
def AdminPage():
    return render_template('AdminPage.html')

@app.route('/AdminPage', methods=['POST'])
def changes():
    if request.method == 'POST':
        global bikes
        conn = get_db_connection()
        cur = conn.cursor()
        image = request.form['image']
        descrip = request.form['description']
        price = request.form['price']
        page = request.form['page']
        name = request.form['name']
        if descrip == '' or price == '' or image == '' or page == '' or name == '':
            error = 'No fields can be empty'
            cur.close()
            conn.close()
            return render_template('AdminPage.html', error = error)
        elif image.endswith('jpg') == True or image.endswith('jpeg') == True or image.endswith('png') == True :
            for i in range(0, len(bikes)):
                if bikes[i]['name'] == name:
                    bikes[i]['name'] = name
                    bikes[i]['price'] = price
            with open("/Users/williemdevenney/Desktop/BikeShopProject/BikeShopFinalProject/MyProject/Templates/PrebuildPage.html", 'r+') as fp:
                error = 'Changes saved'
                soup = BeautifulSoup(fp, 'html.parser')
                print(soup)
                img = soup.find('img', {'id':'image'})
                img['src'] = image
                desc = soup.find('p', {'id':'desc'})
                desc.string = descrip
                cost = soup.find('p', {'id':'cost'})
                cost.string = price
                bike = soup.find('p', {'id':'name'})
                bike.string = name
                fp.truncate(0)
                fp.write(str(soup))
                return render_template('AdminPage.html', error = error)
        else:
            error = 'Not an acceptable link'
            cur.close()
            conn.close()
            return render_template('AdminPage.html', error = error)

@app.route('/PrebuildPage')
def PrebuildPage():
    return render_template('PrebuildPage.html')

if __name__ == '__main__':
    app.run(debug = True)