import time

def main():
    tiles = load()
    part1Answer = part1(tiles, 25)
    print(f"Part 1 Answer: {part1Answer}")
    
    tiles = load()
    start_time = time.time()
    part2Answer = part2(tiles, 75)
    end_time = time.time()
    print(f"Part 2 computation time: {end_time - start_time} seconds")
    print(f"Part 2 Answer: {part2Answer}")

def load():
    with open('day11/input.txt', 'r') as f:
        lines = f.readlines()
        return [ int(string) for string in lines[0].strip().split()]
    
def part1(tiles, numBlinks):
    blinks = 0
    
    while blinks < numBlinks:
        newTiles = []
        
        for tile in tiles:
            
            if tile == 0:
                newTiles.append(1)
            elif len(str(tile)) % 2 == 0:
                halfTileLength = int(len(str(tile))/2)
                
                left = int(str(tile)[:halfTileLength])
                right = int(str(tile)[halfTileLength:])
                
                newTiles.append(left)
                newTiles.append(right)
                
            else:
                newTiles.append(tile * 2024)
                
        tiles = newTiles
 
        blinks += 1
    
    return len(tiles)


def part2(tiles, numBlinks):
    hashTable = {}
    
    return sum([calculate(tile, numBlinks, hashTable) for tile in tiles])
    


def calculate(tile, numBlinks, hashTable = {}):    
    if numBlinks <= 0:
        return 1
    
    hashString = f"{tile}-{numBlinks}"
    
    if hashString in hashTable:
        return hashTable[hashString]
    
    
    
    if tile == 0:
        result = calculate(1, numBlinks - 1)
    elif len(str(tile)) % 2 == 0:
        halfTileLength = int(len(str(tile))/2)
        
        left = int(str(tile)[:halfTileLength])
        right = int(str(tile)[halfTileLength:])
        
        result = calculate(left, numBlinks - 1) + calculate(right, numBlinks - 1)
        
    else:
        result =  calculate(tile * 2024, numBlinks - 1)
    
    hashTable[hashString] = result
    return result

if __name__ == "__main__":
    main()