from tkinter import *


class GUI(object):
    def __init__(self):
        fenster = Tk()
        self.tk = fenster

        fenster.title("Textadventure")
        fenster.geometry("1000x400")

        w = Label(fenster, text="Textausgabe:")
        w.pack()

        s = Scrollbar(fenster)
        t = Text(fenster, height=15, width=91)

        s.pack(side=RIGHT)
        t.pack()

        s.config(command=t.yview)
        t.config(yscrollcommand=s.set)
        quote = "-------------------------------------------------------------------------------------------\n"
        t.insert(END, quote)
        t.config(state=DISABLED)

        w2 = Label(fenster, text="Texteingabe:")
        w2.pack()

        e = Text(fenster, height=2, width=90)
        e.pack()

        b = Button(fenster, text="Enter", command=self.submit)
        b.pack()

        self.textout = t
        self.textentry = e
        self.button = b

    def start(self):
        self.tk.mainloop()

    def write(self, msg):
        try:
            t = self.textout

            t.config(state=NORMAL)
            t.insert(END, msg)
            t.see("end")

            t.config(state=DISABLED)

        except:
            pass

    def submit(self):
        self.gamemanager.inputtrigger()
        self.textentry.delete('1.0', 'end')

    def setGameManager(self, pgamemanager):
        self.gamemanager = pgamemanager

