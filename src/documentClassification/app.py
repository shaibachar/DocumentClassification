import os
from flask import Flask, redirect, url_for, request, render_template
from pymongo import MongoClient

app = Flask(__name__)

db = Db()

@app.route('/')
def statistics():
    book = db.getTradableBook()
    print(book)
    return render_template('statistics.html', book=book)

@app.route('/load', methods = ['GET', 'POST'])
def load_file():
   if request.method == 'POST':
        f = request.files['file']
        rm = ReadMarketData()

        return 'file loaded successfully'

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
