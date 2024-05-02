from flask import Flask ,  jsonify 
app = Flask(__name__)

@app.route('/')                 
def hello_world():
    print("*******"*40)
    print (list)
    print("*******"*40)
    return 'Hello World!'  

@app.route('/say/<name>')
def dojo (name):
    return f"HI {name}"
@app.route('/repeat/<id>/<name>')
def repeat(id,name):
    return f"{name} "*int(id)

specified_routes = ['/', '/say/<name>', '/repeat/<id>/<name>']

# Define your error message
error_message = "Sorry! No response. Try again."

# Define the catch-all route
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    if path not in specified_routes:
        return jsonify({'error': error_message}), 404
    else:
        return jsonify({'message': 'Success!'}), 200


if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.