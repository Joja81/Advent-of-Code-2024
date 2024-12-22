instructions = None


# 0o345300

def main():
    global instructions
    instructions = load()
    print(min(dfs()))
    
    
    
def load():
    with open("day17/input.txt") as f:
        lines = f.readlines()
    
    return [int(num) for num in lines[4].split(":")[1].strip().split(',')]


def dfs(value = 0):
    valid = []
    
    value *= 0o10
    
    for add in range(8):
        curr = value + add

        output = run(curr, [])
        
        
        if output == instructions:
            return [curr]
        
        
        print(output, oct(curr))
        
        if output == instructions[-len(output):]:
            valid.extend(dfs(value = curr))
        
        
        
    return valid


def run(a, output):
    if a <= 0:
        return output
    
    b = a % 8
    b = b ^ 1
    c = int(a / (2**b))
    b = b ^ 5
    b = b ^ c
    a = int(a/8)
    
    output.append(b % 8)
    
    return run(a, output)

if __name__ == "__main__":
    main()