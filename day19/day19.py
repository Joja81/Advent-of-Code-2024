import re

parts = None
words = None

def main():
    load()
    
    matchedWords = part1()
    print(len(matchedWords))
    
    part2Answer = part2(matchedWords)
    print(part2Answer)
    
def load():
    global parts, words
    
    with open("day19/input.txt") as f:
        lines = f.readlines()
        
    parts = [part.strip() for part in lines[0].split(',')]
    words = [word.strip() for word in lines[2:]]
    
    return parts, words

def part1():
    global parts, words
    
    regexString = "^(" + "|".join(parts) + ")+$"
    
    matchedWords = []
    for  word in words:
        currMatch = re.search(regexString, word)
    
        if currMatch != None:
            matchedWords.append(word)
            
            
            
    
    return matchedWords

def part2(matchedWords):
    count = 0
    
    for word in matchedWords:
        count += numSolutions(word)
        
    return count

def numSolutions(word, cache = {}):
    if word == "":
        return 1
    
    if word in cache:
        return cache[word]
    
    count = 0
    for part in parts:
        if word.startswith(part):
            count += numSolutions(word[len(part):], cache)
    
    cache[word] = count
    
    return count

if __name__ == "__main__":
    main()