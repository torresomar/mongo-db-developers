import pymongo
import os
import bottle

@bottle.route('/')
def home_page():
    mythings = ['apple','orange','banana','peach']
    return bottle.template('home',username="Omar Torres",things=mythings)

@bottle.post('/favorite_fruit')
def favorite_fruit():
    fruit = bottle.request.forms.get("fruit")
    if(fruit == None or fruit == ""):
        fruit = "No fruit selected"
    bottle.response.set_cookie('fruit',fruit)
    bottle.redirect('/show_fruit')
    # return bottle.template('fruit_selection',{'fruit':fruit})

@bottle.route('/show_fruit')
def show_fruit():
    fruit = bottle.request.get_cookie("fruit")

    return bottle.template('fruit_selection',{'fruit':fruit})

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
