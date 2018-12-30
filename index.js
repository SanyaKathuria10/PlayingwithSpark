var cassandra = require('cassandra-driver');
var client = new cassandra.Client({contactPoints: ['172.31.44.151'], keyspace: 'stackoverflowdb'});
function sendResponse(callback,result){
    callback(null, {
        statusCode: 200,
        body: result,
        headers: {
            "Access-Control-Allow-Credentials": true,
            "Access-Control-Allow-Origin": "*",
            "Content-Type": "application/json",
        },

    });
}
exports.handler = (event, context, callback) => {
    context.callbackWaitsForEmptyEventLoop = false;
    var requestBody = JSON.parse(event.body);
    console.log(requestBody);
    new Promise(function(resolve,reject){
        client.connect(function(err) {
            console.log(err);
            client.execute("SELECT * from keywords_count", function (err, result) {
                   if (!err){
                       console.log(result.rows);
                       if ( result.rows.length > 0 ) {
                           var response = {
                                statusCode: 201,
                                headers: {
                                    "Access-Control-Allow-Credentials": true,
                                    "Access-Control-Allow-Origin": "*",
                                    "Content-Type": "application/json",
                                },
                                body: JSON.stringify(result.rows)
                            };
                            resolve(result.rows);
                       } else {
                            reject("error");
                       }
                   }
               });
        });
    }).then(function(res){
        console.log("DATA", res);
        sendResponse(callback,JSON.stringify(res));
        context.done();
    }).catch((err) => {
        console.log(err);
        context.done();
    })
};
