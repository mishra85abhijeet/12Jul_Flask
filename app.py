from flask import Flask, redirect, url_for, render_template, request



app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template('webpage.html')

@app.route('/mem/<int:score>')
def mem(score):
    return webpage

@app.route('/rej/<int:score>')
def rej(score):
    return "rejected to member comunity your score is "+ str(score)

# Result checker html page
@app.route("/submit", method=['POST', 'GET'])
def submit():
    total_score=0
    if request.method=='POST':
        



if __name__=='__main__':
    app.run(debug=True)