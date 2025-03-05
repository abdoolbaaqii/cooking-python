def bottle_verse(lyrics):
    print(lyrics)
    
    
lyrics = "99 bottles of beer on the wall, "
lyrics1 = "99 bottles of beer. "
lyrics2 = "Take one down, pass it around, "
lyrics3 = "98 bottles of beer on the wall. "


def print_lyrics():
    print(lyrics1)
    print(lyrics2)
    print(lyrics3)
    
    
for x in range(99, 0, -1):
    print("music", x)
    print(lyrics)
    print_lyrics()
    print()

