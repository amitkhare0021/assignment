from db_config import db

class Document(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    filename = db.Column(db.String(100), nullable=False)
    data = db.Column(db.LargeBinary, nullable=False)
    mimetype = db.Column(db.String(50), nullable=False)

    def __init__(self,filename, data, mimetype):
        self.filename = filename
        self.data = data
        self.mimetype = mimetype