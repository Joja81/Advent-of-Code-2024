
def main():
    lines = load()
    
    part1Answer = part1(lines)
    print(f'Part 1: {part1Answer}')
    
    part2Answer = part2(lines)
    print(f'Part 2: {part2Answer}')

def load():
    with open('day4/input.txt') as f:
        return f.read().splitlines()
    
def part1(lines):
    count = 0
    
    # search horizontal
    count += check_lines(lines)
    
    # search vertical
    vertical_lines = []
    for i in range(len(lines[0])):
        vertical_lines.append(''.join([line[i] for line in lines]))
    
    count += check_lines(vertical_lines)
    
    # search diagonal
    
    diagonal_lines = []

    start_y = -len(lines[0]) + 1
        
    while start_y < len(lines):
        # rightward diagonal
        y = start_y
        x = 0
        line  = ''
        while(x < len(lines[0])):
            if y >= 0 and y < len(lines):
                line += lines[y][x]
                
            y += 1
            x += 1
        
        diagonal_lines.append(line)
        
        # leftward diagonal
        y = start_y
        x = len(lines[0]) - 1
        line  = ''
        while(x >= 0):
            if y >= 0 and y < len(lines):
                line += lines[y][x]
                
            y += 1
            x -= 1
        
        diagonal_lines.append(line)
        
        start_y += 1
            
    count += check_lines(diagonal_lines)
    
    return count
    
def check_lines(lines):
    count = 0
    for line in lines:
        count += line.count('XMAS')
        count += line.count('SAMX')
        
    return count
    
def part2(lines):
    count = 0
    
    y = 0
    
    while y < len(lines) - 2:
        x = 0
        while x < len(lines[0]) - 2:
            left_top = lines[y][x]
            right_top = lines[y][x + 2]
            
            middle = lines[y + 1][x + 1]
            
            left_bottom = lines[y + 2][x]
            right_bottom = lines[y + 2][x + 2]
            
            word_1 = left_top + middle + right_bottom
            word_2 = right_top + middle + left_bottom
            
            if word_1 in ['MAS', 'SAM'] and word_2 in ['MAS', 'SAM']:
                count += 1
            
            x += 1
        y += 1
    
    return count
    




if __name__ == '__main__':
    main()