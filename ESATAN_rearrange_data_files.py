# Node Definitions in ESATAN
# olesjakubb@gmail.com
# 11.05.2018

from os import path as osPath
from tkinter import Tk, messagebox, Button, Label
from tkinter.filedialog import askopenfilename

def delete_newlines_from_node_definitions(oldfile):
	filename = osPath.basename(oldfile)
	parts = filename.split('.')
	parts[0] += '_COL'
	filename = '.'.join(parts)
	head, tail = osPath.split(oldfile)
	newfile = osPath.join(head, filename)
	with open(oldfile, 'r', encoding='utf-8') as infile:
		with open(newfile, 'w', encoding='utf-8') as outfile:
			newline = ''
			for line in infile:
				line = line.strip()
				if line.endswith(','):
					newline += line + ' '
				elif newline and line.endswith(';'):
					newline += line
					outfile.write(newline + '\n')
					newline = ''
				else:
					outfile.write(line + '\n')


def loadFileCallback():
	initialdir = osPath.dirname(osPath.abspath(__file__))
	Tk().withdraw()
	filename = askopenfilename(initialdir = initialdir, title = "Select file", 
		filetypes = (("data files","*.data"),("all files","*.*")))
	try:
		delete_newlines_from_node_definitions(filename)
		messagebox.showinfo("Information", "Finished!")
	except FileNotFoundError:
		messagebox.showinfo("Error", "Cannot open the file: Invalid file or file path")


def center_window(window, width=440, height=320):
	screen_width = window.winfo_screenwidth()
	screen_height = window.winfo_screenheight()
	x = (screen_width/2) - (width/2)
	y = (screen_height/2) - (height/2)
	window.geometry('%dx%d+%d+%d' % (width, height, x, y))


def close_app():
	mainWindow.quit()

title_text = "Rearrange *.data files"
description_text = """The program rearranges ESATAN "*.data" files 
so that the various definitions (ex. definitions 
of nodes, that are written in several lines) 
are written in one line.

The program creates a new file with suffix "_COL", ex.:
SAT_XYZ.NODES.data -> 
SAT_XYZ_COL.NODES.data. """


if __name__ == "__main__":
	mainWindow = Tk()
	mainWindow.title("ESATAN_support_app: Rearrange *.data files")
	center_window(mainWindow)
	titleLabel = Label(mainWindow, text = title_text, font="-weight bold").pack(padx=10, pady=15)
	descriptionLabel = Label(mainWindow, text = description_text, font="bold").pack(padx=30, pady=0)
	LoadButton = Button(mainWindow, text ="Load file", width = 12, height = 2, 
		command = loadFileCallback, font="bold")
	LoadButton.pack(padx=30, pady=30)
	mainWindow.protocol('WM_DELETE_WINDOW', close_app)
	mainWindow.mainloop()


# pyinstaller --onefile --windowed a1.py
# pyinstaller --onefile --windowed a1.py --version-file=file_version_info.txt