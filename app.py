from flask import Flask,render_template,redirect,request
import sklearn.linear_model 
import joblib
#__name__ == __main__
app = Flask(__name__)
model = joblib.load("model.pkl")
@app.route('/')
def hello():
    return render_template("index.html")
@app.route('/', methods = ['POST'])
def get_marks():
    if request.method == 'POST':
        hours = float(request.form['hours'])

        marks = str(model.predict([[hours]])[0][0])
    return render_template("index.html", your_marks = marks)




if __name__ == '__main__':
    app.run(debug=True)