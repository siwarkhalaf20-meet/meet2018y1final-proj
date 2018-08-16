import turtle
import random

joe=turtle.clone()
joe.color('blue')
joe.penup()
joe.goto(0, -250)

#river location
turtle.tracer(1,0)
##river drawing
turtle.penup()
turtle.goto(0, 210)
turtle.pendown()
turtle.goto(1000,210)
turtle.goto(-1000,210)
turtle.penup()
turtle.goto(-1000, -170)
turtle.pendown()
turtle.goto(1000,-170)

turtle.tracer(1,.5)


#turtles showness
turtle.hideturtle()
joe.penup()
#how much you move
SQUARE_SIZE=60
#directions

UP = 0
DOWN = 1
LEFT = 2
RIGHT = 3
direction = UP
#arrow keys
UP_ARROW = "Up"
LEFT_ARROW = "Left"
DOWN_ARROW = "Down"
RIGHT_ARROW = "Right"

lock = True


#direction function
def up():
    global direction 
    direction=UP

    print("You pressed the up key!")
    move_joe()
turtle.onkeypress(up, UP_ARROW) 
#turtle.listen()

def down():
    global direction 
    direction=DOWN 
    print("You pressed the down key!")
    move_joe()
turtle.onkeypress(down,DOWN_ARROW)
#turtle.listen()


def left():
    global direction
    direction=LEFT 
    print("You pressed the left key!")
    move_joe()
turtle.onkeypress(left, LEFT_ARROW)
#turtle.listen()

def right():
    global direction 
    direction=RIGHT 
    print("You pressed the right key!")
    move_joe()
turtle.onkeypress(right,RIGHT_ARROW)
turtle.listen()

turtle.penup()
#make trash
def make_trash():
    min_x=-int(250/SQUARE_SIZE)+1
    max_x=int(250/SQUARE_SIZE)-1
    min_y=-int(350/SQUARE_SIZE)-1
    max_y=int(-250/SQUARE_SIZE)+1
    
    #Pick a position that is a random multiple of SQUARE_SIZE
    trash_x = random.randint(min_x,max_x)*SQUARE_SIZE
    trash_y = random.randint(min_y,max_y)*SQUARE_SIZE-10
    print(trash_x,trash_y)
    trashes.append(turtle.clone())
    trashes[-1].goto(trash_x,trash_y)
    trashes[-1].showturtle()
    global trash_length
    trash_length +=1
    
    

trashes = []
trash_pos = []
trash_ind = None

def move_joe():
    global lock, trash_ind
    if lock:
        lock = False
        joe_pos = joe.pos()
        x_pos = joe_pos[0]
        y_pos = joe_pos[1]

        if direction==RIGHT:
            joe.goto(x_pos + SQUARE_SIZE, y_pos)
            print("You moved right!")
        elif direction==LEFT:
            joe.goto(x_pos - SQUARE_SIZE, y_pos)
            print("You moved left!")
        elif direction==UP:
            joe.goto(x_pos,y_pos+SQUARE_SIZE)
            print("you moved up!")

        else:
            joe.goto(x_pos,y_pos-SQUARE_SIZE)
            print("you moved down!")



        
    for trash in trashes:
        if joe.pos()==trash.pos():
            trash_ind = trashes.index(trash)
            print('lol')
    if trash_ind != None:
        trashes[trash_ind].goto(x_pos+5,y_pos)
        
    

        
    
    lock = True 


#trash amaunt 
trash_length= len(trashes)
while trash_length < 7:
    make_trash()


#grab trash



##logs
pos_list = []
stamp_list = []
turtle.shape('square')
START_LENGTH = 10
LOG_SIZE = 30
turtle.shapesize(2)


turtle.penup()
log1 = turtle.clone()
log2 = turtle.clone()
log3 = turtle.clone()
log4 = turtle.clone()
log5 = turtle.clone()
log6 = turtle.clone()
log7 = turtle.clone()
log8 = turtle.clone()
log9 = turtle.clone()
log10 = turtle.clone()
log11 = turtle.clone()
log12 = turtle.clone()


logs_list = [log1, log2, log3, log4, log5, log6, log7, log8, log9, log10, log11, log12]

log1.goto(800, 170)
log7.goto(800, 170)

log2.goto(1100, 110)
log8.goto(1800, 110)

log3.goto(1700, 50)
log9.goto(2700, 50)

log4.goto(1400, -10)
log10.goto(1700, -10)

log5.goto(1200, -70)
log11.goto(800, -70)

log6.goto(1700, -130)
log12.goto(2200, -130)










TIME_STEP = 100

for i  in range(START_LENGTH):
    for log in logs_list:
        c_pos,z_pos=log.pos()
            

        my_pos=(c_pos-LOG_SIZE,z_pos) 
        log.goto(my_pos) 
   
   
        pos_list.append(my_pos) 

                
        my_stamp = log.stamp()
        stamp_list.append(my_stamp)
        
   

def move_logs():
    x, y = joe.pos()
    if joe.pos() in pos_list:
        joe.goto(x - LOG_SIZE, y)
    for log in logs_list:
        log_x_pos, log_y_pos = log.pos()
        log.goto(log_x_pos - LOG_SIZE, log_y_pos)
        my_pos=log.pos() 
        pos_list.append(my_pos)

        #print(stamp_list)
        new_stamp = log.stamp()
        stamp_list.append(new_stamp)
        old_stamp = stamp_list.pop(0)
        log.clearstamp(old_stamp)
        pos_list.pop(0)
        if log_x_pos == -1000:
            log.hideturtle()
            print("Reached")
            log.goto(log_x_pos + 2100, log_y_pos)
            log.showturtle()
            
    
        
    turtle.ontimer(move_logs,TIME_STEP)
    
    
move_logs()
turtle.mainloop()

