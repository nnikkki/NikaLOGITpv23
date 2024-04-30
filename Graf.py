from tkinter import *
from tkinter import messagebox as mb
import matplotlib.pyplot as plt
import numpy as np

def draw_figure(figure_function):
    figure_function()

def Keith():
    x1=np.arange(0,9.5,0.5)
    y1=(2/27)*x1*x1-3   
    x2=np.arange(-10,0.5,0.5)
    y2=0.04*x2*x2-3
    x3=np.arange(-9,-2.5,0.5)
    y3=(2/9)*(x3+6)**2+1
    x4=np.arange(-3,9.5,0.5)
    y4=(-1/12)*(x4-3)**2+6
    x5=np.arange(5,9,0.5)
    y5=(1/9)*(x5-5)**2+2
    x6=np.arange(5,8.5,0.5)
    y6=(1/8)*(x6-7)**2+1.5
    x7=np.arange(-13,-8.5,0.5)
    y7=(-0.75)*(x7+11)**2+6
    x8=np.arange(-15,-12.5,0.5)
    y8=(-0.5)*(x8+13)**2+3
    x9=np.arange(-15,-10,0.5)
    y9=[1]*len(x9)
    x10=np.arange(3,4,0.5)
    y10=[3]*len(x10)
    plt.figure()
    plt.plot(x1,y1,'b-',x2,y2,'b-',x3,y3,'b-',x4,y4,'b-',x5,y5,'b-',x6,y6,'b-',x7,y7,'b-',x8,y8, 'b-',x9,y9, 'b-', x10,y10,'b-')
    plt.title("Keith")
    plt.xlabel("y")
    plt.ylabel("x")
    plt.grid(True)
    plt.show()

def Kilpkonn():
    x1=np.arange(-7,7,0.5)
    y1=(-3/49)*x1**2+8
    x2=np.arange(-7,7,0.5)
    y2=(4/49)*x2**2+1
    x3=np.arange(-6.8,-2,0.5)
    y3=-0.75*(x3+4)**2+11
    x4=np.arange(2,6.8,0.5)
    y4=-0.75*(x4-4)**2+11
    x5=np.arange(-5.8,-2.8,0.5)
    y5=-(x5+4)**2+9 
    x6=np.arange(2.8,5.8,0.5)
    y6=-(x6-4)**2+9 
    x7=np.arange(-4,4.5,0.5)
    y7=(4/9)*x7**2-5
    x8=np.arange(-5.2,5.5,0.5)
    y8=(4/9)*x8**2-9
    x9=np.arange(-7,-2.8,0.5)
    y9=(-1/16)*(x9+3)**2-6
    x10=np.arange(2.8,7,0.5)
    y10=(-1/16)*(x10-3)**2-6
    x11=np.arange(-7,0,0.5)
    y11=(1/9)*(x11+4)**2-11
    x12=np.arange(0,7,0.5)
    y12=(1/9)*(x12-4)**2-11
    x13=np.arange(-7,-4,0.5)
    y13=-(x13+5)**2
    x14=np.arange(4.5,7.5,0.5)
    y14=-(x14-5)**2
    x15=np.arange(-3,3,0.5)
    y15=(2/9)*x15**2+2
    plt.figure()
    plt.plot(x1,y1,"g-s",x2,y2,"g-s",x3,y3,"g-s",x4,y4,"g-s",x5,y5,"k-s",x6,y6,"k-s",x7,y7,"g-s",x8,y8,"g-s",x9,y9,"g-s",x10,y10,"g-s",x11,y11,"g-s",x12,y12,"g-s",x13,y13,"g-s",x14,y14,"g-s",x15,y15,"r-s")
    plt.title("Kilpkonn")
    plt.ylabel("Y")
    plt.xlabel("X")
    plt.grid(True)
    plt.show()


def Vihmavari():
    x1=np.arange(-12,12,0.5)
    y1=(-1/18)*x1**2+12
    x2=np.arange(-4,4,0.5)
    y2=(-1/8)*x2**2+6
    x3=np.arange(-12,-4,0.5)
    y3=(-1/8)*(x3+8)**2+6
    x4=np.arange(4,12,0.5)
    y4=(-1/8)*(x4-8)**2+6
    x5=np.arange(-4,-0.2,0.1)
    y5=2*(x5+3)**2-9
    x6=np.arange(-4,0.3,0.1)
    y6=1.5*(x6+3)**2-10
    plt.figure()
    plt.plot(x1,y1,"bo-",x2,y2,"bo-",x3,y3,"co-",x4,y4,"co-",x5,y5,"go-",x6,y6,"ro-")
    plt.title("Vihmavari")
    plt.ylabel("Y")
    plt.xlabel("X")
    plt.grid(True)
    plt.show()





def prillid():
    x1 = np.arange(-9, -0.5, 0.5)
    y1 = -(1/16) * (x1 + 5)**2 + 2
    x2 = np.arange(1, 9.5, 0.5)
    y2 = -(1/16) * (x2 - 5)**2 + 2
    x3 = np.arange(-9, -0.5, 0.5)
    y3 = (1/4) * (x3 + 5)**2 - 3
    x4 = np.arange(1, 9.5, 0.5)
    y4 = (1/4) * (x4 - 5)**2 - 3
    x5 = np.arange(-9, -6, 0.5)
    y5 = -(x5 + 7)**2 + 5
    x6 = np.arange(6, 9.5, 0.5)
    y6 = -(x6 - 7)**2 + 5
    x7 = np.arange(-1, 1, 0.01)
    y7 = -0.5 * (x7**2) + 1.5
    plt.figure()
    plt.plot(x1,y1,x2,y2,x3,y3,x4,y4,x5,y5,x6,y6,x7,y7)
    plt.title('Prillid')
    plt.xlabel('y')
    plt.ylabel('x')
    plt.grid(True)
    plt.show() 

import matplotlib.pyplot as plt
import numpy as np

import matplotlib.pyplot as plt
import numpy as np

def Liblikas():
    x1=np.arange(-9,-0.5,0.5)
    y1=(-1/8)*(x1+9)**2+8
    x2=np.arange(1,9,0.5)
    y2=(-1/8)*(x2-9)**2+8
    x3=np.arange(-9,-7.5,0.5)
    y3=7*(x3+8)**2+1
    x4=np.arange(8,9.5,0.5)
    y4=7*(x4-8)**2+1
    x5=np.arange(-8,-1,0.5)
    y5=(1/49)*(x5+1)**2
    x6=np.arange(1,8,0.5)
    y6=(1/49)*(x6-1)**2
    x7=np.arange(-8,-0.5,0.5)
    y7=(-4/49)*(x7+1)**2
    x8=np.arange(1,8.5,0.5)
    y8=(-4/49)*(x8-1)**2
    x9=np.arange(-8,-1.5,0.5)
    y9=(1/3)*(x9+5)**2-7
    x10=np.arange(2,8.5,0.5)
    y10=(1/3)*(x10-5)**2-7
    x11=np.arange(-2,-0.5,0.5)
    y11=-2*(x11+1)**2-2
    x12=np.arange(1,2.5,0.5)
    y12=-2*(x12-1)**2-2
    x13=np.arange(-1,1.5,0.5)
    y13=-4*x13**2+2
    x14=np.arange(-1,1.5,0.5)
    y14=4*x14**2-6
    x15=np.arange(-2,0.5,0.5)
    y15=-1.5*x15+2
    x16=np.arange(0,2.5,0.5)
    y16=1.5*x16+2
    plt.figure()
    plt.plot(x1,y1,"m-o",x2,y2,"m-o",x3,y3,"m-o",x4,y4,"m-o",x5,y5,"m-o",x6,y6,"m-o",x7,y7,"m-o",x8,y8,"m-o",x9,y9,"m-o",x10,y10,"m-o",x11,y11,"m-o",x12,y12,"m-o",x13,y13,"m-",x14,y14,"m-",x15,y15,"m-",x16,y16,"m-")
    plt.title("Liblikas")
    plt.ylabel("Y")
    plt.xlabel("X")
    plt.grid(True)
    plt.show()




root = Tk()
root.geometry("500x400")
root.title("Figure Drawer")
root.configure(bg="#b3e0ff")

frame = Frame(root, bg="#b3e0ff")
frame.pack(pady=10)

label = Label(frame, text="Выберите фигуру:", bg="#b3e0ff")
label.grid(row=0, column=0, pady=10)

kala_button = Button(frame, text="Keith", command=lambda: draw_figure(Keith), bg="#99ccff")
kala_button.grid(row=1, column=0, pady=5, padx=10, sticky="ew")

konnakull_button = Button(frame, text="konnakull", command=lambda: draw_figure(Kilpkonn), bg="#99ff99")
konnakull_button.grid(row=2, column=0, pady=5, padx=10, sticky="ew")

vihmavari_button = Button(frame, text="vihmavari", command=lambda: draw_figure(Vihmavari), bg="#ff99ff")
vihmavari_button.grid(row=3, column=0, pady=5, padx=10, sticky="ew")

prillid_button = Button(frame, text="prillid", command=lambda: draw_figure(prillid), bg="#ffff99")
prillid_button.grid(row=4, column=0, pady=5, padx=10, sticky="ew")

liblikas_button = Button(frame, text="Liblikas", command=lambda: draw_figure(Liblikas), bg="#ff99cc")
liblikas_button.grid(row=5, column=0, pady=5, padx=10, sticky="ew")
 


def draw_figure(figure_function):
    def open_figure():
        confirm = mb.askyesno("Kinnitus", "Kas soovite joonist avada?")
        if confirm:
            figure_function()
    open_figure()

root.mainloop()
