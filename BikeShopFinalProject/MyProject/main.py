from flask import Flask, redirect, url_for
from flask import render_template
from flask import request
app = Flask(__name__)
import psycopg2


@app.route('/')
def main():
    return render_template('StorePage.html')



if __name__ == '__main__':
    app.run(debug=True)