def main():
    line = load()
    
    part1Answer = part1(line)
    print("Part 1: ", part1Answer)
    
    part2Answer = part2(line)
    print("Part 2: ", part2Answer)
    
def load():
    with open('day9/input.txt', 'r') as f:
        lines = f.readlines()
        return lines[0].strip()

def part1(line):
    memory = fillMemory(line)
                
    memory = compressMemoryPart1(memory)
    
    checksum = checksumMemory(memory)
    
    return checksum
            
def compressMemoryPart1(memory):
    idx = 0
    while idx < len(memory):
        if memory[len(memory)-1][0] == 0 or memory[len(memory)-1][1] == -1:
            memory.pop()
            continue
        
        if memory[idx][1] == -1:
            emptySpace = memory[idx][0]
            
            if memory[len(memory)-1][0] >= emptySpace:
                memory[len(memory)-1][0] -= emptySpace
                memory[idx][1] = memory[len(memory)-1][1]
            else:
                memory.insert(idx, memory[len(memory)-1])
                memory[idx + 1][0] -= memory[len(memory)-1][0]
                memory.pop(len(memory)-1)
        
        idx += 1
      
    return memory
    

def part2(line):
    memory = fillMemory(line)
    
    memory = compressMemoryPart2(memory)

    checksum = checksumMemory(memory)
    
    return checksum

def compressMemoryPart2(memory: list):
    idx = len(memory) - 1
    
    while (idx > 0):
        if memory[idx][0] == 0:
            memory.pop(idx)
        elif memory[idx][1] == -1:
            pass
        else:
            searchIdx = 0
            
            while searchIdx < idx:
                if memory[searchIdx][1] == -1 and memory[searchIdx][0] >= memory[idx][0]:
                    memory.insert(searchIdx + 1, [memory[searchIdx][0] - memory[idx][0], -1])
                    
                    idx += 1
                    
                    memory[searchIdx][0] = memory[idx][0]
                    memory[searchIdx][1] = memory[idx][1]
                    memory[idx][1] = -1

                    break
                
                searchIdx += 1
            

        idx -= 1
        
    return memory
    
def outputMemory(memory):
    idx = 0
    
    for item in memory:
        i = 0
        while i < item[0]:
            if item[1] == -1:
                print('.', end='')
            else:
                print(item[1], end='')
            
            
            i += 1
            idx += 1
    print()

def checksumMemory(memory):
    
    score = 0
    idx = 0
    
    for item in memory:
        
        i = 0
        while i < item[0]:
            if item[1] != -1:
                score += item[1] * idx
            i += 1
            idx += 1
            
    return score
    
def fillMemory(line:str):
    memory = []
    
    for idx, item in enumerate(line):
        if item == '0':
            continue
        
        if idx % 2 == 0:
            memory.append([int(item), int(idx/2)])
        else:
            memory.append([int(item), -1])
        
    return memory
        


if __name__ == '__main__':
    main()