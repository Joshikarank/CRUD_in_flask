from core import db

class User(db.Model):
    __tablename__="username"
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    name = db.Column(db.String(20),unique=True,nullable=True)
    place = db.Column(db.String(20),unique=True,nullable=True)
    
    @property
    def to_json(self):
        return {
            "id":self.id,
            "name":self.name,
            "place":self.place
        }