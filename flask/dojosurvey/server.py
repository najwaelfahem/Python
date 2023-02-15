from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'
@app.route("/")
def form():
   return render_template('form.html') 
@app.route('/process', methods=['POST'])
def process_form():
    print(f"{request.form} ****************")
    session['user']=request.form['user']
    session['location'] = request.form['location']
    session['favorite'] = request.form['favorite']
    session['comments'] = request.form['comments']
    return redirect('/display') 
@app.route('/display')
def display():
        print(f"{request.form} ++++++++++++++++")
        print(f"{session} ------------")
    
        return render_template("display.html")
@app.route('/clear')
def clear_session():
    session.clear()
    return redirect('/display')   

    









if __name__=='__main__':
    app.run(debug=True, port=5001)
