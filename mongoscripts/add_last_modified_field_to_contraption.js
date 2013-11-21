/**
 * Created by teo on 11/21/13.
 */
    /*
    "last_modified": ISODate("2013-11-11T14:09:56.925Z"),
     */
conn = new Mongo();
db = conn.getDB("linksdb");

db.contraption.update(
    {},
    {
        $set : {
            "last_modified":ISODate("2013-11-11T14:09:56.925Z")
        }
    },
    {
        upsert:false, multi:true
    }
);