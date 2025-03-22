def calculator():
    firstNumber = float(input("Enter the first number: "))
    secondNumber = float(input("Enter the second number: "))
    theSymbol = input("Enter the symbol: ").strip()

    if theSymbol == "+":
        theResult = firstNumber + secondNumber
    elif theSymbol == "-":
        theResult = firstNumber - secondNumber
    elif theSymbol == "*":
        theResult = firstNumber * secondNumber
    elif theSymbol == "/":
        theResult = firstNumber / secondNumber
    elif theSymbol == "**":
        theResult = firstNumber ** secondNumber
    else:
        print("Enter a right symbol(+ , - , * , / , **)")
    print(theResult)


calculator()