### Homework Chapter 1
***
Homework 1.1
mongorestore -h localhost:[forwarded_port] [path_to_your_dump]
***
Homework 1.2
Add hw1-2.py code into a bottle route or open python console and run with normal connection (You must have pymongo installed in client)
***
Homework 1.3
Add hw1-3.py code into a bottle route.

### Homework Chapter 2
***
Homework 2.1
Download JSON from Handouts
mongoimport --host localhost:[forwarded_port] -d students -c grades < [path_to_file]

### Homework Chapter 4

Homework 4.3

```javascript
db.posts.createIndex({"date":-1});
db.posts.createIndex({"permalink":1});
db.posts.createIndex({"tags":1, "date":-1});
```

