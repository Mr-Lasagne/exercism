def main():
    greeting = input("Greeting: ").lstrip().lower()
    print(prize(greeting))

def prize(s):
    if s.startswith("hello"):
        return "$0"
    elif s.startswith("h"):
        return "$20"
    else:
        return "$100"

main()
    