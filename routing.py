from flask import Flask
from flask_pymongo import PyMongo
from flask import request
from bson.objectid import ObjectId
from flask import jsonify
import prototype
from werkzeug import secure_filename
#from prototype import *


app = Flask(__name__)
# app.config["MONGO_URI"] = "mongodb://localhost:27017/usersdb"
# mongo = PyMongo(app)


UPLOAD_FOLDER = '/bro/uploads/'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/uploadphoto', methods = ['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        #f = request.files['file']
        #print(f)
      #names = request.form['names']
      #f.save(secure_filename(UPLOAD_FOLDER + f.filename))
      #return jsonify(prices_map = prototype.getPricesMap(f.filename))
      print(request.form['name'])
      return 'hi'

# @app.route('/getFinal', methods = ['GET', 'POST'])
# def upload_file():
#    if request.method == 'POST':








<<<<<<< HEAD
@app.route('/uploadphoto', methods = ['GET', 'POST'])
def upload_file():
   if request.method == 'POST':
      f = request.files['file']
      f.save(secure_filename(f.filename))
      file_name = '/Users/nneeranjun/Desktop/broceries/'+f.filename
      map = prototype.itemPriceMapping(file_name)
      return map
""""@app.route('/getFinalCosts', methods = ['GET', 'POST'])
def upload_file():
   if request.method == 'POST':
      user_item_map = request.json"""
=======
>>>>>>> b04e1308fc4da40ba3b4c8d9347bf0f3197289fc

if __name__ == '__main__':
   app.run(debug = True)
