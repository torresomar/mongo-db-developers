// Write a program in the language of your choice that will remove the lowest
// homework score for each student. Since there is a single document for each
// student containing an array of scores, you will need to update the scores
// array and remove the homework.
db = connect("127.0.0.1:29017/school");
lowest_result = db.students.aggregate([
    {"$unwind":"$scores"},
    {"$match":{"scores.type":"homework"}},
    {"$group":
        {"_id":"$_id",
            "minitem":{
                "$min":"$scores.score"
            }
        }
    }]);
lowest_result.result.forEach(function(lowest){
    db.students.update(
        {"_id":lowest._id},
        {"$pull":{
            "scores":{
                "score": lowest.minitem
            }
        }}
    );
});
