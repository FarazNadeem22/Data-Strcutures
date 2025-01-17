# Python Code Description

This repository contains Python code demonstrating dictionary manipulation, iteration, list handling, and Turtle graphics module usage.

## Code Description

### `PDF_extraction.py`

This script utilizes the PyPDF2 library to extract text content from PDF files. The code includes:

- Reading 'starwarspages.pdf' to extract text from each page using a `PdfFileReader`.
- Printing the extracted text from each page of 'starwarspages.pdf'.
- Extracting text from the first page of 'starwars.pdf' and printing it using `getPage` and `extractText`.
- Proper file handling with 'with open' for 'starwarspages.pdf' to ensure the file is closed after usage.

### `Turtle_Graphics.py`

This script demonstrates the use of the `turtle` module for basic graphics drawing. It includes:

- Importing the `st` module from the Turtle graphics library.
- Defining a dictionary `sc` containing state-capital pairs and printing them.
- Working with lists (`d` and `f`) and creating a nested list `cm`.
- Accessing and printing an element from the nested list `cm` using indexing.

## Instructions to Run

1. Ensure Python is installed on your system.
2. Install the necessary Python libraries using `pip install PyPDF2`.
3. Clone or download the repository to your local machine.
4. Execute the Python scripts (`PDF_extraction.py`, `Turtle_Graphics.py`) using a Python interpreter.

## Contribution

Contributions are welcome! Feel free to open issues or pull requests for improvements, bug fixes, or additional features.

