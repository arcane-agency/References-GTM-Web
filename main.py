from flask import Flask,render_template
app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/product")
def product_page():
    return render_template('product.html')

@app.route("/cart")
def cart_page():
    return render_template('cart.html')

@app.route("/checkout_1")
def checkout1_page():
    return render_template('checkout_1.html')

@app.route("/checkout_2")
def checkout2_page():
    return render_template('checkout_2.html')
    
@app.route("/purchase")
def purchase_page():
    return render_template('purchase.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)