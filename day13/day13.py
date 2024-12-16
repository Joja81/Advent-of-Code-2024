import sympy as sym

def main():
    games = load(1)
    part1Answer = solveGames(games)
    print(f"Part 1 Answer {part1Answer}")
    
    games = load(2)
    part2Answer = solveGames(games)
    print(f"Part 2 Answer {part2Answer}")
    
def load(part):
    with open('day13/input.txt', 'r') as f:
        lines = f.readlines()
        
    games = []    
    
    idx = 0
    while idx < len(lines):
        game = {}
        game['a'] = getButton(lines[idx])
        game['b'] = getButton(lines[idx + 1])
        game['prize'] = getPrize(lines[idx + 2], part)
        
        games.append(game)
        
        idx += 4
        
    return games
        
def getButton(line):
    parts = line.strip().split(' ')
    
    x = parts[2].split('+')[1]
    y = parts[3].split('+')[1]
    
    return (int(x[:len(x) - 1]), int(y))

def getPrize(line, part):
    parts = line.strip().split(' ')
    
    x = parts[1].split('=')[1]
    y = parts[2].split('=')[1]
    
    if part == 1:
        return (int(x[:len(x) - 1]), int(y))
    else:
        return (int(x[:len(x) - 1]) + 10000000000000, int(y) + 10000000000000)
        
def solveGames(games):
    return sum([solveGame(game) for game in games])
    
def solveGame(game):
    a,b = sym.symbols('a,b')
    
    xEq = sym.Eq(a*game['a'][0] + b*game['b'][0], game['prize'][0])
    yEq = sym.Eq(a*game['a'][1] + b*game['b'][1], game['prize'][1])
    result = sym.solve([xEq,yEq],(a,b))
    
    aResult = result[a]
    bResult = result[b]
    
    if (aResult).is_integer and (bResult).is_integer:
        return aResult * 3 + bResult
    
    return 0
       
    
if __name__ == "__main__":
    main()