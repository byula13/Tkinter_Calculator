import tkinter as tk
'''Imports TKinter module
tk is an alias for easy access'''

#Button click handler
def press(v):
    entry.insert(tk.END, v)
    '''Called when a number or operator button is clicked 
    Inserts the pressed values at the end od entry widget'''
    
#Clear function
def clear():
    entry.delete(0, tk.END)
    '''Clears the calculator screen
    Deletes all charaters from index 0 to END'''
    
    #Calculation function
def calc():
    try:
        result = eval(entry.get())
        '''entry.get() retrives the expression (e.g 5+3)
        eval() evaluate the string as a python expression'''
        
        entry.delete(0, tk.END)
        '''Clears the old expression'''
        entry.insert(0, result)
        '''Displays the result of expression'''
        
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Invalid Expression")
        '''Handles invalid  expressions (e.g 5++)
        Display "error" instead of crashing'''
        

#Main window creation
root = tk.Tk()
'''Creates the main application window'''

root.title("Calculator")
'''Sets window title'''
 
root.configure(bg="#1e1e1e")
'''Sets the background color (dark theme)'''

root.resizable(False, False) 

#Entry widgets (Display Screen)
entry = tk.Entry(
    root,
    font=("Times new Roman", 20),
    bg="#2d2d2d",
    fg="white",
    bd=0,
    justify="right"
     ) 
'''Acts as calculator display 
Right-aligned for better calculator look'''
             
entry.grid(row=0, column=0, columnspan=4, padx=12, pady=12, ipady=10)
'''place entry at top
columnspan=4 makes it streach across 4 columns'''

#Button Labels
buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "0", ".", "=", "+"
]
'''Represent calculator buttons stored in list to reduce repetitive code'''

#Dynamic Button Creation 
r=1
c=0
'''Rows and column counters for grid layout'''

for b in buttons:#iterates througs each butten label
    cmd = calc if b == "=" else lambda x=b: press(x)
    '''if button is "=", cal calc()
    otherwise call press() with the button value
    lambda x=b prevents late binding issue'''
    
    tk.Button(
        root,
        text=b,
        command=cmd, #these threelines will creates button  widgets
        font=("Calibri", 14),
        width=5,
        height=2,
        bg="#ff9500" if b in "+-*/" else "#3a3a3a",
        #Operator buttons  are Orange, Number buttons are gray
        fg="white",
        bd=0,
    ).grid(row=r, column=c, padx=6, pady=6)
    
    c+=1
    #after 4 columns, move to next row
    if c==4:
        r+=1
        c=0
    #Move to next row after 4  buttons
    
#Clear Button
tk.Button(
    root,
    text="C",
    command=clear,
    font=("Calibri", 14),
    bg="#f3bf3b",
    fg="white",
    bd=0,
    width=22,
    height=2
).grid(row=r, column=0, columnspan=4, pady=8)
'''Clear the calculator
spans across all columns'''

#Event Loop
root.mainloop()
'''Keeps  the window running
Listener for users interactions'''        
    