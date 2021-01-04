from flask import Flask, request, render_template, redirect, flash
from forex_python.converter import CurrencyRates, CurrencyCodes

app = Flask(__name__)
app.config['SECRET_KEY'] = "123abc!"
# app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False


@app.route("/")
def home_page():
    return render_template("/index.html")

@app.route("/results", methods=["POST"])
def convert():
    cr = CurrencyRates()
    cc = CurrencyCodes()
    from_currency = request.form["from_currency"]
    to_currency = request.form["to_currency"]
    amount = int(request.form["amount"])
    symbol = cc.get_symbol(to_currency)
    result = cr.convert(from_currency, to_currency, amount)
    return render_template("/results.html", symbol=symbol, result=result, from_currency=from_currency, to_currency=to_currency)

@app.errorhandler(500)
def handle_error(e):
    # note that we set the 500 status explicitly
    flash("Invalid currency code.")
    return render_template("/index.html"), 500