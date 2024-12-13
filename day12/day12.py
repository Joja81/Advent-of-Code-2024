def main():
    mapData = load()
    part1Answer = part1(mapData)
    print(part1Answer)

def load():
    with open('day12/input.txt', 'r') as f:
        return [line.strip() for line in f.readlines()]

def part1(mapData):
    nodes = createNodes(mapData)
    
    fenceCosts = []
    
    for node in nodes:
        if node['visited']:
            continue
        
        edges, area = exploreRegion(node)
        perimeter = area * 4 - edges
        
        fenceCosts.append(area * perimeter)
    
    return sum(fenceCosts)
        
        
        
        
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

    
    
    

def createNodes(mapData):
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

if __name__ == "__main__":
    main()