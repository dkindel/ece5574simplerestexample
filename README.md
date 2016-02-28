## Python Flask Server
### Team 7 REST API Assign 4

example POST: 
curl -v  -H "Content-Type: application/json" -X POST team7restapi.appspot.com/api/robots/ --data '{"attacker": true, "room":9, "sensors":[{"id":1}, "buildings":{"id":4}}'

example PUT:
curl -v  -H "Content-Type: application/json" -X PUT localhost:8080/api/robots/2/ --data '{"attacker": true, "room":9, "sensors":[{"id":1}, "buildings":{"id":4}}


