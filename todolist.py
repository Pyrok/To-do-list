#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
from Tkinter import *
from tkMessageBox import *
import json

framesList = []
todoList = []
inProgressList = []
doneList = []
tasksList = []

def newList():
    global tasksList
    for i in range(2,5):
        for widget in framesList[i].winfo_children():
            widget.destroy()
    tasksList = []
    tasksList.append(todoList)
    tasksList.append(inProgressList)
    tasksList.append(doneList)
    
def save():
    savedList = json.dumps(tasksList)
    file = open("savedTasks.txt","w")
    file.write(savedList)
    file.close()

def load():
    global tasksList
    file = open("savedTasks.txt","r")
    savedList = json.loads(file.read())
    tasksList = savedList
    for item in tasksList[0]:
        addTask(item, 2)
    for item in tasksList[1]:
        addTask(item, 3)
    for item in tasksList[2]:
        addTask(item, 4)
    file.close()
	
def createFrames(master):
    menubar = Menu(master)
    #Menu 1
    menu1 = Menu(menubar, tearoff=0)
    menu1.add_command(label="New list", command=newList)
    menu1.add_command(label="New task", command=lambda: newTaskFrameUpdate(master))
    menu1.add_command(label="Load", command=load)
    menu1.add_command(label="Save", command=save)
    menu1.add_separator()
    menu1.add_command(label="Quit", command=master.quit)
    menubar.add_cascade(label="File", menu=menu1)
    #Menu 3
    menu2 = Menu(menubar, tearoff=0)
    menu2.add_command(label="About", command=lambda:showwarning("About", "Developed by Ulysse PETIT (Pyrok)"))
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
    todoFrame.grid(row=1, column=0, padx=10, pady=10, sticky = W+E)
    framesList.append(todoFrame)
	
    inProgressFrame = Frame(bottomFrame, borderwidth=2)
    inProgressFrame.grid(row=1, column=1, padx=10, pady=10, sticky = W+E)
    framesList.append(inProgressFrame)

    doneFrame = Frame(bottomFrame, borderwidth=2)
    doneFrame.grid(row=1, column=2, padx=10, pady=10, sticky = W+E)
    framesList.append(doneFrame)
	
    # Adding labels
    label1 = Label(bottomFrame, text="To Do", width=25)
    label1.grid(row=0, column=0, padx=10, pady=5)
    label2 = Label(bottomFrame, text="In Progress", width=25)
    label2.grid(row=0, column=1, padx=10, pady=5)
    label3 = Label(bottomFrame, text="Done", width=25)
    label3.grid(row=0, column=2, padx=10, pady=5)

def newTaskFrameUpdate(master):
    #Re-display the top frame it is not
    framesList[0].pack(fill=BOTH, side=TOP, padx=5, pady=5)
    #Updating the frame with components
    labelName = Label(framesList[0], text="Name of the task")
    labelName.pack(side=TOP, padx=5, pady=5)
    entryField = Entry(framesList[0])
    entryField.pack(fill=X, expand=True, padx=5, pady=5)
    buttonAdd = Button(framesList[0], text="Add", command=lambda: addTaskManually(master, labelName, entryField, buttonAdd))
    buttonAdd.pack(fill=X, padx=5, pady=5)	

def addTaskManually(master, label, entry, button):
    global tasksList
    taskName = entry.get()
    tasksList[0].append(taskName)
    addTask(taskName, 2)
    label.pack_forget()
    entry.pack_forget()
    button.pack_forget()
    framesList[0].pack_forget()

def addTask(buttonName, frameId):
    newTask = Button(framesList[frameId], text=buttonName, command=lambda: move(newTask))
    if frameId == 2:
        newTask["bg"]="#FA5858"
    if frameId == 3:
        newTask["bg"]="orange"
    if frameId == 4:
        newTask["bg"]="#04B404"
    newTask["overrelief"]="ridge"
    newTask["wraplength"]=150
    newTask.pack(fill=X, padx=5, pady=5)

def move(taskButton):
    global tasksList
    taskName = taskButton['text']
    if taskName in tasksList[0]:
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
        taskButton.destroy()
        tasksList[2].remove(taskName)
        return

def main():
    #Initialising the lists
    tasksList.append(todoList)
    tasksList.append(inProgressList)
    tasksList.append(doneList)
	#Create the window
    master = Tk()
    master["bg"]="white"
    master.title("To do list - by Ulysse PETIT")
    master.resizable(width=FALSE, height=FALSE)
    createFrames(master)
    master.mainloop()

if __name__=="__main__":
    main()