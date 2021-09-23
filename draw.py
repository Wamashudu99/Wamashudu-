# TODO: Step 1 - get shape (it can't be blank and must be a valid shape!)
def get_shape():
    while True:

        shape = input("Shape?: ").lower()
 #Users gets asked to input the shape they want to print
        if shape == 'square':
            return shape
        elif shape == 'triangle':
            return shape
        elif shape == 'pyramid':
            return shape
        elif shape == 'diamond':
            return shape
        

    
# TODO: Step 1 - get height (it must be int!)
def get_height():

    while True:
        height = input("Height?: ")
#Users gets asked to input the height of the shape they want to print
        if height.isdigit():
            if int(height) > 0 and int(height) <= 80:
                #The height inputed should be betweeen 0 and 80
                return int(height)



# TODO: Step 2
def draw_pyramid(height, outline):

   #if the users choose to print a full pyramid, this is the code that will run          
    if outline == False:
    
    
     k = 0
   
   #Used for loops to get and print the height of the pyramid
     for i in range(1, height+1):
        for space in range(1, (height-i)+1):
            print(end=" ")
 

        while k!=(2*i-1):
        #printing space required and staying in same line    
            print("*", end="")
            k += 1
        
        k = 0
        print( )
        #printing new line  

    #if the users choose to print a hollow pyramid, this is the code that will run 
    elif outline == True:

    #Used for loops to get and print the height of the hollow pyramid
     for i in range(height):
        for j in range(height- 1 -i):
            #printing space required and staying in same line
            print(' ', end='') 
        
        for j in range(2*i+1):
            if j==0 or j==2*i or i==height-1:
                print('*',end='')
            else:
                print(' ', end='')
        print() 
        #printing new line  
             

# TODO: Step 3
def draw_square(height, outline):

#if the users choose to print a full square, this is the code that will run     
    if outline == False:

        i = 0

#Used for while loops to get and print the height of the square
        while(i < height):
            j = 0
            while(j < height):      
                j = j + 1
                print('*', end = '')
            i = i + 1
            print('')

#if the users choose to print a a hollow square, this is the code that will run       
    elif outline == True:

    

     row = 1
#Used for while loops to get and print the height based on the rows and columns of the hollow square
     while(row <= height):
        column = 1
        while(column <= height ):
            if(row == 1 or row == height or column == 1 or column == height):
                print('*', end = '')
            else:
                print(' ', end = '')
            column = column + 1
        row = row + 1
        print()

 # TODO: Step 4
def draw_triangle(height, outline):

#if the users choose to print a full triangle, this is the code that will run     
    if outline == False:

     #Used for loops to get and print the height of the triangle
        for i in range(1, height):
            print(i*"*")
        for j in range(height):
            print("*", end="") #spaces
        print()
        #printing new lines

#if the users choose to print a hollow triangle, this is the code that will run     
    elif outline == True:

#Used for loops to get and print the height of the hollow triangle
        for i in range(height):
            for j in range(i+1):
                if j==0 or j==i or i==height-1:
                    print('*',end="") #spaces
                else:
                    print(" ", end="") #spaces
            print()
            #printing new lines

# TODO: Steps 2 to 4, 6 - add support for other shapes
def draw_diamond(height, outline):

  #if the users choose to print a full diamond, this is the code that will run  
    if outline == False:

        for i in range(height):
         print(" "*(height-i), "*"*(i*2+1))
        for i in range(height-2, -1, -1):
         print(" "*(height-i), "*"*(i*2+1))

#if the users choose to print a hollow diamond, this is the code that will run 
    elif outline == True:   
       
          #Upper part of hollow diamond
        for i in range(1, height+1):
            for j in range(1,height-i+1):
                print(" ", end="")
            for j in range(1, 2*i):
                if j==1 or j==2*i-1:
                    print("*", end="")
                else:
                    print(" ", end="")
            print()

        #Lower part of hollow diamond
        for i in range(height-1,0, -1):
            for j in range(1,height-i+1):
                print(" ", end="")
            for j in range(1, 2*i):
                if j==1 or j==2*i-1:
                    print("*", end="")
                else:
                    print(" ", end="")
            print()
    
    
def draw(shape, height, outline):
    #This function basically provides support for the shapes
    
    if shape == "pyramid":
    
       return  draw_pyramid(height,outline)

    elif shape == "square":
        
       return  draw_square(height,outline)

    elif shape == "triangle":
        
       return draw_triangle(height,outline)
    
    elif shape == "diamond":
        
        return draw_diamond(height,outline)

    
# TODO: Step 5 - get input from user to draw outline or solid

def get_outline():

#User gets asked to input 'Y/N' for the outline of the shape chosen
    outlines = input("Outline only?: ").lower()

#if the users choice is 'Y' then a hollow shape will be printed out
    if outlines.upper() == "Y":

        outline = True
 
#if the users choice is 'N' then a full shape will be printed out 
    elif outlines.upper() == "N":

        outline = False

    return outline

if __name__ == "__main__":
    shape_param = get_shape()
    height_param = get_height()
    outline_param = get_outline()
    draw(shape_param, height_param, outline_param)

