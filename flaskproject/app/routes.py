from app import app
import requests
from flask import render_template, request
from app.models import model, formopener, API

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")
    
@app.route('/results', methods=["GET", "POST"])
def results():
    userdata = dict(request.form)
    product = userdata["product"][0]
    cost = userdata["cost"][0]
    buyinvt = userdata["buyinvt"][0]
    curinvt = userdata["curinvt"][0]
    sales = userdata["sales"][0]
    money = userdata["money"][0]
    price = userdata["price"][0]
    profit_per_product = str(float(price) - float(cost))
    buy_stock = str(float(buyinvt) * float(cost))
    profit_cur = str(float(profit_per_product) * float(curinvt))
    profit_after = str((float(buyinvt) + float(curinvt)) * float(profit_per_product))
    end_of_year = str(float(sales) * float(profit_per_product))
    end_of_year_sales = str(float(money) - float(end_of_year))
    goal = int((float(money) - float(end_of_year)) / float(profit_per_product))
    # return ("It will cost " + buy_stock + " dollars to purchase " + str(buyinvt) + " of the " + product + ". If you sell all of your current inventory, you will make " + profit_cur + " dollars. If you sell your current inventory and the inventory you are purchasing, you will make " + profit_after + " dollars. So far you have made " + end_of_year + " dollars this year. To reach your goal, you need to make " + end_of_year_sales + " dollars or sell " + str(goal) + " of the " + product) 
    return render_template("results.html", product = product, buy_stock = buy_stock, buyinvt = buyinvt, profit_per_product = profit_per_product, profit_cur = profit_cur, profit_after = profit_after, end_of_year = end_of_year, end_of_year_sales = end_of_year_sales, goal = goal)
@app.route("/s")
def s():
    return render_template("s.html")
@app.route("/info")
def info():
    response = API.showPrice()
    response[0]['Product_Name']
    print(response[0]["Best_Price"])
    price_US = float(response[0]['Best_Price'].replace(",", ""))/69.01
    response[0]['Seller_Name']
    return render_template('patrick_is_cool.html', data=response, price_US = price_US)
    