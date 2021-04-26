#import libraries
from tkinter import *
from tkinter import ttk
import random
from colors import *
from win32api import GetSystemMetrics
import numpy

#import algorithms
from Algorithms.BubbleSort import BubbleSort
from Algorithms.SelectionSort import SelectionSort
from Algorithms.InsertionSort import InsertionSort
from Algorithms.MergeSort import MergeSort
from Algorithms.QuickSort import QuickSort
from Algorithms.HeapSort import HeapSort
from Algorithms.CountingSort import CountingSort

global temp
#window
window = Tk()
window.title("Algorithm Visualization")
window.minsize=(GetSystemMetrics(0),GetSystemMetrics(1))
window.config(bg = "white")

#variables definition
algorithm_name = StringVar()
speed_name = StringVar()
algorithm_type = StringVar()
x_start = IntVar()
y_start = IntVar()
x_end = IntVar()
y_end = IntVar()
type_list =['None','Sorting','Path Finding']
algo_list = {
    "None":['None'],
    "Sorting" : ['None','Bubble Sort','Merge Sort','Selection Sort','Insertion Sort','Quick Sort','Heap Sort','Counting Sort'],
    "Path Finding" : ['None']
}

coordinate_list = {
    'x' : [int(x) for x in range(-GetSystemMetrics(0)-1//2,GetSystemMetrics(0)//2)],
    'y' : [int(x) for x in range(-GetSystemMetrics(1)-1//2,GetSystemMetrics(1)//2)]
}
speed_list = ['None','Fast', 'Medium', 'Slow']

def drawData(data,colorArray):
    canvas.delete("all")
    canvas_width = GetSystemMetrics(0)
    canvas_height = 2*GetSystemMetrics(1)/3
    x_width = canvas_width / (len(data) + 1)
    offset = 4
    spacing = 2
    normalizedData = [i / max(data) for i in data]

    for i, height in enumerate(normalizedData):
        x0 = i * x_width + offset + spacing
        y0 = canvas_height - height * 390
        x1 = (i + 1) * x_width + offset
        y1 = canvas_height
        canvas.create_rectangle(x0, y0, x1, y1, fill=colorArray[i])

    window.update_idletasks()

#generating random data for sorting
def generate():
    global data
    data = numpy.random.randint(150, size = 100)
    data=data.tolist()
    drawData(data,[BLUE for x in range(len(data))])

#setting visualization speed
def set_speed():
    if speed_menu.get() == 'Slow':
        return 0.3
    elif speed_menu.get() == 'Medium':
        return 0.1
    else:
        return 0.001

def find_path():
    pass

def draw_path():
    pass

def sort():
    timeTick = set_speed()
    if algo_menu.get() == 'Bubble Sort':
        BubbleSort(data, drawData, timeTick)
    elif algo_menu.get() == 'Selection Sort':
        SelectionSort(data, drawData, timeTick)
    elif algo_menu.get() == 'Insertion Sort':
        InsertionSort(data, drawData, timeTick)
    elif algo_menu.get() == 'Merge Sort':
        MergeSort(data, 0, len(data)-1, drawData, timeTick)
    elif algo_menu.get() == 'Quick Sort':
        QuickSort(data, 0, len(data)-1, drawData, timeTick)
    elif algo_menu.get() == 'Heap Sort':
        HeapSort(data, drawData, timeTick)
    else:
        CountingSort(data, drawData, timeTick)

#change algorithm menu after selecting algorithm type
def change_algo_menu():
    algo_menu['values'] = algo_list[algorithm_type.get()]

#buttons with algorithm type
def additional_buttons():
    if algorithm_type.get() == "Sorting":
        #if type is sorting
        #button for sort command
        global button1
        button1 = Button(UI_frame, text="Sort", command=sort, bg=DARK_BLUE, fg = "white")
        button1.grid(row=5, column=1, padx=5, pady=5)
        #button for generating array
        global button3
        button3 = Button(UI_frame, text="Generate Array", command=generate, bg=DARK_BLUE, fg = "white")
        button3.grid(row=5, column=0, padx=5, pady=5)

    elif algorithm_type.get() == "Path Finding":
        try:
            button1.grid_remove()
            button3.grid_remove()
        except:
            pass

        label3 = Label(UI_frame, text="Starting Coordinates (x,y):", bg=WHITE)
        label3.grid(row=3, column=0, padx=10, pady=5, sticky=W)

        x_s = ttk.Combobox(UI_frame, textvariable = x_start, values = coordinate_list['x'])
        x_s.grid(row=3, column = 1, padx= 10, pady = 5, sticky = W)
        x_s.current(0)

        y_s = ttk.Combobox(UI_frame, textvariable = y_start, values = coordinate_list['y'])
        y_s.grid(row=3, column = 2, padx= 10, pady = 5, sticky = W)
        y_s.current(0)

        label4 = Label(UI_frame, text="End Coordinates (x,y):", bg=WHITE)
        label4.grid(row=4, column=0, padx=10, pady=5, sticky=W)

        x_e = ttk.Combobox(UI_frame, textvariable = x_end, values = coordinate_list['x'])
        x_e.grid(row=4, column = 1, padx= 10, pady = 5, sticky = W)
        x_e.current(0)

        y_e = ttk.Combobox(UI_frame, textvariable = y_end, values = coordinate_list['y'])
        y_e.grid(row=4, column = 2, padx= 10, pady = 5, sticky = W)
        y_e.current(0)

        button5 = Button(UI_frame, text="Find Path", command=find_path, bg=DARK_BLUE, fg = "white")
        button5.grid(row=4, column=3, padx=5, pady=5)
    else:
        pass


UI_frame = Frame(window, width= GetSystemMetrics(0), height=GetSystemMetrics(1)/3, bg=WHITE)
UI_frame.grid(row=0, column=0, padx=10, pady=5)

#label of algorithm type
label0 = Label(UI_frame, text="Algorithm Type: ", bg=WHITE)
label0.grid(row=0, column=0, padx=10, pady=5, sticky=W)
type_menu = ttk.Combobox(UI_frame, textvariable=algorithm_type, values=type_list)
type_menu.grid(row=0, column=1, padx=5, pady=5)
type_menu.current(0)

#label of algorithm
label1 = Label(UI_frame, text="Algorithm: ", bg=WHITE)
label1.grid(row=1, column=0, padx=10, pady=5, sticky=W)
algo_menu = ttk.Combobox(UI_frame, textvariable=algorithm_name, values=algo_list[algorithm_type.get()])
algo_menu.grid(row=1, column=1, padx=5, pady=5)
algo_menu.current(0)

#label for selecting speed
label2 = Label(UI_frame, text="Speed: ", bg=WHITE)
label2.grid(row=2, column=0, padx=10, pady=5, sticky=W)
speed_menu = ttk.Combobox(UI_frame, textvariable=speed_name, values=speed_list)
speed_menu.grid(row=2, column=1, padx=5, pady=5)
speed_menu.current(0)

canvas = Canvas(window, width=GetSystemMetrics(0), height=2*GetSystemMetrics(1)/3, bg=WHITE)
canvas.grid(row=4, column=0, padx=10, pady=5)

#button for changing algorithms after selecting type
button2 = Button(UI_frame, text="Confirm", command=change_algo_menu, bg=DARK_BLUE, fg = "white")
button2.grid(row=0, column=2, padx=5, pady=5)

#button for getting addition buttons depending on algorithm type
button4 = Button(UI_frame, text="Confirm", command=additional_buttons, bg=DARK_BLUE, fg = "white")
button4.grid(row=1, column=2, padx=5, pady=5)

window.mainloop()