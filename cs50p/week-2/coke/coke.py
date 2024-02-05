def main():
    coin_calculator()
    
def coin_calculator():
    amount_due = 50
    while amount_due > 0:
        print(f"Amount Due: {amount_due}")
        coin = int(input("Insert Coin: "))
        if coin in [25, 10, 5]:
            amount_due -= coin
    change_owed = abs(amount_due)
    print(f"Changed Owed: {change_owed}")
    
main()
