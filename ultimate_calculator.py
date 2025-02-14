import sys 
import colour

print("\n========COMPLETE PROGRAMMER'S CALCULATOR BY BIOZFROG========")
option = input("""Choose an option: 

    1. Denary into Binary
    2. Denary into Hexadecimal
    3. Denary into Octal
    4. Binary into Denary
    5. Binary into Hexadecimal
    6. Binary into Octal
    7. Hexadecimal into Binary
    8. Hexadecimal into Denary
    9. Hexadecimal into Octal
    10. Octal into Denary
    11. Octal into Binary
    12. Octal into Hexadecimal\n
O. other calculations.....

""").lower()
try:
    
    if option == "1":
        # Denary to Binary
        print("\n    - - - - - - - - - - - -")
        number = int(input("    Enter a Denary number: "))
        original_number = number
        bin_list = []
        while number > 0:
            remainder = number % 2
            bin_list.append(remainder)
            number = number // 2
        bin_list.reverse()
        binary = "".join(map(str, bin_list))
        while len(binary) % 4 != 0:
            binary = "0" + binary
        binary = " ".join(binary[i:i+4] for i in range(0, len(binary), 4))
        print(f"\n    The Binary for {original_number} is {binary}")
    elif option == "2":
        # Denary to Hexadecimal
        print("\n    - - - - - - - - - - - -")
        number = int(input("    Enter a Denary number: "))
        original_number = number
        remain_list = []
        hex_digits = "0123456789ABCDEF"
        while number > 0:
            remainder = number % 16
            remain_list.append(hex_digits[remainder]) 
            number = number // 16
        remain_list.reverse()
        hex_result = "".join(remain_list)
        print(f"\n    The Hex for {original_number} is {hex_result}")
        
    elif option == "3":
        # Denary to Octal
        print("\n    - - - - - - - - - - - -")
        number = int(input("    Enter a Denary number: "))
        original_number = number
        oct_list = []
        while number > 0:
            remainder = number % 8
            oct_list.append(remainder)
            number = number // 8
        oct_list.reverse()
        oct = "".join(map(str, oct_list))
        print(f"\n    The Hex value fo {original_number} is {oct}")
        
    elif option == "4":
        # Binary to Denary
        print("\n    - - - - - - - - - - - -")
        number = input("    Enter a Binary number: ")
        original_number = number
        if not all(char in "01" for char in original_number):
            sys.exit()
        power = 0
        denary_sum = 0
        for digit in reversed(number):
            digit = int(digit)
            denary = result = digit * (2 ** power)
            power +=1 
            denary_sum += denary
        print(f"\n    The Denary of {original_number} is {denary_sum}")
    elif option == "5":
        # Binary to Hex
        print("\n    - - - - - - - - - - - -")
        number = input(    "Enter a Binary number: ")
        original_number = number
        hex_num = ""
        if len(original_number) < 4 or not all(char in "01" for char in original_number):
            sys.exit()
        while len(number) % 4 != 0:
            sys.exit()
        chunks = [number[i:i+4] for i in range(0, len(number), 4)]
        for chunk in chunks:
            if chunk == "0000":
                hex_num += "0"
            elif chunk == "0001":
                hex_num += "1"
            elif chunk == "0010":
                hex_num += "2"
            elif chunk == "0011":
                hex_num += "3"
            elif chunk == "0100":
                hex_num += "4"
            elif chunk == "0101":
                hex_num += "5"
            elif chunk == "0110":
                hex_num += "6"
            elif chunk == "0111":
                hex_num += "7"
            elif chunk == "1000":
                hex_num += "8"
            elif chunk == "1001":
                hex_num += "9"
            elif chunk == "1010":
                hex_num += "A"
            elif chunk == "1011":
                hex_num += "B"
            elif chunk == "1100":
                hex_num += "C"
            elif chunk == "1101":
                hex_num += "D"
            elif chunk == "1110":
                hex_num += "E"
            elif chunk == "1111":
                hex_num += "F"
        print(f"\n    The Hex of {original_number} is {hex_num}")
    elif option == "6":
        # Binary to Octal
        print("\n    - - - - - - - - - - - -")
        number = input("    Enter a Binary number: ")
        original_number = number
        oct_num = ""
        if len(original_number) < 3 or not all(char in "01" for char in original_number):
            sys.exit()
        while len(number) % 3 != 0:
            number = "0" + number
        chunks = [number[i:i+3] for i in range(0, len(number), 3)]
        for chunk in chunks:
            if chunk == "000":
                oct_num += "0"
            elif chunk == "001":
                oct_num += "1"
            elif chunk == "010":
                oct_num += "2"
            elif chunk == "011":
                oct_num += "3"
            elif chunk == "100":
                oct_num += "4"
            elif chunk == "101":
                oct_num += "5"
            elif chunk == "110":
                oct_num += "6"
            elif chunk == "111":
                oct_num += "7"
        print(f"\n    The Hex of {original_number} is {oct_num}")
    elif option == "7":
        # Hex to Binary
        print("\n    - - - - - - - - -")
        number = input("    Enter a Hex value: ")
        original_number = number
        if not all(char in "0123456789ABCDEF" for char in original_number):
            sys.exit()
        bin_num = ""
        for digit in number:
            digit = str(digit)
            if digit == "0":
                bin_num += "0000 "
            elif digit == "1":
                bin_num += "0001 "
            elif digit == "2":
                bin_num += "0010 "
            elif digit == "3":
                bin_num += "0011 "
            elif digit == "4":
                bin_num += "0100 "
            elif digit == "5":
                bin_num += "0101 "
            elif digit == "6":
                bin_num += "0110 "
            elif digit == "7":
                bin_num += "0111 "
            elif digit == "8":
                bin_num += "1000 "
            elif digit == "9":
                bin_num += "1001 "
            elif digit == "A":
                bin_num += "1010 "
            elif digit == "B":
                bin_num += "1011 "
            elif digit == "C":
                bin_num += "1100 "
            elif digit == "D":
                bin_num += "1101 "
            elif digit == "E":
                bin_num += "1110 "
            elif digit == "F":
                bin_num += "1111 "
        print(f"\n    The Binary value of Hex {original_number} is {bin_num}")
    elif option == "8":
        # Hex to Denary
        print("\n    - - - - - - - - -")
        number = input("    Enter a Hex value: ").upper() 
        original_number = number
        denary_sum = 0
        for digit in number:
            if digit == "A":
                value = 10
            elif digit == "B":
                value = 11
            elif digit == "C":
                value = 12
            elif digit == "D":
                value = 13
            elif digit == "E":
                value = 14
            elif digit == "F":
                value = 15
            else:
                value = int(digit)
            denary_sum = denary_sum * 16 + value
        print(f"\n    The Decimal (Denary) value of Hex {original_number} is {denary_sum}")
    elif option == "9":
        # Hex to Octal (First hex to denary then denary to octal)
        print("\n    - - - - - - - - -")
        number = input("    Enter a Hex value: ")
        original_number = number
        denary_sum = 0
        oct_list = []
        for digit in number:
            if digit == "A":
                value = 10
            elif digit == "B":
                value = 11
            elif digit == "C":
                value = 12
            elif digit == "D":
                value = 13
            elif digit == "E":
                value = 14
            elif digit == "F":
                value = 15
            else:
                value = int(digit)
            denary_sum = denary_sum * 16 + value
        while denary_sum > 0:
            remainder = denary_sum % 8
            oct_list.append(remainder)
            denary_sum = denary_sum // 8
        oct_list.reverse()
        oct = "".join(map(str, oct_list))
        print(f"\n    The Hex value fo {original_number} is {oct}")
    elif option == "10":
        # Octal to Denary
        print("\n    - - - - - - - - - - ")
        number = input("    Enter a Octal number: ")
        original_number = number
        power = 0
        denary_sum = 0
        for digit in reversed(number):
            digit = int(digit)
            result = digit * (8 ** power)
            power +=1 
            denary_sum += result
        print(f"\n    The Denary of {original_number} is {denary_sum}")
    elif option == "11":
        # Octal to Binary
        print("\n    - - - - - - - - - - ")
        number = input("    Enter an Octal number: ")
        original_number = number
        bin_num = ""
        for digit in number:
            if digit == "0":
                bin_num += "000 "
            elif digit == "1":
                bin_num += "001 "
            elif digit == "2":
                bin_num += "010 "
            elif digit == "3":
                bin_num += "011 "
            elif digit == "4":
                bin_num += "100 "
            elif digit == "5":
                bin_num += "101 "
            elif digit == "6":
                bin_num += "110 "
            elif digit == "7":
                bin_num += "111 "
        bin_num = bin_num.rstrip()
        print(f"\n    The Binary of {original_number} is {bin_num}")
    elif option == "12":
        # Octal to Hexadecimal
        print("\n    - - - - - - - - - - ")
        number = input("    Enter an Octal number: ")
        original_number = number
        power = 0
        denary_sum = 0
        remain_list = []
        for digit in reversed(number):
            digit = int(digit)
            result = digit * (8 ** power)
            power +=1 
            denary_sum += result
        hex_digits = "0123456789ABCDEF"
        while denary_sum > 0:
            remainder = denary_sum % 16
            remain_list.append(hex_digits[remainder]) 
            denary_sum = denary_sum // 16
        remain_list.reverse()
        hex_result = "".join(remain_list)
        print(f"\n    The Binary of {original_number} is {hex_result}")
    elif option == "o" or option == "O":
        option_sec = input("""\n\nChoose any number system calculation:\n
        1. Two's Complement Format (4 bits representation)
        2. Logical Shifts
        3. Color Hex Code & RGB values """)
        if option_sec == "1":
            print("\n    - - - - - - - - ")
            num = int(input("    Enter a number: "))
            input = num
            original_number = num
            num = abs(num)
            bin_list = []
            answer = []
            inverted_num = ""
            while num > 0:
                remainder = num % 2
                bin_list.append(remainder)
                num = num // 2
            bin_list.reverse()
            binary = "".join(map(str, bin_list))
            while len(binary) % 4 != 0:
                binary = "0" + binary
            binary = " ".join(binary[i:i+4] for i in range(0, len(binary), 4))
            for char in binary:
                if char == "0":
                    inverted_num += "1"
                elif char == "1":
                    inverted_num += "0"
            original_number = inverted_num
            if not all(char in "01" for char in original_number):
                sys.exit()
            power = 0
            denary_sum = 0
            for digit in reversed(inverted_num):
                digit = int(digit)
                denary = result = digit * (2 ** power)
                power +=1 
                denary_sum += denary
            denary_sum += 1
            while denary_sum > 0:
                remainder = denary_sum % 2
                answer.append(remainder)
                denary_sum = denary_sum // 2
            answer.reverse()
            answer = "".join(map(str, answer))
            while len(answer) % 4 != 0:
                answer = "0" + answer
            answer = " ".join(answer[i:i+4] for i in range(0, len(answer), 4))
            print(f"\n    {input} ({original_number}) in Two's complement is {answer}")
        elif option_sec == "2":
            print("\n    - - - - - - - - ")
            bin_in = input("    Enter a Binary: ")
            inp = bin_in
            power = 0
            inp_denary = 0
            for digit in reversed(bin_in):
                digit = int(digit)
                denary = result = digit * (2 ** power)
                power +=1 
                inp_denary += denary
            bin_time = int(input(f"    How many times do you want to Shift {inp}: "))
            bin_side = input("    Which kind of Logical Shift would you like to execute? (Right, Left): ")
            bin_list = []
            if not all(char in "01" for char in bin_in):
                sys.exit()
            for char in bin_in:
                bin_list.append(int(char))
            
            if bin_side == "Right" or bin_side == "right" or bin_side == "r" or bin_side == "R":
                bin_list = [0] * bin_time + bin_list[:-bin_time]
                answer = "".join(map(str, bin_list))
                power = 0
                answer_denary = 0
                for digit in reversed(str(answer)):
                    digit = int(digit)
                    denary = result = digit * (2 ** power)
                    power +=1 
                    answer_denary += denary
                print(f"\n    {inp} ({inp_denary}) >> {bin_time} = {answer} ({answer_denary})")
            elif bin_side == "Left" or bin_side == "left" or bin_side == "l" or bin_side == "L":
                bin_list = bin_list[bin_time:]
                answer = "".join(map(str, bin_list))
                answer = answer + "0"
                power = 0
                answer_denary = 0
                for digit in reversed(str(answer)):
                    digit = int(digit)
                    denary = result = digit * (2 ** power)
                    power +=1 
                    answer_denary += denary
                print(f"\n    {inp} ({inp_denary}) << {bin_time} = {answer} ({answer_denary})")
        elif option_sec == "3":
            print("\n    - - - - - - - - - - ")
            color_name = input("    Enter a color name: ")
            rgb = colour.Color(color_name).rgb
            r = int(rgb[0]*255)
            g = int(rgb[1]*255)
            b = int(rgb[2]*255)
            hex_code = '#{:02x}{:02x}{:02x}'.format(r, g, b)
            print(f"    \nThe RGB value of {color_name} is ({r}, {g}, {b}) and Hex code is {hex_code}")

    else:
        print("\nIncorrect Input Detected.")
except:
    print("\nIncorrect Input Detected.")
