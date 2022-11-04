from pony import orm
from pony.orm import Database, Required, Set, Json, PrimaryKey, Optional
from pony.orm.core import db_session
import datetime

db = Database()
db.bind(provider='sqlite', filename='//data/data/ru.travelfood.simple_ui/databases/SimpleWMS', create_db=True)


class Bird(db.Entity):
    name = Required(str)
    color = Required(str)


def init():
    db.generate_mapping(create_tables=True)  
