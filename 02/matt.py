
max_colors = {
    "red" : 12,
    "green" : 13, 
    "blue" : 14
}

def solution1(filename):

    sum = 0
    with open("./input.txt") as input:

        for line in input:
            # print(line)
            valid_game = True
            halves = line.split(":")

            game_number = halves[0].split(" ")[1]
            games = halves[1].split(";")

            for game in games:

                num_and_colors = [i.strip() for i in game.split(",")]

                for color in num_and_colors: # "3 blue"

                    for max_color, max_number in max_colors.items(): # "red" : 12
                        
                        if max_color in color and int(color.split(" ")[0]) > max_number:
                            valid_game = False
                            break

            if (valid_game):
                print(game_number)
                sum += int(game_number)
    
    return sum
            

def solution2(filename):
    pass


file = "" #input("what file is your input?\n")


print(f"Solution 1: {solution1(file)}")
print(f"Solution 2: {solution2(file)}")