from flask import Flask, request, render_template, redirect, flash
from forex_python.converter import CurrencyRates, CurrencyCodes

app = Flask(__name__)
app.config['SECRET_KEY'] = "123abc!"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

@app.route("/")
def home_page():
    return render_template("/index.html")

@app.route("/results", methods=["POST"])
def convert():
    cr = CurrencyRates()
    cc = CurrencyCodes()

    from_currency = request.form["from_currency"].upper()
    to_currency = request.form["to_currency"].upper()
    valid_from_cn = cc.get_currency_name(from_currency)
    valid_to_cn = cc.get_currency_name(to_currency)
    symbol = cc.get_symbol(to_currency)
    try:
        amount = float(request.form["amount"])
    except:
        amount = None 

    try:
        result = cr.convert(from_currency, to_currency, amount)
    except:
        if valid_from_cn == None:
            flash(f"Currency unavailable: {from_currency}")
            # return render_template("/index.html")

        if valid_to_cn == None:
            flash(f"Currency unavailable: {to_currency}")
            # return render_template("/index.html")

        if amount == None:
            flash("Please enter valid amount.")
            # return render_template("/index.html")

        return render_template("/index.html")
    return render_template("/results.html", symbol=symbol, result=round(result,2), from_currency=from_currency, to_currency=to_currency)
