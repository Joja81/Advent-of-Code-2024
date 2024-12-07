import time

def main():
    equations = load()
    
    part1Answer = part1(equations)
    print("Part 1 Answer: " + str(part1Answer))
    
    part2Answer = part2(equations)
    print("Part 2 Answer: " + str(part2Answer))
    
def load():
    with open("day7/input.txt") as f:
        lines = f.read().splitlines()
    
    return [loadLine(line) for line in lines]
        
def loadLine(line):
    line = line.split(":")
    
    lineDict = {}
    lineDict['target'] = int(line[0].strip())
    lineDict['values'] = [int(number) for number in line[1].strip().split(" ")]
    
    return lineDict

def part1(equations):              
    return sum(equation['target'] for equation in equations if part1CheckEquation(equation['target'], equation['values']))
        
def part1CheckEquation(target: int, values: list[int], operators: list[str] = []):
    if len(values) == 1:
        return values[0] == target
    if values[0] > target:
        return False
    
    # Try multiplication
    mulResult = part1CheckEquation(target, [values[0] * values[1]] + values[2:], operators + ['*'])

    # Try addition
    addResult = part1CheckEquation(target, [values[0] + values[1]] + values[2:], operators + ['+'])
    
    return mulResult or addResult    

def part2(equations):              
    return sum(equation['target'] for equation in equations if part2CheckEquation(equation['target'], equation['values']))
        
def part2CheckEquation(target: int, values: list[int], operators: list[str] = []):
    if len(values) == 1:
        return values[0] == target
    if values[0] > target:
        return False
    
    # Try multiplication
    mulResult = part2CheckEquation(target, [values[0] * values[1]] + values[2:], operators + ['*'])

    # Try addition
    addResult = part2CheckEquation(target, [values[0] + values[1]] + values[2:], operators + ['+'])
    
    # Try concatenation
    conResult = part2CheckEquation(target, [int(str(values[0]) + str(values[1]))] + values[2:], operators + ['+'])
    
    return mulResult or addResult or conResult  

if __name__ == "__main__":
    main()
