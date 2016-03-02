## Python Flask Server
### Team 7 REST API Assign 4

### How to use Team 7's REST API

-----------------------------------------


The base url is located at http://team7restapi.appspot.com/api/robots/
No credentials are needed.  Any method can be run against any path here.
There is a notification shown on the screen if you access / or /api/ that simply tells you to redirect to /api/robots/ as that is the base of everything.
The documentation you'll want to access the resources is included as a static html file alongside this txt file.

\*\*\*IMPORTANT\*\*\*

If a test crashes the server (which IS your job, after all!) you will get a 500 error back.  
In this instance, all your changes will have been lost and the server will "restart" with the 2 robots.
Don't expect anything you have done (creation of robots, updates to robots, deletions, anything) to stay around after a 500 http response.

Also note that all paths must end in a slash (/) or you'll get back an error.  
\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*



The server is started with 2 default robots, robot 1 and robot 2.  They have some unique properties between them but aren't all that special, really.

GET requests can be made to every resource below that.  For instance, you can call GET on /api/robots/1/sensors and that will return all
of the sensors for robot with the id 1. No data needs to be passed along with any GET request.



POST can only be called on the base url of /api/robots in order to create a new robot.  The implementation will create a new robot and build a new id for it.  
JSON may or may not be passed to it.  If you decide not to pass data, curl will need to pass nothing.  It's a caveat of curl, not our implementation.
Default values will be passed in if none are or if there are any missing.  A representation of data for curl looks like this:
'{"attacker": true, "room":9, "sensors":[{"id":1}], "buildings":{"id":4}}'

The JSON representation of that robot will be returned in the response.  


PUT can be called on any resource and it will *replace* any and all data that you provide.  That is, if you point to /api/robots/1/sensors/ and pass it 
two new sensors when it already has one in place, it will only have 2 remaining when done.  This is for the idempotence of the PUT method.  You 
may call it 10000 times and still, only those two will be placed.  
Passed is in through JSON is the same form as the POST method (though PUT can be more widely used).
The response from PUT is the JSON respresentation of the resource that was just modified.  


DELETE can only delete a robot, a sensor, or all robots, depending on the path provided.  
Returned is a response with {'result':true} if successful.





### Example http requests with curl

example POST: 
curl -v  -H "Content-Type: application/json" -X POST team7restapi.appspot.com/api/robots/ --data '{"attacker": true, "room":9, "sensors":[{"id":1}], "buildings":{"id":4}}'

example PUT:
curl -v  -H "Content-Type: application/json" -X PUT localhost:8080/api/robots/2/ --data '{"attacker": true, "room":9, "sensors":[{"id":1}], "buildings":{"id":4}}
curl -v -H "Content-Type: application/json" -L -X PUT localhost:8080/api/robots/1/status/ --data '{"status":8}'

example GET:
curl -v -X GET localhost:8080/api/robots/

