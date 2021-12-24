from tkinter import *
import time
import random
import playsound as ps
import threading

# =====WINDOW CREATION=====
window = Tk()
window.title('Duelist\'s Practice')
window.configure(bg='#9e0001')
window.geometry("1000x800")

# =====GLOBAL VARIABLES=====
start = 0
stop = 0
magCount = 1


# =====BUTTON INITIALIZERS=====
def init():
    global stop
    global magCount
    t1 = threading.Thread(target=clickSound)
    t2 = threading.Thread(target=gunshotSound)
    stop = time.time() * 1000
    if magCount > 0:
        displayResult(stop - start)
        t2.start()
        magCount = magCount - 1
        time.sleep(1)
        duelEnd()
    else:
        t1.start()
        targetButton.config(state=DISABLED)
        duelEnd()


def init2(e):
    global magCount
    if magCount > 0:
        targetButton.config(state=NORMAL)
        t1 = threading.Thread(target=timerStart)
        t2 = threading.Thread(target=tensionSound)
        t1.start()
        t2.start()
    else:
        print("Empty magazine.  Please reset.")


def reset():
    global magCount
    magCount = 1
    timerLabel.config(text="Hover over the cylinder when ready.")
    drawLabel.config(text='')
    killShotLabel.config(text='')
    targetButton.config(state=DISABLED)
    print("Game reset")


# =====SOUNDS=====
def gunshotSound():
    ps.playsound('sounds/gunshot.mp3')


def tensionSound():
    ps.playsound('sounds/tension.wav')


def clickSound():
    ps.playsound('sounds/click.wav')


def riffSound():
    ps.playsound('sounds/Duel Complete.mp3')


# =====CHECKERS=====
def earlyChecker():
    drawButton.bind("<Leave>", tooEarly)
    time.sleep(random.randint(5, 9))


def fairPlay(e):
    print("Fair play")


def tooEarly(e):
    timerLabel.config(text="You drew too early, please wait for the tension to finish playing.")
    targetButton.config(state=DISABLED)


def timerStart():
    global start
    timerLabel.config(text="Steady...")
    earlyChecker()
    drawButton.bind("<Leave>", fairPlay)
    timerLabel.config(text="Draw!")
    start = time.time() * 1000


# =====OUTPUTS=====
def displayResult(result):
    drawLabel.config(text=str(int(result - 170)) + "ms")


def duelEnd():
    t1 = threading.Thread(target=riffSound)
    t1.start()


# =====IMAGES=====
silhouette = PhotoImage(file='images/silhouette.png')
cylinder = PhotoImage(file='images/cylinder1.png')

# =====BUTTONS=====
targetButton = Button(window, image=silhouette, command=init, borderwidth=0, bg='#9e0001', state=DISABLED,
                      activebackground='#9e0001')
targetButton.pack(pady=20)

drawButton = Button(window, image=cylinder, borderwidth=0, bg='#9e0001',
                    activebackground='#9e0001')
drawButton.pack(pady=90)

resetButton = Button(window, text='Reset', command=reset, bg='#791A1B', font='Stencil 20 bold',
                     activebackground='#791A1B', borderwidth=0)
resetButton.place(relx=0.1, rely=0.1, anchor='se')

# =====LABELS=====
label = Label(window, text='', bg='#9e0001')
label.pack(pady=20, padx=50)

timerLabel = Label(window, text="Hover over the cylinder when ready.", bg='#9e0001', font='Stencil 14 bold')
timerLabel.pack(padx=100)

drawLabel = Label(window, text='', bg='#9e0001', font='Stencil 16 bold')
drawLabel.place(x=650, y=350)

killShotLabel = Label(window, text='', bg='#9e0001', font='Stencil 30 bold')
killShotLabel.place(x=1050, y=500)

# =====ACTIONS=====
drawButton.bind("<Enter>", init2)

mainloop()
