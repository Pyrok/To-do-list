#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
from Tkinter import *
from tkMessageBox import *

framesList = []
todoList = []
inProgressList = []
doneList = []
tasksList = []

def move(taskButton):
    taskName = taskButton['text']
    taskButton.pack_forget()
    if taskName in tasksList[0]:
        #print("Item in the first list")
        taskButton.pack_forget()
        tasksList[0].remove(taskName)
        tasksList[1].append(taskName)
        newButton = Button(framesList[3], text=taskName, command=lambda: move(newButton))
        newButton["bg"]="orange"
        newButton["overrelief"]="ridge"
        newButton["wraplength"]=150
        newButton.pack(fill=BOTH, padx=5, pady=5)
        return
    if taskName in tasksList[1]:
        #print("Item in the second list")
        taskButton.pack_forget()
        tasksList[1].remove(taskName)
        tasksList[2].append(taskName)
        newButton = Button(framesList[4], text=taskName, command=lambda: move(newButton))
        newButton["bg"]="#04B404"
        newButton["overrelief"]="ridge"
        newButton["wraplength"]=150
        newButton.pack(fill=BOTH, padx=5, pady=5)
        return
    if taskName in tasksList[2]:
        #print("Item in the third list")
        tasksList[2].remove(taskName)
        taskButton.pack_forget()
        return

def createFrames(master):
    menubar = Menu(master)
    #Menu 1
    menu1 = Menu(menubar, tearoff=0)
    menu1.add_command(label="New list")
    menu1.add_command(label="New task", command=lambda: newTaskFrameUpdate(master))
    menu1.add_command(label="Load")
    menu1.add_separator()
    menu1.add_command(label="Quit", command=master.quit)
    menubar.add_cascade(label="File", menu=menu1)
    #Menu 3
    menu2 = Menu(menubar, tearoff=0)
    menu2.add_command(label="About", command=lambda:showwarning("About", "Developed by Ulysse PETIT"))
    menubar.add_cascade(label="Help", menu=menu2)

    master.config(menu=menubar)

    #Top Frame for inputs
    topFrame = Frame(master, borderwidth=2, relief=GROOVE)
    topFrame.pack(fill=BOTH, side=TOP, padx=5, pady=5)
    framesList.append(topFrame)
	
	#Bottom Frame as a container
    bottomFrame = Frame(master, borderwidth=2, relief=GROOVE)
    bottomFrame.pack(fill=BOTH, side=BOTTOM, padx=5, pady=5)
    framesList.append(bottomFrame)
	
	#Status Frames
    todoFrame = Frame(bottomFrame, borderwidth=2)
    todoFrame.grid(row=1, column=0, padx=10, pady=10)
    framesList.append(todoFrame)
	
    inProgressFrame = Frame(bottomFrame, borderwidth=2)
    inProgressFrame.grid(row=1, column=1, padx=10, pady=10)
    framesList.append(inProgressFrame)

    doneFrame = Frame(bottomFrame, borderwidth=2)
    doneFrame.grid(row=1, column=2, padx=10, pady=10)
    framesList.append(doneFrame)
	
    # Adding labels
    label1 = Label(bottomFrame, text="To Do")
    label1.grid(row=0, column=0, padx=10, pady=5)
    label2 = Label(bottomFrame, text="In Progress")
    label2.grid(row=0, column=1, padx=10, pady=5)
    label3 = Label(bottomFrame, text="Done")
    label3.grid(row=0, column=2, padx=10, pady=5)

def newTaskFrameUpdate(master):
    #Re-display the top frame it is not
    framesList[0].pack(fill=BOTH, side=TOP, padx=5, pady=5)
    #Updating the frame with components
    labelName = Label(framesList[0], text="Name of the task")
    labelName.pack(side=TOP, padx=5, pady=5)
    entryField = Entry(framesList[0])
    entryField.pack(fill=X, expand=True, padx=5, pady=5)
    buttonAdd = Button(framesList[0], text="Add", command=lambda: addTask(master, labelName, entryField, buttonAdd))
    buttonAdd.pack(fill=X, padx=5, pady=5)	

def addTask(master, label, entry, button):
    taskName = entry.get()
    tasksList[0].append(taskName)
    newButton = Button(framesList[2], text=taskName, command=lambda: move(newButton))
    newButton["bg"]="#FA5858"
    newButton["overrelief"]="ridge"
    newButton["wraplength"]=150
    newButton.pack(fill=BOTH, padx=5, pady=5)
    label.pack_forget()
    entry.pack_forget()
    button.pack_forget()
    framesList[0].pack_forget()

def main():
    #Initialising the lists
    tasksList.append(todoList)
    tasksList.append(inProgressList)
    tasksList.append(doneList)
	#Create the window
    master = Tk()
    master["bg"]="white"
    master.title("To do list - by Ulysse PETIT")
    createFrames(master)
    master.mainloop()

if __name__=="__main__":
    main()