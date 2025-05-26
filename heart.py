from flask import Flask,render_template,request
import pickle

model=pickle.load(open("model.pkl","rb"))


app=Flask(__name__)

@app.route("/")
def Start():
    return render_template("index.html")

@app.route("/",methods=['POST'])

def getData():
    # name=request.form['name']
    age=request.form['age']
    gender=request.form['gender']
    heart_rate=request.form['heart-rate']
    sbp=request.form['sbp']
    dbp=request.form['dbp']
    blood_sugar=request.form['blood-sugar']
    ck_mb=request.form['ck-mb']
    troponin=request.form['troponin']
    Age=int(age)
    hRate=int(heart_rate)
    systolic_bp=int(sbp)
    diastolic_bp=int(dbp)
    b_sugar=float(blood_sugar)
    ckmb=float(ck_mb)
    trop=float(troponin)
    value=0
    if gender=='Male':
        value=1
    result=model.predict([[Age,value,hRate,systolic_bp,diastolic_bp,b_sugar,ckmb,trop]])
    return render_template("index.html",data=result)

if __name__=="__main__":
    app.run(debug=True)