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
    amount = int(request.form["amount"])

    try:
        result = cr.convert(from_currency, to_currency, amount)
    except:
        if valid_from_cn == None:
            flash(f"Currency unavailable: {from_currency}")
            return render_template("/index.html")

        if valid_to_cn == None:
            flash(f"Currency unavailable: {to_currency}")
            return render_template("/index.html")

        if type(amount) != int:
            flash("Please enter valid amount.")
            return render_template("/index.html")


    return render_template("/results.html", symbol=symbol, result=round(result,2), from_currency=from_currency, to_currency=to_currency)

# The object returned from CurrencyCodes() has a get_currency_name() method 
# that attempts to map a code to a name. If that returns None, the code is invalid. 
# The object returned from CurrencyRates() includes a convert() method that will throw 
# an exception if the conversion is invalid. If you check the results of the 
# get_currency_name() method and wrap the convert call in a try-except, you can determine 
# if the data is invalid and if 1 or more error messages should be displayed via flash.
