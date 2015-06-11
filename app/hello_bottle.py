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

@bottle.route('/homeworks/1.2')
def homework_1_2():
    db_add = os.environ['DB_1_PORT_27017_TCP_ADDR']
    connection = pymongo.MongoClient(db_add, 27017)
    db = connection.m101
    collection = db.funnynumbers
    magic = 0
    try:
        iter = collection.find()
        for item in iter:
            if((item['value'] % 3) == 0):
                magic = magic + item['value']
    except Exception as e:
        print "Error trying to read collection:", type(e),e

    return "The answer to Homework One, Problem 2 is " + str(int(magic))

@bottle.route('/homeworks/1.3/<n>')
def homework_1_3(n):
    db_add = os.environ['DB_1_PORT_27017_TCP_ADDR']
    connection = pymongo.MongoClient(db_add, 27017)
    db = connection.m101
    collection = db.funnynumbers
    n = int(n)
    magic = 0
    try:
        iter = collection.find({},limit=1, skip=n).sort('value', direction=1)
        for item in iter:
            return str(int(item['value'])) + "\n"
    except Exception as e:
        return "HEE"
        print "Error trying to read collection:", type(e), e

bottle.debug(True)
bottle.run(host='0.0.0.0', port=8000)
