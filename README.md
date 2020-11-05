# GoogleTasksJSONtoTXT

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A very simple tool to convert Google Tasks [Takeout](https://takeout.google.com/) JSON file format to plain TXT files.

# How it works

As of November 2020, the JSON File geneated by [Google Takeout](https://takeout.google.com/) (see [Tasks_sample.json](Tasks_sample.json)), contains as expected, a very well structured description of your Tasks. The file is composed by an array of _items_ (your lists) and the _items_ by another array of _items_ (your tasks) ...
For utilitarian purposes, this project will generate a text file for each of your lists, and each file will contain the respective tasks.

Currently, the user can either run the [python script](run_silent.py) or use a _very very very very_ basic user interface trough the [script run_gui](run_gui.py) or [Windows Executable](https://github.com/thethales/GoogleTasksJSONtoTXT/releases)

# How to Use

As mentioned previously you can either run the [python script](run_silent.py) or use a _very very very very_ basic user interface trough the [script run_gui](run_gui.py) or trough the Windows binarie avaliable at the [releases section](https://github.com/thethales/GoogleTasksJSONtoTXT/releases). Both methods are described below:

## Method 1: Graphical User Interface (GUI)

### On Windows

1. Download the [lastet release](https://github.com/thethales/GoogleTasksJSONtoTXT/releases)
2. Go to [Google TakeOut](https://takeout.google.com/) select and download the Google Tasks JSON file and place it anywhere of your liking
3. Execute the App
4. Click the _Select JSON File_ button and select the file exported from Google Takeout.
5. Click the _Extract Lists_ button to generate the TXT files.
6. Click the _Open Output Directory_ button to see the results.

```
Note: This project makes use of this magical piece of software named [Auto-py-to-exe](https://github.com/brentvollebregt/auto-py-to-exe/) 
to generate windows executables
```
### On other Platforms

1. Download or clone this respository contents (or download de source files of the [lastet release](https://github.com/thethales/GoogleTasksJSONtoTXT/releases))
2. Go to [Google TakeOut](https://takeout.google.com/) select and download the Google Tasks JSON file and place it anywhere of your liking
3. Execute the script [run_gui.py](run_gui.py)
4. Click the _Select JSON File_ button and select the file exported from Google Takeout.
5. Click the _Extract Lists_ button to generate the TXT files.
6. Click the _Open Output Directory_ button to see the results or look up the folder named _Output_ of your copy of this project


## Method 2: Python Script CLI

1. Download or clone this respository contents
2. Go to [Google TakeOut](https://takeout.google.com/) select and download the Google Tasks JSON file 
3. Place the _Tasks.json_ file into the project directory
4. Run the file [run_silent.py](run_silent.py)
   - The script will populate the _output_ directory with _.txt_ files for each _TaskList_ listed on  _Tasks.json_
5. Check the _Output_ folder for the results


# Requirements

- Python 3.8 or above
   - [Tkinter] (https://docs.python.org/3/library/tkinter.html)


# Why ?

I needed to import my GTasks lists to [Trello](http://www.trello.com). Currently the Trello app does not offer an official import function, but, by default is able to convert multiline texts to multiple items (cards) on a list. 
Since [Google TakeOut](https://takeout.google.com/) will only exports tasks to JSON and copying/pasting from the GTasks HTML interface is not an option, a simple Python Script ought to suffice.
And since I already had my hands in this project, I happened to try and learn a little of Python GUIs devlopment.

