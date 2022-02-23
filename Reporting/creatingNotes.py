def saved():    
    global savedScreen
    savedScreen = Toplevel(screen)
    setScreen(savedScreen, "Saved Screen", "300x250")
    Label(savedScreen, text="Saved").pack()
    
def save():
    filename = raw_filename.get()
    notes = raw_notes.get()

    data = open(filename, "w")
    data.write(notes)
    data.close()
    Label(createNoteScreen, text="Saved").pack()
    #saved()

def createNotes():
    sessionScreen.destroy()
    global createNoteScreen
    createNoteScreen = Toplevel(screen)
    setScreen(createNoteScreen, "Create Notes", "300x250")

    global raw_filename
    global raw_notes
    raw_filename = StringVar()
    raw_notes = StringVar()
    Label(createNoteScreen, text="Please enter file name: ").pack()
    Entry(createNoteScreen, textvariable=raw_filename).pack()
    Label(createNoteScreen, text="Please enter your notes: ").pack()
    Entry(createNoteScreen, textvariable=raw_notes).pack()
    Button(createNoteScreen, text="Save", command=save).pack()

def locateNotes():
    global locateNotesScreen
    locateNotesScreen = Toplevel(screen)
    setScreen(locateNotesScreen, "Locate Notes", "300x250")
    fileSearch = searchRaw_file.get()
    data = open(fileSearch,"r")
    data2 = data.read()
    Label(locateNotesScreen, text=data2).pack()

def viewNotes():
    sessionScreen.destroy()
    global viewNotesScreen
    viewNotesScreen = Toplevel(screen)
    setScreen(viewNotesScreen, "View Notes", "300x250")

    all_files = os.listdir()
    Label(viewNotesScreen, text="Files").pack()
    Label(viewNotesScreen, text=all_files).pack()
    global searchRaw_file
    searchRaw_file = StringVar()
    Entry(viewNotesScreen, textvariable=searchRaw_file).pack()
    Button(viewNotesScreen, text="Search",command=locateNotes).pack()

def deleteNote():
    noteToDelete = deleteFile.get()
    os.remove(noteToDelete)
    Label(deleteNotesScreen, text=noteToDelete + " was deleted.").pack()

def delete_notes():
    global deleteNotesScreen
    deleteNotesScreen = Toplevel(screen)
    setScreen(deleteNotesScreen, "Delete Notes", "300x250")

    all_files = os.listdir()
    Label(deleteNotesScreen, text="Files").pack()
    Label(deleteNotesScreen, text=all_files).pack()
    global deleteFile
    deleteFile = StringVar()
    Entry(deleteNotesScreen, textvariable=deleteFile).pack()
    Button(deleteNotesScreen, command=deleteNote, text="Delete").pack()

def session():
    global sessionScreen
    sessionScreen = Toplevel(screen)
    setScreen(sessionScreen, "Session", "300x250")
    Label(sessionScreen, text="Welcome to Dashboard").pack()
    Button(sessionScreen, text="Create Note", command=createNotes).pack()
    Button(sessionScreen, text="View Note", command=viewNotes).pack()
    Button(sessionScreen, text="Delete Notes", command=delete_notes).pack()
