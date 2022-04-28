from flask import Flask, redirect, url_for
from flask import render_template
from flask import request
app = Flask(__name__)
import psycopg2

def db_connect():
    conn = psycopg2.connect(
    host = 'localhost',
    database = 'FinalBike',
    )
    return conn

@app.route('/')
def main():
    return render_template('StorePage.html')


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
# @app.route('/end',methods=['POST', 'GET'])
# def end1():
#     pass



if __name__ == '__main__':
    app.run(debug=True)