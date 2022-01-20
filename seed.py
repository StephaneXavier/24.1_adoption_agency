from models import Pet, db
from app import app

db.drop_all()
db.create_all()


p1 = Pet(name = 'Joe', species = 'dog', age = 12, notes = 'reliable, intelligent', photo_url ='https://images.news18.com/ibnlive/uploads/2021/08/1628056310_dogdrinking-1200x800.png?impolicy=website&width=510&height=356')
p2 = Pet(name = 'Robert', species = 'cat', age = 3, notes = 'crafty', photo_url = 'https://cdn.pixabay.com/photo/2014/11/30/14/11/cat-551554__340.jpg')
p3 = Pet(name = 'Sonny', species = 'porcupine', available = False)
p4 = Pet(name = 'Ed', species = 'dog', available = False)
p5 = Pet(name = 'Sam', species = 'cat')

db.session.add_all([p1,p2,p3,p4,p5])
db.session.commit()