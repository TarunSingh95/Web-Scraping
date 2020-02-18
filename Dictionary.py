'''
Author: Tarun Singh
Online dictionary using BeautifulSoup Web Scraping and Tkinter(GUI)
User searches for a word. The search results are extracted from http://www.merriam-webster.com
'''

import requests
from bs4 import BeautifulSoup
from tkinter import *

def click():
    to_find= search_word.get()
    search_word_meaning.delete(0.0, END)
    
    response = requests.get("https://www.merriam-webster.com/dictionary/" + to_find)
    soup = BeautifulSoup(response.text, "html.parser")
    
    title = soup.find(class_="hword").text
    type_of = soup.find(class_="important-blue-link").text
    definition = soup.find(class_="dtText").text.replace(": ", "\n")
    
    search_word_meaning.insert(1.0, title + "\n")
    search_word_meaning.insert(2.0, type_of)
    search_word_meaning.insert(3.0, definition)

window = tkinter.Tk()
window.geometry("700x450")
window.title("Dictionary")

Label(window, text="Enter the word").pack()

search_word = Entry(window, width=20)
search_word.pack()

search_word_meaning = Text(window, width=400)
search_word_meaning.pack()

Button(window, text="Search", command=click).pack()

window.mainloop()
