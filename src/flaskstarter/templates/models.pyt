from {{project}}.ext.database import db

class Example(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    field1 = db.Column(db.String(30), unique=True, nullable=False)
    field2 = db.Column(db.String(100), nullable=False)