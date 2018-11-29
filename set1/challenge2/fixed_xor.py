#! /usr/bin/env python3

# Filename: Fixed XOR
# Function: Takes two equal-length buffers and produces their XOR combination 

# Cryptopals - Set1 - Challenge2
# Cryptopals Link: http://cryptopals.com/sets/1/challenges/2
# Link to my blogpost: 

# Author: Adwaith Gautham

# License: MIT (Link: https://mit-license.org/)
# Use it, play with it and learn from it!

# Run like this:    $ chmod u+x fixed_xor.py
#                   $ ./base64.py <encode / decode> <hex / raw / base64> InputFilename OutputFilename




import sys

def err_exit(errmsg) : 
    print(errmsg)
    sys.exit()

class fixedxor : 


    def find_fixed_xor(self, input_filename1, input_filename2, output_filename) : 

        try: 
            input_file1 = open(input_filename1, 'r')
        except FileNotFoundError: 
            err_exit("Error: Input File1 not found")

        try: 
            input_file2 = open(input_filename2, 'r')
        except FileNotFoundError: 
            err_exit("Error: Input File2 not found")
        
        try: 
            output_file = open(output_filename, 'w')
        except: 
            err_exit("Error: Unable to open Output File")

        inter_filename = output_filename + '.raw'
        inter_file = open(inter_filename, 'wb')

        input_data1 = input_file1.read()
        input_data2 = input_file2.read()

        input_data1 = input_data1[ : len(input_data1) - 1]
        input_data2 = input_data2[ : len(input_data2) - 1]

        # Hex decode both inputs
        raw_data1 = bytes.fromhex(input_data1)
        raw_data2 = bytes.fromhex(input_data2)

        # Both inputs are equal in size
        data_length = len(raw_data1)
        
        raw_result = bytes()

        for i in range(0, data_length) : 
            
            x = raw_data1[i] ^ raw_data2[i]
            raw_result = raw_result + bytes([x])

        inter_file.write(raw_result)

        hex_result = bytes.hex(raw_result)
        output_file.write(hex_result)


        input_file1.close()
        input_file2.close()
        output_file.close()
        inter_file.close()






def usage(argv0) : 

    print("Usage: $ ", argv0, " InputFile1 InputFile2 OutputFile")
    print("\nInstruction: ")
    print("1. Data in InputFile1 and InputFile2 are assumed to be hex-encoded")
    print("2. A .raw file will be created which will have the raw-data of the fixed-xor result")

if __name__ == "__main__" : 

    if len(sys.argv) != 4 : 
        usage(sys.argv[0])
        sys.exit()
    

    input_filename1 = sys.argv[1]
    input_filename2 = sys.argv[2]
    output_filename = sys.argv[3]

    fxor = fixedxor()
    
    fxor.find_fixed_xor(input_filename1, input_filename2, output_filename)
    
