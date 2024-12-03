def main():
    values = load()
    
    part1Answer = part1(values)
    print("Part 1: " + str(part1Answer))
    
    part2Answer = part2(values)
    print("Part 2: " + str(part2Answer))

def load():
    
    with open('day2/input.txt', 'r') as f:
        lines = f.readlines()
        lines = [[int(number) for number in line.split()] for line in lines]
        
    return lines

def part1(values):
    results = [(part1CheckSafe(line, True) or part1CheckSafe(line, False)) for line in values]
    safe = [x for x in results if x == True]
    return len(safe)
    

def part1CheckSafe(line, increase):
    i = 1;
    while i < len(line):
        if not checkValues(line[i-1], line[i], increase): 
            return False 
        
        i += 1
        
    return True

def part2(values):
    results = [(part2CheckSafe(line, True) or part2CheckSafe(line, False)) for line in values]
    safe = [x for x in results if x == True]
    return len(safe)

def part2CheckSafe(line, increase, tolerate = True):
    i = 1;
    while i < len(line):
        valid = checkValues(line[i-1], line[i], increase)
        
        if not valid:
            if not tolerate:
                return False
            else:
                return (part2CheckSafe(spliceIndex(line, i), increase, tolerate=False) or part2CheckSafe(spliceIndex(line, i-1), increase, tolerate=False))
           
        
        i += 1
        
    return True

def spliceIndex(line, index):
    return line[:index] + line[index+1:]

def checkValues(val1, val2, increase):
    if increase:
        if val2 - 3 > val1:
            return False
        if val2 - 1 < val1:
            return False
    else:
        if val2 + 3 < val1:
            return False
        if val2 + 1 > val1:
            return False
    return True



if __name__ == "__main__":
    main()