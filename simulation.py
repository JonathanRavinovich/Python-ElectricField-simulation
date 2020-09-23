import tkinter
import random as rand
import math

'''
this class is the particle in the simulation
it has x y positions, mass, original x (the x that he been created with), original y (the y that he been created with),
velocity (vector), velocity in the x axis (vector), velocity in the y axis (vector), acceleration, original velocity and
the gradient

(xready and yready used for the graphics, when they both true the particle will removed from the particle list)
'''
class particle:

    def __init__(self,x,y,m,q):
        self.x = x
        self.y = y
        self.m = m
        self.q = q
        self.ox = x
        self.oy = y
        self.vel = 0
        self.velx = 0
        self.vely = 0
        self.a = 0
        self.ov = 0
        self.time = 0
        self.xready = False
        self.yready = False
        self.grad = ((self.y-300)/(self.x-500))
    #this function is updating the particle, its updating the x axis position and y axis position
    def update(self,tx,ty):

        self.time += delay
        #checking if the charges are not both positive or negative and then the particle updating with pull
        if (q<0 and Q>=0) or (q>=0 and Q<0):
            #checking if it near the electric field center if yes xready is true
            if abs(tx-self.x)<10:
                self.xready = True
            #checking if the particle x is higher or lower from the 
            if(self.x<tx):
                self.x+=math.cos(math.atan(self.grad))*self.vel
                self.y+=math.sin(math.atan(self.grad))*self.vel
            else:
                self.x-=math.cos(math.atan(self.grad))*self.vel
                self.y-=math.sin(math.atan(self.grad))*self.vel

            if abs(ty-self.y)<10:
                self.yready = True
        #if the charges are both positive or both negative the particles updating with repel
        else:

            if(self.x<tx):
                self.x-=math.cos(math.atan(self.grad))*self.vel
                self.y-=math.sin(math.atan(self.grad))*self.vel
            else:
                self.x+=math.cos(math.atan(self.grad))*self.vel
                self.y+=math.sin(math.atan(self.grad))*self.vel




class electricField:

    def __init__(self,x,y,q,d):
        self.x = x
        self.y = y
        self.q = q
        self.d = d

    def getForce(self,d,q):
        k = 9*(10**9)

        try:
            e = (k*self.q)/(d*d)
        except:
            e = 0

        f = e * q

        return f



def getMaxVel():
    vel = 0
    for i in particles:
        if i.vel>vel:
            vel = i.vel

    return vel

def getMinVel():
    vel = getMaxVel()
    for i in particles:
        if i.vel<vel:
            vel = i.vel

    return vel

def updateGraphics():
    canvas.delete("all")

    canvas.create_oval(ef.x-10,ef.y-10,ef.x+10,ef.y+10,fill="black")
    canvas.create_oval(ef.x-ef.d,ef.y-ef.d,ef.x+ef.d,ef.y+ef.d)

    for i in particles:
        canvas.create_oval(i.x-2,i.y-2,i.x+2,i.y+2)

        if debugMode == True:
            canvas.create_line(i.x,i.y,ef.x,i.y)
            canvas.create_line(ef.x,i.y,ef.x,ef.y)
            canvas.create_line(i.x,i.y,ef.x,ef.y)

    canvas.create_text(32,10,text="particles: "+str(len(particles)))
    canvas.create_text(40,20,text="max velocity: ")
    canvas.create_text(135,20,text="{0:.4f}".format(getMaxVel()))
    canvas.create_text(40,30,text="min velocity: ")
    canvas.create_text(135,30,text="{0:.4f}".format(getMinVel()))
    canvas.create_text(42,40,text="current mass: ")
    canvas.create_text(110,40,text=str(m))
    canvas.create_text(53,50,text="current particle q: ")
    canvas.create_text(133,51,text=str(q))
    canvas.create_text(70,60,text="current pointer charge q: ")
    canvas.create_text(165,60,text=str(Q))
    canvas.create_text(90,72,text="time: ")
    canvas.create_text(215,72,text=str(int(timeCounter)))




def update():
    dis = 0

    global max_particles
    global delay

    max_particles = max_particles_slider.get()
    delay = delay_slider.get()

    global q
    global Q
    global m
    global timeCounter

    timeCounter += delay/1000

    ef.q = Q

    for i in particles:
        if (i.ox<ef.x and i.x>ef.x) or (i.ox>ef.x and i.x<ef.x) or (i.oy<ef.y and i.y>ef.y) or (i.oy>ef.y and i.y<ef.y):
            del particles[particles.index(i)]
            updateGraphics()
            break

    for i in range(len(particles)):
        if (particles[i].xready == True and particles[i].yready== True) or particles[i].x>1000 or particles[i].x<0 or particles[i].y>600 or particles[i].y<0:
            del particles[i]
            updateGraphics()
            break

    for i in range(len(particles)):
        p = particles[i]
        dis = (math.sqrt((p.x-ef.x)**2+(p.y-ef.y)**2))
        particles[i].a = ef.getForce(dis,q)/p.m
        particles[i].ov = particles[i].a

        particles[i].velx = particles[i].velx + particles[i].a * (particles[i].time/1000)

        particles[i].vely = particles[i].vely + particles[i].a * (particles[i].time/1000)

        particles[i].vel = math.sqrt(pow(particles[i].velx,2)+pow(particles[i].vely,2))

        particles[i].update(500,300)
        particles[i].m = m
        particles[i].q = q


def createParticle():
    global m
    randomx = 0
    randomy = 0

    if len(particles)<max_particles:
        if (q<0 and Q>=0) or (q>=0 and Q<0):
            randomx = rand.randint(100,900)
            randomy = rand.randint(100,600)

            while randomx==500:
                randomx = rand.randint(100,900)
            while randomy==300:
                randomy = rand.randint(100,600)

            particles.append(particle(randomx,randomy,m,q))
        else:

            randomx = rand.randint(450,550)
            randomy = rand.randint(250,350)

            while randomx==500:
                randomx = rand.randint(450,550)
            while randomy==300:
                randomy = rand.randint(250,350)

            particles.append(particle(randomx,randomy,m,q))
            #dis = math.sqrt((particles[len(particles)-1].x-ef.x)**2+(particles[len(particles)-1].y-ef.y)**2)
           # particles[len(particles)-1].velx = ef.getForce(dis,particles[len(particles)-1].q)/m
           # particles[len(particles)-1].vely = ef.getForce(dis,particles[len(particles)-1].q)/m


def getMassEntry():
    global m
    try:
        m = float(massEntry.get())
    except ValueError:
        pass

def getqEntry():
    global q
    try:
        q = float(qEntry.get())
    except ValueError:
        pass

def getQEntry():
    global Q
    try:
        Q = float(QEntry.get())
    except ValueError:
        pass

def keyboard(event):

    global debugMode

    if event.char == '\r':
        getqEntry()
        getMassEntry()
        getQEntry()

    if event.char == 'p':
        if debugMode == False:
            debugMode = True
        else:
            debugMode = False


particles = []

timeCounter = 0
delay = 10
m = 4
Q = 10**-6
q = -(10**-6)
max_particles = 1

debugMode = False

ef = electricField(500,300,Q,500)


root = tkinter.Tk()

canvas = tkinter.Canvas(root,width=1000,height = 600,background="gray63",highlightbackground="gray63")
canvas.pack()

max_particles_label = tkinter.Label(root,text="Particles",bg="blue",fg="white")
max_particles_label.place(x=0,y=688)

max_particles_slider = tkinter.Scale(root,from_=0,to=300,orient=tkinter.HORIZONTAL)
max_particles_slider.set(1)
max_particles_slider.place(x=52,y=680,width=220)

delay_slider = tkinter.Scale(root,from_=10,to=10000,orient=tkinter.HORIZONTAL,)
delay_slider.set(10)
delay_slider.place(x=390,y=680,width=220)

delay_label = tkinter.Label(root,text="update delay\n(1000 - 1 sec)",bg="blue",fg="white")
delay_label.place(x=300,y=684)



root.configure(background='blue')
root.title("Simulation")

massLabel = tkinter.Label(root,text="Mass (Kg)",bg="blue",fg="white")
massLabel.place(x=0,y=604)

massEntry = tkinter.Entry(root,bg="black",fg="white")
massEntry.place(x=56,y=606)

qLabel = tkinter.Label(root,text="Particle Charge (C)",bg="blue",fg="white")
qLabel.place(x=0,y=638)

qEntry = tkinter.Entry(root,bg="black",fg="white")
qEntry.place(x=104,y=640)

QLabel = tkinter.Label(root,text="Field Charge (C)",bg="blue",fg="white")
QLabel.place(x=180,y=604)

QEntry = tkinter.Entry(root,bg="black",fg="white")
QEntry.place(x=270,y=606)

desLabel = tkinter.Label(root,bg="blue",fg="white",text="Description:\n this program is simulating an electric field")
desLabel.place(x=400,y=604)

root.geometry("1000x800")

root.bind("<Key>",keyboard)


updateGraphics()
update()

def task():
    updateGraphics()
    createParticle()
    update()
    root.after(delay,task)

root.after(delay,task)

tkinter.mainloop()


