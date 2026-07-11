from flask import Flask, render_template, request

app = Flask(__name__)

# Car prices
car_prices = {
    "Polo Trendline": 870000,
    "Polo Highline": 1009000,
    "Virtus Trendline": 1105000,
    "Virtus Highline": 1308000,
    "Taigun Trendline": 1489000,
    "Taigun Highline": 1549000,
    "Taigun Topline": 1771000
}

# Car images
car_images = {
    "Polo Trendline": "images/polo.jpg",
    "Polo Highline": "images/polo.jpg",

    "Virtus Trendline": "images/virtus.jpg",
    "Virtus Highline": "images/virtus.jpg",

    "Taigun Trendline": "images/taigun.jpg",
    "Taigun Highline": "images/taigun.jpg",
    "Taigun Topline": "images/taigun.jpg"
}


# Additional charges
rto = 113990
insurance_price = 47300
tcs = 11000
accessories_price = 15000


@app.route("/", methods=["GET", "POST"])
def home():

    selected_car = None
    showroom_price = None
    car_image = None

    discount = None
    discount_amount = 0

    final_price = None

    insurance = None
    accessories = None

    insurance_cost = 0
    accessories_cost = 0

    error = None


    if request.method == "POST":

        # Selected car
        selected_car = request.form["car"]

        showroom_price = car_prices[selected_car]

        # Fetch car image
        car_image = car_images[selected_car]


        # Discount
        discount = request.form["discount"].strip()


        # Insurance and accessories
        insurance = request.form["insurance"]
        accessories = request.form["accessories"]


        print("Selected Car:", selected_car)
        print("Showroom Price:", showroom_price)
        print("Discount:", discount)
        print("Insurance:", insurance)
        print("Accessories:", accessories)


        # -------------------------
        # Calculate Discount
        # -------------------------

        try:

            if discount == "":
                discount_amount = 0


            elif discount.endswith("%"):

                percentage = float(discount[:-1])

                discount_amount = (
                    showroom_price * percentage
                ) / 100


            else:

                discount_amount = float(discount)



            # Discount allowed only with extra features

            if (
                discount_amount > 0
                and insurance == "No"
                and accessories == "No"
            ):

                error = "Anyone of the additional features have to be added."

                discount_amount = 0



            # Maximum discount limit

            if discount_amount > 30000:

                error = (
                    "Maximum discount allowed is ₹30,000. "
                    "Discount limited to ₹30,000."
                )

                discount_amount = 30000



        except ValueError:

            error = "Please enter a valid discount."

            discount_amount = 0



        print("Discount Amount:", discount_amount)



        # -------------------------
        # Insurance Cost
        # -------------------------

        if insurance == "Yes":

            insurance_cost = insurance_price

        else:

            insurance_cost = 0



        # -------------------------
        # Accessories Cost
        # -------------------------

        if accessories == "Yes":

            accessories_cost = accessories_price

        else:

            accessories_cost = 0



        print("Insurance Cost:", insurance_cost)
        print("Accessories Cost:", accessories_cost)



        # -------------------------
        # Final Bill
        # -------------------------

        final_price = (
            showroom_price
            + rto
            + insurance_cost
            + tcs
            + accessories_cost
            - discount_amount
        )


        print("RTO:", rto)
        print("TCS:", tcs)
        print("Final Bill:", final_price)



    return render_template(
        "index.html",

        cars=car_prices,

        selected_car=selected_car,
        showroom_price=showroom_price,
        car_image=car_image,

        discount=discount,
        discount_amount=discount_amount,

        final_price=final_price,

        insurance=insurance,
        accessories=accessories,

        insurance_cost=insurance_cost,
        accessories_cost=accessories_cost,

        rto=rto,
        tcs=tcs,

        error=error
    )


if __name__ == "__main__":
    app.run(debug=True)