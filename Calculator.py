def main():
    operator = menuPrint()

    if operator == 1:
        dividendSentence = "Please Enter The Dividend Number:"
        dividerSentence = "Please Enter The Divider Number:"
        errorSentence = "Incorrect Entry! Please Enter Integers!"
        dividend, divider = numberCheckTwo(dividendSentence, dividerSentence, errorSentence)
        while divider == 0:
            print("Incorrect Entry! Divider Can't Be Equal to Zero! Please Enter Again.")
            divider = numberCheckOne(dividerSentence, errorSentence)
        makeDivision(dividend,divider)

    elif operator == 2:
        baseSentence = "Enter The Base Number:"
        exponentSentence = "Enter The Exponent Number"
        errorSentence = "Incorrect Entry! Base and Exponent Must Be Numbers."
        base, exponent = numberCheckTwo(baseSentence, exponentSentence, errorSentence)
        if base == 0 and exponent == 0:
            print("If Base and Exponent are Equal to Zero, This Exponentiation is Undefined!")
        else:
            result = base ** exponent
            print(f"Result of {base} base {exponent} is {result:.2f} ")

    elif operator == 3:
        numberSentence = "Enter The Number to Check Prime or Not:"
        errorSentence = "Incorrect Entry! Please Enter Positive Integers!"
        number = numberCheckOne(numberSentence, errorSentence)
        while number < 0:
            print("Incorrect Entry! Prime Numbers are Positive Integers! Please Enter Positive Integer.")
            number = numberCheckOne(numberSentence, errorSentence)

        for divider in range(2, int(number ** 0.5) + 1):
            if number % divider == 0:
                print(f"{number} is Not a Prime Number")
                break
        else:
            print(f"{number} is Prime Number")

    elif operator == 4:

        
def menuPrint():
    print(
        "1.Division"
        "2.Exponentiation"
        "3.Prime Number"
        "4.Dividers"
        "5.Root"
        "6.Root"
        "7.Combination"
        "8.Permutation"
        "9.Factorial"
    )

    operator = numberCheckOne("Please Enter The Number of Operation That You Want to Choose:",
                              "Incorrect Entry! Please Enter a Integer Between 1-9 to Choose Operation")

    while 9 < operator < 1:
        print("Incorrect Entry! Please Enter a Integer Between 1-9")
        operator = int(input("Please Enter The Number of Operation That You Want to Choose:"))

    return operator

def makeDivision(dividend, divider):
    remainder = dividend % divider
    quotient = dividend // divider
    division = dividend / divider
    fraction = f"{division.as_integer_ratio()[0]}/{division.as_integer_ratio()[1]}"
    print(
        f"Result = {division:.2f}   ({fraction})"
        f"\nQuotient = {quotient}"
        f"\nRemainder = {remainder}"
    )

def exponentiation(number, exponent):

def primeNumber(number):

def findDividers(dividend):

def takeRoot(number, root):

def combination(first,second):

def permutation(first,second):

def factorial(number):

def numberCheckTwo(sentence1, sentence2, sentence3):
    try:
        number1 = int(input(sentence1))
        number2 = int(input(sentence2))
    except TypeError:
        print(sentence3)
        number1 = int(input(sentence1))
        number2 = int(input(sentence2))
    return number1, number2

def numberCheckOne(sentence1, sentence2):
    try:
        number1 = int(input(sentence1))
    except TypeError:
        print(sentence2)
        number1 = int(input(sentence1))
    return number1