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
O. Other calculations.....
M. Methods of Conversions.....

""").lower()
try:
    
    if option == "1":
        # Denary to Binary
        print("\n    - - - - - - - - - - - -")
        number = int(input("    Enter a Denary number: "))
        original_number = number
        print(f"    We will divide the number ({number}) by 2 until we reach 0, and keep track of the remainders. See the steps below:\n")


        bin_list = []
        step = 1
        while number > 0:
            print(f"    Step {step}:")
            print(f"       Number: {number}")
            remainder = number % 2
            print(f"       Remainder when divided by 2 is {remainder} : ({number} // 2 = {remainder})")

            bin_list.append(remainder)
            number = number // 2
            print(f"       Result of division: {number}\n")
            step += 1

        bin_list.reverse()
        binary = "".join(map(str, bin_list))
        while len(binary) % 4 != 0:
            binary = "0" + binary
        binary = " ".join(binary[i:i+4] for i in range(0, len(binary), 4))

        print(f"\n    The remainders in reverse order give us the binary representation:")
        print(f"    The Binary for {original_number} is {binary}")
    elif option == "2":
        # Denary to Hexadecimal
        print("\n    - - - - - - - - - - - -")
        number = int(input("    Enter a Denary number: "))
        print(f"    \nWe will divide the number ({number}) by 16 until we reach 0, and keep track of the remainders. See the steps below:\n")
        original_number = number
        remain_list = []
        step = 1
        hex_digits = "0123456789ABCDEF"
        while number > 0:
            print(f"    Step {step}:")
            print(f"       Number: {number}")
            remainder = number % 16
            print(f"       Remainder when divided by 16 is {remainder} ({hex_digits[remainder]}) : ({number} // 16 = {remainder})")
            remain_list.append(hex_digits[remainder]) 
            number = number // 16
            print(f"       Result of division: {number}\n")
            step += 1

        remain_list.reverse()
        hex_result = "".join(remain_list)
        print(f"\n    The remainders in reverse order give us the hex representation:")
        print(f"    The Hex for {original_number} is {hex_result}")
        
    elif option == "3":
        # Denary to Octal
        print("\n    - - - - - - - - - - - -")
        number = int(input("    Enter a Denary number: "))
        print(f"   \n We will divide the number ({number}) by 8 until we reach 0, and keep track of the remainders. See the steps below:\n")

        original_number = number
        oct_list = []
        step = 1
        while number > 0:
            print(f"    Step {step}:")
            print(f"       Number: {number}")
            remainder = number % 8
            print(f"       Remainder when divided by 8 is {remainder}")
            print(f"       Remainder when divided by 8 is {remainder} : ({number} // 8 = {remainder})")
            oct_list.append(remainder)
            number = number // 8
            print(f"       Result of division: {number}\n")
            step += 1
        oct_list.reverse()
        oct = "".join(map(str, oct_list))
        print(f"\n    The remainders in reverse order give us the octal representation:")
        print(f"    The Octal value for {original_number} is {oct}")
        
    elif option == "4":
        # Binary to Denary
        print("\n    - - - - - - - - - - - -")
        number = input("    Enter a Binary number: ")
        original_number = number
        if not all(char in "01" for char in original_number):
            print("    Invalid Binary number.")
            sys.exit()
        print("    We will multiply each binary digit by 2 raised to the power of its position (starting from 0). See the steps below:\n")
        power = 0
        step = 1
        denary_sum = 0
        for digit in reversed(number):
            print(f"    Step {step}:")
            digit = int(digit)
            denary = result = digit * (2 ** power)
            power +=1 
            denary_sum += denary
            step += 1
            print(f"       Result of multiplication: {denary} (2^{power-1} = {denary})\n")

        print(f"    The sum of all the results gives us the Denary representation:")
        print(f"    The Denary of {original_number} is {denary_sum}")
    elif option == "5":
        # Binary to Hex
        print("\n    - - - - - - - - - - - -")
        number = input("    Enter a Binary number: ")
        original_number = number
        if not all(char in "01" for char in original_number):
            print("    Invalid Binary number.")
            sys.exit()
        print(f"\n    We will first divide the binary into 4 chunks, and then use the Hexadecimal Table to convert. See the steps below:\n")
        print("    Binary to Hexadecimal Table:")
        print("      -0000 -> 0")
        print("      -0001 -> 1")
        print("      -0010 -> 2")
        print("      -0011 -> 3")
        print("      -0100 -> 4")
        print("      -0101 -> 5")
        print("      -0110 -> 6")
        print("      -0111 -> 7")
        print("      -1000 -> 8")
        print("      -1001 -> 9")
        print("      -1010 -> A")
        print("      -1011 -> B")
        print("      -1100 -> C")
        print("      -1101 -> D")
        print("      -1110 -> E")
        print("      -1111 -> F\n")

        print(f"    Step 1:")
        print(f"      Break the binary number ({number}) into chunks of 4 bits each : {" ".join([number[i:i+4] for i in range(0, len(number), 4)])}")

        hex_num = ""
        step = 1

        while len(number) % 4 != 0:
            number = "0" + number

        chunks = [number[i:i+4] for i in range(0, len(number), 4)]
        binary_to_hex = {
            "0000": "0", "0001": "1", "0010": "2", "0011": "3",
            "0100": "4", "0101": "5", "0110": "6", "0111": "7",
            "1000": "8", "1001": "9", "1010": "A", "1011": "B",
            "1100": "C", "1101": "D", "1110": "E", "1111": "F"
        }

        for step, chunk in enumerate(chunks, start=1):
            print(f"    Step {step+1}:")
            print(f"       Chunk {chunk} is equal to {binary_to_hex[chunk]}")
            hex_num += binary_to_hex[chunk]

        print(f"\n    Combine all the digits to get the Hexadecimal representation:")
        print(f"    The Hex of {original_number} is {hex_num}")
    elif option == "6":
        # Binary to Octal
        print("\n    - - - - - - - - - - - -")
        number = input("    Enter a Binary number: ")
        original_number = number
        if not all(char in "01" for char in original_number):
            print("    Invalid Binary number.")
            sys.exit()
        print(f"   \n We will first divide the binary into 3 chunks, and then use the Octal Table to convert. See the steps below:\n")
        print("    Binary to Octal Table:")
        print("      -000 -> 0")
        print("      -001 -> 1")
        print("      -010 -> 2")
        print("      -011 -> 3")
        print("      -100 -> 4")
        print("      -101 -> 5")
        print("      -110 -> 6")
        print("      -111 -> 7")
        oct_num = ""

        print(f"    Step 1:")
        print(f"       Break  the binary number ({number}) into chunks of 3 bits each : {" ".join([number[i:i+3] for i in range(0, len(number), 3)])}")

        binary_to_octal = {
            "000": "0", "001": "1", "010": "2", "011": "3",
            "100": "4", "101": "5", "110": "6", "111": "7",
        }
        while len(number) % 3 != 0:
            number = "0" + number
        chunks = [number[i:i+3] for i in range(0, len(number), 3)]
        for step, chunk in enumerate(chunks, start=0):
            print(f"    Step {step+1}:")
            print(f"      Chunk {chunk} is equal to {binary_to_octal[chunk]}")
            oct_num += binary_to_octal[chunk]

        print(f"\n    Combine all the digits to get the Hexadecimal representation:")
        print(f"    The Octal of {original_number} is {oct_num}")
    elif option == "7":
        # Hex to Binary
        print("\n    - - - - - - - - -")
        number = input("    Enter a Hex value: ").upper()
        print(f"\n    We will convert each Hex digit to its 4-bit binary equivalent using the Hexadecimal Table below. See the steps below:\n")
        print("    Hexadecimal to Binary Table:")
        print("      -0000 -> 0")
        print("      -0001 -> 1")
        print("      -0010 -> 2")
        print("      -0011 -> 3")
        print("      -0100 -> 4")
        print("      -0101 -> 5")
        print("      -0110 -> 6")
        print("      -0111 -> 7")
        print("      -1000 -> 8")
        print("      -1001 -> 9")
        print("      -1010 -> A")
        print("      -1011 -> B")
        print("      -1100 -> C")
        print("      -1101 -> D")
        print("      -1110 -> E")
        print("      -1111 -> F\n")
        original_number = number
        if not all(char in "0123456789ABCDEF" for char in original_number):
            print("    Invalid Hexadecimal number.")
            sys.exit()
        bin_num = ""
        step = 1
        hex_to_binary = {
            "0": "0000", "1": "0001", "2": "0010", "3": "0011",
            "4": "0100", "5": "0101", "6": "0110", "7": "0111",
            "8": "1000", "9": "1001", "A": "1010", "B": "1011",
            "C": "1100", "D": "1101", "E": "1110", "F": "1111"
        }
        for step, digit in enumerate(original_number.upper(), start=1):
            print(f"    Step {step}:")
            print(f"       Hex digit {digit} is equal to its binary equivalent: {hex_to_binary[digit]}")
            bin_num += hex_to_binary[digit] + " "

        print(f"\n    Combine all the binary digits to get the binary representation:")
        print(f"    The Binary value of Hex {original_number} is {bin_num.strip()}")
    elif option == "8":
        # Hex to Denary
        print("\n    - - - - - - - - -")
        number = input("    Enter a Hex value: ").upper() 
        print("    We will multiply each hex digit by 16 raised to the power of its position (starting from 0). See the steps below:\n")
        original_number = number
        if not all(char in "0123456789ABCDEF" for char in original_number):
            print("    Invalid Hexadecimal number.")
            sys.exit()
        denary_sum = 0
        step = 1
        hex_into_denary={"A": "1010", "B": "1011",
            "C": "1100", "D": "1101", "E": "1110", "F": "1111"
        }

        denary_sum = 0
        for step, digit in enumerate(original_number.upper(), start=1):
            print(f"    Step {step}:")
            print(f"       Hex digit {digit} is equal to its denary equivalent: {int(digit, 16)}")
            denary_sum = denary_sum * 16 + int(digit, 16)
        print(f"\n    Combine all the results to get the denary representation:")
        print(f"    The Decimal (Denary) value of Hex {original_number} is {denary_sum}")
    elif option == "9":
        # Hex to Octal (First hex to denary then denary to octal)
        print("\n    - - - - - - - - -")
        number = input("    Enter a Hex value: ")
        original_number = number
        if not all(char in "0123456789ABCDEF" for char in original_number):
            print("    Invalid Hexadecimal number.")
            sys.exit()
        denary_sum = 0
        oct_list = []
        print("    We will first convert Hex into denary. So we will first multiply each hex digit by 16 raised to the power of its position (starting from 0). See the steps below:\n")
        step = 1
        hex_into_denary={"A": "1010", "B": "1011",
            "C": "1100", "D": "1101", "E": "1110", "F": "1111"
        }

        denary_sum = 0
        for step, digit in enumerate(original_number.upper(), start=1):
            print(f"    Step {step}:")
            print(f"       Hex digit {digit} is equal to its denary equivalent: {int(digit, 16)}")
            denary_sum = denary_sum * 16 + int(digit, 16)
        
        print(f"\n    Combine all the results to get the denary representation:")
        print(f"    The Denary value of Hex {original_number} is {denary_sum}\n")
        print(f"\n    We will divide the number ({denary_sum}) by 8 until we reach 0, and keep track of the remainders. See the steps below:\n")
        while denary_sum > 0:
            print(f"    Step {step}:")
            step += 1
            print(f"       Number: {number}")
            remainder = denary_sum % 8
            print(f"       Remainder when divided by 8 is {remainder} : ({number} // 8 = {remainder})")
            oct_list.append(remainder)
            denary_sum = denary_sum // 8
            print(f"       Result of division: {number}\n")
        oct_list.reverse()
        oct = "".join(map(str, oct_list))
        
        print(f"\n    The remainders in reverse order give us the octal representation:")
        print(f"    The Hex value fo {original_number} is {oct}")
    elif option == "10":
        # Octal to Denary
        print("\n    - - - - - - - - - - ")
        number = input("    Enter a Octal number: ")
        original_number = number
        if any(char in "89" for char in original_number):
            sys.exit()
        print(f"    We will multiply each octal digit by 8 raised to the power of its position (starting from 0). See the steps below:\n")

        
        power = 0
        step = 1
        denary_sum = 0
        for digit in reversed(number):
            print(f"    Step {step}:")
            step += 1
            print(f"       Number: {number}")
            digit = int(digit)
            result = digit * (8 ** power)
            print(f"       Result of multiplication: {result} (8^{power} = {result})")
            power +=1 
            denary_sum += result
        print(f"\n    The sum of all the results gives us the denary representation:")
        print(f"\n    The Denary of {original_number} is {denary_sum}")
    elif option == "11":
        # Octal to Binary
        print("\n    - - - - - - - - - - ")
        number = input("    Enter an Octal number: ")
        original_number = number
        if any(char in "89" for char in original_number):
            sys.exit()
        print(f"   \n We will convert each Octal digit to its 3-bit binary equivalent using the Octal Table below. See the steps below:\n")
        
        print("    Octal to Binary Table:")
        print("      -000 -> 0")
        print("      -001 -> 1")
        print("      -010 -> 2")
        print("      -011 -> 3")
        print("      -100 -> 4")
        print("      -101 -> 5")
        print("      -110 -> 6")
        print("      -111 -> 7")
        bin_num = ""
        octal_to_binary = {
            "0": "000", "1": "001", "2": "010", "3": "011",
            "4": "100", "5": "101", "6": "110", "7": "111",
        }
        
        for step, chunk in enumerate(number, start=1):
                print(f"\n  Step {step}:")
                print(f"       Row (of Octal to Binary Table) number {chunk} is used : {octal_to_binary[chunk]}")
                bin_num += octal_to_binary[chunk]

        print(f"\n    The chunks used in reverse order gives us the binary representation:")
        print(f"    The Binary of {original_number} is {bin_num}")
    elif option == "12":
        # Octal to Hexadecimal
        print("\n    - - - - - - - - - - ")
        number = input("    Enter an Octal number: ")
        original_number = number
        
        if any(char in "89" for char in original_number):
            sys.exit()

        print(f" \n We will first convert Octal into denary. So we will first multiply each octal digit by 8 raised to the power of its position (starting from 0). See the steps below:\n")
        power = 0
        denary_sum = 0
        step = 1

        for digit in reversed(number):
            print(f"    Step {step}:")
            step += 1
            print(f"       Digit: {digit}")
            digit = int(digit)
            result = digit * (8 ** power)
            print(f"       Result of multiplication: {result} ({digit} * 8^{power} = {result})")
            power += 1
            denary_sum += result

        print(f"\n The sum of all the results gives us the denary representation:")
        print(f" The Denary of {original_number} octal is {denary_sum}\n")

        print(f" \n We will divide the number ({denary_sum}) by 16 until we reach 0, and keep track of the remainders. See the steps below:\n")
        hex_digits = "0123456789ABCDEF"
        remain_list = []
        step = 1
        number = denary_sum  

        while number > 0:
            print(f"    Step {step}:")
            print(f"       Number: {number}")
            remainder = number % 16
            print(f"       Remainder when divided by 16 is {remainder} ({hex_digits[remainder]}) : ({number} // 16 = {remainder})")
            remain_list.append(hex_digits[remainder])
            number = number // 16
            print(f"       Result of division: {number}\n")
            step += 1

        remain_list.reverse()
        hex_result = "".join(remain_list)

        print(f"\n    The remainders in reverse order give us the hex representation:")
        print(f"    The hex of {original_number} is {hex_result}")
    elif option == "o" or option == "O":
        option_sec = input("""\n\nChoose any number system calculation:\n
        1. Two's Complement Format (4 bits representation)
        2. Logical Shifts
        3. Color Hex Code & RGB values """)
        if option_sec == "1":
            print("\n    - - - - - - - - ")
            num = int(input("    Enter a number: "))
            print(f"\n    We will first convert the number into binary. So we will divide the number ({num}) by 2 until we reach 0, and keep track of the remainders.. See the steps below:\n")
            input = num
            original_number = num
            num = abs(num)
            bin_list = []
            answer = []
            inverted_num = ""
            step = 1
            while num > 0:
                print(f"    Step {step}:")
                print(f"       Number: {num} absolute value of {original_number}" if input < 0 else f"       Number: {num}")
                remainder = num % 2
                print(f"       Remainder when divided by 2 is {remainder} : ({num} // 2 = {remainder})")
                bin_list.append(remainder)
                num = num // 2
                print(f"       Result of division: {num}\n")
                step += 1
            bin_list.reverse()
            binary = "".join(map(str, bin_list))
            print(f"\n    We will now invert the binary digits.\n")
            original_binary = binary
            while len(binary) % 4 != 0:
                binary = "0" + binary
            binary = " ".join(binary[i:i+4] for i in range(0, len(binary), 4))
            for char in binary:
                if char == "0":
                    inverted_num += "1"
                elif char == "1":
                    inverted_num += "0"
            original_numbers = inverted_num
            if not all(char in "01" for char in original_numbers):
                sys.exit()
            power = 0
            denary_sum = 0
            powers = 0
            denary_sums = 0
            print(f"    Inverted binary digits of {binary} ({input}) is {original_numbers} ({denary_sums})\n")
            for digits in reversed(original_numbers):
                digits = int(digits)
                denarye = result = digits * (2 ** powers)
                powers +=1 
                denary_sums += denarye
            print(f"    We will now add 1 (0001) to the inverted binary to get the Two's complement representation: ")
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
            print(f"\n    {original_numbers} ({denary_sums}) + 0001 (1) = {answer} ({denary_sums + 1})")
            print(f"    The Two's Complement representation of {input} is {answer} ({denary_sums + 1})")
        elif option_sec == "2":
            print("\n    - - - - - - - - ")
            bin_in = input("    Enter a Binary: ")
            if not all(char in "01" for char in bin_in):
                print("    Invalid Binary number.")
                sys.exit()
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
            print(f"\n    We will shift each binary digit of ({inp}) by {bin_time} times to the {bin_side} side." if bin_time > 1 else f"\n    We will shift each binary digit of ({inp}) by {bin_time} time to the {bin_side} side.")
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
                print(f"\n    {inp} ({inp_denary}) when is logically shifted {bin_time} times to {bin_side} is equal to {answer} ({answer_denary}) : {inp} ({inp_denary}) >> {bin_time} = {answer} ({answer_denary})" if bin_time > 1 else f"\n    {inp} ({inp_denary}) when is logically shifted {bin_time} time to {bin_side} is equal to {answer} ({answer_denary}) : {inp} ({inp_denary}) >> {bin_time} = {answer} ({answer_denary})")
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
                print(f"\n    {inp} ({inp_denary}) when is logically shifted {bin_time} times to {bin_side} is equal to {answer} ({answer_denary}) : {inp} ({inp_denary}) << {bin_time} = {answer} ({answer_denary})" if bin_time > 1 else f"\n    {inp} ({inp_denary}) when is logically shifted {bin_time} time to {bin_side} is equal to {answer} ({answer_denary}) : {inp} ({inp_denary}) << {bin_time} = {answer} ({answer_denary})")
        elif option_sec == "3":
            print("\n    - - - - - - - - - - ")
            color_name = input("    Enter a color name: ")
            rgb = colour.Color(color_name).rgb
            r = int(rgb[0]*255)
            g = int(rgb[1]*255)
            b = int(rgb[2]*255)
            hex_code = '#{:02x}{:02x}{:02x}'.format(r, g, b)
            print(f"\n    The RGB value of {color_name} is ({r}, {g}, {b}) and Hex code is {hex_code}")
    elif option == "m" or option == "M":
        option_sec = input("""Choose an conversation: 

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
        12. Octal into Hexadecimal\n""")

        if option_sec == "1":
            print("\n    Method 1:")
            print("       We will first find the largest power of 2 that is less than or equal to the denary number. Then, we will repeatedly subtract powers of 2 from the denary number until we reach zero.\n       Then, we will record the powers of 2 that were used, representing each used power of 2 with a 1 and unused powers with a 0. Then, reading the digits from bottom to top (in reverse)\n       will give us the binary representation.\n")
            print("    Example:")
            print("       Denary: 142\n")
            print("       => 142 - 128 (2^7) = 14")
            print("       => 14 - 8 (2^3) = 6")
            print("       => 6 - 4 (2^2) = 2")
            print("       => 2 - 2 (2^1) = 0\n")
            print("       2^0 = 1 ---------> 0 (Not used)")
            print("       2^1 = 2 ---------> 1 (Used)")
            print("       2^2 = 4 ---------> 1 (Used)")
            print("       2^3 = 8 ---------> 1 (Used)")
            print("       2^4 = 16 ---------> 0 (Not used)")
            print("       2^5 = 32 ---------> 0 (Not used)")
            print("       2^6 = 64 ---------> 0 (Not used)")
            print("       2^7 = 128 ---------> 1 (Used)\n")
            print("       10001110 = 142")

            print("\n    Method 2:")
            print("       We will repeatedly divide the denary number by 2 until we hit zero. Then, any division leaving behind any remainder will be represented as 1, and vice versa. Then, reading the digits\n       from bottom to top (in reverse) will give use the binary representation. \n")
            print("    Example:")
            print("       Denary: 142\n")
            print("       => 142 / 2 = 71 ---------> No remainder 0")
            print("       => 71 / 2 = 35 ---------> Remainder 1")
            print("       => 35 / 2 = 17 ---------> Remainder 1")
            print("       => 17 / 2 = 8 ---------> Remainder 1")
            print("       => 8 / 2 = 4 ---------> No remainder 0")
            print("       => 4 / 2 = 2 ---------> No remainder 0")
            print("       => 2 / 2 = 1 ---------> No remainder 0")
            print("       => 1 / 2 = 0 ---------> Remainder 1\n")
            print("       10001110 = 142")
        
        elif option_sec == "2":
            print("\n   We will repeatedly divide the denary number by 16 until we reach zero, calculating the remainder at each step. Then, reading the remainders from bottom to top (in reverse order) will\n   give us the hexadecimal representation.\n")
            print("     Following is the Hexadecimal Table:\n")
            print("       -0 -> 0")
            print("       -1 -> 1")
            print("       -2 -> 2")
            print("       -3 -> 3")
            print("       -4 -> 4")
            print("       -5 -> 5")
            print("       -6 -> 6")
            print("       -7 -> 7")
            print("       -8 -> 8")
            print("       -9 -> 9")
            print("       -10 -> A")
            print("       -11 -> B")
            print("       -12 -> C")
            print("       -13 -> D")
            print("       -14 -> E")
            print("       -15 -> F\n")

            print("    Example:")
            print("       Denary: 7076236\n")
            print("       => 7076236 / 16 = 442264 (7076236 - (442264 x 16)) --------->  12 (C)")
            print("       => 442264 / 16 = 27641 (442264 - (27641 x 16)) --------->  8")
            print("       => 27641 / 16 = 1727 (27641 - (1727 x 16)) --------->  9")
            print("       => 1727 / 16 = 107 (1727 - (107 x 16)) --------->  15 (F)")
            print("       => 107 / 16 = 6 (107 - (6 x 16)) --------->  11 (B)")
            print("       => 6  / 16 = 0 (6 - (0 x 16)) --------->  6")
            print("       7076236 = 6BF98C")
    else:
        print("\nIncorrect Input Detected.")
except:
    print("\nIncorrect Input Detected.")
