from flask import Flask, render_template, request


def register_routes(app: Flask) -> None:
    @app.route("/", methods=["GET", "POST"])
    def index():
        if request.method == "POST":
            item_price = float(request.form["item_price"])
            number_of_items = int(request.form["number_of_items"])
            total_price = item_price * number_of_items
            return render_template(
                "index.html",
                item_price=item_price,
                number_of_items=number_of_items,
                total_price=total_price,
            )
        return render_template("index.html")
