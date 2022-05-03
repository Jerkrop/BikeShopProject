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
    # if request.form is not['five'] or ['three'] or ['two'] or ['one']:
    #     four = request.form['four']
    # if request.form is not['five'] or ['four'] or ['two'] or ['one']:
    #     three = request.form['three']
    # if request.form is not['five'] or ['four'] or ['three'] or ['one']:
    #     two = request.form['two']
    # if request.form is not['five'] or ['four'] or ['three'] or ['two']:
    #     one = request.form['one']
    review = request.form['review']
    five = request.form['five' or 'four' or 'three' or 'two' or 'one']
    print(five)
    
    if five =='five':
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
        return render_template(main)
        
    return render_template('EndPointPage.html')




if __name__ == '__main__':
    app.run(debug=True)