# Implements operations on hexadecimal numbers.
# CSC 225, Assignment 1
# Given code, Winter '23


def binary_to_hex(number):
    """
    Convert a 16-bit binary number to 4-digit hexadecimal.
    TODO: Implement this function.

    :param number: A bitstring representing the number to convert
    :return: A 4-digit hexadecimal string, the converted number
    """
    numList = [number[:4], number[4:8], number[8:12], number[12:]]
    output = "0x"
    for num in numList:
        output = output + bit_to_char(num)
    return output
    
def bit_to_char(bits):
    output = 0
    numList = [*bits]
    i = len(numList) - 1
    for num in numList:
        num1 = 1 if num == '1' else 0
        output = ((num1) * (2**i)) + output
        i = i - 1
    match output:
        case 10:
            return 'A'
        case 11:
            return 'B'
        case 12:
            return 'C'
        case 13:
            return 'D'
        case 14:
            return 'E'
        case 15:
            return 'F'
        case 0: 
            return "0"
        case 1: 
            return "1"
        case 2: 
            return "2"
        case 3: 
            return "3"
        case 4: 
            return "4"
        case 5: 
            return "5"
        case 6: 
            return "6"
        case 7: 
            return "7"
        case 8: 
            return "8"
        case 9: 
            return "9"

def hex_to_binary(number):
    """
    Convert a 4-digit hexadecimal number to 16-bit binary.
    TODO: Implement this function.

    :param number: A 4-digit hexadecimal string, the number to convert
    :return: A bitstring representing the converted number
    """
    number = number[2:]
    output = ""
    for char in number:
        output = output + char_to_bin(char)
    return output
        
    
def char_to_bin(char):
    match char.upper():
        case 'A':
            char = 10 
        case 'B':
            char = 11  
        case 'C':
            char = 12  
        case 'D':
            char = 13  
        case 'E':
            char = 14  
        case 'F':
            char = 15  
        case '0': 
            char = 0
        case '1': 
            char = 1
        case '2': 
            char = 2
        case '3': 
            char = 3
        case '4': 
            char = 4
        case '5': 
            char = 5
        case '6': 
            char = 6
        case '7': 
            char = 7
        case '8': 
            char = 8
        case '9': 
            char = 9
            
        
            
    i = 3
    output = ''
    while i >= 0:
        if char >= (2 ** i):
            output = output + '1'
            char = char - (2 ** i)
        else:
            output = output + '0'
        i = i - 1
    return output
        