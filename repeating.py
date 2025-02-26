def repeat(word , number):
    print(word * number)
    
    
forgiveness = "Astaghfirullah  "
hobby = "Subhanallah  "


def first_two_lines():
    repeat(forgiveness, 3)
    repeat(hobby, 3)
    
    
habit = "Alhamdulillahi  "
praising = "Allahu akbar  "
believe = "La'ilaha ila Allah  "


def last_three_lines():
    repeat(habit, 3)
    repeat(praising, 3)
    repeat(believe, 1)
    
    
def print_sentence():
    first_two_lines()
    last_three_lines()
    
    
for i in range(3):
    print("keywords", i)
    print_sentence()
    print()