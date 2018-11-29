#! /usr/bin/env python3

# Filename: base64.py
# Function: base64 encoding and decoding

# Cryptopals - Set1 - Problem1
# Cryptopals Link: http://cryptopals.com/sets/1/challenges/1
# Link to RFC: https://tools.ietf.org/html/rfc4648
# Link to my blogpost: 

# Author: Adwaith Gautham

# License: MIT (Link: https://mit-license.org/)
# Use it, play with it and learn from it!

# Run like this:    $ chmod u+x base64.py
#                   $ ./base64.py <encode / decode> <hex / raw / base64> InputFilename OutputFilename


import sys

b64_lookup_table = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

def err_exit(errmsg) : 
    print(errmsg)
    sys.exit();


class base64 : 
    
    # base64 encode function for raw data
    def encode(self, input_filename, output_filename) : 
        
        try: 
            input_file = open(input_filename, 'rb')
        except FileNotFoundError: 
            err_exit("Error: Input File not Found")

        try: 
            output_file = open(output_filename, 'w')
        except: 
            err_exit("Error: Unable to open Output File")
        

        complete_input_data = input_file.read()

        counter = 0
        
        # The workhorse of encode function
        while counter < len(complete_input_data) : 
            
            # List of variables used
            binary_data = list()
            binary_data_4_bytes = list()
            encoded_data = str()
            binary_data_3_bytes = str()

            # 3 bytes from input file
            input_data = complete_input_data[counter : counter + 3]
    
            # Create a list of binary_data of 3 input bytes
            for x in range(0, len(input_data)) : 
                binary_data.append(bin(input_data[x])[2:])

            # Add Leading zeroes to make every byte an 8-bit number
            # A byte is 8-bits, but python will not store the Leading zeroes if any. In this step, we are adding those zeroes
            for x in range(0, len(binary_data)) : 
                if len(binary_data[x]) % 8 != 0 : 
                    binary_data[x] = '0' * (8 - len(binary_data[x]) % 8) + binary_data[x]
            
            # Get the byte stream
            for x in range(0, len(binary_data)) : 
                binary_data_3_bytes = binary_data_3_bytes + binary_data[x]
            
            # Normal case - 24 bits
            if len(binary_data_3_bytes) == 24: 
                binary_data_4_bytes.append(binary_data_3_bytes[0:6])
                binary_data_4_bytes.append(binary_data_3_bytes[6:12])
                binary_data_4_bytes.append(binary_data_3_bytes[12:18])
                binary_data_4_bytes.append(binary_data_3_bytes[18:24])
            
            # Edge case1 : 16 bits 
            elif len(binary_data_3_bytes) == 16: 
                binary_data_3_bytes = binary_data_3_bytes + '00'
                binary_data_4_bytes.append(binary_data_3_bytes[0:6])
                binary_data_4_bytes.append(binary_data_3_bytes[6:12])
                binary_data_4_bytes.append(binary_data_3_bytes[12:18])
            
            # Edge case2: 8 bits
            elif len(binary_data_3_bytes) == 8: 
                binary_data_3_bytes = binary_data_3_bytes + '0000'
                binary_data_4_bytes.append(binary_data_3_bytes[0:6])
                binary_data_4_bytes.append(binary_data_3_bytes[6:12])
            
            
            # Getting the encoded data of the 3 input bytes
            # Size of encoded_data = 4 bytes
            for x in binary_data_4_bytes: 
                lookup_index = int('0b' + x, 2)
                encoded_data = encoded_data + str(b64_lookup_table[lookup_index])
            
            # Add padding for 16-bit and 8-bit cases
            # (pad) character is '='
            if len(encoded_data) == 2: 
                encoded_data = encoded_data + '=='

            elif len(encoded_data) == 3: 
                encoded_data = encoded_data + '='

            # Write those 4 bytes into Output File
            output_file.write(encoded_data)

            counter = counter + 3

            # Just to beautify it :P
            #if counter % 81 == 0 : 
            #    output_file.write('\n')

        
        # After everything, close files
        input_file.close()
        output_file.close()


    def encode_hex(self, input_filename, output_filename) : 
        
        try: 
            input_file = open(input_filename, 'r')
        except FileNotFoundError: 
            err_exit("Error: Input File not Found")


        temp_filename = input_filename + ".raw"
        temp_file = open(temp_filename, 'wb')

        raw_output_data = bytes()

        input_hex_data = input_file.read()

        x = len(input_hex_data)
        
        # Removing the trailing newline
        input_hex_data = input_hex_data[:x-1]
        raw_output_data = bytes.fromhex(input_hex_data)


        temp_file.write(raw_output_data)

        input_file.close()
        temp_file.close()

        self.encode(temp_filename, output_filename)
        
    
    def decode(self, input_filename, output_filename) : 
        
        print("Decode method still under construction")


def usage(argv0) : 

    print("Usage: $ ", argv0, " <encode / decode> <hex / raw / base64> InputFilename OutputFilename")
    print("\nInstructions: ")
    print("1. Select if you want to encode or decode. ")
    print("2. Specify the input type - hexadecimal input or raw bytes. ")
    print("3. Place the matter you want to encode or decode in an Input File. ")
    print("4. Specify the name of the Output File. ")
    print("5. encode option can use all 3 input types - hex, raw, base64. ")
    print("6. decode option can use only 1 input type - base64. ")


if __name__ == "__main__" : 

    # Correct Usage
    if len(sys.argv) != 5 : 
        usage(sys.argv[0]);
        sys.exit();
    
    action = sys.argv[1]
    input_type = sys.argv[2]
    input_filename = sys.argv[3]
    output_filename = sys.argv[4]
    
    
    # Checking for invalid actions
    if action != "encode" and action != "decode" : 
        err_exit("Error: Invalid action")
    
    # Checking for invalid input types
    if input_type != "hex" and input_type != "raw" : 
        err_exit("Error: Invalid input type")

    # Creating a base64 object
    b64 = base64()

    # encode
    if action == "encode" : 
        
        if input_type == "raw" or input_type == "base64": 
            b64.encode(input_filename, output_filename)
        
        elif input_type == "hex" : 
            b64.encode_hex(input_filename, output_filename)
    
    # decode
    elif action == "decode" : 
        
        if input_type == "base64" : 
            b64.decode(input_filename, output_filename)
        
        else : 
            err_exit("Error: Cannot decode non-base64 data")
