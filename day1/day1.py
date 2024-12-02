

def main():
    list1, list2 = load()

    part1Answer = part1(list1, list2)
    
    print(f"Part 1: {part1Answer}")
    
    part2Answer = part2(list1, list2)
    
    print(f"Part 2: {part2Answer}")
    
def load():
    with open('day1/input.txt', 'r') as f:
        lines = f.readlines()
        lines = [line.split() for line in lines]
    
    return [int(line[0]) for line in lines], [int(line[1]) for line in lines]

def part1(list1, list2):
    list1.sort()
    list2.sort()
    
    total = 0
    
    for i in range(len(list1)):
        sum = abs(list1[i] - list2[i])
        total += sum
        
    return total
    
def part2(list1, list2):
    list2Dict = {}
    
    for num in list2:
        if num in list2Dict:
            list2Dict[num] += 1
        else:
            list2Dict[num] = 1
    
    total = 0
    
    for num in list1:
        if num in list2Dict:
            total += num * list2Dict[num]
    return total





if __name__ == "__main__":
    main()
