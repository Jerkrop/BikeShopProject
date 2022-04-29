from flask import Flask, redirect, url_for
from flask import render_template
from flask import request
app = Flask(__name__)
import psycopg2

# connects to the database
def db_connect():
    conn = psycopg2.connect(
    host = 'localhost',
    database = 'FinalBike',
    )
    return conn


# connects to the mainpage
@app.route('/')
def main():
    return render_template('StorePage.html')

# connect to the end page and adds the review table for the end page
@app.route('/end')
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
    return render_template('EndPointPage.html')

# i dont even know
# def review_table():
    


# Not yet done do not tocuh or remove this
@app.route('/end',methods=['POST', 'GET'])
def end1():
    review = request.form['review']
    five = request.form['five']
    four = request.form['four']
    three = request.form['three']
    two = request.form['two']
    one = request.form['one']
    if request.form['five'] is five:
        conn = db_connect()
        cur = conn.cursor()
        cur.execute('INSERT INTO Bikerev (five_star) VALUES(%s)',(review,))
        conn.commit()
        cur.close()
        conn.close()
    elif request.form['four']is four:
        conn = db_connect()
        cur = conn.cursor()
        cur.execute('INSERT INTO Bikerev (four_star) VALUES(%s)',(review,))
        conn.commit()
        cur.close()
        conn.close()
    elif request.form['three'] is three:
        conn = db_connect()
        cur = conn.cursor()
        cur.execute('INSERT INTO Bikerev (three_star) VALUES(%s)',(review,))
        conn.commit()
        cur.close()
        conn.close()
    elif request.form['two'] is two:
        conn = db_connect()
        cur = conn.cursor()
        cur.execute('INSERT INTO Bikerev (two_star) VALUES(%s)',(review,))
        conn.commit()
        cur.close()
        conn.close()
    elif request.form['one'] is one:
        conn = db_connect()
        cur = conn.cursor()
        cur.execute('INSERT INTO Bikerev (one_star) VALUES(%s)',(review,))
        conn.commit()
        cur.close()
        conn.close()
    else:
        return render_template(main)
        
    return render_template('EndPointPage.html')




if __name__ == '__main__':
    app.run(debug=True)