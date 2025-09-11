def convert():
    print("Hello and welcome to the unit converter!")

    try:
        value = float(input("Enter value to convert:"))
    except ValueError:
        print("invalid input, please enter a number.")
        return

    convert_type = input(
        "Choose what to convert:\n"
        "P: price, before --> after discount  and tax\n"
        "S: Speed, km/h --> mph\n"
    ).lower()

    if convert_type == "p":
        discount = 10
        tax_rate= 0.20
        final_Price = (value - discount ) * (1 + tax_rate)
        print(
            f"The final price of {value} after {discount} kr discount and "
            f"{tax_rate*100}% tax is: {final_Price:.2f} kr"
        )

    elif convert_type == "s":
        mph = value * 0.62137
        print(f"{value} km/h is equivalent to {mph:.2f} mph")

    else:
        print("Invalid converter, please enter P or S.")
        return
