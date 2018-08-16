import turtle
import random
whats_up = input('hey you are going to see a river now just cross it and do something')
print(whats_up)
turtle.bgpic('backg.gif')
turtle.register_shape('adg.gif')
joe=turtle.clone()
joe.shape('adg.gif')
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

scorev = 0


turtle.tracer(1,.05)
##make the bing##
turtle.register_shape("a.gif")
bin1 = turtle.clone()
bin1.shape("a.gif")
bin1.penup()
bin1.goto(-240,350)

   
turtle.register_shape("b.gif")
bin2 = turtle.clone()
bin2.shape("b.gif")
bin2.penup()
bin2.goto(0,350)

turtle.register_shape("c.gif")
bin3 = turtle.clone()
bin3.shape("c.gif")
bin3.penup()
bin3.goto(240,350)

def score(positionscore):
    turtle.undo()
    global scorev
    turtle.goto(positionscore)
    scorev += 1
    turtle.hideturtle()
    turtle.write(scorev, font=("Arial", 16, "normal"))


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

safe1 = turtle.clone()
safe2 = turtle.clone()
safe2 = turtle.clone()


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

def random_pos():
    min_x=-int(250/SQUARE_SIZE)+1
    max_x=int(250/SQUARE_SIZE)-1
    min_y=-int(350/SQUARE_SIZE)-1
    max_y=int(-250/SQUARE_SIZE)+1

    trash_x = random.randint(min_x,max_x)*SQUARE_SIZE
    trash_y = random.randint(min_y,max_y)*SQUARE_SIZE-10

    return trash_x,trash_y



#make trash
def make_trash():
    turtle.register_shape('e.gif')
    turtle.register_shape('trash.gif')
    turtle.register_shape('pe.gif')
    trashes.append(turtle.clone())
    trashes[-1].goto(random_pos())
    trashes[-1].shape("pe.gif")
    trashes[-1].showturtle()
    global trash_length
    trash_length +=1

    trashes.append(turtle.clone())
    #turtle.register_shape('papers.gif')
    trashes[-1].shape("trash.gif")
    trashes[-1].goto(random_pos())
    trashes[-1].showturtle()    

    trashes.append(turtle.clone())
    #turtle.register_shape('trash.gif')
    trashes[-1].shape('e.gif')
    trashes[-1].goto(random_pos())
    trashes[-1].showturtle()

'''
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
    
'''
##make joe move
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

        print(joe.pos())

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
        trashes[trash_ind].goto(x_pos,y_pos)
    if joe.pos() == bin1.pos():
        if trash_ind != None:
            if trashes[trash_ind].shape() == "trash.gif":
                print('trash')
                trashes[trash_ind].ht()
                trash_ind = None
                score((0, -400))
            
    if joe.pos() == bin2.pos():
        if trash_ind != None:
            if trashes[trash_ind].shape() == "e.gif":
                print('trash')
                trashes[trash_ind].ht()
                trash_ind = None
                score((0, -400))
            
    if joe.pos() == bin3.pos():
        if trash_ind != None:
            if trashes[trash_ind].shape() == "pe.gif":
                print('trash')
                trashes[trash_ind].ht()
                trash_ind = None
                score((0, -400))
           
   
        
        
    

        
    
    lock = True 



##make the logs apper randomlly

#grab trash

#turtle.register_shape('square')

##logs
pos_list = []
stamp_list = []
turtle.shape('square')
START_LENGTH = 10  #HOW LONG ARE THE LOGS
LOG_SIZE = 30
turtle.shapesize(2)
turtle.color('brown')



turtle.penup()
logs_list = []
for i in range(50):
    logs_list.append(turtle.clone())

x_min = 1000
x_max = 4000


def ran_y():
    y_max = 200//60
    y_min = -120//60
    return random.randint(y_min, y_max)*60 - 10

for log in logs_list:
    x = random.randint(x_min//30,x_max//30)*30
    y = ran_y()
    print(y)
    log.goto(x,y)
    

TIME_STEP = 100

for i  in range(START_LENGTH):
    for log in logs_list:
        log_x_pos, log_y_pos=log.pos()
        my_pos=(log_x_pos-LOG_SIZE,log_y_pos) 
        log.goto(my_pos) 
        pos_list.append(my_pos) 
        my_stamp = log.stamp()
        stamp_list.append(my_stamp)
        
   
die = 0
joe_stamp = None
def move_logs():
    global die, joe_stamp
    joe.st()
    if joe_stamp != None:
        joe.clearstamp(joe_stamp)
    
    x, y = joe.pos()
    #print("joe pos:",joe.pos(),"pos list:",pos_list)
    if joe.pos() in pos_list:
        joe.ht()
        joe_stamp = joe.stamp()
        print("on log")
        
        joe.goto(x - LOG_SIZE, y)
        if trash_ind != None:
            x_pos, y_pos = joe.pos()
            trashes[trash_ind].goto(x_pos+5,y_pos)
    elif y > -170 and y < 210:
        joe.goto(0,-250)
        die += 1
        if die == 3:
            quit()
    else:
        joe.goto((x//60)*60,y)
        #quit()
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
        if log_x_pos <= -1000:
            log.hideturtle()
            #print("Reached")
            if random.randint(1,5) == 1:
                log.goto(2100, log_y_pos)
                log.showturtle()
            
    
        
    turtle.ontimer(move_logs,TIME_STEP)
'''turtle.register_shape("index.gif")
bin1 = turtle.clone()
bin1.shape("index.gif")
bin1.penup()
bin1.goto(-200,345)

   
turtle.register_shape("RecycleBinIPyramidlid.gif")
bin2 = turtle.clone()
bin2.shape("RecycleBinIPyramidlid.gif")
bin2.penup()
bin2.goto(10,350)

turtle.register_shape("paperbin.gif")
bin3 = turtle.clone()
bin3.shape("paperbin.gif")
bin3.penup()
bin3.goto(200,350)'''
##turtle.register_shape('adg.gif')
##joe=turtle.clone()
##joe.shape('adg.gif')    
#trash amaunt 
trash_length= len(trashes)
while trash_length < 3:
    make_trash()
move_logs()
turtle.mainloop()

