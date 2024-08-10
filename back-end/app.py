from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename
from db_config import db, migrate  
from summarize_helper import summarize_text
from models import Document 

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:Blocking@localhost/assignment'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

db.init_app(app)
migrate.init_app(app, db)


ALLOWED_EXTENTIONS = {'txt', 'pdf','docx'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENTIONS

@app.route('/upload', methods=['POST'])
@cross_origin()
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    file = request.files['file']

    if file.filename =='':
        return jsonify({'error':'No selected file'}), 400
    

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file_data = file.read()
        mimetype = file.content_type

        new_document = Document(filename=filename, data=file_data, mimetype=mimetype)
        db.session.add(new_document)
        db.session.commit()

        return jsonify({'id': new_document.id}), 201
    
    return jsonify({'error': 'File type not allowed'}), 400

@app.route('/summarize', methods=['POST'])
@cross_origin()
def summarize_file():
    data = request.get_json()
    print(data)
    if not data:
        return jsonify({'error': 'Invalid JSON'}), 400

    doc_id = data.get('id')
    if not doc_id:
        return jsonify({'error': 'No Document Id Provided'}), 400

    document = Document.query.get(doc_id)
    if not document:
        return jsonify({'error': 'Document not Found'}), 404
    
    try:
        summary = summarize_text(document.data.decode('utf-8'))
        return jsonify({'id':doc_id, 'summary':summary}), 200
    except Exception as e:
        return jsonify({'error':'Error occurred while summarizing document'}), 500
    



if __name__ == '__main__':
    app.run(debug=True)