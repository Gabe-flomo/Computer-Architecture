"""CPU functionality."""

import sys
HLT = 0b00000001
LDI = 0b10000010
PRN = 0b01000111
MUL = 0b10100010

class CPU:
    """Main CPU class."""

    def __init__(self):
        """Construct a new CPU."""
        # Add list properties to the CPU class to hold 256 bytes of memory and 8 general-purpose registers
        self.ram = [None] * (256)
        self.reg = [0] * (8)
        self.pc = 0

    def load(self,filename):
        """Load a program into memory."""

        address = 0

        # For now, we've just hardcoded a program:

        # program = [
        #     # From print8.ls8
        #     0b10000010, # LDI R0,8
        #     0b00000000,
        #     0b00001000,
        #     0b01000111, # PRN R0
        #     0b00000000,
        #     0b00000001, # HLT
        # ]

        # for instruction in program:
        #     self.ram[address] = instruction
        #     address += 1
        try:
            with open(filename) as file:
                for line in file:
                    # ignore comments
                    content = line.split("#")
                    # strip whitespace
                    value = content[0].split()
                    print(value)
                    
                    
                    value = int(value[0],2)
                    
                    self.ram[address] = value
                    address += 1
        except Exception:
            import os
            raise FileNotFoundError(f"No file named {filename} in {os.getcwd()}")
        print(self.ram[:12])

    def alu(self, op, reg_a, reg_b):
        """ALU operations."""

        if op == "ADD":
            self.reg[reg_a] += self.reg[reg_b]
        elif op == "MUL":
            self.reg[reg_a] *= self.reg[reg_b]
        else:
            raise Exception("Unsupported ALU operation")

    def trace(self):
        """
        Handy function to print out the CPU state. You might want to call this
        from run() if you need help debugging.
        """

        print(f"TRACE: %02X | %02X %02X %02X |" % (
            self.pc,
            #self.fl,
            #self.ie,
            self.ram_read(self.pc),
            self.ram_read(self.pc + 1),
            self.ram_read(self.pc + 2)
        ), end='')

        for i in range(8):
            print(" %02X" % self.reg[i], end='')

        print()

    def run(self):
        """Run the CPU."""
        running = True
        while running:

            # read the memory address that's stored in register PC, 
            # and store that result in IR, the Instruction Register
            IR = self.ram[self.pc]
            # print("PC",self.pc)
            # print("LDI", LDI)
            # print("PRN", PRN)
            # print("HLT", HLT)
            

            # Using ram_read(), read the bytes at PC+1 and PC+2 
            # from RAM into variables operand_a and operand_b in case the instruction needs them.
            operand_a = self.ram_read(self.pc + 1)
            operand_b = self.ram_read(self.pc + 2)

            if IR == LDI:
               
                #r = int(input("Which register (1-8): "))
                # r = sys.argv[0]
                #v = int(input("Enter a value: "))
                    
                self.reg[operand_a] = operand_b
                self.pc += 3

            if IR == HLT:
                print("stopping")
                running = False
                self.pc += 1

            if IR == PRN:
                #r = int(input("Which register (1-8): "))
                # print(self.reg[r])
                print(self.reg[operand_a])
                self.pc += 2
            
            if IR == MUL:
                print("MUL")
                self.alu("MUL", operand_a, operand_b)
                self.pc += 3
                
                #print(self.reg[operand_a])
            

        


    def ram_read(self, address):
        '''
        accept the address to read and return the value stored there.
        '''
        return self.ram[address]

    def ram_write(self, address, value):
        '''
        accept a value to write, and the address to write it to.
        '''
        self.ram[address] = value

