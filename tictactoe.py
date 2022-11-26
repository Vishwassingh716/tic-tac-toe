import random

a=0
b=0
pa=pb=0
p1=p2=p3=p4=p5=p6=p7=p8=p9=m='s'
#c1=c2=c3=c4=c5=c6=c7=c8=c9=n='s'
class pos:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def upw(self,v):
        v.penup()
        if(self.b<60):
            self.b=self.b+60
        else:
            self.b=self.b-120
        v.goto(self.a,self.b)
        v.pendown()
    def up(self):
        if(self.b<60):
            self.b=self.b+60
        else:
            self.b=self.b-120
    def down(self,v):
        v.penup()
        if(self.b>-60):
            self.b = self.b-60
        else:
            self.b+=120
        v.goto(self.a, self.b)
        v.pendown()
    def left(self,v):
        v.penup()
        if(self.a>-60):
            self.a=self.a-60
        else:
            self.a+=120
        v.goto(self.a, self.b)
        v.pendown()
    def right(self,v):
        v.penup()
        if(self.a<60):
            self.a=self.a+60
        else:
            self.a-=120
        v.goto(self.a, self.b)
        v.pendown()
z=pos(a,b)
pc=pos(pa,pb)
from tkinter import*
import turtle as tt
game = Tk()
game.geometry("400x600")
game.title("TIC X TAC X TOE")
Label(game,text="||| MAIN MENU |||",background="grey").pack()
Label(game,text="||| TIC X TAC O TOE X |||",background="grey").pack()
pl = Button(game,text="PLAYER VS PLAYER",activeforeground='white',activebackground='grey',command=lambda : click()).pack()
plc = Button(game,text="PLAYER VS COMPUTER",activeforeground='white',activebackground='grey',command=lambda : pvc()).pack()
ca= Canvas(game,background='grey',width=400,height=400,cursor="spider")
ca.create_line(150,100,150,280)
ca.create_line(210,100,210,280)
ca.create_line(90,160,270,160)
ca.create_line(90,220,270,220)
ca.pack()
exit = Button(game,text="EXIT",activeforeground='white',activebackground='grey',command=lambda :game.destroy()).pack()
def pvc():
    p = Toplevel()
    p.geometry("600x600")
    p.title("TIC X TAC O TOE X")
    Label(p, text="||| TIC X TAC O TOE X |||", background="grey").pack()
    Label(p, text="||| PLAYER VS COMPUTER |||", background="grey").pack()
    #b1 = Button(p, text="X", background="grey", activebackground="white", activeforeground="grey", height=2, width=4,command=lambda: mark(pc.a,pc.b))
    #b1.pack()
    cp = Canvas(p, width=400, height=400, cursor="spider")
    y = tt.RawTurtle(cp)
    y.goto(0,0)
    b2 = Button(p, text="O", background="grey", height=2, width=4, command=lambda: mark1(pc.a, pc.b))
    b2.pack()
    up = Button(p, text="^", background="grey", activebackground="white", activeforeground="grey", height=2, width=4,
                command=lambda: pc.upw(y))
    up.pack(side=LEFT)
    down = Button(p, text="v", activebackground="white", activeforeground="grey", background="grey", height=2, width=4,
                  command=lambda: pc.down(y))
    down.pack(side=RIGHT)
    left = Button(p, text="<", activebackground="white", activeforeground="grey", background="grey", height=2, width=4,
                  command=lambda: pc.left(y))
    left.pack(side=LEFT)
    right = Button(p, text=">", activebackground="white", activeforeground="grey", background="grey", height=2, width=4,
                   command=lambda: pc.right(y))
    right.pack(side=RIGHT)
    graph={1:(-60,60),2:(0,60),3:(60,60),4:(-60,0),5:(0,0),6:(60,0),7:(-60,-60),8:(0,-60),9:(60,-60)}
    inv={(-60,60):1,(0,60):2,(60,60):3,(-60,0):4,(0,0):5,(60,0):6,(-60,-60):7,(0,-60):8,(60,-60):9}
    position=[1,2,3,4,5,6,7,8,9]
    al=[]
    fin=[]
    '''
    def win(u,v,w):
        if (al.count(u) == 1 and al.count(v) == 1 and al.count(w) == 0 and position.count(w) == 1):
            q=graph.get(w)
            y.goto(q[0] + 15, q[1] + 15)
            y.pendown()
            y.goto(q[0] - 15, q[1] - 15)
            y.penup()
            y.goto(q[0] - 15, q[1] + 15)
            y.pendown()
            y.goto(q[0] + 15, q[1] - 15)
            y.penup()
            position.remove(w)
            '''
    def mark1(a, b):
        y.penup()
        y.pensize(3)
        y.goto(a, b - 10)
        y.pendown()
        al.append(inv.get((a, b)))
        position.remove(inv.get((a, b)))
        y.circle(15)
        #al.append(inv.get((a,b)))
        #position.remove(inv.get((a,b)))
        print(al,"al")
        mark(a,b)
    def mark(a, b):
        y.pensize(3)
        #i=ru(graph,position)
        #for j in al:
            #if(j==i):
                #return mark(a,b)
            #if(len(position)==0):
                #return
        if (al.count(1) == 1 and al.count(2) == 1 and al.count(3) == 1):
            y.penup()
            y.goto(graph.get(1))
            y.pendown()
            y.goto(graph.get(3))
            y.penup()
            Label(p, text="||| YOU WIN |||", background="grey").pack()
            Button(p, text="NEW GAME", activebackground="white", activeforeground="grey", background="grey", height=2, width=9,
                   command=lambda: pvc()).pack()
            return
        elif (al.count(4) == 1 and al.count(5) == 1 and al.count(6) == 1):
            y.penup()
            y.goto(graph.get(4))
            y.pendown()
            y.goto(graph.get(6))
            y.penup()
            Label(p, text="||| YOU WIN |||", background="grey").pack()
            Button(p, text="NEW GAME", activebackground="white", activeforeground="grey", background="grey", height=2,
                   width=9,command=lambda: pvc()).pack()
            return
        elif (al.count(7) == 1 and al.count(8) == 1 and al.count(9) == 1):
            y.penup()
            y.goto(graph.get(7))
            y.pendown()
            y.goto(graph.get(9))
            y.penup()
            Label(p, text="||| YOU WIN |||", background="grey").pack()
            Button(p, text="NEW GAME", activebackground="white", activeforeground="grey", background="grey", height=2,
                   width=9,
                   command=lambda: pvc()).pack()
            return
        elif (al.count(1) == 1 and al.count(4) == 1 and al.count(7) == 1):
            y.penup()
            y.goto(graph.get(1))
            y.pendown()
            y.goto(graph.get(7))
            y.penup()
            Label(p, text="||| YOU WIN |||", background="grey").pack()
            Button(p, text="NEW GAME", activebackground="white", activeforeground="grey", background="grey", height=2,
                   width=9,
                   command=lambda: pvc()).pack()
            return
        elif (al.count(2) == 1 and al.count(5) == 1 and al.count(8) == 1):
            y.penup()
            y.goto(graph.get(2))
            y.pendown()
            y.goto(graph.get(8))
            y.penup()
            Label(p, text="||| YOU WIN |||", background="grey").pack()
            Button(p, text="NEW GAME", activebackground="white", activeforeground="grey", background="grey", height=2,
                   width=9,
                   command=lambda: pvc()).pack()
            return
        elif (al.count(3) == 1 and al.count(6) == 1 and al.count(9) == 1):
            y.penup()
            y.goto(graph.get(3))
            y.pendown()
            y.goto(graph.get(9))
            y.penup()
            Label(p, text="||| YOU WIN |||", background="grey").pack()
            Button(p, text="NEW GAME", activebackground="white", activeforeground="grey", background="grey", height=2,
                   width=9,
                   command=lambda: pvc()).pack()
            return
        elif (al.count(1) == 1 and al.count(5) == 1 and al.count(9) == 1):
            y.penup()
            y.goto(graph.get(1))
            y.pendown()
            y.goto(graph.get(9))
            y.penup()
            Label(p, text="||| YOU WIN |||", background="grey").pack()
            Button(p, text="NEW GAME", activebackground="white", activeforeground="grey", background="grey", height=2,
                   width=9,
                   command=lambda: pvc()).pack()
            return
        elif (al.count(3) == 1 and al.count(5) == 1 and al.count(7) == 1):
            y.penup()
            y.goto(graph.get(3))
            y.pendown()
            y.goto(graph.get(7))
            y.penup()
            Label(p, text="||| YOU WIN |||", background="grey").pack()
            Button(p, text="NEW GAME", activebackground="white", activeforeground="grey", background="grey", height=2,
                   width=9,
                   command=lambda: pvc()).pack()
            return
        i = ru(graph, position)
        for j in al:
            if (j == i):
                return mark(a, b)

        def win(u, v, w):

            if (al.count(u) == 1 and al.count(v) == 1 and al.count(w) == 0 and position.count(w) == 1):
                q = graph.get(w)
                y.goto(q[0] + 15, q[1] + 15)
                y.pendown()
                y.goto(q[0] - 15, q[1] - 15)
                y.penup()
                y.goto(q[0] - 15, q[1] + 15)
                y.pendown()
                y.goto(q[0] + 15, q[1] - 15)
                y.penup()
                fin.append(w)
                if (fin.count(1) == 1 and fin.count(2) == 1 and fin.count(3) == 1):
                    y.penup()
                    y.goto(graph.get(1)[0]+15,graph.get(1)[1]+15)
                    y.pendown()
                    y.goto(graph.get(3)[0]+15,graph.get(3)[0]+15)
                    y.penup()
                    Label(p, text="||| YOU LOSE |||", background="grey").pack()
                    Button(p, text="NEW GAME", activebackground="white", activeforeground="grey", background="grey",
                           height=2,
                           width=9,
                           command=lambda: pvc()).pack()
                    return
                elif (fin.count(4) == 1 and fin.count(5) == 1 and fin.count(6) == 1):
                    y.penup()
                    y.goto(graph.get(4)[0]+15,graph.get(4)[0]+15)
                    y.pendown()
                    y.goto(graph.get(6)[0]+15,graph.get(6)[0]+15)
                    y.penup()
                    Label(p, text="||| YOU LOSE |||", background="grey").pack()
                    Button(p, text="NEW GAME", activebackground="white", activeforeground="grey", background="grey",
                           height=2,
                           width=9,
                           command=lambda: pvc()).pack()
                    return
                elif (fin.count(7) == 1 and fin.count(8) == 1 and fin.count(9) == 1):
                    y.penup()
                    y.goto(graph.get(7)[0]+15,graph.get(7)[0]+15)
                    y.pendown()
                    y.goto(graph.get(9)[0]+15,graph.get(9)[0]+15)
                    y.penup()
                    Label(p, text="||| YOU LOSE |||", background="grey").pack()
                    Button(p, text="NEW GAME", activebackground="white", activeforeground="grey", background="grey",
                           height=2,
                           width=9,
                           command=lambda: pvc()).pack()
                    return
                elif (fin.count(1) == 1 and fin.count(4) == 1 and fin.count(7) == 1):
                    y.penup()
                    y.goto(graph.get(1))
                    y.pendown()
                    y.goto(graph.get(7))
                    y.penup()
                    Label(p, text="||| YOU LOSE |||", background="grey").pack()
                    Button(p, text="NEW GAME", activebackground="white", activeforeground="grey", background="grey",
                           height=2,
                           width=9,
                           command=lambda: pvc()).pack()
                    return
                elif (fin.count(2) == 1 and fin.count(5) == 1 and fin.count(8) == 1):
                    y.penup()
                    y.goto(graph.get(2))
                    y.pendown()
                    y.goto(graph.get(8))
                    y.penup()
                    Label(p, text="||| YOU LOSE |||", background="grey").pack()
                    Button(p, text="NEW GAME", activebackground="white", activeforeground="grey", background="grey",
                           height=2,
                           width=9,
                           command=lambda: pvc()).pack()
                    return
                elif (fin.count(3) == 1 and fin.count(6) == 1 and fin.count(9) == 1):
                    y.penup()
                    y.goto(graph.get(3))
                    y.pendown()
                    y.goto(graph.get(9))
                    y.penup()
                    Label(p, text="||| YOU LOSE |||", background="grey").pack()
                    Button(p, text="NEW GAME", activebackground="white", activeforeground="grey", background="grey",
                           height=2,
                           width=9,
                           command=lambda: pvc()).pack()
                    return
                elif (fin.count(1) == 1 and fin.count(5) == 1 and fin.count(9) == 1):
                    y.penup()
                    y.goto(graph.get(1))
                    y.pendown()
                    y.goto(graph.get(9))
                    y.penup()
                    Label(p, text="||| YOU LOSE |||", background="grey").pack()
                    Button(p, text="NEW GAME", activebackground="white", activeforeground="grey", background="grey",
                           height=2,
                           width=9,
                           command=lambda: pvc()).pack()
                    return
                elif (fin.count(3) == 1 and fin.count(5) == 1 and fin.count(7) == 1):
                    y.penup()
                    y.goto(graph.get(3))
                    y.pendown()
                    y.goto(graph.get(7))
                    y.penup()
                    Label(p, text="||| YOU LOSE |||", background="grey").pack()
                    Button(p, text="NEW GAME", activebackground="white", activeforeground="grey", background="grey",
                           height=2,
                           width=9,
                           command=lambda: pvc()).pack()
                    return
                print(fin, "final")
                position.remove(w)

        if(al.count(1)==1 and al.count(2)==1 and al.count(3)==0 and position.count(3)==1):
            win(1,2,3)
        elif(al.count(1)==1 and al.count(2)==0 and al.count(3)==1 and position.count(2)==1):
            win(1,3,2)
        elif (al.count(2) == 1 and al.count(1) == 0 and al.count(3) == 1 and position.count(1) == 1):
            win(2, 3, 1)
        elif (al.count(4) == 1 and al.count(5) == 1 and al.count(6) == 0 and position.count(6) == 1):
            win(4,5,6)
        elif (al.count(4) == 1 and al.count(6) == 1 and al.count(5) == 0 and position.count(5) == 1):
            win(4,6,5)
        elif (al.count(6) == 1 and al.count(5) == 1 and al.count(4) == 0 and position.count(4) == 1):
            win(6,5,4)
        elif (al.count(7) == 1 and al.count(8) == 1 and al.count(9) == 0 and position.count(9) == 1):
            win(7,8,9)
        elif (al.count(7) == 1 and al.count(9) == 1 and al.count(8) == 0 and position.count(8) == 1):
            win(7,9,8)
        elif (al.count(8) == 1 and al.count(9) == 1 and al.count(7) == 0 and position.count(7) == 1):
            win(8,9,7)
        elif (al.count(1) == 1 and al.count(4) == 1 and al.count(7) == 0 and position.count(7) == 1):
            win(1,4,7)
        elif (al.count(1) == 1 and al.count(7) == 1 and al.count(4) == 0 and position.count(4) == 1):
            win(1,7,4)
        elif (al.count(4) == 1 and al.count(7) == 1 and al.count(1) == 0 and position.count(1) == 1):
            win(4,7,1)
        elif (al.count(2) == 1 and al.count(5) == 1 and al.count(8) == 0 and position.count(8) == 1):
            win(2,5,8)
        elif (al.count(5) == 1 and al.count(8) == 1 and al.count(2) == 0 and position.count(2) == 1):
            win(5,8,2)
        elif (al.count(8) == 1 and al.count(2) == 1 and al.count(5) == 0 and position.count(5) == 1):
            win(8,2,5)
        elif (al.count(3) == 1 and al.count(6) == 1 and al.count(9) == 0 and position.count(9) == 1):
            win(3,6,9)
        elif (al.count(3) == 1 and al.count(9) == 1 and al.count(6) == 0 and position.count(6) == 1):
            win(3,9,6)
        elif (al.count(6) == 1 and al.count(9) == 1 and al.count(3) == 0 and position.count(3) == 1):
            win(6,9,3)
        elif (al.count(1) == 1 and al.count(5) == 1 and al.count(9) == 0 and position.count(9) == 1):
            win(1,5,9)
        elif (al.count(1) == 1 and al.count(9) == 1 and al.count(5) == 0 and position.count(5) == 1):
            win(1,9,5)
        elif (al.count(5) == 1 and al.count(9) == 1 and al.count(1) == 0 and position.count(1) == 1):
            win(5,9,1)
        elif (al.count(3) == 1 and al.count(5) == 1 and al.count(7) == 0 and position.count(7) == 1):
            win(3,5,7)
        elif (al.count(3) == 1 and al.count(7) == 1 and al.count(5) == 0 and position.count(5) == 1):
            win(3,7,5)
        elif (al.count(5) == 1 and al.count(7) == 1 and al.count(2) == 0 and position.count(3) == 1):
            win(5,7,3)
        else:
            if(i!=(a,b)):
                position.remove(inv.get(i))
                y.goto(i[0] + 15, i[1] + 15)
                y.pendown()
                y.goto(i[0] - 15, i[1] - 15)
                y.penup()
                y.goto(i[0] - 15, i[1] + 15)
                y.pendown()
                y.goto(i[0] + 15, i[1] - 15)
                y.penup()
                fin.append(inv.get(i))
                print(fin, "final")
            else:
                mark(a,b)
    def ru(g, p):
        v = random.choices(position)
        print(v[0])
        i = graph.get(v[0])
        print(i)
        y.penup()
        y.goto(i[0], i[1])
        #position.remove(v[0])
        #fin.append(v[0])
        #print(fin,"final")
        print(position)
        return i
    y.penup()
    y.backward(30)
    y.right(90)
    y.pendown()
    y.forward(90)
    y.backward(180)
    y.penup()
    y.forward(60)
    y.right(90)
    y.pendown()
    y.forward(60)
    y.backward(180)
    y.penup()
    y.forward(60)
    y.right(90)
    y.pendown()
    y.forward(60)
    y.backward(180)
    y.penup()
    y.forward(60)
    y.right(90)
    y.pendown()
    y.forward(60)
    y.back(180)
    y.penup()
    y.goto(0, 0)
    cp.pack()
    exit = Button(p, text="EXIT", activeforeground='white', activebackground='grey', command=lambda: p.destroy()).pack()
    p.mainloop()
def click():
   r = Toplevel()
   r.geometry("600x600")
   r.title("TIC X TAC O TOE X")
   Label(r,text="||| TIC X TAC O TOE X |||",background="grey").pack()
   Label(r, text="||| PLAYER VS PLAYER |||", background="grey").pack()
   '''
   b1=Button(r,text="X",background="grey", activebackground="white",activeforeground="grey",height=2,width=4,command=lambda :cross(z.a,z.b))
   b1.pack()
   b2=Button(r,text="O",background="grey",height=2,width=4,command=lambda :o(z.a,z.b))
   b2.pack()
   up=Button(r,text="^",background="grey",activebackground="white",activeforeground="grey",height=2,width=4,command=lambda :z.upw())
   up.pack(side=LEFT)
   down=Button(r,text="v",activebackground="white",activeforeground="grey",background="grey",height=2,width=4,command=lambda : z.down())
   down.pack(side=RIGHT)
   left=Button(r,text="<",activebackground="white",activeforeground="grey",background="grey",height=2,width=4,command=lambda : z.left())
   left.pack(side=LEFT)
   right=Button(r,text=">",activebackground="white",activeforeground="grey",background="grey",height=2,width=4,command=lambda: z.right())
   right.pack(side=RIGHT)
   '''
   c = Canvas(r,width=400,height=400,cursor="spider")
   '''c.create_line(150,100,150,280)
   c.create_line(210,100,210,280)
   c.create_line(90,160,270,160)
   c.create_line(90,220,270,220)'''
   x=tt.RawTurtle(c)
   b1 = Button(r, text="X", background="grey", activebackground="white", activeforeground="grey", height=2, width=4,
               command=lambda: cross(z.a, z.b))
   b1.pack()
   b2 = Button(r, text="O", background="grey", height=2, width=4, command=lambda: o(z.a, z.b))
   b2.pack()
   up = Button(r, text="^", background="grey", activebackground="white", activeforeground="grey", height=2, width=4,
               command=lambda: z.upw(x))
   up.pack(side=LEFT)
   down = Button(r, text="v", activebackground="white", activeforeground="grey", background="grey", height=2, width=4,
                 command=lambda: z.down(x))
   down.pack(side=RIGHT)
   left = Button(r, text="<", activebackground="white", activeforeground="grey", background="grey", height=2, width=4,
                 command=lambda: z.left(x))
   left.pack(side=LEFT)
   right = Button(r, text=">", activebackground="white", activeforeground="grey", background="grey", height=2, width=4,
                  command=lambda: z.right(x))
   right.pack(side=RIGHT)
   def mark1(a,b):
       x.pensize(3)
       x.goto(a, b - 10)
       x.pendown()
       x.circle(15)

   def mark(a, b):
       x.pensize(3)
       x.goto(a + 15, b + 15)
       x.pendown()
       x.goto(a - 15, b - 15)
       x.penup()
       x.goto(a - 15, b + 15)
       x.pendown()
       x.goto(a + 15, b - 15)

   #x.hideturtle()
   #tt.bgcolor("purple")
   #def play():
    #x.penup()
    #x.goto(0,0)
   def cross(a,b):
       global m
       if(m!="x"):
           x.penup()
           if(a==0 and b==0):
               global p5
               if p5 == 's':
                   p5 = "x"
                   m = "x"
                   mark(a, b)
           elif (a == 0 and b == 60):
               global p2
               if p2 == 's':
                   p2 = "x"
                   m = "x"
                   mark(a, b)
           elif(a==60 and b==0):
               global p6
               if p6 == 's':
                   p6 = "x"
                   m = "x"
                   mark(a, b)
           elif (a == 0 and b == -60):
               global p8
               if p8 == 's':
                   p8 = "x"
                   m = "x"
                   mark(a, b)
           elif (a == 60 and b == 60):
               global p3
               if p3 == 's':
                   p3 = "x"
                   m = "x"
                   mark(a, b)
           elif(a==60 and b==-60):
               global p9
               if p9=='s':
                   p9="x"
                   m = "x"
                   mark(a,b)
           elif (a == -60 and b == -60):
               global p7
               if p7=='s':
                   p7 = "x"
                   m = "x"
                   mark(a, b)
           elif (a == -60 and b == 0):
               global p4
               if p4=='s':
                   p4 = "x"
                   m = "x"
                   mark(a, b)
           elif (a == -60 and b == 60):
               global p1
               if p1=='s':
                   p1 = "x"
                   m = "x"
                   mark(a, b)
           if (p1 == 'x' and p2=='x' and p3 == 'x'):
               x.penup()
               x.goto(-80, 60)
               x.pendown()
               x.goto(80, 60)
               Label(r, text="||| X IS WINNER |||", background="grey").pack()
           elif (p1 == 'x' and p4=='x'and p7 == 'x'):
               x.penup()
               x.goto(-60, 80)
               x.pendown()
               x.goto(-60, -80)
               Label(r, text="||| X IS WINNER |||", background="grey").pack()
           elif (p1 == 'x' and p5=='x'and p9 == 'x'):
               x.penup()
               x.goto(-80, 80)
               x.pendown()
               x.goto(80, -80)
               Label(r, text="||| X IS WINNER |||", background="grey").pack()
           elif (p9 == 'x' and p8=='x'and p7 == 'x'):
               x.penup()
               x.goto(80, -60)
               x.pendown()
               x.goto(-80, -60)
               Label(r, text="||| X IS WINNER |||", background="grey").pack()
           elif (p3 == 'x' and p6=='x'and p9 == 'x'):
               x.penup()
               x.goto(60, 80)
               x.pendown()
               x.goto(60, -80)
               Label(r, text="||| X IS WINNER |||", background="grey").pack()
           elif (p4 == 'x' and p5=='x'and p6 == 'x'):
               x.penup()
               x.goto(-80, 0)
               x.pendown()
               x.goto(80, 0)
               Label(r, text="||| X IS WINNER |||", background="grey").pack()
           elif (p2 == 'x' and p5=='x'and p8 == 'x'):
               x.penup()
               x.goto(0, 80)
               x.pendown()
               x.goto(0, -80)
               Label(r,text="||| X IS WINNER |||",background="grey").pack()
           elif (p3 == 'x' and p5=='x'and p7 == 'x'):
               x.penup()
               x.goto(80, 80)
               x.pendown()
               x.goto(-80, -80)
               Label(r, text="||| X IS WINNER |||", background="grey").pack()
   def o(a,b):
       global m
       if(m!="o"):
           x.penup()
           if (a == 0 and b == 0):
               global p5
               if p5 == 's':
                   p5 = "o"
                   m='o'
                   mark1(a, b)
           elif (a == 0 and b == 60):
               global p2
               if p2 == 's':
                   p2 = "o"
                   m = 'o'
                   mark1(a, b)
           elif (a == 60 and b == 0):
               global p6
               if p6 == 's':
                   p6 = "o"
                   m = 'o'
                   mark1(a, b)
           elif (a == 0 and b == -60):
               global p8
               if p8 == 's':
                   p8 = "o"
                   m = 'o'
                   mark1(a, b)
           elif (a == 60 and b == 60):
               global p3
               if p3 == 's':
                   p3 = "o"
                   m = 'o'
                   mark1(a, b)
           elif (a == 60 and b == -60):
               global p9
               if p9 == 's':
                   p9 = "o"
                   m = 'o'
                   mark1(a, b)
           elif (a == -60 and b == -60):
               global p7
               if p7 == 's':
                   p7 = "o"
                   m = 'o'
                   mark1(a, b)
           elif (a == -60 and b == 0):
               global p4
               if p4 == 's':
                   p4 = "o"
                   m = 'o'
                   mark1(a, b)
           elif (a == -60 and b == 60):
               global p1
               if p1 == 's':
                   p1 = "o"
                   m = 'o'
                   mark1(a, b)
           if (p1 == 'o' and p2 == 'o' and p3 == 'o'):
               x.penup()
               x.goto(-80, 60)
               x.pendown()
               x.goto(80, 60)
               Label(r, text="||| O IS WINNER |||", background="grey").pack()
           elif (p1 == 'o' and p4 == 'o' and p7 == 'o'):
               x.penup()
               x.goto(-60, 80)
               x.pendown()
               x.goto(-60, -80)
               Label(r, text="||| O IS WINNER |||", background="grey").pack()
           elif (p1 == 'o' and p5 == 'o' and p9 == 'o'):
               x.penup()
               x.goto(-80, 80)
               x.pendown()
               x.goto(80, -80)
               Label(r, text="||| O IS WINNER |||", background="grey").pack()
           elif (p9 == 'o' and p8 == 'o' and p7 == 'o'):
               x.penup()
               x.goto(80, -60)
               x.pendown()
               x.goto(-80, -60)
               Label(r, text="||| O IS WINNER |||", background="grey").pack()
           elif (p3 == 'o' and p6 == 'o' and p9 == 'o'):
               x.penup()
               x.goto(60, 80)
               x.pendown()
               x.goto(60, -80)
               Label(r, text="||| O IS WINNER |||", background="grey").pack()
           elif (p4 == 'o' and p5 == 'o' and p6 == 'o'):
               x.penup()
               x.goto(-80, 0)
               x.pendown()
               x.goto(80, 0)
               Label(r, text="||| O IS WINNER |||", background="grey").pack()
           elif (p2 == 'o' and p5 == 'o' and p8 == 'o'):
               x.penup()
               x.goto(0, 80)
               x.pendown()
               x.goto(0, -80)
               Label(r, text="||| O IS WINNER |||", background="grey").pack()
           elif (p3 == 'o' and p5 == 'o' and p7 == 'o'):
               x.penup()
               x.goto(80, 80)
               x.pendown()
               x.goto(-80, -80)
               Label(r, text="||| O IS WINNER |||", background="grey").pack()
   '''def upw(a,b):
       x.goto(a,b+60)'''
   x.penup()
   x.backward(30)
   x.right(90)
   x.pendown()
   x.forward(90)
   x.backward(180)
   x.penup()
   x.forward(60)
   x.right(90)
   x.pendown()
   x.forward(60)
   x.backward(180)
   x.penup()
   x.forward(60)
   x.right(90)
   x.pendown()
   x.forward(60)
   x.backward(180)
   x.penup()
   x.forward(60)
   x.right(90)
   x.pendown()
   x.forward(60)
   x.back(180)
   x.penup()
   x.goto(0,0)
   c.pack()
   exit = Button(r, text="EXIT", activeforeground='white', activebackground='grey',command=lambda: r.destroy()).pack()
   r.mainloop()
game.mainloop()