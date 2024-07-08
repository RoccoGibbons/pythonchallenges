from math import log, ceil

def main():
    convert = input("Would you like to convert between denary and binary(1), denary and hex(2), or binary and hex(3) ")
    
    result = ""

    if convert == "1":
        convert2 = input("Would you like to convert denary to binary(1), or binary to denary(2)? ")

        if convert2 == "1":
            result = d_to_b()
        elif convert2 == "2":
            result = b_to_d()
        else:
            print("Input a valid option")
    
    elif convert == "2":
        convert2 = input("Would you like to convert denary to hex(1), or hex to denary(2) ")

        if convert2 == "1":
            result = "0x" + d_to_h()
        elif convert2 == "2":
            result = h_to_d()
        else:
            print("Input a valid option")

    elif convert == "3":
        convert2 = input("Would you like to convert binary to hex(1), or hex to binary(2) ")

        if convert2 == "1":
            result = "0x" + b_to_h()
        elif convert2 == "2":
            result = h_to_b()
            print()
        else:
            print("Input a valid option")

    else:
        print("Input a valid option")
    
    print(result)


def num_input():
     while True:
        try:
            num = int(input("Please input your whole denary number: "))
        except ValueError:
            print("Input a valid number")
            continue
        else:
            break
     return num


def binary_input(): 
    invalid_nums = ['2', '3', '4', '5', '6', '7', '8', '9']
    while True:
        valid = True
        
        binary = input("Please input your binary number: ")
        try:
            int(binary)
        except ValueError:
            print("Input a valid binary number")
            continue
        else:
            for n in binary:
                if n in invalid_nums:
                    valid = False
            if valid == False:
                print("Input a valid binary number")
                continue
            break
    return binary


def hexadecimal_input():
    valid_chars = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    while True:
        valid = True

        hexadecimal = input("Please input your hexadecimal number: ")
        hexadecimal = hexadecimal.upper()

        if hexadecimal[:2] == "0X":
            hexadecimal = hexadecimal[2:]
        
        for c in hexadecimal:
            if c not in valid_chars:
                valid = False
        if valid == False:
            print("Input a valid hexadecimal number")
            continue

        return hexadecimal


def d_to_b():
    num = num_input()
    bits = num_of_bits_bin(num)
    binary = ""
    
    for i in range(bits - 1, -1, -1):
        maxi = pow(2, i)
        if (num / maxi) >= 1:
            binary += "1"
            num = num - maxi
        else:
            binary += "0"

    return binary
        

def b_to_d():
    binary = binary_input()

    num = 0
    column = 1

    for i in range(len(binary) - 1, -1, -1):
        num += int(binary[i]) * column
        column *= 2

    return num


def d_to_h():
    num = num_input()
    bits = num_of_bits_hex(num)
    hexa = ""

    for i in range(bits - 1, -1, -1):
        maxi = pow(16, i)
        digit = num // maxi
        if digit < 10:
            hexa += str(digit)
        else:
            match digit:
                case 10:
                    hexa += "A"
                case 11:
                    hexa += "B"
                case 12:
                    hexa += "C"
                case 13:
                    hexa += "D"
                case 14:
                    hexa += "E"
                case 15:
                    hexa += "F"
                case _:
                    print("Something went wrong - d to h match statement")
        num -= (maxi * digit)
    
    return hexa


def h_to_d():
    hexa = hexadecimal_input()
    num = 0
    length = len(hexa)

    for i in range(length):
        column = pow(16, length - i - 1)
        if hexa[i].isdigit():
            num += column * int(hexa[i])
            continue
        match hexa[i]:
            case "A":
                num += column * 10
            case "B":
                num += column * 11
            case "C":
                num += column * 12
            case "D":
                num += column * 13
            case "E":
                num += column * 14
            case "F":
                num += column * 15
            case _:
                print("Something went wrong - h to d match statement")
    return num


def b_to_h():
    binary = binary_input()
    length = len(binary)
    zeroCount = 4 - (length % 4)
    if zeroCount == 4:
        zeroCount = 0
    fullLengthBinary = "0" * zeroCount + binary
    length = len(fullLengthBinary)

    groups = []
    start, end = 0, 4

    for i in range(int(length / 4)):
        groups.append(fullLengthBinary[start: end])
        start += 4
        end += 4
    
    hexa = ""

    for binary in groups:
        num = 0
        counter = 3
        for j in binary:
            column = pow(2, counter)
            if j == "1":
                num += column
            counter -= 1

        if num < 10:
            hexa += str(num)
            continue
        match num:
            case 10:
                hexa += "A"
            case 11:
                hexa += "B"
            case 12:
                hexa += "C"
            case 13:
                hexa += "D"
            case 14:
                hexa += "E"
            case 15:
                hexa += "F"
            case _:
                print("Something went wrong - b to h match")
    return hexa


def h_to_b():
    hexa = hexadecimal_input()
    binary = ""

    for n in hexa:
        if n.isdigit():
            num = int(n)
        else:
            match n:
                case "A":
                    num = 10
                case "B":
                    num = 11
                case "C":
                    num = 12
                case "D":
                    num = 13
                case "E":
                    num = 14
                case "F":
                    num = 15
        column = 8
        for i in range(4):
            if (num / column) >= 1:
                binary += "1"
                num -= column
            else:
                binary += "0"
            column /= 2
    return str(int(binary))


def num_of_bits_bin(num):
    bits = ceil(log2(num, 2))
    return bits


def num_of_bits_hex(num):
    bits = ceil(log(num, 16))
    return bits


main()
