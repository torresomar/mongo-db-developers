import pymongo
import os
import bottle

@bottle.route('/')
def home_page():
    mythings = ['apple','orange','banana','peach']
    return bottle.template('home',username="Omar Torres",things=mythings)

@bottle.route('/hello/<name>')
def index(name):
    db_add = os.environ['DB_1_PORT_27017_TCP_ADDR']
    connection = pymongo.MongoClient(db_add, 27017)
    db = connection.mongo_db_developers
    name = db.names
    item = name.find_one()
    print "!"
    return '<b>Hello hey %s!</b>' % item['name']

bottle.debug(True)
bottle.run(host='0.0.0.0', port=8000)
