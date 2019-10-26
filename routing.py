from flask import Flask
from flask_pymongo import PyMongo
from flask import request
from bson.objectid import ObjectId
from flask import jsonify
from werkzeug import secure_filename


app = Flask(__name__)
#app.config["MONGO_URI"] = "mongodb://localhost:27017/usersdb"
#mongo = PyMongo(app)


UPLOAD_FOLDER = '/example_img.png'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# @app.route('/register', methods=['POST'])
# def register():
#     json_data = request.get_json(force=True)
#     id = mongo.db.users.insert(json_data)
#     print(str(id))
#     return str(id)


# @app.route('/uploadphoto', methods=['GET', 'POST'])
# def upload_file():
#     if request.method == 'POST':
#         # check if the post request has the file part
#         if 'file' not in request.files:
#             flash('No file part')
#             return redirect(request.url)
#         file = request.files['file']
#         # if user does not select file, browser also
#         # submit an empty part without filename
#         if file.filename == '':
#             flash('No selected file')
#             return redirect(request.url)
#         if file:
#             filename = secure_filename(file.filename)
#             file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
#             return redirect(url_for('uploaded_file',
#                                     filename=filename))
#     return file


# @app.route('/upload')
# def upload_file():
#    return render_template('upload.html')

@app.route('/uploadphoto', methods = ['GET', 'POST'])
def upload_file():
   if request.method == 'POST':
      f = request.files['file']
      f.save(secure_filename(f.filename))
      return "hi"

if __name__ == '__main__':
   app.run(debug = True)
