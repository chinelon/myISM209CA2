from main import db


class Clients(db.Model):  # notice that our class extends db.Model
    __tablename__ = 'clientregister'  # this is the name we want the table in database to have. id=db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(20), unique=False, nullable=False)
    lastname = db.Column(db.String(20), unique=False, nullable=False)
    dateofbirth = db.Column(db.Integer, unique=False, nullable=True)
    address = db.Column(db.String(50), unique=True, nullable=False)
    nationality = db.Column(db.String(20), unique=False, nullable=False)
    nin = db.Column(db.Integer, primary_key=True)

    def __repr__(self):
        return '<Register {}>'.format(self.id)
