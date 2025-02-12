def habit(food):
    print(f"I love {food}")


# 1- functions that perform a task
# 2- functions that return a value
def make_habit(food):
    return f"I love {food}"


ABQ = make_habit("pounded yam")
file = open("ABQ.REASON", "w")
file.write(ABQ)