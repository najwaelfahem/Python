from flask import Flask  
app = Flask(__name__)    
@app.route('/')          
def hello_world():
    return 'Hello World!' 
@app.route('/dojo')
def dojo(): 
    return 'dojo'
@app.route('/say/<name>') 
def say(name): 
    return f"hi {name}"
@app.route('/repeat/<int:times>/<name>')
def repeat(name,times):
    return f" hi {name}" * (times)

if __name__=="__main__":       
    app.run(debug=True)    

