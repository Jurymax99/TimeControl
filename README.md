# TimeControl
## Installation 

Download as ZIP and extract the files.

## Running

Type the following in your console:
```
python3 timeControl.py
```
Once started, type h to get the following message:
```
Enter s to start counting your worktime
Once started type s to stop the clock and h to get help
Enter q to quit
```

## Data
The app will generate a _CSV_ file named _data.csv_ with 4 columns (Day, Hour, WorkTime and Concept).
Every time a workday ends, the data is automatically saved in the file.

## Possible Errors
If the file _data.csv_ is opened with a program while the app is trying to write it, an _I/O Error_ will be thrown. As the program prints the info once is trying to write it, it is not fully lost, and can be entered in _data.csv_ manually.

## Author
David Gabaldà Montero