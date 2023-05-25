def convert():
    dollars = eval(input("Enter amount in dollars: "))
    print(convert_to_Polish_zloty(dollars))


def convert_to_Polish_zloty(amount):
    return amount * 4.46


convert()
