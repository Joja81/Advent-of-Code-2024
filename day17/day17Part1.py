a = None
b = None
c = None

instructions = None

pointer = 0

output = []

def main():
    global a
    load()
    
    a = 0o345300
    
    part1()
    
    print(','.join(output))

def load():
    global a, b, c, instructions
    
    
    with open("day17/exampleInput.txt") as f:
        lines = f.readlines()
    
    a = int(lines[0].split(":")[1].strip())
    b = int(lines[1].split(":")[1].strip())
    c = int(lines[2].split(":")[1].strip())
    
    instructions = [int(num) for num in lines[4].split(":")[1].strip().split(',')]

def part1():
    global pointer, instructions
    
    
    while pointer >= 0 and pointer < len(instructions):
        operation()
        pointer += 2
        

def comboOperand():
    global instructions, pointer
    
    value = instructions[pointer + 1]
    
    if value in [0, 1, 2, 3]:
        return value
    
    if value == 4:
        return a
    if value == 5:
        return b
    if value == 6:
        return c
    
    raise Exception("Couldn't read combo")
    
def literalOperand():
    global instructions, pointer
    
    return instructions[pointer + 1]
    
def operation():
    global a, b , c, instructions, pointer, output
    
    
    opcode = instructions[pointer]
    if opcode == 0:
        a = a // (2 ** comboOperand())
    elif opcode == 1:
        b = b ^ literalOperand()
    elif opcode == 2:
        b = comboOperand() % 8
    elif opcode == 3:
        if a != 0:    
            pointer = literalOperand() - 2
    elif opcode == 4:
        b = b ^ c
    elif opcode == 5:
        output.append(str(comboOperand() % 8))
    elif opcode == 6:
        b = a // (2 ** comboOperand())
    elif opcode == 7:
        c = a // (2 ** comboOperand())



if __name__ == "__main__":
    main()