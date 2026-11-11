
import math


def parse_plan(code):
    if not isinstance(code, str):
        return None

    parts = code.split('-')

    if len(parts) != 2:
        return None

    plan, months = parts

    if not plan.strip() or not months.isdigit():
        return None

    months = int(months)

    if months <= 0:
        return None

    return plan.upper(), months


def calculate_bmi(data):
    if not isinstance(data, str):
        return None

    parts = data.split(',')

    if len(parts) != 2:
        return None

    try:
        weight = float(parts[0])
        height = float(parts[1])
    except ValueError:
        return None

    if not math.isfinite(weight) or not math.isfinite(height):
        return None

    if weight <= 0 or height <= 0:
        return None

    return round(weight / (height ** 2), 1)


def average_workout(minutes):
    if not isinstance(minutes, str):
        return None

    values = minutes.split()

    if not values:
        return None

    if not all(value.isdigit() for value in values):
        return None

    values = [int(value) for value in values]

    return sum(values) // len(values)


def main():
    print("==== Running parse_plan ====")
    user_input = input("Enter a plan code (e.g. GOLD-12): ")
    result = parse_plan(user_input)
    print("Plan and Months:", result)

    print("\n==== Running calculate_bmi ====")
    user_input = input("Enter weight and height (e.g. 70,1.75): ")
    result = calculate_bmi(user_input)
    print("BMI:", result)

    print("\n==== Running average_workout ====")
    user_input = input(
        "Enter workout minutes separated by spaces (e.g. 45 60 30): "
    )
    result = average_workout(user_input)
    print("Average Minutes:", result)


if __name__ == "__main__":
    main()
