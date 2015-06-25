#### Chapter 4

Pluggable Storage Engines

- Mongo now allows pluggable engines
- Is the interface between the persistent storage and the DB itself
- The storage engine is the one that directly sets the format of indexes and the data file format

###### Engines

- MMAP
- WiredTiger

###### MMAPv1

- Uses MMAP system call to allocate files and mem.
- Mongo needs a place to allocate docs
- Collection Level Locking
- Try to update in place within pagination limits if not possible we have to allocate into new location

[__100 GB VM__]

[__100 GB __] 

###### Indexes

Indexes will have a B-Tree or B+Tree structure depending on the engine.

If an index is not present within the collection the query will have to visit each document to perfomr the query.

The index must take into account multikey values.

Multikey and DotNotation

###### Index Creation Sparse

This allows creating indexes in a collection for documents that may or may not have certain fields declared. Only the documents with the indexed field will be indexed. If you issue a sort within the indexed parse field it will run a full collection scan since the database will fallback to that method.

###### Index Creation Background

In Mongo we have two index creation queues.

- Foreground
- Background

In case we are using a Foreground Indexing:

- Faster
- Blocks Writes & Reads in DB

In case we are using a Background Indexing:

- Slower
- Does not block W&R in DB

Note: If we want to index a collection without affecting its performance we can use Replcia Sets. Run the Foreground Indexing one by one and stop request to given Replica Set.

###### Explain

Explain 2.0

db.foo.find().explain() => Old

db.foo.explain():
- find
- update
- remove
- aggregate

###### Covered Queries

Sometimes queries can be covered with the indexing options Mongo offers. These type of queries are known as covered queries.

###### Geospatial Indexes

Cartesian Style
```javascript
var x = 19, y = 21;
var myDocSchema = {
  "nameOfField": [x,y]
}
ensureIndex({"nameOfField": '2d'});
// Query example
db.collection.find({nameOfField:{$near: [x,y]}});
```

###### Geospatial Spherical

Latitude and Longitude

GeoJSON => geojson.org

```javascript
db.places.ensureIndex({"nameOfField": "2dsphere"});
db.places.find({
  location:{
    $near:{
      $geometry:{
        type: "Point",
        coordinates: [lat,lng],
        $maxDistance: distance
      }
    }
  }
});
```
###### Full Text Search Index

```javascript
db.sentences.ensureIndex({"words":"text"});
```
