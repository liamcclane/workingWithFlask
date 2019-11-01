# Flask Fundamentals: 
# Lia McClane: 10/30/2019 Wed

from flask import Flask, render_template  # Import Flask to allow us to create our appcopy and add render_template

app = Flask(__name__)    # Create a new instance of the Flask class called "app"
# print(__name__) outputs "__main__"

@app.route('/')
def index():
    return render_template("index.html", phrase="hello", times=5)	# notice the 2 new named arguments!
if __name__=="__main__":
    app.run(debug=True)



# @app.route('/')           # The "@" decorator associates this route with the function immediately following
# def hello_world():        # This is also the default 'Home page' since there is nothing after the /
#     # message = "this is a sting litteral that is going to be put on the front of my webpage"
#     return render_template('index.html')        # returns the string message

# @app.route('/hello/<name>') # for a route '/hello/____' anything after '/hello/' gets passed as a variable 'name'
# def hello(name):
#     print(f"inside the hello(name) function {name}")
#     print("regular message", flush=True)
#     return "Hello, " + name

# @app.route('/success')      # now when a users requests localhost:5000/success this function will run
# def success():
#     return "success we have moved to another pg"      # app.run(debug=True) should be the very last statement! 


if __name__=="__main__":   # Ensure this file is being run directly and not from a different module
    app.run(debug=True)    # Run the app in debug mode

