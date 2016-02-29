#!flask/bin/python
from flask import Flask, jsonify, abort, request, redirect

app = Flask(__name__)

robots = [
        {
            'id': 1,
            'floor': 1,
            'room': 1, 
            'attacker': False, 
            'status': 1, 
            'movement': 1,
            'sensors':[
                {
                    "id": 1,
                    "ref": "/api/sensors/1/"
                    },
                {
                    "id": 2,
                    "ref": "/api/sensors/2/"
                    }
                ],
            'building': 
            {
                "id": "1",
                "ref": "/api/buildings/1/"
                }
            },
        {
            'id': 2,
            'floor': 1,
            'room': 2, 
            'attacker': True, 
            'status': 1, 
            'movement': 1,
            'sensors':[
                ],
            'building': 
            {
                "id": 1,
                "ref": "/api/buildings/1/"
                }
            }
        ]

def set_robot(robot):
    data = request.get_json()
    if not data:
        abort(400, "No data in the request")
    if 'floor' in data:
        if type(data['floor']) is not int:
            abort(400, "\'floor\' isn't an integer")
        else:
            robot['floor'] = data['floor']

    if 'room' in data:
        if type(data['room']) is not int:
            abort(400, "\'room\' isn't an integer")
        else:
            robot['room'] = data['room']

    if 'attacker' in data:
        if type(data['attacker']) is not bool:
            abort(400, "\'attacker\' isn't a bool")
        else:
            robot['attacker'] = data['attacker']

    if 'status' in data:
        if type(data['status']) is not int:
            abort(400, "\'status\' isn't an integer")
        else:
            robot['status'] = data['status']

    if 'sensors' in data:
        if not isinstance(data['sensors'], list):
            abort(400, "\'sensors\' isn't a list")
        #check to make sure they're all ints
        for sensor_id in data['sensors']:
            if 'id' not in sensor_id or type(sensor_id['id']) is not int:
                abort(400, "\'id\' isn't defined for the sensor")
        #We replace the ENTIRE list, not just add sensors
        del robot['sensors'][:]
        for sensor_id in data['sensors']:
            new_sensor = {
                    "id": sensor_id['id'],
                    "ref": "/api/sensors/"+str(sensor_id['id'])+"/"
                    }
            robot['sensors'].append(new_sensor)

    if 'building' in data:
        if "id" not in data['building'] or type(data['building']['id']) is not int:
            abort(400, "\'id\' isn't defined for the building")
        new_bldg = {
                "id": data['building']['id'],
                "ref": "/api/buildings/" + str(data['building']['id'])+"/"
                }
        robot['building'] = new_bldg

@app.route('/', methods=['GET'])
@app.route('/api/', methods=['GET'])
def get_home():
    return "To access the API, navigate to /api/robots"

@app.route('/api/robots/', methods=['GET'])
def get_robots():
    return jsonify({'robots': robots})

@app.route('/api/robots/<int:r_id>/', methods=['GET'])
def get_robot(r_id):
    robot = [robot for robot in robots if robot['id'] == r_id]
    if len(robot) == 0:
        abort(404, "Could not find the robot with the provided id")
    return jsonify({'robot': robot[0]})

@app.route('/api/robots/<int:r_id>/status/', methods=['GET'])
def get_robot_status(r_id):
    robot = [robot for robot in robots if robot['id'] == r_id]
    if len(robot) == 0:
        abort(404, "Could not find the robot with the provided id")
    return jsonify({'status': robot[0]['status']})

@app.route('/api/robots/<int:r_id>/floor/', methods=['GET'])
def get_robot_floor(r_id):
    robot = [robot for robot in robots if robot['id'] == r_id]
    if len(robot) == 0:
        abort(404, "Could not find the robot with the provided id")
    return jsonify({'floor': robot[0]['floor']})

@app.route('/api/robots/<int:r_id>/room/', methods=['GET'])
def get_robot_room(r_id):
    robot = [robot for robot in robots if robot['id'] == r_id]
    if len(robot) == 0:
        abort(404, "Could not find the robot with the provided id")
    return jsonify({'room': robot[0]['room']})


@app.route('/api/robots/<int:r_id>/building/', methods=['GET'])
def get_robot_building(r_id):
    robot = [robot for robot in robots if robot['id'] == r_id]
    if len(robot) == 0:
        abort(404, "Could not find the robot with the provided id")
    return redirect(robot[0]['building']['ref'])

@app.route('/api/buildings/<int:bldg_id>/', methods=['GET'])
def get_buidling(bldg_id):
    #We shouldn't care about building json stuff since that's out of our purview
    return "This is where the building json stuff for " +str(bldg_id) + " will go!"


@app.route('/api/robots/<int:r_id>/sensors/', methods=['GET'])
def get_robot_sensors(r_id):
    robot = [robot for robot in robots if robot['id'] == r_id]
    if len(robot) == 0:
        abort(404, "Could not find the robot with the provided id")
    return jsonify({'sensors': robot[0]['sensors']})


@app.route('/api/robots/<int:r_id>/sensors/<int:snsr_id>/', methods=['GET'])
def get_robot_sensor(r_id, snsr_id):
    robot = [robot for robot in robots if robot['id'] == r_id]
    if len(robot) == 0:
        abort(404, "Could not find the robot with the provided id")
    sensors = robot[0]['sensors']
    if len(sensors) == 0:
        abort(404, "Could not find the sensor with the provided id")
    sensor = [sensor for sensor in sensors if sensor['id'] == snsr_id]
    if len(sensor) == 0:
        abort(404, "Could not find the sensor with the provided id")
    return redirect(sensor[0]['ref'])

@app.route('/api/sensors/<int:snsr_id>/', methods=['GET'])
def get_sensor(snsr_id):
    #We shouldn't care about sensor json stuff since that's out of our purview
    return "This is where the sensor json stuff for " +str(snsr_id) + " will go!"


@app.route('/api/robots/<int:r_id>/sensors/<int:snsr_id>/', methods=['DELETE'])
def remove_sensor(r_id, snsr_id):
    robot = [robot for robot in robots if robot['id'] == r_id]
    if len(robot) == 0:
        abort(404, "Could not find the robot with the provided id")
    sensors = robot[0]['sensors']
    sensor = [sensor for sensor in sensors if sensor['id'] == snsr_id]
    if len(sensor) == 0:
        abort(404, "Could not find the sensor with the provided id")
    sensors.remove(sensor[0])
    return jsonify({'sensors': sensors})




#Add a sensor with POST - keeps other sensors added intact
@app.route('/api/robots/<int:r_id>/sensors/', methods=['POST'])
def add_sensor(r_id):
    robot = [robot for robot in robots if robot['id'] == r_id]
    if len(robot) == 0:
        abort(404, "Could not find the provided id in the body")
    sensors = robot[0]['sensors']
    if not data or 'id' not in data or type(data['id']) is not int:
        abort(400, "Could not find \"id\" in the body")

    sensor = {
            'id': data['id'],
            'ref': "/api/sensors/"+str(data['id'])+"/"
            }
    sensors.append(sensor)
    return jsonify({'sensor': sensor}), 201



@app.route('/api/robots/', methods=['POST'])
def create_robot():
    if len(robots) == 0:
        newbot = {
                'id': 1,
                'floor': 1,
                'room': 1, 
                'attacker': False, 
                'status': 1, 
                'movement': 1,
                'sensors': [],
                'building': {
                    'id': 1,
                    'ref': '/api/buildings/1/'
                    }
                }
    else:
        newbot = {
                'id': robots[-1]['id']+1,
                'floor': 1,
                'room': 1, 
                'attacker': False, 
                'status': 1, 
                'movement': 1,
                'sensors': [],
                'building': {
                    'id': 1,
                    'ref': '/api/buildings/1/'
                    }
                }
        set_robot(newbot)
    robots.append(newbot)
    return jsonify({'robot': newbot}), 201

@app.route('/api/robots/<int:r_id>/', methods=['PUT'])
def update_robot(r_id):
    robot = [robot for robot in robots if robot['id'] == r_id]
    if len(robot) == 0:
        abort(404, "Could not find the robot with the provided id")
    set_robot(robot[0])
    return jsonify({'robot': robot[0]})


@app.route('/api/robots/<int:r_id>/', methods=['DELETE'])
def delete_robot(r_id):
    robot = [robot for robot in robots if robot['id'] == r_id]
    if len(robot) == 0:
        abort(404, "Could not find the robot with the provided id")
    robots.remove(robot[0])
    return jsonify({'result': True})

@app.route('/api/robots/', methods=['DELETE'])
def delete_robots():
    robots.remove(robot[:])
    return jsonify({'result': True})


@app.errorhandler(404)
def custom404(error):
    response = jsonify({'message': error.description})
    response.status_code = 404
    return response

@app.errorhandler(400)
def custom400(error):
    response = jsonify({'message': error.description})
    response.status_code = 400
    return response

@app.errorhandler(500)
def custom500(error):
    response = jsonify({'message': error.description})
    response.status_code = 500
    return response

@app.errorhandler(415)
def custom415(error):
    response = jsonify({'message': error.description})
    response.status_code = 415
    return response

@app.errorhandler(405)
def custom405(error):
    response = jsonify({'message': error.description})
    response.status_code = 405
    return response

@app.errorhandler(302)
def custom302(error):
    response = jsonify({'message': error.description})
    response.status_code = 302
    return response


if __name__ == '__main__':
    app.run(debug=True)

