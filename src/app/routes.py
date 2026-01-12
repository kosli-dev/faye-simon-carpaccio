from flask import Flask, render_template, request


def register_routes(app: Flask) -> None:
    @app.route("/", methods=["GET", "POST"])
    def index():
        states = {"UT": 6.85, "NV": 8.00, "TX": 6.25, "AL": 4.00, "CA": 8.25}
        state_list = [state for state in states.keys()]
        print(state_list)
        if request.method == "POST":
            item_price = float(request.form["item_price"])
            number_of_items = int(request.form["number_of_items"])
            total_price = round(item_price * number_of_items, 2)
            tax_rate = states[request.form["state"]]
            total_price_with_tax = round(total_price * (1 + tax_rate / 100), 2)
            return render_template(
                "index.html",
                item_price=item_price,
                number_of_items=number_of_items,
                selected_state=request.form["state"],
                states=state_list,
                total_price=total_price,
                total_price_with_tax=total_price_with_tax,
                tax_rate=tax_rate,
            )
        return render_template("index.html", states=state_list)
