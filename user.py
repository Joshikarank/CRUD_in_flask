from core import db,init_app
from flask import request
from core.models import User

app=init_app()

#intro page
@app.route('/')
def index():
    return {"message":"welcome to fundoo notes"}

#register an user
@app.post('/register')
def register():
    user = User(**request.json)
    if user: 
        db.session.add(user)
        db.session.commit()
        # user = User.query.filter_by(email=request.json['email']).first()
        return {'message':'User created successfully', 'status': 201, 'data': 'user.to_json'},201
    return {'message':'invalid in put'}


#delete an user
@app.delete('/deletes/<int:id>')
def delete_name(id):   
    try:     
        user = User.query.filter_by(id=id).first()
        if user:
            db.session.delete(user)
            db.session.commit()
            return {'message':'User deleted successfully'}
        return {'message':'user not found'}
    except Exception as e:
        print(e)
        return {'message':'error'}

#update an user
@app.put('/update_user/<int:id>')
def update_details(id):
    try:
        user = User.query.filter_by(id=id).first()
        if user:
            data = request.get_json()
            user.name = data['name']
            user.place = data['place']
            db.session.commit()
            return {'message': 'user updated'}, 200
        return {'message':'user not found'}
    except Exception as e:
        print(e)

@app.route('/upd/<int:id>' , methods =  ['PATCH','PUT'])
def updates(id):
    try:
        user = User.query.filter_by(id=id).first()
        if user:
            data = request.get_json()
            user.name = data['name']
            user.place = data['place']
            db.session.commit()
            return {'message': 'updates completed'}
        return {'message': 'id not found'}
    except Exception as e:
        print(e)