import sqlalchemy
import pymysql
import pandas as pd
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from sqlalchemy import Table
from sqlalchemy import Column, Integer, Text
import csv

from flask import Flask, jsonify, render_template
import config

app = Flask(__name__, template_folder='templates')
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://root:{config.pw}@127.0.0.1:3306/wine_db'

# reflect an existing database into a new model
Base = automap_base()
engine = create_engine(f'mysql+pymysql://root:{config.pw}@127.0.0.1:3306/wine_db')

# reflect the tables
Base.prepare(engine, reflect=True)
# matching that of the table name.
# Wine = Base.classes.wine
session = Session(engine)

class MyClass(Base):
    __table__ = Table('wine', Base.metadata,
  
    Column('browser',Text), 
    Column('Cab Sauv', Integer), 
    Column('Pinot Noir', Integer), 
    Column('Syrah', Integer),
    Column('Sangiovese', Integer), 
    Column('Merlot'),
    Column('Malbec', Integer), 
    Column('Sauv Blanc'),
    Column('Chard', Integer),
    Column('Chenin Blanc', Integer),
    Column('Reisling', Integer),
    Column('Gerwurtzraminer', Integer), 
    extend_existing=True, autoload=True, autoload_with = engine
    )


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/wine')
def wine():
    return render_template('wine.html')


@app.route("/cabsauv")
def cab():

    return render_template('cabsauv.html')

@app.route("/sauvblanc")
def sb():

    return render_template('sauvblanc.html')

@app.route("/syrah")
def syrah():
    return render_template('syrah.html')

@app.route("/merlot")
def merlot():
    return render_template('merlot.html')

@app.route("/pinonoir")
def pinonoir():
    return render_template('pinonoir.html')

@app.route("/malbec")
def malbec():
    return render_template('malbec.html')

@app.route("/chard")
def chard():
    return render_template('chard.html')

@app.route("/chenblan")
def chenblan():
    return render_template('chenblan.html')

@app.route("/reisling")
def reisling():
    return render_template('reisling.html')

@app.route("/cabsauv_data", methods= ['GET'])
def cab_data():
    cab_dict = []
    cab = session.query(MyClass.__table__)
    cabdf = pd.DataFrame(cab)
    cabfinal_df = cabdf[['browser','Cab Sauv']]
    cab_dict.append(cabfinal_df.to_dict())
    
    return jsonify(cab_dict)

@app.route("/syrah_data")
def syrah_data():
    
    syrah = session.query(MyClass.__table__).filter_by(WINE='Syrah').first()
    return jsonify(syrah)

@app.route("/merlot_data")
def merlot_data():
    
    merlot = session.query(MyClass.__table__).filter_by(WINE='Merlot').first()
    return jsonify(merlot)

@app.route("/pinotnoir_data")
def pinotnoir_data():
    
    pinotnoir = session.query(MyClass.__table__).filter_by(WINE='Pinot Noir').first()
    return jsonify(pinotnoir)

@app.route("/sauvblanc_data")
def sb_data():
    
    sauvblanc = session.query(MyClass.__table__).filter_by(WINE='Sauv Blanc').first()
    return jsonify(sauvblanc)

@app.route("/chard_data")
def chard_data():
    
    chard = session.query(MyClass.__table__).filter_by(WINE='Chard').first()
    return jsonify(chard)

@app.route("/gerwurtz_data")
def gerwurtz_data():
    
    gerwurtz = session.query(MyClass.__table__).filter_by(WINE='Chard').first()
    return jsonify(gerwurtz)

    # records = session.query(Wine).first()
    # for record in records:
    #     return jsonify(record.__dict__)
# filter_by(WINE = 'Cab Sauv').first()
    # data = session.query(Wine).filter_by(WINE = 'Cab Sauv').all()
    # wine_list = [e for e in data]
    # return jsonify(wine_list)

# @app.route('/contact', methods=['GET', 'POST'])
# def app_user():
#     if request.method == "POST":
#         details = request.form
#         firstName = details['fname']
#         lastName = details['lname']
#         email = details['email']
#         cur = mysql.connection.cursor()
#         cur.execute("INSERT INTO MyUsers(firstName, lastName, email) VALUES (%s, %s, %s)", (firstName, lastName, email))
#         mysql.connection.commit()
#         cur.close()
#         return 'success'
# #     return render_template('contact.html')

if __name__ == '__main__':
       app.run(debug=True)
