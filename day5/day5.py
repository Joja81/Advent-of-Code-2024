def main():
    orders, updates = load()
    
    part1Answer = part1(orders, updates)
    print(f'Part 1: {part1Answer}')
    
    part2Answer = part2(orders, updates)
    print(f'Part 2: {part2Answer}')
    
def load():
    with open('day5/input.txt') as f:
        lines = f.readlines()
    
    blank_line_index = next((i for i, line in enumerate(lines) if line.strip() == ''), None)
    
    orders_lines = lines[:blank_line_index]
    updates_lines = lines[blank_line_index+1:]
    
    orders = {}
    for line in orders_lines:
        [x, y] = (int(part)  for  part in line.split('|'))
        
        if x in orders.keys():
            orders[x].append(y)
        else:
            orders[x] = [y]    

    updates = [  [int(number) for  number in  line.strip().split(',')] for line in updates_lines]
            
    return orders, updates

def part1(orders, updates):
    sum = 0
    
    for update in updates:
        correct_order = []
        
        for page in update:
            must_be_before = orders[page] if page in orders.keys() else []
            
            index = next((i for i, p in enumerate(correct_order) if p in must_be_before), len(correct_order))
            
            correct_order.insert(index, page)
                
        if correct_order == update:
            sum += update[len(update) // 2]
            
    return sum

def part2(orders, updates):
    sum = 0
    
    for update in updates:
        correct_order = []
        
        for page in update:
            must_be_before = orders[page] if page in orders.keys() else []
            
            index = next((i for i, p in enumerate(correct_order) if p in must_be_before), len(correct_order))
            
            correct_order.insert(index, page)
                
        if correct_order != update:
            sum += correct_order[len(correct_order) // 2]
            
    return sum
    
    

if __name__ == '__main__':
    main()