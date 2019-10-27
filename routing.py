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
      #names = request.form['names']
      #
      #return jsonify(prices_map = prototype.getPricesMap(f.filename))
      #print(request.form['name'])
            f = request.files['file']
            f.save(secure_filename(UPLOAD_FOLDER + f.filename))
            prices_map = prototype.itemPriceMapping('bro_uploads_'+f.filename)
            return jsonify(prices_map)

# @app.route('/getFinal', methods = ['GET', 'POST'])
# def upload_file():
#    if request.method == 'POST':


if __name__ == '__main__':
   app.run(debug = True)
