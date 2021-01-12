from flask import Flask, render_template# Import Flask to allow us to create our app
app = Flask(__name__) # __main__ Create a new instance of the Flask class called "app"

@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    return render_template("index.html", phrase="hello", times=5)

@app.route('/dojo')
def dojo():
    return 'Dojo'

@app.route('/say/<name>')
def say(name):
    print(name)
    return 'Hi ' + name

@app.route('/repeat/<num>/<string>')
def repeat_string(num, string):
    return f"{string}" * int(num) 

@app.route('/lists')
def render_lists():
    student_info = [
        {'name' : 'Michael', 'age' : 35},
        {'name' : 'John', 'age' : 30 },
        {'name' : 'Mark', 'age' : 25},
        {'name' : 'KB', 'age' : 27}
    ]
    return render_template("lists.html", random_numbers = [3,1,5], students = student_info)


# @app.route('/hello/<name>')
# def first_html(name):
#     return render_template("index.html",
#     name_from_backend = name)#{{name_from_backend}}
        

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.