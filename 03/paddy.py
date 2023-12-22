import re
def solution1():
    sum = 0
    with open("./input1.txt") as input:
        
        regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
        for line in input:
            if(regex.search(line) == true):
                for element in line:
                    if(regex.search(element == true)):
                        num = element.enumerate
    return sum

print(f"Solution 1: {solution1()}")
        