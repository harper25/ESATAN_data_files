# ESATAN_data_files

Simple Python GUI tool (Tkinter) for rearrangement of ESATAN *.data files.

## Description
The program rearranges ESATAN "*.data" files so that the definitions (ex. definitions of nodes, that are written in several lines) are reformatted to one line.
The program creates a new file with suffix "_COL", ex.:
SAT_XYZ.NODES.data -> SAT_XYZ_COL.NODES.data.

- GUI: 

![ ](/images/GUI.JPG)

- file before: 
![ ](/images/before.JPG)

- file after:
![ ](/images/after.JPG)

This improved formatting is particularly useful when editing an attribute in several rows at once.

## Usage
#### Python file
Please, run a following command in a Command Line:
`python ESATAN_rearrange_data_files.py`

`ESATAN_rearrange_data_files.py` imports modules, which are included in every standard Python distribution, so there is no need to install additional packages with `pip`.
The file `requirements.txt` lists modules, which are necessary to build an executable for Windows. This can be done with:
`pyinstaller --onefile --windowed ESATAN_rearrange_data_files.py`

#### Exe for Windows
Please, run `ESATAN_rearrange_data_files.exe` from folder `dist/`.
