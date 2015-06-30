###### Agregation
```javascript
use db;
db.products.aggregate([
  {$group:
    {
      _id:"$manufacterer",
      num_products:{$sum:1}
    }
  }
]);
```

