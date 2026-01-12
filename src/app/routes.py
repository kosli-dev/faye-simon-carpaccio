from flask import Flask, render_template, request


def register_routes(app: Flask) -> None:
    @app.route("/", methods=["GET", "POST"])
    def index():
        states = {"UT": 6.85, "NV": 8.00, "TX": 6.25, "AL": 4.00, "CA": 8.25}
        discounts = {50000: 0.15, 10000: 0.10, 7000: 0.07, 5000: 0.05, 1000: 0.03}
        state_list = [state for state in states.keys()]

        actual_discount_rate = 0
        discount_amount = 0

        if request.method == "POST":
            item_price = float(request.form["item_price"])
            number_of_items = int(request.form["number_of_items"])
            total_price = round(item_price * number_of_items, 2)
            tax_rate = states[request.form["state"]]

            for discount_threshold, discount_rate in discounts.items():
                if total_price >= discount_threshold:
                    actual_discount_rate = discount_rate * 100
                    discount_amount = round(total_price * discount_rate, 2)
                    total_price = round(total_price * (1 - discount_rate), 2)
                    break
                
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
                discount_rate=actual_discount_rate,
                discount_amount=discount_amount,
            )
        return render_template("index.html", states=state_list)
