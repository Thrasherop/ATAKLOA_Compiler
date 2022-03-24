from lib2to3.pytree import convert
import sys 



def convert_to_binary(integer):
    """
    Converts an integer to binary
    """
    return bin(int(integer, 16))[2:]

def parse_line(line):

    """
    Returns the hex of the instruction
    """

    # breaks the line into a list
    partial_list = line.split(" ")
    instruction = partial_list[0]

    # If it is a NOP instruction, then just return 0000
    if "NOP" in instruction:
        print("Turned NOP into 0000")
        return "0000"

    params = partial_list[1].split(",")

    


    # Converts the params to binary
    for this_param in params:
        param_raw = convert_to_binary(this_param)

        while len(param_raw) < 4:
            param_raw = "0" + param_raw

        params[params.index(this_param)] = param_raw

        #params[params.index(this_param)] = padded_param


    instruction_bin = ""

    # Finds the hex of the instruction
    if instruction == "NOP":
        instruction_bin = "0000"
    elif instruction == "LD":
        instruction_bin = "0001"
    elif instruction == "MOV":
        instruction_bin = "0010"
    elif instruction == "DISP":
        instruction_bin = "0011"
    elif instruction == "XOR":
        instruction_bin = "0100"
    elif instruction == "AND":
        instruction_bin = "0101"
    elif instruction == "OR":
        instruction_bin = "0110"
    elif instruction == "ADD":
        instruction_bin = "0111"
    elif instruction == "SUB":
        instruction_bin = "1111"
    else:
        print("Invalid instruction")
        exit()


    # Builds the rest of the binary
    num_params = len(params)

    final_bin = ""

    if instruction == "NOP":
        final_bin = instruction_bin + "000000000000"

    elif instruction == "LD":
        Rd = params[0]
        data = params[1]
        final_bin = instruction_bin  + Rd + "0000" + data

    elif instruction == "MOV":
        Rd = params[0]
        Ra = params[1]
        final_bin = instruction_bin  + Rd  + Ra + "0000"

    elif instruction == "DISP":
        Ra = params[0]
        Rb = params[1]
        final_bin = instruction_bin + "0000" + Ra  + Rb

    else:
        # The rest of the instuctions have the same parameter set up
        Rd = params[0]
        Ra = params[1]
        Rb = params[2]

        final_bin = instruction_bin  + Rd  + Ra  + Rb

    #print(final_bin)
    
    # turns it into hex, pads it, and turns it into a string
    hex_raw = hex(int(final_bin, 2))
    hex_str = str(hex_raw).replace("0x", "")
    
    # Pads
    while len(hex_str) < 4:
        hex_str = "0" + hex_str

    final_hex = hex_str.upper()

    line = line.replace("\n", "")
    print("Turned `" + line + "` into " + final_hex + "(" + final_bin + ")")


    return final_hex



def inline_args(args):

    # Opens the first file
    with open(args[0], 'r') as f:

        lines = f.readlines()

    # Loops through the lines

    all_instructions = []

    for line in lines:

        print(line)

        # Skips any line that starts with a //
        if line[0] == '/' and line[1] == '/':
            continue

        # Skips any empy line
        if line == "\n":
            continue



        all_instructions.append(parse_line(line))
        

    # Writes the instructions to the file
    with open(args[1], 'w') as f:
        # Adds the header
        f.write("v2.0 raw\n")

        for instruction in all_instructions:
            f.write(instruction + " ")


    

def main():

    # Checks for flags
    if "-h" in sys.argv or "--help" in sys.argv:
        print("\n\nUsage: ATAKLOA_Compiler.py <assembly_file> <binary_output>\n\nView README.md for more info \n\n")
        exit()


    # Parses the arguments
    if len(sys.argv) <= 2:
        print("Insufficient arguments given")
        exit()

    else:
        args_raw = sys.argv[1:]
        inline_args(args_raw)

    pass

if __name__ == '__main__':
    main()