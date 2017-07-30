from tkinter import *

root = Tk()

w1 = Label(root, text="Micro:")
w1.grid(row=0, column=0)

e1 = Entry(root, width=12)
e1.insert(0, "84000000")
e1.grid(row=0, column=1, columnspan=3, sticky=W)

w2 = Label(root, text="Speed(Hz):")
w2.grid(row=0, column=4)

e2 = Entry(root, width=12)
e2.insert(0, "20000")
e2.grid(row=0, column=5, columnspan=3, sticky=W)

w3 = Label(root, text="Spread:")
w3.grid(row=0, column=8)

e3 = Entry(root, width=15)
e3.insert(0, "10")
e3.grid(row=0, column=9, sticky=W)

w4 = Label(root, text="Preescaler:")
w4.grid(row=1, column=0)

e4 = Entry(root, width=5)
e4.insert(0, "0")
e4.grid(row=1, column=1, sticky=W)

w5 = Label(root, text="-")
w5.grid(row=1, column=2)

e5 = Entry(root, width=5)
e5.insert(0, "200")
e5.grid(row=1, column=3, sticky=E)

w6 = Label(root, text="Period:")
w6.grid(row=1, column=4)

e6 = Entry(root, width=5)
e6.insert(0, "1")
e6.grid(row=1, column=5, sticky=W)

w7 = Label(root, text="-")
w7.grid(row=1, column=6)

e7 = Entry(root, width=5)
e7.insert(0, "65535")
e7.grid(row=1, column=7, sticky=E)

t = Text(root, height=20, width=50)
t.grid(row=2, column=0, columnspan=10, sticky=W+E+N+S)
t.tag_configure('big', font=('Times', 15))

def calculate():

#    def calc2(m, ps, p):
#        last = 0
#        return def next2():
#            nonlocal m, ps, p
#            nonlocal last
#            
#            new = round(m / ((ps + 1) * (p)) + 1)
#            while new == last:
#                new = round(m / ((ps + 1) * (p)) + 1)
#            return round(m / ((ps + 1) * (p)) + 1)
    
    def calc(m, ps, p):
        return round(m / ((ps + 1) * (p)) + 1)
    print("---START---")

    t.delete("1.0", END)

    micro = int(e1.get())
    speed = int(e2.get())
    spread = int(e3.get())
    preescaler_start = int(e4.get())
    preescaler_Stop = int(e5.get())
    period_start = int(e6.get())
    period_Stop = int(e7.get())

    text = ""
    num_temp = 0

    for ps in range(preescaler_start, preescaler_Stop):
        for p in range(period_start, period_Stop):
            num = calc(micro, ps, p)
            # print("Speed:{}Hz, Prescaler:{}, Period:{}\n".format(num, ps, p))
        
            if calc(micro, ps, period_Stop) > (speed + spread) or (num < (speed - spread)) or num == 0:
                break
            if (ps + 1) * (p) <= 0 or num == num_temp:
                continue
            num_temp = num
            if (abs(num - speed) <= spread):
                text += "Speed:{}Hz, Prescaler:{}, Period:{}\n".format(num, ps, p)
                continue
        if num == 0:
            break
    if text == "":
        text = "No value found."
    t.insert(END, text, "big")
    print("---STOP---")

btn = Button(root, text="RUN", command=calculate)
btn.grid(row=1, column=8, columnspan=2)

root.mainloop()