
valid_digits = {
    "one" : "1",
    "two" : "2",
    "three" : "3",
    "four" : "4",
    "five" : "5",
    "six" : "6",
    "seven" : "7",
    "eight" : "8",
    "nine" : "9"
}

sum = 0
with open("./input.txt") as input:

    # loop through each line
    for line in input:

        for key, value in valid_digits.items():
            if (key in line):
                line = line.replace(key, f"{key}{value}{key}")

        num = ""
        # in each line, go forwards and backwards through the line to find numbers
        for forward in line:
            if (forward.isdigit()):
                # print(forward)
                num = forward
                break

        for backward in line[::-1]:
            if (backward.isdigit()):
                # print(backward)
                num += backward
                break
        
        # print(num)

        sum += int(num)
            
print(sum)
