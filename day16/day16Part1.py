from heapq import heappush, heappop, heapify 

def main():
    maze = load()
    
    part1Answer = part1(maze)
    print(f"Part 1 Answer: {part1Answer}")
    
def load():
    with open("day16/input.txt") as f:
        lines = f.readlines()

    return lines

def part1(maze):    
    x, y = findStart(maze)
    
    w, h = len(maze[0]), len(maze)
    expense =  [[[-1, -1, -1, -1] for _ in range(w)] for _ in range(h)]
    expense[y][x][1] = 0
    
    heap = MinHeap()
    heap.insertKey((0, x, y, 1))
    
    while len(heap.heap) > 0:
        cost, x, y, direction = heap.extractMin()
        
        if expense[y][x][direction] != -1 == expense[y][x][direction] <= cost:
            continue
        
        explore(maze, expense, heap, x, y, direction, cost)

    x, y = findEnd(maze)
    return min(expense[y][x])

def explore(maze, expense, heap, x, y, direction, cost):
    
    expense[y][x][direction] = cost
    
    if direction == 0:
        if checkLocation(maze, expense, x, y - 1, direction):
            cost = expense[y][x][0] + 1
            heap.insertKey((cost, x, y - 1, 0))
    elif direction == 1:
        if checkLocation(maze, expense, x + 1, y, direction):
            cost = expense[y][x][1] + 1
            heap.insertKey((cost, x + 1, y, 1))
    elif direction == 2:
        if checkLocation(maze, expense, x, y + 1, direction):
            cost = expense[y][x][2] + 1
            heap.insertKey((cost, x, y + 1, 2))
    elif direction == 3:
        if checkLocation(maze, expense, x - 1, y, direction):
            cost = expense[y][x][3] + 1
            heap.insertKey((cost, x - 1, y, 3))
    
    # Check all directions
    for i in range(4):
        if i == direction:
            continue
        
        if checkLocation(maze, expense, x, y, i):
            diff = abs(i - direction)
            cost = 2000 if diff == 2 else 1000
            
            cost = expense[y][x][direction] + cost
            heap.insertKey((cost, x, y, i))
    
    
def checkLocation(maze, expense, x, y, direction):
    if y < 0 or y >= len(maze):
        return False
    
    if x < 0 or x >= len(maze[0]):
        return False
    
    if maze[y][x] not in  [".", "S", "E"]:
        return False
    
    return expense[y][x][direction] == -1
    
    

def convertDirection(direction):
    if direction == 'n':
        return 0
    elif direction == 'e':
        return 1
    elif direction == 's':
        return 2
    elif direction == 'w':
        return 3

def findStart(maze):
    for y, line in enumerate(maze):
        for x, cell in enumerate(line):
            if cell == "S":
                return x, y
    
    raise Exception("Couldn't find start")


def findEnd(maze):
    for y, line in enumerate(maze):
        for x, cell in enumerate(line):
            if cell == "E":
                return x, y
    
    raise Exception("Couldn't find end")


class MinHeap:
    # Constructor to initialize a heap
    def __init__(self):
        self.heap = [] 

    def parent(self, i):
        return (i-1)/2
    
    # Inserts a new key 'k'
    def insertKey(self, k):
        heappush(self.heap, k)           

    # Decrease value of key at index 'i' to new_val
    # It is assumed that new_val is smaller than heap[i]
    def decreaseKey(self, i, new_val):
        self.heap[i]  = new_val 
        while(i != 0 and self.heap[self.parent(i)] > self.heap[i]):
            # Swap heap[i] with heap[parent(i)]
            self.heap[i] , self.heap[self.parent(i)] = (
            self.heap[self.parent(i)], self.heap[i])
            
    # Method to remove minimum element from min heap
    def extractMin(self):
        return heappop(self.heap)

    # This function deletes key at index i. It first reduces
    # value to minus infinite and then calls extractMin()
    def deleteKey(self, i):
        self.decreaseKey(i, float("-inf"))
        self.extractMin()

    # Get the minimum element from the heap
    def getMin(self):
        return self.heap[0]

if __name__ == "__main__":
    main()