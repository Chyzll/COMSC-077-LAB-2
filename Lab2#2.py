# GROUP 9: Duy Luu, Kristine Nguyen, Nitya Prasad
# 2025SP-COMSC-077
# Lab 2 #2
# This program aims to converts a signed integer between signed magnitude and 2's complement. The input could be signed magnitude or 2's complement

def validateInput(inputNumber, inputType):
    if ((inputType != "1") and (inputType != "2")): # makes sure they inputted 1 or 2 for the type
        print("Please input either 1 or 2 for the type!")
        return False
    if (len(inputNumber) != 8): # making sure its 8 characters
        print("Please input 8 characters!")
        return False
    for character in inputNumber: # loop thru every character in the string
        if character not in "01":
            print("Invalid input! Please input only 0 or 1!")
            return False
    # if it gets here then it passed all the checks
    return True

def invert(inputNumber):
    # Keeping the first bit unchanged but inverting the rest of them
    return inputNumber[0] + ''.join('1' if bit == '0' else '0' for bit in inputNumber[1:])

def conversionFunction(inputNumber):
    if (inputNumber.startswith("0")): # if it starts with 0 then it is positive and since positive numbers have the same format in signed magnitude and 2's complement then the string doesn't change
        return inputNumber
    
    invertedNumber = invert(inputNumber)
    # print(invertedNumber)

    carryOver = 1
    resultantString = ""
    for i in range(len(invertedNumber) - 1, -1, -1): # loop thru every character [EXCEPT for the first] in the string going backwards
        bit = int(invertedNumber[i]) + carryOver # adding one to the integer value of the bit which is either 0 or 1
        if bit == 1: # cancel the carryOver
            carryOver = 0
        elif bit == 2: # continue the carryOver
            bit = bit % 2
            carryOver = 1

        resultantString = str(bit) + resultantString
    
    return resultantString

# Starting function
def askInput():
    # failInput = False
    while (True): # (failInput == False):
        inputNumber = input("Input an 8-bit binary string!: ")
        inputType = input("Is this [1] 2's complement or [2] Signed magnitude?:")
        isValid = validateInput(inputNumber, inputType)
        if (isValid == True):
            break # failInput = True
    convertedValue = conversionFunction(inputNumber)
    print(convertedValue)

    redo = input("Would you like to run the program again?: [Y/N]")
    if str.upper(redo) == "Y":
        askInput()

askInput()