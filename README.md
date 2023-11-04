# Sorting Algorithm Visualizer

This Sorting Algorithm Visualizer is a GUI application built with Tkinter in Python. It allows users to visualize different sorting algorithms in action and understand their time complexities.

<video width="320" height="240" controls>
  <source src="demo.mov" type="video/mp4">
  Your browser does not support the video tag.
</video>


## Features

- Visualize sorting algorithms graphically in real-time.
- Compare the time complexity of algorithms graphically.
- Supports multiple sorting algorithms including Bubble Sort, Quick Sort, and Merge Sort.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

Before running the application, make sure you have Python installed on your machine. You can download Python [here](https://www.python.org/downloads/).

### Installing

Clone the repository to your local machine:

```bash
git clone https://github.com/your-username/sorting-visualizer.git
```

Navigate to the cloned repository:

```bash
cd sorting-visualizer
```
Install the required dependencies:

```bash
pip install -r requirements.txt
```

### Running the Application
To run the application, execute the following command in the terminal:

```bash
python main.py
```

### Usage

Once the application starts, you can:

- Select a sorting algorithm from the dropdown menu.
- Click 'Generate Array' to create a new random array.
- Click 'Start Sorting' to begin the visualization.
- Observe the sorting process on the screen.

### Building the Executable

To create an executable for the application, you can use PyInstaller:

```bash
pyinstaller --onefile --windowed main.py
```

The executable will be located in the dist directory.

### Built With

- Python 3 - The programming language used.
- Tkinter - The GUI toolkit used.
