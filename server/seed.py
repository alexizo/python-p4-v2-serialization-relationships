from models import db, Zookeeper, Enclosure, Animal
from app import app

with app.app_context():
    db.drop_all()
    db.create_all()

    z1 = Zookeeper(name="Christina Hill", birthday="1961-08-19")
    z2 = Zookeeper(name="Johnny Smith", birthday="1972-09-22")

    e1 = Enclosure(environment="Savannah", open_to_visitors=True)
    e2 = Enclosure(environment="Ocean", open_to_visitors=False)

    a1 = Animal(name="Heather", species="Tiger", zookeeper=z1, enclosure=e2)
    a2 = Animal(name="Paul", species="Elephant", zookeeper=z2, enclosure=e1)
    a3 = Animal(name="Jennifer", species="Hippo", zookeeper=z2, enclosure=e1)

    db.session.add_all([z1, z2, e1, e2, a1, a2, a3])
    db.session.commit()

    print("Database seeded!")
