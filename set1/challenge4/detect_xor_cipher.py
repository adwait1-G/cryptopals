#! /usr/bin/env python3

# Filename: detect_xor_cipher.py
# Function: To find the key, decrypt the message from a single-byte XOR cipher given.

# There are 2 methods defined to break this cipher:
# 1. Brute forcing through all 1 - 255 numbers
# 2. Frequency Analysis

# This program will list all probable options which mostly have xor_cipher

# Cryptopals - Set1 - Problem4
# Cryptopals Link: http://cryptopals.com/sets/1/challenges/4
# Link to my blogpost: 

# Author: Adwaith Gautham

# License: MIT (Link: https://mit-license.org/)
# Use it, play with it and learn from it!

# Run like this:    $ chmod u+x detect_xor_cipher.py
#                   $ ./xor_cipher.py InputFile > OutputFile


import sys
import xor_cipher

def err_exit(errmsg): 
    print(errmsg)
    sys.exit()

def usage(argv0) : 
    print("Usage: $ ", argv0, " InputFile")
    print("\nInstructions: ")
    print("1. The input file should contain hex-encoded strings separated by newline.")


if __name__ == "__main__" : 

    if len(sys.argv) != 2: 
        usage(sys.argv[0])
        sys.exit()

    
    input_filename = sys.argv[1]

    try: 
        input_file = open(input_filename, 'r')
    except: 
        err_exit("Error: Unable to open InputFile")

    
    input_data = input_file.read()
    input_data = input_data.split('\n')

    xc = xor_cipher.xor_cipher()
    
    for hex_data in input_data : 
        
        temp_file = open("temp.temp", 'w')
        temp_file.write(hex_data)
        temp_file.close()

        xc.bruteforce_method(temp_file)
    








































