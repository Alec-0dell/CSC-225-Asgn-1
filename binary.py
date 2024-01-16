# Implements operations on binary numbers.
# CSC 225, Assignment 1
# Given code, Winter '23


def add(addend_a, addend_b):
    """
    Add two 8-bit, two's complement binary numbers; ignore carries/overflows.

    :param addend_a: A bitstring representing the first number
    :param addend_b: A bitstring representing the second number
    :return: A bitstring representing the sum
    """
    #ensure both inputs are strings of equal lengths only containing 1's and 0's
    aList = [*addend_a]
    bList = [*addend_b]
    carryover = 0
    output = ''
    for i in range(len(addend_a)):
        num1 = 1 if aList.pop() == "1" else 0 
        num2 = 1 if bList.pop() == "1" else 0           
        sum = (num1) + (num2) + carryover
        if sum == 0:
            carryover = 0
            output = '0' + output
        elif sum == 1:
            carryover = 0
            output = '1' + output
        elif sum == 2:
            carryover = 1
            output = '0' + output
        else:
            carryover = 1
            output = '1' + output
    return output


def negate(number):
    """
    Negate an 8-bit, two's complement binary number.
    TODO: Implement this function. Do *not* convert the number to decimal.

    :param number: A bitstring representing the number to negate
    :return: A bistring representing the negated number
    """
    num = flip(number)
    return add(num, "00000001")

def flip(number):
    numList = [*number]
    output=''
    for num in numList:
        if (num == "1"):
            output = output + '0'
        else:
            output = output + '1' 
    return output

def subtract(minuend, subtrahend):
    """
    Subtract one 8-bit, two's complement binary number from another.
    TODO: Implement this function. Do *not* convert the numbers to decimal.

    :param minuend: A bitstring representing the number from which to subtract
    :param subtrahend: A bitstring representing the number to subtract
    :return: A bitstring representing the difference
    """
    #Cheating way:
    #return (add(minuend, negate(subtrahend)))
    minList = [*minuend]
    subList = [*subtrahend]
    output = ''
    i = len(minList)-1
    while i >= 0:
        if minList[i] > subList[i]:
            output = '1' + output
        elif minList[i] < subList[i]:
            minList[:i] = carry_one(minList[:i])
            output = '1' + output 
        else: 
            output =  '0' + output
        i = i - 1
    return output
                
                
def carry_one(minList):
    i = len(minList) - 1
    while i >= 0:
        if minList[i] == '0':
            minList[i] = '1'
        elif minList[i] == '1':
            minList[i] = '0'
            return minList
        i = i - 1
    return minList
    
            
def binary_to_decimal(number):
    """
    Convert an 8-bit, two's complement binary number to decimal.
    TODO: Implement this function.

    :param number: A bitstring representing the number to convert
    :return: An integer, the converted number
    """
    output = 0
    isNeg = number[0] == '1'
    if isNeg:
        number = negate(number)
    numList = [*number]
    i = len(numList) - 1
    for num in numList:
        num1 = 1 if num == '1' else 0
        output = ((num1) * (2**i)) + output
        i = i - 1
    if isNeg:
        return -output
    else:
        return output

        



def decimal_to_binary(number):
    """
    Convert a decimal number to 8-bit, two's complement binary.
    TODO: Implement this function.

    :param number: An integer, the number to convert
    :return: A bitstring representing the converted number
    :raise OverflowError: If the number cannot be represented with 8 bits
    """
    if number > 127 or number < -128:
        raise OverflowError
    else:
        if number < 0:
            return negate(decimal_to_binary_pos(-number))
        else:
            return decimal_to_binary_pos(number)
        
def decimal_to_binary_pos(number):
    output = ""
    cur_number = number
    i = 7
    while i >= 0:
        if cur_number >= (2 ** i):
            output = output + '1'
            cur_number = cur_number - (2 ** i)
        else:
            output = output + '0'
        i = i - 1
    return output
            