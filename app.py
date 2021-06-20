from flask import Flask, redirect, request
from flask.templating import render_template
import model


app = Flask(__name__)




@app.route('/', methods=['GET'])

def home():

    return render_template("index.html")


@app.route('/submit',methods=['GET','POST'])
def submit():

    if(request.method=='POST'):

        customer = request.form['customer']
        dealer = request.form['dealer']
        rating  = request.form['rating']
        comments = request.form['customer']
        model.add(customer,dealer,rating,comments)
        message = "Success"
        

        

        return render_template("success.html",message=message)



app.run(port=9000,debug=True)

