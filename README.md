# GoogleTasksJSONtoTXT

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A very simple tool to convert Google Tasks [Takeout](https://takeout.google.com/) JSON file format to plain TXT files.

# How it works

Currently, each list is converted to a separate _TXT_ file containing the respective tasks in the _Output_ folder.
The user can either run the [python script](run_silent.py) or use a _very very very very_ basic user interface trough the [script run_gui](run_gui.py)

# How to Use with User Interface Version

1. Download or clone this respository contents

2. Go to [Google TakeOut](https://takeout.google.com/) select and download the Google Tasks JSON file and place it anywhere of your liking
3. Execute the script [run_gui.py](run_gui.py)
4. Click the _Select JSON File_ button and select the file.
5. Click the _Extract Lists_ button and wait for the message of conclusion. 
6. Click the _Open Output Directory_ button to see the results or look up the folder named _Output_ of your copy of this project

# How to Use it silently and quickly

1. Download or clone this respository contents
2. Go to [Google TakeOut](https://takeout.google.com/) select and download the Google Tasks JSON file 
3. Place the _Tasks.json_ file into the project directory
4. Run the file [run_silent.py](run_silent.py)
   - The script will populate the _output_ directory with _.txt_ files for each _TaskList_ listed on  _Tasks.json_
5. Check the _Output_ folder for the results

# Requirements

- Python 3.8 or above
- [Tkinter] (https://docs.python.org/3/library/tkinter.html)

=======
2. Go to [Google TakeOut](https://takeout.google.com/) select and download the Google Tasks JSON file 
3. Place the _Tasks.json_ file into the project directory
4. Run the file _main.py_
   - The script will populate the _output_ directory with _.txt_ files for each _TaskList_ listed on  _Tasks.json_


# Why ?

I needed to import my GTasks lists to [Trello](http://www.trello.com). Currently the Trello app does not offer an official import function, but, by default is able to convert multiline texts to multiple items (cards) on a list. 
Since [Google TakeOut](https://takeout.google.com/) will only exports tasks to JSON and copying/pasting from the GTasks HTML interface is not an option, a simple Python Script ought to suffice.

