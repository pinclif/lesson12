def calculate_bmi(weight, height):
    try:
        bmi = weight / (height/100)** 2
        return bmi
    except ZeroDivisionError:
        return None


def get_bmi_category(bmi):
    if bmi is None:
        return "Error: invalid data"
    elif bmi < 18.5:
        return "Underweight"
    elif bmi < 24.9:
        return "Normal body weight"
    elif bmi < 29.9:
        return "Overweight (preobesity)"
    else:
        return "Obesity"


def main():
    try:
        weight = float(input("Enter your weight in kilograms: "))
        height = float(input("Enter your height in centimeters: "))

        bmi = calculate_bmi(weight, height)
        bmi_category = get_bmi_category(bmi)

        print("Body mass index (BMI):", bmi)
        print("Explanation:", bmi_category)
    except ValueError:
        print("Error: invalid data")


if __name__ == "__main__":
    main()