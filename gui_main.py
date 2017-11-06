#! /usr/bin/env python
#
# GUI module generated by PAGE version 4.9
# In conjunction with Tcl version 8.6
#    Oct 12, 2017 07:53:45 PM
import sys

try:
    from Tkinter import *
except ImportError:
    from tkinter import *

try:
    import ttk
    py3 = 0
except ImportError:
    import tkinter.ttk as ttk
    py3 = 1

import gui_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = Tk()
    top = New_Toplevel_1 (root)
    gui_support.init(root, top)
    root.protocol('WM_DELETE_WINDOW', destroy_app)
    root.mainloop()

w = None
def create_New_Toplevel_1(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = Toplevel (root)
    top = New_Toplevel_1 (w)
    gui_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_New_Toplevel_1():
    global w
    w.destroy()
    w = None

def destroy_app():
    global root
    root.destroy()
    exit(0)

class New_Toplevel_1:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#d9d9d9' # X11 color: 'gray85'

        top.geometry("555x398+408+185")
        top.title("PlotIt")

        v = IntVar()

        self.Canvas1 = Canvas(top)
        self.Canvas1.place(relx=0.04, rely=0.05, relheight=0.75, relwidth=0.72)
        self.Canvas1.configure(background="white")
        self.Canvas1.configure(borderwidth="2")
        self.Canvas1.configure(relief=RIDGE)
        self.Canvas1.configure(selectbackground="#c4c4c4")
        self.Canvas1.configure(width=394)

        self.fx = Entry(top)
        self.fx.place(relx=0.11, rely=0.85, relheight=0.05, relwidth=0.53)
        self.fx.configure(background="white")
        self.fx.configure(font="TkFixedFont")
        self.fx.configure(width=296)
        self.fx.bind('<Return>', lambda x: gui_support.Plot(self.fx.get(), self.x_lower.get(), self.x_upper.get(), "#FFFF00", self.Canvas1))
        self.fx.configure(fg='#000000')

        self.Label1 = Label(top)
        self.Label1.place(relx=0.77, rely=0.08, height=18, width=47)
        self.Label1.configure(text='''x lower''')

        self.x_lower = Entry(top)
        self.x_lower.place(relx=0.88, rely=0.08, relheight=0.05, relwidth=0.08)
        self.x_lower.configure(background="white")
        self.x_lower.configure(font="TkFixedFont")
        self.x_lower.configure(width=46)
        self.x_lower.insert(0, '0')
        self.x_lower.configure(fg='#000000')

        self.Label2 = Label(top)
        self.Label2.place(relx=0.77, rely=0.13, height=18, width=51)
        self.Label2.configure(text='''x upper''')

        self.x_upper = Entry(top)
        self.x_upper.place(relx=0.88, rely=0.13, relheight=0.05, relwidth=0.08)
        self.x_upper.configure(background="white")
        self.x_upper.configure(font="TkFixedFont")
        self.x_upper.configure(width=46)
        self.x_upper.insert(0, '100')
        self.x_upper.configure(fg='#000000')

        self.Label3 = Label(top)
        self.Label3.place(relx=0.04, rely=0.85, height=18, width=35)
        self.Label3.configure(text='''f(x)=''')

        self.bt_plot = Button(top)
        self.bt_plot.place(relx=0.67, rely=0.85, height=26, width=47)
        self.bt_plot.configure(activebackground="#d9d9d9")
        self.bt_plot.configure(command= lambda: gui_support.Plot(self.fx.get(), self.x_lower.get(), self.x_upper.get(), "#FFFF00", self.Canvas1))
        self.bt_plot.configure(cursor="fleur")
        self.bt_plot.configure(text='''Plot''')
        self.bt_plot.configure(width=47)

        self.Label3 = Label(top)
        self.Label3.place(relx=0.78, rely=0.34, height=18, width=100)
        self.Label3.configure(text=" Choose the Color ")

        self.current_color = StringVar(top)
        self.current_color.set('Red')
        self.colors = {'Red','Blue','Cyan','Black','Green'}
        self.dropdown_menu = OptionMenu(top,self.current_color,*self.colors, command = self.Dropdown_Changed)
        self.dropdown_menu.pack(side = 'top', anchor = 'w')
        self.dropdown_menu.place(relx=0.78, rely=0.40, height=18, width=100)

        self.color_input = Entry(top)
        self.color_input.place(relx=0.78, rely=0.47, relheight=0.05, relwidth=0.10)
        self.color_input.configure(background="white")
        self.color_input.configure(font="TkFixedFont")
        self.color_input.insert(0, '#ABCDEF')
        self.color_input.configure(fg='#000000')

        self.bt_go = Button(top)
        self.bt_go.place(relx=0.90, rely=0.47, height=20, width=40)
        self.bt_go.configure(activebackground="#d9d9d9")
        self.bt_go.configure(command= lambda: gui_support.Plot(self.fx.get(), self.x_lower.get(), self.x_upper.get(), self.color_input.get(), self.Canvas1))
        self.bt_go.configure(cursor="fleur")
        self.bt_go.configure(text='''Go''')
        self.bt_go.configure(width=47)

    def Dropdown_Changed(self, current_color):
        color = '#000000'
        if current_color == 'Red':
            color = '#FF0000'
        elif current_color == 'Blue':
            color = '#0000FF'
        elif current_color == 'Cyan':
            color = '#00FFFF'
        elif current_color == 'Black':
            color = '#000000'
        elif current_color == 'Green':
            color = '#008000'
        self.color_input.delete(0,100)
        self.color_input.insert(0,color)

    @staticmethod
    def popup1(event):
        Popupmenu1 = Menu(root, tearoff=0)
        Popupmenu1.configure(activebackground="#f9f9f9")
        Popupmenu1.post(event.x_root, event.y_root)






if __name__ == '__main__':
    vp_start_gui()
