import random
import string
import datetime

from tkinter import *
import tkinter


def password_gen(length=12):
    """
    Will generate the desired password and will save the
    output to a file if the path is provided.

    :param length: desired length of the password

    :rtype: string
    """
    path = ''
    application = ''

    if E1.get() != '':
        length = int(Entry.get(E1))


    if E2.get() != '':
        path = E2.get()

    if E3.get() != '':
        application = E3.get()

    # added all the chars in a list form
    chars = list(string.ascii_letters)+list(string.digits)+list(string.punctuation)
    # shuffling the list
    random.shuffle(chars)
    # a list to store strings
    templist = []



    for item in range(length):
        char = random.choice(chars)
        templist.append(char)
        #removing the used char so no repetition in the pass
        chars.remove(char)


    password = "".join(templist)

    # writing the password the file with the date stamp
    if path != '':
        file = open(path, 'a')
        file.write('\n'+ 8*'-' + str(datetime.datetime.now()) + 8*'-' + '\n')
        file.write(application +':- ' + password + '\n')
        file.close()

    Entry.delete(E4, 0, 'end')
    Entry.insert(E4, 0, password)
    return password



top = tkinter.Tk()
L1 = Label(top, text="Password Generator",).grid(row=0,column=1)
L2 = Label(top, text="Length",).grid(row=1,column=0)
L3 = Label(top, text="Path of the File",).grid(row=2,column=0)
L4 = Label(top, text="App/Website",).grid(row=3,column=0)
L5 = Label(top, text="Result",).grid(row=4,column=0)
E1 = Entry(top, bd =5)
E1.grid(row=1,column=1)
E2 = Entry(top, bd =5)
E2.grid(row=2,column=1)
E3 = Entry(top, bd =5)
E3.grid(row=3,column=1)
E4 = Entry(top, bd = 5)
E4.grid(row=4,column=1)
B=Button(top, text ="Generate", command= password_gen).grid(row=6,column=1,)

top.mainloop()





