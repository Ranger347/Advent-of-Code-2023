def solution1(filename):
    
    sum = 0
    with open(filename) as input:

        for line in input:
            # print(line)
            numbers = line.split(":")[1].strip()

            winning_numbers = [ i.strip() for i in numbers.split("|")[0].strip().split(" ") if i ]
            nums_i_have = [ i.strip() for i in numbers.split("|")[1].strip().split(" ") if i ]

            matches = 0

            for i in winning_numbers:
                for j in nums_i_have:

                    if int(i) is int(j):
                        matches += 1

            if matches > 0:
                sum += 2 ** (matches - 1)
   
    return sum
            
def recursiveHelper(copies):
    
    if copies <= 0:
        return




def solution2(filename):

    sum = 0
    with open(filename) as input:

        cards = {}
        for i, line in enumerate(input):
            info = [] # matches, cards, cards left
            # print(line)
            card_number = line.split(":")[0]
            numbers = line.split(":")[1].strip()

            winning_numbers = [ i.strip() for i in numbers.split("|")[0].strip().split(" ") if i ]
            nums_i_have = [ i.strip() for i in numbers.split("|")[1].strip().split(" ") if i ]

            matches = 0

   
    return sum

file = "input.txt" #input("what file is your input?\n")

print(f"Solution 1: {solution1(file)}")
print(f"Solution 2: {solution2(file)}")
