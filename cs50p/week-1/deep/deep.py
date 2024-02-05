def main():
    answer = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ").strip().lower()
    print(is_correct(answer))

def is_correct(s):
    if s == "42" or s == "forty-two" or s == "forty two":
        return "Yes"
    else:
        return "No"

main()
