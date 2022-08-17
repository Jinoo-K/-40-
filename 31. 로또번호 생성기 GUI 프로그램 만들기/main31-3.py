import random
import tkinter
import tkinter.font

lotto_num = range (1,46)

def buttonClick():
    for i in range(5):
        lottoPick = map(str, random.sample(lotto_num, 6))
        lottoPick = " , ".join(lottoPick)
        lottoPick = str(i+1) + "회" + lottoPick
        print(lottoPick)
        listbox.insert(i, lottoPick)
    listbox.pack()

window = tkinter.Tk()
window.title("lotto")
window.geometry("500x300+800+300")
window.resizable(False, False)

button = tkinter.Button(window, overrelief="solid", text="번호 확인", width=15, command=buttonClick, repeatdelay=1000, repeatinterval=100)
button.pack()

font = tkinter.font.Font(size = 15)
listbox = tkinter.Listbox(window, selectmode="extended", height=5, font=font)
listbox.insert(0, "1회:")
listbox.insert(1, "2회:")
listbox.insert(2, "3회:")
listbox.insert(3, "4회:")
listbox.insert(4, "5회:")
listbox.pack()

window.mainloop()