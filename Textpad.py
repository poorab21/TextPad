from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
window=Tk()
window.title("Untitled - Notepad")
menubar = Menu(window)
window.config(menu=menubar)
updated = 0
def Updated(event):
    global updated
    updated=1
def New():
    global window,text,updated
    if window.title()=="Untitled - Notepad" and updated==1:
        response = messagebox.askyesnocancel("Save Data","Would you like to Save changes to "+window.title())
        if response==None:
            pass
        elif response==False:
            text.delete("0.1",END)
            updated=0
        elif response==True:
            filename = filedialog.asksaveasfilename(initialdir="C:/")
            if filename:
                file_text = open(filename,'w')
                file_text.write(text.get("0.1",END))
                file_text.close()
                text.delete("0.1",END)
                updated=0
    elif window.title() != "Untitled - Notepad" and updated==1:
        response = messagebox.askyesnocancel("Save Changes","Would you like to Save Changes to "+window.title())
        if response==None:
            pass
        elif response==False:
            text.delete("0.1",END)
            window.title("Untitled - Notepad")
            updated=0
        elif response==True:
            filename = str(window.title())
            filename = filename.replace(" - Notepad","")
            file_text = open(filename,'w')
            file_text.write(text.get("0.1",END))
            file_text.close()
            text.delete("0.1",END)
            window.title("Untitled - Notepad")
            updated=0
    elif window.title()=="Untitled - Notepad" and updated==0:
        text.delete("0.1",END)
    elif window.title() != "Untitled - Notepad" and updated==0:
        text.delete("0.1",END)
        window.title("Untitled - Notepad")
def Open():
    global window,updated,text
    if window.title()=="Untitled - Notepad" and updated==1:
        response = messagebox.askyesnocancel("Save Changes","Would you like to Save "+window.title())
        if response==True:
            filename = filedialog.asksaveasfilename(initialdir="C:/")
            if filename:
                file_text = open(filename,'w')
                file_text.write(text.get("0.1",END))
                file_text.close()
                updated=0
                window.title(filename+" - Notepad")
                file_text.close()
                file_retrieve = filedialog.askopenfilename(initialdir="C:/")
                if file_retrieve:
                    window.title(file_retrieve+" - Notepad")
                    file_retrieve_text = open(file_retrieve,'r')
                    text.delete("0.1",END)
                    text.insert("0.1",file_retrieve_text.read())
                    file_retrieve_text.close()
        elif response==False:
            filename = filedialog.askopenfilename(initialdir="C:/")
            if filename:
                window.title(filename+" - Notepad")
                file_text = open(filename,'r')
                text.delete("0.1",END)
                text.insert("0.1",file_text.read())
                file_text.close()
                updated=0
        elif response==None:
            pass
    elif window.title()=="Untitled - Notepad" and updated==0:
        filename = filedialog.askopenfilename(initialdir="C:/")
        if filename:
            window.title(filename+" - Notepad")
            file_text = open(filename,'r')
            text.delete("0.1",END)
            text.insert("0.1",file_text.read())
            file_text.close()
    elif window.title() != "Untitled - Notepad" and updated==0:
        filename = filedialog.askopenfilename(initialdir="C:/")
        if filename:
            text.delete("0.1",END)
            window.title(filename+" - Notepad")
            file_text = open(filename,'r')
            text.insert("0.1",file_text.read())
            file_text.close()
    elif window.title() != "Untitled - Notepad" and updated==1:
        response = messagebox.askyesnocancel("Save Changes","Would you like to save changes to "+window.title())
        if response==None:
            pass
        elif response==False:
            filename = filedialog.askopenfilename(initialdir="C:/")
            if filename:
                file_text = open(filename,'r')
                text.delete("0.1",END)
                text.insert("0.1",file_text.read())
                file_text.close()
                window.title(filename+" - Notepad")
                updated=0
        elif response==True:
            file_retrieve = filedialog.askopenfilename(initialdir="C:/")
            if file_retrieve:
                filename = str(window.title())
                filename = filename.replace(" - Notepad","")
                file_text = open(filename,'w')
                file_text.write(text.get("0.1",END))
                text.delete("0.1",END)
                file_text.close()
                updated=0
                window.title(file_retrieve+" - Notepad")
                file_retrieve_text = open(file_retrieve,'r')
                text.insert("0.1",file_retrieve_text.read())
                file_retrieve_text.close()
def Save():
    global window,updated,text
    if window.title()=="Untitled - Notepad" and updated==0:
        filename = filedialog.asksaveasfilename(initialdir="C:/")
        if filename:
            file_text = open(filename,'w')
            file_text.write(text.get("0.1",END))
            file_text.close()
    elif window.title()=="Untitled - Notepad" and updated==1:
        filename = filedialog.asksaveasfilename(initialdir="C:/")
        if filename:
            file_text = open(filename, 'w')
            file_text.write(text.get("0.1", END))
            file_text.close()
            updated=0
    elif window.title() != "Untitled - Notepad" and updated==1:
        filename = str(window.title())
        filename = filename.replace(" - Notepad","")
        file_text = open(filename,'w')
        file_text.write(text.get("0.1",END))
        updated=0
        file_text.close()
def Save_As():
    global updated,text
    filename = filedialog.asksaveasfilename(initialdir="C:/")
    if filename:
        file_text = open(filename,'w')
        file_text.write(text.get("0.1",END))
        window.title(filename+" - Notepad")
        updated=0
def Exit():
    global window,text
    if window.title()=="Untitled - Notepad" and updated==1:
        response= messagebox.askyesnocancel("Save File","Would you like to Save "+window.title())
        if response==True:
            filename = filedialog.asksaveasfilename(initialdir="C:/")
            if filename:
                file_text = open(filename,'w')
                file_text.write(text.get("0.1",END))
                file_text.close()
        elif response==False:
            window.quit()
        elif response==None:
            pass
    elif window.title() != "Untitled - Notepad" and updated==1:
        response = messagebox.askyesnocancel("Save Changes","Would you like to Save Changes to "+window.title())
        if response==True:
            filename = str(window.title())
            filename = filename.replace(" - Notepad","")
            file_text = open(filename,'w')
            file_text.write(text.get("0.1",END))
            file_text.close()
            window.quit()
        elif response==False:
            window.quit()
        elif response==None:
            pass
    elif window.title() != "Untitled - Notepad" and updated==0:
        window.quit()
    elif window.title()=="Untitled - Notepad" and updated==0:
        window.quit()
file_menu = Menu(menubar,tearoff=False)
menubar.add_cascade(label="file",menu=file_menu)
file_menu.add_command(label="New",command=New)
file_menu.add_command(label="Open",command=Open)
file_menu.add_command(label="Save",command=Save)
file_menu.add_command(label="Save As",command=Save_As)
file_menu.add_command(label="Exit",command=Exit)

frame = Frame(window,width=window.winfo_screenwidth(),height=window.winfo_screenheight())
frame.pack()
scroll = Scrollbar(frame,orient=VERTICAL)
scroll.pack(side=RIGHT,fill=Y)
scroll2 = Scrollbar(frame,orient=HORIZONTAL)
scroll2.pack(side=BOTTOM,fill=X)
text = Text(frame,width=window.winfo_screenwidth(),height=window.winfo_screenheight(),yscrollcommand=scroll.set,xscrollcommand=scroll2.set,wrap="none",font=("times",20))
text.pack()
scroll.config(command=text.yview)
scroll2.config(command=text.xview)
text.bind("<KeyPress>",Updated)
window.mainloop()
________________________________________________________________________________________________________________________________
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from tkinter import font
from tkinter import colorchooser
window=Tk()
v=IntVar()
window.title("Untitled - Notepad")
window.iconbitmap('Notepad.ico')
menubar = Menu(window)
window.config(menu=menubar)
font_text = font.Font(family="helvetica",size=20,slant="roman",weight="normal")
updated = 0
def Updated(event):
    global updated
    updated=1
def New():
    global window,text,updated
    if window.title()=="Untitled - Notepad" and updated==1:
        response = messagebox.askyesnocancel("Save Data","Would you like to Save changes to "+window.title())
        if response==None:
            pass
        elif response==False:
            text.delete("0.1",END)
            updated=0
        elif response==True:
            filename = filedialog.asksaveasfilename(initialdir="C:/")
            if filename:
                file_text = open(filename,'w')
                file_text.write(text.get("0.1",END))
                file_text.close()
                text.delete("0.1",END)
                updated=0
    elif window.title() != "Untitled - Notepad" and updated==1:
        response = messagebox.askyesnocancel("Save Changes","Would you like to Save Changes to "+window.title())
        if response==None:
            pass
        elif response==False:
            text.delete("0.1",END)
            window.title("Untitled - Notepad")
            updated=0
        elif response==True:
            filename = str(window.title())
            filename = filename.replace(" - Notepad","")
            file_text = open(filename,'w')
            file_text.write(text.get("0.1",END))
            file_text.close()
            text.delete("0.1",END)
            window.title("Untitled - Notepad")
            updated=0
    elif window.title()=="Untitled - Notepad" and updated==0:
        text.delete("0.1",END)
    elif window.title() != "Untitled - Notepad" and updated==0:
        text.delete("0.1",END)
        window.title("Untitled - Notepad")
def Open():
    global window,updated,text
    if window.title()=="Untitled - Notepad" and updated==1:
        response = messagebox.askyesnocancel("Save Changes","Would you like to Save "+window.title())
        if response==True:
            filename = filedialog.asksaveasfilename(initialdir="C:/")
            if filename:
                file_text = open(filename,'w')
                file_text.write(text.get("0.1",END))
                file_text.close()
                updated=0
                window.title(filename+" - Notepad")
                file_text.close()
                file_retrieve = filedialog.askopenfilename(initialdir="C:/")
                if file_retrieve:
                    window.title(file_retrieve+" - Notepad")
                    file_retrieve_text = open(file_retrieve,'r')
                    text.delete("0.1",END)
                    text.insert("0.1",file_retrieve_text.read())
                    file_retrieve_text.close()
        elif response==False:
            filename = filedialog.askopenfilename(initialdir="C:/")
            if filename:
                window.title(filename+" - Notepad")
                file_text = open(filename,'r')
                text.delete("0.1",END)
                text.insert("0.1",file_text.read())
                file_text.close()
                updated=0
        elif response==None:
            pass
    elif window.title()=="Untitled - Notepad" and updated==0:
        filename = filedialog.askopenfilename(initialdir="C:/")
        if filename:
            window.title(filename+" - Notepad")
            file_text = open(filename,'r')
            text.delete("0.1",END)
            text.insert("0.1",file_text.read())
            file_text.close()
    elif window.title() != "Untitled - Notepad" and updated==0:
        filename = filedialog.askopenfilename(initialdir="C:/")
        if filename:
            text.delete("0.1",END)
            window.title(filename+" - Notepad")
            file_text = open(filename,'r')
            text.insert("0.1",file_text.read())
            file_text.close()
    elif window.title() != "Untitled - Notepad" and updated==1:
        response = messagebox.askyesnocancel("Save Changes","Would you like to save changes to "+window.title())
        if response==None:
            pass
        elif response==False:
            filename = filedialog.askopenfilename(initialdir="C:/")
            if filename:
                file_text = open(filename,'r')
                text.delete("0.1",END)
                text.insert("0.1",file_text.read())
                file_text.close()
                window.title(filename+" - Notepad")
                updated=0
        elif response==True:
            file_retrieve = filedialog.askopenfilename(initialdir="C:/")
            if file_retrieve:
                filename = str(window.title())
                filename = filename.replace(" - Notepad","")
                file_text = open(filename,'w')
                file_text.write(text.get("0.1",END))
                text.delete("0.1",END)
                file_text.close()
                updated=0
                window.title(file_retrieve+" - Notepad")
                file_retrieve_text = open(file_retrieve,'r')
                text.insert("0.1",file_retrieve_text.read())
                file_retrieve_text.close()
def Save():
    global window,updated,text
    if window.title()=="Untitled - Notepad" and updated==0:
        filename = filedialog.asksaveasfilename(initialdir="C:/")
        if filename:
            file_text = open(filename,'w')
            file_text.write(text.get("0.1",END))
            file_text.close()
    elif window.title()=="Untitled - Notepad" and updated==1:
        filename = filedialog.asksaveasfilename(initialdir="C:/")
        if filename:
            file_text = open(filename, 'w')
            file_text.write(text.get("0.1", END))
            file_text.close()
            updated=0
    elif window.title() != "Untitled - Notepad" and updated==1:
        filename = str(window.title())
        filename = filename.replace(" - Notepad","")
        file_text = open(filename,'w')
        file_text.write(text.get("0.1",END))
        updated=0
        file_text.close()
def Save_As():
    global updated,text
    filename = filedialog.asksaveasfilename(initialdir="C:/")
    if filename:
        file_text = open(filename,'w')
        file_text.write(text.get("0.1",END))
        window.title(filename+" - Notepad")
        updated=0
def Exit():
    global window,text
    if window.title()=="Untitled - Notepad" and updated==1:
        response= messagebox.askyesnocancel("Save File","Would you like to Save "+window.title())
        if response==True:
            filename = filedialog.asksaveasfilename(initialdir="C:/")
            if filename:
                file_text = open(filename,'w')
                file_text.write(text.get("0.1",END))
                file_text.close()
        elif response==False:
            window.quit()
        elif response==None:
            pass
    elif window.title() != "Untitled - Notepad" and updated==1:
        response = messagebox.askyesnocancel("Save Changes","Would you like to Save Changes to "+window.title())
        if response==True:
            filename = str(window.title())
            filename = filename.replace(" - Notepad","")
            file_text = open(filename,'w')
            file_text.write(text.get("0.1",END))
            file_text.close()
            window.quit()
        elif response==False:
            window.quit()
        elif response==None:
            pass
    elif window.title() != "Untitled - Notepad" and updated==0:
        window.quit()
    elif window.title()=="Untitled - Notepad" and updated==0:
        window.quit()
def Clear():
    global text,updated
    text.delete("0.1",END)
    updated=1
def Select_All():
    global text
    text.tag_add("sel","0.1",END)
def Italic():
    global text,font_text
    if font_text['slant']=="roman":
        font_text['slant']="italic"
    elif font_text['slant']=="italic":
        font_text['slant']="roman"
    text['font'] = font_text
def Bold():
    global text, font_text
    if font_text['weight'] == "normal":
        font_text['weight'] = "bold"
    elif font_text['weight'] == "bold":
        font_text['weight'] = "normal"
    text['font'] = font_text
def Helvetica():
    global font_text,text
    font_text['family']="helvetica"
    text['font']=font_text
def Times():
    global font_text,text
    font_text['family'] = "times"
    text['font'] = font_text
def Size(a,b,c):
    global s1,font_text,text,v
    font_text['size']=v.get()
    text['font']=font_text
def Font_Size():
    global text,v,window2,s1
    window2=Toplevel()
    s1 = Scale(window2, from_=0, to=100, variable=v,orient=HORIZONTAL)
    v.trace('w',Size)
    s1.pack()
def Wrap():
    global text
    if text['wrap']=="none":
        text['wrap']=WORD
    else:
        text['wrap']="none"
def Text_Color():
    global text
    text['fg']=colorchooser.askcolor()[1]
def Background():
    global text
    text['bg']=colorchooser.askcolor()[1]
file_menu = Menu(menubar,tearoff=False)
menubar.add_cascade(label="file",menu=file_menu)
file_menu.add_command(label="New",command=New)
file_menu.add_command(label="Open",command=Open)
file_menu.add_command(label="Save",command=Save)
file_menu.add_command(label="Save As",command=Save_As)
file_menu.add_command(label="Exit",command=Exit)

edit_menu = Menu(menubar,tearoff=False)
menubar.add_cascade(label="edit",menu=edit_menu)
edit_menu.add_command(label="Select all",command=Select_All)
edit_menu.add_command(label="Clear",command=Clear)

format = Menu(menubar,tearoff=False)
font_Style = Menu(format,tearoff=False)
font_family = Menu(format,tearoff=False)
menubar.add_cascade(label="format",menu=format)
format.add_cascade(label="Font-Style",menu=font_Style)
font_Style.add_command(label="Italic",command=Italic)
font_Style.add_command(label="Bold",command=Bold)
format.add_command(label="Font-Size",command=Font_Size)
format.add_cascade(label="Font-Family",menu=font_family)
font_family.add_command(label="Helvetica",command=Helvetica)
font_family.add_command(label="Times",command=Times)
format.add_command(label="word wrap",command=Wrap)

color_edit = Menu(menubar,tearoff=False)
menubar.add_cascade(label="Color",menu=color_edit)
color_edit.add_command(label="Text",command=Text_Color)
color_edit.add_command(label="Background",command=Background)

frame = Frame(window,width=window.winfo_screenwidth(),height=window.winfo_screenheight())
frame.pack()
scroll = Scrollbar(frame,orient=VERTICAL)
scroll.pack(side=RIGHT,fill=Y)
scroll2 = Scrollbar(frame,orient=HORIZONTAL)
scroll2.pack(side=BOTTOM,fill=X)
text = Text(frame,width=window.winfo_screenwidth(),height=window.winfo_screenheight(),yscrollcommand=scroll.set,xscrollcommand=scroll2.set,wrap="none",font=font_text)
text.pack()
scroll.config(command=text.yview)
scroll2.config(command=text.xview)
text.bind("<KeyPress>",Updated)
window.mainloop()
