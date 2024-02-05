def main():
    meal_time = convert(input("What time is it? ").strip())
    if convert("7:00") <= meal_time <= convert("8:00"):
        print("breakfast time")
    elif convert("12:00") <= meal_time <= convert("13:00"):
        print("lunch time")
    elif convert("18:00") <= meal_time <= convert("19:00"):
        print("dinner time")

def convert(time):
    hours, minutes = time.replace(" a.m.", "").replace(" p.m.", "").split(":")
    hrs = float(hours)
    mins = float(minutes)
    if " p.m." in time and hrs != 12:
        return (hrs + 12) + (mins / 60)
    elif " a.m." in time and hrs == 12:
        return (hrs == 0) + (mins / 60)
    else:
        return hrs + (mins / 60)

if __name__ == "__main__":
    main()
    