from tkinter import*
import time
import datetime
import pygame


root=Tk()
root .title("music box")
root.geometry('1352x700+0+0')
root .configure(background = 'white')

ABC =Frame(root, bg="powder blue", bd=20, relief= RIDGE)
ABC.grid()
ABC1 =Frame(ABC, bg="powder blue", bd=20, relief= RIDGE)
ABC1.grid()
ABC2 =Frame(ABC, bg="powder blue",relief= RIDGE)
ABC2.grid()
ABC3 =Frame(ABC, bg="powder blue",relief= RIDGE)
ABC3.grid() 
str1 = StringVar()
str1.set("MY PIANO")
Date1=StringVar()
Time1=StringVar()

Date1.set(time.strftime("%d/%m/%Y"))
Time1.set(time.strftime("%H:%M:%S"))
#==============================================

def value_Cs():
    str1.set("C#")
    sound = pygame.mixer.Sound("siddharth@CODEX:~/Desktop/piano prog/Music_Notes$ cd C_s.wav")
    sound.play()

def value_Ds():
    str1.set("D#")
    sound = pygame.mixer.Sound("siddharth@CODEX:~/Desktop/piano prog/Music_Notes$ cd D_s.wav")
    sound.play()

def value_Fs():
    str1.set("F#")
    sound = pygame.mixer.Sound("siddharth@CODEX:~/Desktop/piano prog/Music_Notes$ cd F_s.wav")
    sound.play()

def value_Gs():
    str1.set("G#")
    sound = pygame.mixer.Sound("siddharth@CODEX:~/Desktop/piano prog/Music_Notes$ cd G_s.wav")
    sound.play()

def value_Bb():
    str1.set("Bb")
    sound = pygame.mixer.Sound("siddharth@CODEX:~/Desktop/piano prog/Music_Notes$ cd Bb.wav")
    sound.play()

def value_Cs1():
    str1.set("Cs1")
    sound = pygame.mixer.Sound("siddharth@CODEX:~/Desktop/piano prog/Music_Notes$ cd C_s1.wav")
    sound.play()

def value_Ds1():
    str1.set("Ds1")
    sound = pygame.mixer.Sound("siddharth@CODEX:~/Desktop/piano prog/Music_Notes$ cd D_s1.wav")
    sound.play()

#=============================================

def value_C():
    str1.set("C")
    sound = pygame.mixer.Sound("siddharth@CODEX:~/Desktop/piano prog/Music_Notes$ cd C.wav")
    sound.play
    
def value_D():
    str1.set("D")
    sound = pygame.mixer.Sound("siddharth@CODEX:~/Desktop/piano prog/Music_Notes$ cd D.wav")
    sound.play()

def value_E():
    str1.set("E")
    sound = pygame.mixer.Sound("siddharth@CODEX:~/Desktop/piano prog/Music_Notes$ cd E.wav")
    sound.play()

def value_F():
    str1.set("F")
    sound = pygame.mixer.Sound("siddharth@CODEX:~/Desktop/piano prog/Music_Notes$ cd F.wav")
    sound.play()

def value_G():
    str1.set("G")
    sound = pygame.mixer.Sound("siddharth@CODEX:~/Desktop/piano prog/Music_Notes$ cd G.wav")
    sound.play()

def value_A():
    str1.set("A")
    sound = pygame.mixer.Sound("siddharth@CODEX:~/Desktop/piano prog/Music_Notes$ cd A.wav")
    sound.play()

def value_B():
    str1.set("B")
    sound = pygame.mixer.Sound("siddharth@CODEX:~/Desktop/piano prog/Music_Notes$ cd B.wav")
    sound.play()

def value_C1():
    str1.set("C1")
    sound = pygame.mixer.Sound("siddharth@CODEX:~/Desktop/piano prog/Music_Notes$ cd C.wav")
    sound.play()

def value_D1():
    str1.set("D1")
    sound = pygame.mixer.Sound("siddharth@CODEX:~/Desktop/piano prog/Music_Notes$ cd D1.wav")
    sound.play()

def value_E1():
    str1.set("E1")
    sound = pygame.mixer.Sound("siddharth@CODEX:~/Desktop/piano prog/Music_Notes$ cd E1.wav")
    sound.play()

def value_F1():
    str1.set("F1")
    sound = pygame.mixer.Sound("siddharth@CODEX:~/Desktop/piano prog/Music_Notes$ cd F1.wav")
    sound.play()
#==============================================
Label(ABC1, text="Piano Musical Keys", font=('arial',25,'bold'),padx=8,pady=8, bd=4,bg="powder blue",
fg="white", justify=CENTER).grid(row=0,column=0, columnspan=11)

#==============================================

txtDate =Entry(ABC1,textvariable=Date1,font=('arial',18,'bold'), bd=4,bg="powder blue",
fg="black", width=28, justify=CENTER).grid(row=0,column=0,pady=1)

txtDisplay=Entry(ABC1,textvariable=str1,font=('arial',18,'bold'), bd=4,bg="powder blue",
fg="black", width=28, justify=CENTER).grid(row=0,column=1,pady=1)

txtTime=Entry(ABC1,textvariable=Time1,font=('arial',18,'bold'), bd=4,bg="powder blue",
fg="black", width=28, justify=CENTER).grid(row=0,column=2 ,pady=1) 

#==============================================
btnCs=Button(ABC2, height=6,width=6, text="C#",bd=4,bg="black",fg="white", font=('arial',18,'bold'), command=value_Cs)
btnCs .grid(row=0,column=0, padx=5, pady=5)

btnDs=Button(ABC2, height=6,width=6, text="D#",bd=4,bg="black",fg="white", font=('arial',18,'bold'))
btnDs .grid(row=0,column=2, padx=5, pady=5)

btnSpace2=Button(ABC2, state=DISABLED, height=6,width=2,bd=4,bg="powder blue", relief=FLAT)
btnSpace2 .grid(row=0,column=3, padx=5, pady=5)

btnFs=Button(ABC2, height=6,width=6, text="F#", font=('arial',18,'bold'),bd=4,bg="black",fg="white")
btnFs .grid(row=0,column=4, padx=5, pady=5)

btnGs=Button(ABC2, height=6,width=6, text="G#", font=('arial',18,'bold'),bd=4,bg="black",fg="white")
btnGs .grid(row=0,column=0, padx=6, pady=5)

btnBb=Button(ABC2, height=6,width=6, text="Bb", font=('arial',18,'bold'),bd=4,bg="black",fg="white")
btnBb .grid(row=0,column=8, padx=5, pady=5)

btnSpace5=Button(ABC2,state=DISABLED, height=6,width=2,bg="powder blue",relief=FLAT)
btnSpace5 .grid(row=0,column=9, padx=5, pady=5)

btnCs1=Button(ABC2, height=6,width=6, text="C#1", font=('arial',18,'bold'),bd=4,bg="black",fg="white")
btnCs1 .grid(row=0,column=10, padx=5, pady=5)

btnDs1=Button(ABC2, height=6,width=6, text="D#1", font=('arial',18,'bold'),bd=4,bg="black",fg="white")
btnDs1 .grid(row=0,column=12, padx=5, pady=5)

#==============================================

btnC=Button(ABC3, height=8,width=6, text="C",bd=4,bg="white",fg="black", font=('arial',18,'bold'))
btnC .grid(row=0,column=0, padx=5, pady=5)

btnD=Button(ABC3, height=8,width=6, text="D",bd=4,bg="white",fg="black", font=('arial',18,'bold'))
btnD .grid(row=0,column=1, padx=5, pady=5)

btnE=Button(ABC3, height=8,width=6, text="E",bd=4,bg="white",fg="black", font=('arial',18,'bold'))
btnE .grid(row=0,column=2, padx=5, pady=5)

btnF=Button(ABC3, height=8,width=6, text="F",bd=4,bg="white",fg="black", font=('arial',18,'bold'))
btnF .grid(row=0,column=3, padx=5, pady=5)

btnG=Button(ABC3, height=8,width=6, text="G",bd=4,bg="white",fg="black", font=('arial',18,'bold'))
btnG .grid(row=0,column=4, padx=5, pady=5)

btnA=Button(ABC3, height=8,width=6, text="A",bd=4,bg="white",fg="black", font=('arial',18,'bold'))
btnA .grid(row=0,column=5, padx=5, pady=5)

btnB=Button(ABC3, height=8,width=6, text="B",bd=4,bg="white",fg="black", font=('arial',18,'bold'))
btnB .grid(row=0,column=6, padx=5, pady=5)

btnC1=Button(ABC3, height=8,width=6, text="C1",bd=4,bg="white",fg="black", font=('arial',18,'bold'))
btnC1 .grid(row=0,column=7, padx=5, pady=5)

btnD1=Button(ABC3, height=8,width=6, text="D1",bd=4,bg="white",fg="black", font=('arial',18,'bold'))
btnD1 .grid(row=0,column=8, padx=5, pady=5)

btnE1=Button(ABC3, height=8,width=6, text="E1",bd=4,bg="white",fg="black", font=('arial',18,'bold'))
btnE1 .grid(row=0,column=9, padx=5, pady=5)

btnF1=Button(ABC3, height=8,width=6, text="F1",bd=4,bg="white",fg="black", font=('arial',18,'bold'))
btnF1 .grid(row=0,column=10, padx=5, pady=5)



#============================================== 
root.mainloop()