from flask import Flask, request, render_template, redirect, flash, session
from forex_python.converter import CurrencyRates, CurrencyCodes

app = Flask(__name__)


@app.route("/")
def home_page():
    return render_template("/index.html")

@app.route("/results")
def show_result():
    return render_template("/results.html")

@app.route("/results", methods=["POST"])
def convert():
    cr = CurrencyRates()
    cc = CurrencyCodes()
    from_currency = request.form["from_currency"]
    to_currency = request.form["to_currency"]
    amount = round(int(request.form["amount"]),2)
    symbol = cc.get_symbol(to_currency)
    result = cr.convert(from_currency, to_currency, amount)
    return render_template("/results.html", symbol=symbol, result=result, from_currency=from_currency, to_currency=to_currency)