#!flask/bin/python
from flask import Flask, jsonify, abort, request

app = Flask(__name__)

robots = [
    {
        'id': 1,
        'floor': 1,
        'room': 1, 
        'attacker': False, 
        'status': 1, 
        'movement': 1
    },
    {
        'id': 2,
        'floor': 1,
        'room': 2, 
        'attacker': True, 
        'status': 1, 
        'movement': 1
    }
]

@app.route('/todo/api/v1.0/robots', methods=['GET'])
def get_robots():
    return jsonify({'robots': robots})

@app.route('/todo/api/v1.0/robots/<int:r_id>', methods=['GET'])
def get_robot(r_id):
    robot = [robot for robot in robots if robot['id'] == r_id]
    if len(robot) == 0:
        abort(404)
    return jsonify({'robot': robot[0]})

@app.route('/todo/api/v1.0/robots/status/<int:r_id>', methods=['GET'])
def get_robot_status(r_id):
    robot = [robot for robot in robots if robot['id'] == r_id]
    if len(robot) == 0:
        abort(404)
    return jsonify({'robot': robot[0]['status']})

@app.route('/todo/api/v1.0/robots/floor/<int:r_id>', methods=['GET'])
def get_robot_floor(r_id):
    robot = [robot for robot in robots if robot['id'] == r_id]
    if len(robot) == 0:
        abort(404)
    return jsonify({'robot': robot[0]['floor']})

@app.route('/todo/api/v1.0/robots/room/<int:r_id>', methods=['GET'])
def get_robot_room(r_id):
    robot = [robot for robot in robots if robot['id'] == r_id]
    if len(robot) == 0:
        abort(404)
    return jsonify({'robot': robot[0]['room']})

@app.route('/todo/api/v1.0/robots', methods=['POST'])
def create_robot():
    if len(robots) == 0:
       	newbot = {
		'id': 1,
		'floor': 1,
		'room': 1, 
		'attacker': False, 
		'status': 1, 
		'movement': 1
    	}
    else:
    	newbot = {
		'id': robots[-1]['id']+1,
		'floor': 1,
		'room': 1, 
		'attacker': False, 
		'status': 1, 
	'movement': 1
    	}
    robots.append(newbot)
    return jsonify({'robot': newbot}), 201

@app.route('/todo/api/v1.0/robots/<int:r_id>', methods=['PUT'])
def update_robot(r_id):
    robot = [robot for robot in robots if robot['id'] == r_id]
    if len(task) == 0:
        abort(404)
    if not request.json:
        abort(400)
    if 'floor' in request.json and type(request.json['floor']) is not int:
        abort(400)
    if 'room' in request.json and type(request.json['room']) is not int:
        abort(400)
    if 'attacker' in request.json and type(request.json['attacker']) is not bool:
        abort(400)
    if 'status' in request.json and type(request.json['status']) is not int:
        abort(400)
    robot[0]['floor'] = request.json.get('floor', task[0]['floor'])
    robot[0]['room'] = request.json.get('room', task[0]['room'])
    robot[0]['attacker'] = request.json.get('attacker', task[0]['attacker'])
    robot[0]['status'] = request.json.get('status', task[0]['status'])
    return jsonify({'robot': robot[0]})

@app.route('/todo/api/v1.0/robots/<int:r_id>', methods=['DELETE'])
def delete_robot(r_id):
    robot = [robot for robot in robots if robot['id'] == r_id]
    if len(robot) == 0:
        abort(404)
    robots.remove(robot[0])
    return jsonify({'result': True})

@app.route('/todo/api/v1.0/robots', methods=['DELETE'])
def delete_robots():
    robots.remove(robot[:])
    return jsonify({'result': True})

if __name__ == '__main__':
    app.run(debug=True)

