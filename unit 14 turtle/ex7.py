import tkinter as tk

# Function to draw the letter "C" with 20% of the circle removed from both ends
def draw_C(canvas):
    # Draw the upper curve (red)
    #                 left top  rds  top       
    canvas.create_line(90, 110, 150, 110, fill="blue", width=15)
    #                left top  rds  deg 
    canvas.create_arc(50, 50, 150, 150, start=216, extent=140, outline="blue", width=15, style="arc")
    canvas.create_arc(50, 50, 150, 150, start=160, extent=120, outline="green", width=15, style="arc")
    canvas.create_arc(50, 50, 150, 150, start=90, extent=120, outline="yellow", width=15, style="arc")
    
    # Draw the bottom curve (blue)
    canvas.create_arc(50, 50, 150, 150, start=36, extent=108, outline="red", width=15, style="arc")
    
    

# Create a tkinter window
root = tk.Tk()
root.title("Letter C")

# Create a canvas
canvas = tk.Canvas(root, width=600, height=600, bg="white")
canvas.pack()

# Draw the letter "C"
draw_C(canvas)

# Start the tkinter event loop
root.mainloop()
