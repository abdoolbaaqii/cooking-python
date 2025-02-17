def habit(food):
    print(f"I love {food}")


def habit(food):
    return f"I love {food}"


message = habit("pounded yam")
print(message)
file = open("content.py", "w")
file.write(message)