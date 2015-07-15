###### Agregation
```javascript
use db;
// This is similar to the way MYSQL works with group_by clauses
// Instead Mongo will return a new object with the info
db.products.aggregate([
  {$group:
    {
      _id:"$manufacterer",
      num_products:{$sum:1}
    }
  }
]);
```

###### Aggregation Pipeline

- Collection
- $project => Reshape a document 1:1 Documents returned
- $match => Filtering step n:1 Reduce Documents returned
- $group => Aggregate step n:1 
- $sort => Sort step 1:1
- $skip => Skip step n:1
- $limit => Limit step n:1
- $unwind => Normalize step 1:n
- $out => Redirect output 1:1
- $redact => Security
- $geonear => Documents based in location

##### Compound grouping

We have to add a compound _id

```javascript
{
  _id: { // We can group by many fields...
    "manufacterer":"$manufacterer",
    "category":"$category"
  },
  num_products: {
    $sum:1
  }
}
```

Note: _id field within MongoDB can be either a scalar or a document

##### Agregation Expressions

- $sum 
- $avg
- $min
- $max
- $push => Create an array that will be filled by a condition
- $addtoset => Will create a similar array but with unique elements, hence set
- $first
- $last

##### Sum Expression
```javascript
{
  _id: { "maker":"$manufacterer"},
  sum_prices: {$sum:"$price"}
}
```

###### $group-stages
We can do double groupings in mongo.
```javascript
db.fun.aggregate([{
  $group:{
    _id:{
      a:"$a",
      b:"$b"
    }, 
    c:{$max:"$c"}
  }},
  {
  $group:
    {
      _id:"$_id.a",
      c:{$min:"$c"}}
  }]);

{ "_id" : 0, "a" : 0, "b" : 0, "c" : 21 }
{ "_id" : 1, "a" : 0, "b" : 0, "c" : 54 } //
{ "_id" : 2, "a" : 0, "b" : 1, "c" : 52 } //
{ "_id" : 3, "a" : 0, "b" : 1, "c" : 17 }
{ "_id" : 4, "a" : 1, "b" : 0, "c" : 22 } // 
{ "_id" : 5, "a" : 1, "b" : 0, "c" : 5 }
{ "_id" : 6, "a" : 1, "b" : 1, "c" : 87 }
{ "_id" : 7, "a" : 1, "b" : 1, "c" : 97 } //
```
