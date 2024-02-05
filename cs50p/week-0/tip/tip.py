# Apply dollars_to_float and percent_to_float to corresponding inputs, calculate tip, print tip
def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")

# Define dollars_to_float by stripping any '$' and returning as float
def dollars_to_float(d):
    return float(d.strip('$'))

# Define percent_to_float by replacing trailing '%' with '*10^-2' to remove '%' and divide by 100 in one clean step
def percent_to_float(p):
    return float(p.replace('%', 'e-2'))

main()
