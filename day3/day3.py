import re


def main():
    inputString = load()
    
    part1Answer = part1(inputString)
    print("Part 1: " + str(part1Answer))
    
    part2Answer = part2(inputString)
    print("Part 2: " + str(part2Answer))
    
def load():
    with open('day3/input.txt', 'r') as f:
        lines = f.readlines()
        lines = [line.strip() for line in lines]
        
    return ''.join(lines)

def part1(inputString):
    multiplicationStrings = re.findall(r'mul\(\d{1,3},\d{1,3}\)', inputString)
    
    nums = [ processMulInstruction(multiplicationString) for multiplicationString in multiplicationStrings ]
    
    total = 0
    
    for num in nums:
        total += num
        
    return total
    
def part2(inputString):
    validInstructions = re.findall(r"(mul\(\d{1,3},\d{1,3}\))|(do\(\))|(don't\(\))", inputString)

    mulEnabled = True
    total = 0
    
    for instruction in validInstructions:
        if instruction[0] != '':
            if mulEnabled:
                total += processMulInstruction(instruction[0])
        elif instruction[1] != '':
            mulEnabled = True
        elif instruction[2] != '':
            mulEnabled = False
    
    return total
    
def processMulInstruction(instruction):
    nums = re.findall(r'\d{1,3}', instruction)
    
    return int(nums[0]) * int(nums[1])

if __name__ == "__main__":
    main()
    
    
    