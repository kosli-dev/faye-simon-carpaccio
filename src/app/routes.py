from flask import Flask, render_template, request


def register_routes(app: Flask) -> None:
    @app.route("/", methods=["GET", "POST"])
    def index():
        if request.method == "POST":
            item_price = float(request.form["item_price"])
            number_of_items = int(request.form["number_of_items"])
            total_price = round(item_price * number_of_items, 2)
            ut_tax_rate = 6.85
            total_price_with_tax = round(total_price * (1 + ut_tax_rate / 100), 2)
            return render_template(
                "index.html",
                item_price=item_price,
                number_of_items=number_of_items,
                total_price=total_price,
                total_price_with_tax=total_price_with_tax,
                ut_tax_rate=ut_tax_rate,
            )
        return render_template("index.html")
