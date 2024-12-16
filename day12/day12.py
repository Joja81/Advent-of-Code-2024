def main():
    mapData = load()
    part1Answer = part1(mapData)
    print(part1Answer)
    
    mapData = load()
    part2Answer = part2(mapData)
    print(part2Answer)

def load():
    with open('day12/input.txt', 'r') as f:
        return [line.strip() for line in f.readlines()]

def part1(mapData):
    nodes = createNodesPart1(mapData)
    
    fenceCosts = []
    
    for node in nodes:
        if node['visited']:
            continue
        
        edges, area = exploreRegion(node)
        perimeter = area * 4 - edges
        
        fenceCosts.append(area * perimeter)
    
    return sum(fenceCosts)
        
def part2(mapData):
    nodes = createNodesPart2(mapData)
    
    regionSides = {}
    regionAreas = {}
    regionChar = {}
    
    i = 0
    for node in [j for sub in nodes for j in sub]:
        if node['visited']:
            continue
        
        regionAreas[i] = findRegions(node, i)
        regionSides[i] = 0
        regionChar[i] = node['char']
        
        i += 1
        
    # Check vertical sides
    checkVertical(nodes, regionSides, 'left')
    checkVertical(nodes, regionSides, 'right')
    
    # Check horizontal sides
    checkHorizontal(nodes, regionSides, 'up')
    checkHorizontal(nodes, regionSides, 'down')
    
    for key in regionSides:
        print(key, regionChar[key], regionAreas[key], regionSides[key])
        
    return sum([(regionAreas[key]*regionSides[key]) for key in regionSides])
        
def checkVertical(nodes, regionSides ,side):
    x = 0
    while x < len(nodes[0]):
        y = 0
        
        currType = None
        while y < len(nodes):
            node = nodes[y][x]        
            if node[side] == False:
                if currType != None:
                    regionSides[currType] += 1
                    currType = None
            
            if node[side] == True:
                if node['region'] != currType:
                    if currType != None:
                        regionSides[currType] += 1
                    currType = node['region']            
            y += 1
        
        if currType != None:
            regionSides[currType] += 1
        
        x += 1
        
         
def checkHorizontal(nodes, regionSides ,side):
    y = 0
    while y < len(nodes):
        x = 0
        
        currType = None
        while x < len(nodes[0]):
            node = nodes[y][x]        
            if node[side] == False:
                if currType != None:
                    regionSides[currType] += 1
                    currType = None
            
            if node[side] == True:
                if node['region'] != currType:
                    if currType != None:
                        regionSides[currType] += 1
                    currType = node['region']            
            x += 1
            
        if currType != None:
            regionSides[currType] += 1
            
        y += 1
        
       
        
def exploreRegion(node):
    node['visited'] = True
    
    area = 1
    edges = len(node['neighbors'])
    
    for neighbor in node['neighbors']:
        if neighbor['visited']:
            continue
        
        neighborEdges, neighborArea = exploreRegion(neighbor)
        area += neighborArea
        edges += neighborEdges
        
    return edges, area

def findRegions(node, region):
    node['visited'] = True
    node['region'] = region
    
    numNodes = 1
    
    for neighbor in node['neighbors']:
        if neighbor['visited']:
            continue
        
        
        numNodes += findRegions(neighbor, region)
        
    return numNodes

def createNodesPart1(mapData):
    nodes = []
    
    for line in mapData:
        
        currLineNodes = []
        
        line
        
        for char in line:
            currLineNodes.append({
                "char": char,
                "neighbors": [],
                "visited": False
            })
    
        nodes.append(currLineNodes)
        
    for y, row in enumerate(nodes):
        for x, node in enumerate(row):
            if x > 0 and nodes[y][x - 1]["char"] == node["char"]:
                node["neighbors"].append(nodes[y][x - 1])
            if x < len(row) - 1 and nodes[y][x + 1]["char"] == node["char"]:
                node["neighbors"].append(nodes[y][x + 1])
            if y > 0 and nodes[y - 1][x]["char"] == node["char"]:
                node["neighbors"].append(nodes[y - 1][x])
            if y < len(nodes) - 1 and nodes[y + 1][x]["char"] == node["char"]:
                node["neighbors"].append(nodes[y + 1][x])        
    
    
    return [j for sub in nodes for j in sub]


def createNodesPart2(mapData):
    nodes = []
    
    for line in mapData:
        
        currLineNodes = []
        
        line
        
        for char in line:
            currLineNodes.append({
                "char": char,
                "neighbors": [],
                "visited": False
            })
    
        nodes.append(currLineNodes)
        
    for y, row in enumerate(nodes):
        for x, node in enumerate(row):
            if x > 0 and nodes[y][x - 1]["char"] == node["char"]:
                node['left'] = False
                node["neighbors"].append(nodes[y][x - 1])
            else:
                node["left"] = True
                
            if x < len(row) - 1 and nodes[y][x + 1]["char"] == node["char"]:
                node['right'] = False
                node["neighbors"].append(nodes[y][x + 1])
            else:
                node["right"] = True
                
            if y > 0 and nodes[y - 1][x]["char"] == node["char"]:
                node['up'] = False
                node["neighbors"].append(nodes[y - 1][x])
            else:
                node['up'] = True
                
            if y < len(nodes) - 1 and nodes[y + 1][x]["char"] == node["char"]:
                node['down'] = False
                node["neighbors"].append(nodes[y + 1][x])     
            else:
                node['down'] = True   
    
    
    return nodes


if __name__ == "__main__":
    main()