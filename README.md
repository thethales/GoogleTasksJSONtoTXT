# GoogleTasksJSONtoTXT

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A very simple tool to convert Google Tasks [Takeout](https://takeout.google.com/) JSON file format to plain TXT files.

# How it works

Currently, each list is converted to a separate _TXT_ file containing the respective tasks.

# How to Use

1. Download or clone this respository contents
2. Go to [Google TakeOut](https://takeout.google.com/) select and download the Google Tasks JSON file 
3. Place the _Tasks.json_ file into the project directory
4. Run the file _main.py_
   - The script will populate the _output_ directory with _.txt_ files for each _TaskList_ listed on  _Tasks.json_

# Why ?

I needed to import my GTasks lists to [Trello](http://www.trello.com). Currently the Trello app does not offer an official import function, but, by default is able to convert multiline texts to multiple items (cards) on a list. 
Since [Google TakeOut](https://takeout.google.com/) will only exports tasks to JSON and copying/pasting from the GTasks HTML interface is not an option, a simple Python Script ought to suffice.

