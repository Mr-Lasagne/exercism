def main():
    expression = input("Expression: ").strip()
    x, y, z = expression.split(" ")
    
    numx = float(x)
    numz = float(z)
    
    print(round(result(numx, y, numz), 1))

def result(n1, o, n2):
    if o == "+":
        return float(n1 + n2)
    elif o == "-":
        return float(n1 - n2)
    elif o == "*":
        return float(n1 * n2)
    elif o == "/":
        return float(n1 / n2)

main()
