from flask import Flask, render_template, request,redirect,url_for,flash
import requests
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = "itisasecret"
currencys=['ALL','USD','EUR','JPY','GBP','CHF','CAD','ZAR','CNH','SEK','NZD']

@app.route("/",methods=["POST","GET"])
def index():
    if request.method == "POST":
        API = "b85dd27984616fcd4258"
        fromCurr = request.form.get('fromCurr')
        toCurr = request.form.get('toCurr')
        amt = request.form.get('amt')
        if fromCurr and toCurr:
            try:
                url = f"https://free.currconv.com/api/v7/convert?q={fromCurr}_{toCurr}&compact=ultra&apiKey={API}"
                rates = requests.get(url).json()[f'{fromCurr}_{toCurr}']
                resAmt = round(float(amt)*rates,2)
                return render_template("index.html",currency=currencys,result=f"You could get {resAmt} {toCurr} with {amt} {fromCurr}")
            except:
                flash("Error occured",'danger')
                return redirect(url_for('index'))
        else:
            flash("Error occured",'danger')
            return redirect(url_for('index'))

    return render_template("index.html",currency=currencys)

if __name__ == "__main__":
    app.run(debug=True)