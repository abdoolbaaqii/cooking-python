# This is a file for local variables and parameters


def print_twice(cat):
    print(cat)
    print(cat)
    

def cat_twice(part1, part2):
    cat = part1 + part2
    print_twice(cat)
    
    
line1 = "Always look on the "
line2 = "bright side of life."
cat_twice(line1, line2)

