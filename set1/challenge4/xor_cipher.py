#! /usr/bin/env python3

# Filename: xor_cipher.py
# Function: To find the key, decrypt the message from a single-byte XOR cipher given.

# There are 2 methods defined to break this cipher:
# 1. Brute forcing through all 1 - 255 numbers
# 2. Frequency Analysis

# Cryptopals - Set1 - Problem3
# Cryptopals Link: http://cryptopals.com/sets/1/challenges/3
# Link to my blogpost: 

# Author: Adwaith Gautham

# License: MIT (Link: https://mit-license.org/)
# Use it, play with it and learn from it!

# Run like this:    $ chmod u+x xor_cipher.py
#                   $ ./xor_cipher.py InputFile > OutputFile



import sys


def err_exit(errmsg) : 
    print(errmsg)
    sys.exit()


def usage(argv0) : 
    print("Usage: $ ", argv0, "InputFile > OutputFile")
    print("\nInstruction: ")
    print("1. The Input is assumed to be a hex-encoded string")
    print("2. Output will be both in raw and hex form")



class xor_cipher: 

    def __init__(self) : 

        self.standard_frequency_table = {    'a' : 8.167, 
                                    'b' : 1.492, 
                                    'c' : 2.782, 
                                    'd' : 4.253, 
                                    'e' : 12.702, 
                                    'f' : 2.228, 
                                    'g' : 2.015, 
                                    'h' : 6.094, 
                                    'i' : 6.966, 
                                    'j' : 0.153, 
                                    'k' : 3.872, 
                                    'l' : 4.025, 
                                    'm' : 2.406, 
                                    'n' : 6.749, 
                                    'o' : 7.507, 
                                    'p' : 1.929, 
                                    'q' : 0.095, 
                                    'r' : 5.987, 
                                    's' : 6.327, 
                                    't' : 9.256, 
                                    'u' : 2.758, 
                                    'v' : 0.978, 
                                    'w' : 5.370, 
                                    'x' : 0.150, 
                                    'y' : 3.978, 
                                    'z' : 0.074
                }

    def frequency_method(self, input_filename) : 
        
        try: 
            input_file = open(input_filename, 'r')
        except: 
            err_exit("Error: Unable top open InputFile")
    
        hex_input_data = input_file.read()
        
        try: 
            raw_input_data = bytes.fromhex(hex_input_data)
        except: 
            hex_input_data = hex_input_data[ : len(hex_input_data) - 1]
            raw_input_data = bytes.fromhex(hex_input_data)


        input_length = len(raw_input_data)
        
        freq_table = dict()

        print("raw_input_data: ", raw_input_data)

        counter = 0

        while counter < input_length: 
            
            if raw_input_data[counter] in list(freq_table): 
                freq_table[raw_input_data[counter]] = freq_table[raw_input_data[counter]] + 1

            else : 
                freq_table[raw_input_data[counter]] = 1

            counter = counter + 1

        for raw_byte in raw_input_data: 
            print(raw_byte, end=' ')
        print('\n')


        for raw_byte, freq in freq_table.items() : 
            print("raw_byte = ", raw_byte, ", freq = ", freq)


    def bruteforce_method(self, input_filename) : 

        try: 
            input_file = open(input_filename, 'r')
        except: 
            err_exit("Error: Unable to open InputFile")


        hex_input_data = input_file.read()
    
        try: 
            raw_input_data = bytes.fromhex(hex_input_data)
        except: 
            hex_input_data = hex_input_data[ : len(hex_input_data) - 1]
            raw_input_data = bytes.fromhex(hex_input_data)
        
        input_length = len(raw_input_data)
    
        print("raw_input_data: ", raw_input_data)
    

        for xor_char in range(1, 256) :  
            xor_result = bytes()
            hex_result = ''

            for x in raw_input_data: 
                xor_result = xor_result + bytes([xor_char ^ x])

                hex_result = bytes.hex(xor_result)
            
            #print("xor_character: ", xor_char);
            #print("xor_result(raw): ", xor_result)
            #print("xor_result(hex): ", hex_result)
            #print("===========================================================\n")       

            

            all_ascii_flag = 1

            for x in xor_result: 

                if x < 0x20 or x > 0x7e : 
                    all_ascii_flag = 0
                    break
            
            if all_ascii_flag == 1: 
                print("xor_char = ", xor_char)
                print("xor_result = ", xor_result)
                print("hex_result = ", hex_result)

    
if __name__ == "__main__" : 

    if len(sys.argv) != 2 : 
        usage(sys.argv[0])
        sys.exit()
    
    input_filename = sys.argv[1]


    xc = xor_cipher()

    xc.bruteforce_method(input_filename)
    
    xc.frequency_method(input_filename)


