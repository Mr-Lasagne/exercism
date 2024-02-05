# Take an int input, apply the energy function to the input, then print the input
def main():
    mass = int(input("Mass: "))
    E = energy(mass)
    print("Energy =", E, "Joules")

# Define a function that calculates mc^2
def energy(m):
    c = 300000000
    return m * c**2

main()
