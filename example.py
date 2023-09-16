from flask import Flask

app = Flask(__name__) 

employee_data = {}

# Greeting
@app.route("/greeting",methods=['GET'])
def greeting():
    return 'Hello World!'

def generate_employee_id():
    if not employee_data:
        return 1
    else:
        return max(employee_data.keys()) + 1

# Create Employee
@app.route('/employee', methods=['POST'])
def create_employee():
    data = request.json

    # Generate a unique ID for the new employee
    new_employee_id = generate_employee_id()

    # Create a new employee record
    new_employee = {
        'employee id': new_employee_id
        'name': data.get('name')
        'city': data.get('city')
    }

    # Add the new employee to the data store
    employee_data[new_employee_id] = new_employee

    return jsonify(new_employee), 200  # 200 indicates resource created

# Get all Employee details
@app.route('/employees/all', methods=['GET'])
def get_all_employees():
    return jsonify(list(employee_data.values()))

# Get Employee details
@app.route('/employee/<int:id>', methods=['GET'])
def get_employee(id):
    employee = employee_data.get(id)
    if employee:
        return jsonify(employee)
    else:
        return jsonify({'error': 'Employee not found'}), 404  # 404 indicates not found

if __name__ == '__main__':
    app.run(port=8080, host='0.0.0.0')

