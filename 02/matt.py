def solution1(filename):
    
    max_colors = {
        "red" : 12,
        "green" : 13, 
        "blue" : 14
    }

    sum = 0
    with open(filename) as input:

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
                # print(game_number)
                sum += int(game_number)
    
    return sum
            

def solution2(filename):

    min_colors = {
        "red" : -1,
        "green" : -1,
        "blue" : -1
    }

    sum = 0
    with open(filename) as input:

        for line in input:
            # print(line)
            halves = line.split(":")
            games = halves[1].split(";")

            for game in games:

                num_and_colors = [i.strip() for i in game.split(",")]

                for color in num_and_colors: # "3 blue"

                    for min_color, min_number in min_colors.items(): # "red" : 12
                        
                        current_num = int(color.split(" ")[0])
                        if min_color in color and current_num > min_number:
                            min_colors.update({min_color : current_num})

            add_mult = 1
            for min_color, min_number in min_colors.items():
                # print(f"color: {min_color} and num: {min_number}")
                add_mult *= min_number
                min_colors.update({min_color : -1})
            
            # print(f"{add_mult}\n")
            sum += add_mult
    
    return sum

file = input("what file is your input?\n")

print(f"Solution 1: {solution1(file)}")
print(f"Solution 2: {solution2(file)}")
