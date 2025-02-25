def repeat(word, number):
    print(word * number)
    
    
reward = "Subhanallah, "
number = 3


def first_two_lines():
    repeat(reward, number)
    repeat(reward, number)


award = "Alhamdulillahi, "


def last_three_lines():
    repeat(award, 3)
    print("Allahu akbar, ")
    repeat(reward, 3)
        

def print_sentence():
    first_two_lines()
    last_three_lines()

    
for i in range(2):
    print("senntence", i)
    print_sentence()
    print()
    
    
    
    



    
