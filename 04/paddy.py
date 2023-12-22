def solution1():
    sum = 0
    with open("./input1.txt") as input:
        for line in input:
            numbers = line.split(":")[1].strip()
            
            winningnumbers = [i.strip() for i in numbers.split("|")[0].strip().split(" ") if i]
            inumbers = [i.strip() for i in numbers.split("|")[1].strip().split(" ") if i]
            
            matches = 0
            
            for i in winningnumbers:
                
                for j in inumbers:
                    
                    if int(i) is int(j):
                        
                        matches += 1
            
            if matches > 0:
                
                sum += 2**(matches - 1)
            
            
            #print(winningnumbers)
            #print(inumbers)
            
            
            
        
    return sum

def solution2():
    
    sum = 0
    with open("./input1.txt") as input:
        for line in input:
            numbers = line.split(":")[1].strip()
            matchescard = []
            winningnumbers = [i.strip() for i in numbers.split("|")[0].strip().split(" ") if i]
            inumbers = [i.strip() for i in numbers.split("|")[1].strip().split(" ") if i]
            
            matches = 0
            
            for i in winningnumbers:
                
                for j in inumbers:
                    
                    if int(i) is int(j):
                        
                        matches += 1
                    matchescard.append(matches)
            nummatch = 0
            for k in range(201):
                if matchescard[k] > 0:
                    nummatch += 2**matchescard[k]
                
            
            sum += nummatch
    return sum

print(f"Solution 1: {solution1()}")
print(f"Solution 2: {solution2()}")