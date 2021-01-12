from flask import Flask, render_template
app = Flask(__name__) 

@app.route('/')          
def hello_world():
    return render_template("playground.html")

@app.route('/play/')
def play():
    return render_template("playground.html", num=3, color="#9EC5F8")

@app.route('/play/<num>')
def play_times(num):
    return render_template("playground.html", num=int(num), color="#9EC5F8") 

@app.route('/play/<num>/<color>')
def play_color(num, color):
    return render_template("playground.html", num=int(num), color=(color)) 


        

if __name__=="__main__":   
    app.run(debug=True)  