import tkinter as tk
import random
from Algorithms import bubble_sort, insertion_sort, selection_sort, merge_sort, quick_sort, heap_sort, counting_sort, bucket_sort
from AlgorithmDescription import algorithm_descriptions
is_sorted = False  # This will be False when not sorted, True when sorted

def draw_data(canvas, data, colorArray):
    canvas.delete("all")
    c_height = 380
    c_width = 600
    x_width = c_width / (len(data) + 1)
    offset = 30
    spacing = 10
    for i, height in enumerate(data):
        x0 = i * x_width + offset + spacing
        y0 = c_height - height
        x1 = ((i + 1) * x_width) + offset
        y1 = c_height
        canvas.create_rectangle(x0, y0, x1, y1, fill=colorArray[i])
        canvas.create_text(x0+2, y0, anchor=tk.SW, text=str(data[i]), font=("Helvetica", 8))
    root.update_idletasks()


def start_sorting():
    global arr, is_sorted
    if not arr: return
    
    if is_sorted:  # If already sorted, reset the array
        generate_array()
        is_sorted = False
        b1.config(text="Start Sorting")  # Change button text back to "Start Sorting"
    else:
        time_delay = 0.09  # Set the time delay for drawing
        alg = alg_menu.get()
        if alg == 'Bubble Sort':
            bubble_sort(canvas, arr, draw_data, root, time_delay)
        elif alg == 'Selection Sort':
            selection_sort(canvas, arr, draw_data, root, time_delay)
        elif alg == 'Insertion Sort':
            insertion_sort(canvas, arr, draw_data, root, time_delay)
        elif alg == 'Merge Sort':
            merge_sort(canvas, arr, draw_data, root, time_delay)
        elif alg == 'Quick Sort':
            quick_sort(canvas, arr, draw_data,  time_delay, 0, len(arr) - 1)
        elif alg == 'Heap Sort':
            heap_sort(canvas, arr, draw_data,  time_delay)
        elif alg == 'Counting Sort':
            counting_sort(canvas, arr, draw_data,  time_delay)
        elif alg == 'Bucket Sort':
            bucket_sort(canvas, arr, draw_data,  time_delay)
        
        is_sorted = True
        b1.config(text="Reset")  # Change button text to "Reset" after sorting

# Generate a random array
def generate_array():
    global arr, is_sorted
    arr = [random.randrange(10, 400) for _ in range(30)]
    draw_data(canvas, arr, ['red' for x in range(len(arr))])
    is_sorted = False
    b1.config(text="Start Sorting")  # Ensure the button text is "Start Sorting"

# Function to update the description label
def update_description(*args):
    alg = alg_menu.get()
    description_label.config(text=algorithm_descriptions.get(alg, "Select a sorting algorithm"))

root = tk.Tk()
root.title('Sorting Algorithm Visualizer')
root.maxsize(900, 600)

arr = []

canvas = tk.Canvas(root, width=600, height=400, bg='white')
canvas.pack(pady=20)

# User Interface Area
UI_frame = tk.Frame(root, width=600, height=300, bg='grey')
UI_frame.pack(fill="x", expand=True, padx=10, pady=5)

# Label for algorithm description, defined before the update_description function
description_label = tk.Label(UI_frame, text="Select a sorting algorithm", bg='grey', wraplength=500, justify="left")
description_label.pack(side="left", padx=10, pady=5)

# Dropdown to select sorting algorithm
l1 = tk.Label(UI_frame, text="Algorithm: ", bg='grey')
l1.pack(side="left", padx=10, pady=5)
alg_menu = tk.StringVar(root)

# Function to update the description label
def update_description(*args):
    alg = alg_menu.get()
    description_label.config(text=algorithm_descriptions.get(alg, "Select a sorting algorithm"))

# Now set the trace
alg_menu.trace('w', update_description)

alg_dropdown = tk.OptionMenu(UI_frame, alg_menu, *algorithm_descriptions.keys())
alg_dropdown.pack(side="left", padx=5, pady=5)
alg_menu.set("Bubble Sort")  # Default value


# Button for starting the sorting process
b1 = tk.Button(UI_frame, text="Start Sorting", command=start_sorting, bg='red')
b1.pack(side="left", padx=5, pady=5)

# Button for generating array
b3 = tk.Button(UI_frame, text="New", command=generate_array, bg='white')
b3.pack(side="left", padx=5, pady=5)

# Generate initial random data
generate_array()  # This will create and draw the initial random array

root.mainloop()
