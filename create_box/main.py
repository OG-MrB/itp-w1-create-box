"""This is the entry point of the program."""


def create_box(height, width, character):
    line = character * width
    num1 = 0
    box = ''
    
    
    if height < 1 or width < 1:
        return 'invalid'
    while num1 < height:
        box += line + '\n'
        num1 += 1 
    return box
    
    
if __name__ == '__main__':
    create_box(3, 4, '*')





def create_outline(height, width, character):

    num1 = 0
    top = character * width
    bottom = character * width
    sides = (width - (width - 2)) * character
    while num1 < height:
        if num1 == 0:
            print top
        elif  num1 > 1 and num1 < height:
            print ("sides")
        else:
            print ("bottom")
        num1 += 1

create_outline(8,8,'^')


