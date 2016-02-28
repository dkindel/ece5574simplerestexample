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

@app.route('/', methods=['GET'])
def get_home():
    return "To access the API, navigate to /api/robots"

@app.route('/api/robots', methods=['GET'])
def get_robots():
    return jsonify({'robots': robots})

@app.route('/api/robots/<int:r_id>', methods=['GET'])
def get_robot(r_id):
    robot = [robot for robot in robots if robot['id'] == r_id]
    if len(robot) == 0:
        abort(404)
    return jsonify({'robot': robot[0]})

@app.route('/api/robots/status/<int:r_id>', methods=['GET'])
def get_robot_status(r_id):
    robot = [robot for robot in robots if robot['id'] == r_id]
    if len(robot) == 0:
        abort(404)
    return jsonify({'robot': robot[0]['status']})

@app.route('/api/robots/floor/<int:r_id>', methods=['GET'])
def get_robot_floor(r_id):
    robot = [robot for robot in robots if robot['id'] == r_id]
    if len(robot) == 0:
        abort(404)
    return jsonify({'robot': robot[0]['floor']})

@app.route('/api/robots/room/<int:r_id>', methods=['GET'])
def get_robot_room(r_id):
    robot = [robot for robot in robots if robot['id'] == r_id]
    if len(robot) == 0:
        abort(404)
    return jsonify({'robot': robot[0]['room']})

@app.route('/api/robots', methods=['POST'])
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

@app.route('/api/robots/<int:r_id>', methods=['PUT'])
def update_robot(r_id):
    robot = [robot for robot in robots if robot['id'] == r_id]
    if len(robot) == 0:
        abort(404)
    data = request.get_json()
    if not data:
        abort(400)
    if 'floor' in data:
        if type(data['floor']) is not int:
            abort(400)
        else:
            robot[0]['floor'] = data['floor']

    if 'room' in data:
        if type(data['room']) is not int:
            abort(400)
        else:
            robot[0]['room'] = data['room']

    if 'attacker' in data:
        if type(data['attacker']) is not bool:
            abort(400)
        else:
            robot[0]['attacker'] = data['attacker']

    if 'status' in data:
        if type(data['status']) is not int:
            abort(400)
        else:
            robot[0]['status'] = data['status']
    return jsonify({'robot': robot[0]})

@app.route('/api/robots/<int:r_id>', methods=['DELETE'])
def delete_robot(r_id):
    robot = [robot for robot in robots if robot['id'] == r_id]
    if len(robot) == 0:
        abort(404)
    robots.remove(robot[0])
    return jsonify({'result': True})

@app.route('/api/robots', methods=['DELETE'])
def delete_robots():
    robots.remove(robot[:])
    return jsonify({'result': True})

if __name__ == '__main__':
    app.run(debug=True)

