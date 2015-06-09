import pymongo
import os
from bottle import route, run, template


@route('/hello/<name>')
def index(name):
    db_add = os.environ['DB_1_PORT_27017_TCP_ADDR']
    connection = pymongo.MongoClient(db_add, 27017)
    db = connection.mongo_db_developers
    name = db.names
    item = name.find_one()
    return '<b>Hello %s!</b>' % item['namem']

run(host='0.0.0.0', port=8000)
