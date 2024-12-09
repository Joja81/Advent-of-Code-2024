from itertools import combinations


def main():
    inputData = load()
    
    part1Answer = part1(inputData)
    print(part1Answer)
    
    part2Answer = part2(inputData)
    print(part2Answer)
    
def load():
    with open('day8/input.txt', 'r') as f:
        lines = f.readlines()
        lines = [list(line.strip()) for line in lines]
        return lines

def part1(inputData):
    antiNodes = []
    for line in inputData:
        zeros = [0] * len(line)
        antiNodes.append(zeros)
        
    nodesDict = {}
    
    for y, line in enumerate(inputData):
        for x, node in enumerate(line):
            if not node == '.':
                if node in nodesDict:
                    nodesDict[node].append((x, y))
                else:
                    nodesDict[node] = [(x, y)]
                    
    for key in nodesDict:
        locations = nodesDict[key]
        
        for loc1, loc2 in combinations(locations, 2):
            
            xDistance = loc1[0] - loc2[0]
            yDistance = loc1[1] - loc2[1]
            
            if checkInBounds(loc1[0] + xDistance, loc1[1] + yDistance, inputData):
                antiNodes[loc1[1] + yDistance][loc1[0] + xDistance] += 1
            if checkInBounds(loc2[0] - xDistance, loc2[1] - yDistance, inputData):
                antiNodes[loc2[1] - yDistance][loc2[0] - xDistance] += 1
            
    count = sum(sum(1 for cell in row if cell > 0) for row in antiNodes)
    return count
            
def part2(inputData):
    antiNodes = []
    for line in inputData:
        zeros = [0] * len(line)
        antiNodes.append(zeros)
        
    nodesDict = {}
    
    for y, line in enumerate(inputData):
        for x, node in enumerate(line):
            if not node == '.':
                if node in nodesDict:
                    nodesDict[node].append((x, y))
                else:
                    nodesDict[node] = [(x, y)]
                    
    for key in nodesDict:
        locations = nodesDict[key]
        
        for loc1, loc2 in combinations(locations, 2):
            
            xDistance = loc1[0] - loc2[0]
            yDistance = loc1[1] - loc2[1]
            
            antiNodes[loc1[1]][loc1[0]] += 1
            antiNodes[loc2[1]][loc2[0]] += 1
            
            currXDistance = xDistance
            currYDistance = yDistance
            while checkInBounds(loc1[0] + currXDistance, loc1[1] + currYDistance, inputData):
                antiNodes[loc1[1] + currYDistance][loc1[0] + currXDistance] += 1
                currXDistance += xDistance
                currYDistance += yDistance
            
            currXDistance = xDistance
            currYDistance = yDistance
            while checkInBounds(loc2[0] - currXDistance, loc2[1] - currYDistance, inputData):
                antiNodes[loc2[1] - currYDistance][loc2[0] - currXDistance] += 1
                currXDistance += xDistance
                currYDistance += yDistance
            
    count = sum(sum(1 for cell in row if cell > 0) for row in antiNodes)
    return count


def checkInBounds(x, y, inputData):
    if x < 0 or x >= len(inputData[0]):
        return False
    if y < 0 or y >= len(inputData):
        return False
    return True     

if __name__ == '__main__':
    main()
