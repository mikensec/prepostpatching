#!/usr/bin/python3
#compare.py by Michael Nieto
import tkinter as tk
from tkinter import filedialog
import difflib

def comparetext(txt1, txt2):

    first_txt_file = open(txt1,'r')
    string_from_txt1 = first_txt_file.read()
    string_from_txt1 = string_from_txt1.strip()
    first_txt_file.close()
    
    second_txt_file = open(txt2,'r')
    string_from_txt2 = second_txt_file.read()
    string_from_txt2 = string_from_txt2.strip()
    second_txt_file.close()

    diff = difflib.ndiff(string_from_txt1.splitlines(),string_from_txt2.splitlines())
    print('\n'.join(diff))

root = tk.Tk()
root.withdraw()

filename1 = filedialog.askopenfilename(title = "Select first file to compare!")
filename2 = filedialog.askopenfilename(title = "Select second file to compare!")
comparetext(filename1, filename2)


