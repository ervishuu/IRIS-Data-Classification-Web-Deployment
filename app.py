from flask import Flask,render_template,request,jsonify
import pickle
import joblib
model = joblib.load("iris.pkl")
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/predict',methods=['POST'])
def predict():
  if request.method == "POST" :

     SL = float(request.form["sl"])
     SW = float(request.form["sw"])
     PL = float(request.form["pl"])
     PW = float(request.form["pw"])


     result = model.predict([[SL,SW,PL,PW]])
     if result[0] == 0:
        return render_template('index.html',data=["The flower is classified as Setosa","green"])

     elif result[0] == 1:
        return render_template('index.html', data=["The flower is classified as Versicolor", "red"])

     else:
        return render_template('index.html',data=["The flower is classified as Virginica","blue"])



if __name__ == "__main__":
    app.run(debug=True)