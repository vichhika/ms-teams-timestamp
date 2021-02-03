# Microsoft Teams Student Timestamp

ms-team-timestamp.py is a Python script that calculate timestamp of student has joined meeting.

```bash
pip install foobar
```

## Usage

```sh
sh-5.1$ python ms-team-timestamp.py -h
usage: ms-team-timestamp.py [-h] -i CSV-FILE-PATH -t HH:MM:SS:AM/PM [-o OUTPUT-FILENAME]

Calculate Timestamp that student has joined meeting.

optional arguments:
  -h, --help          show this help message and exit
  -i CSV-FILE-PATH    add csv file location. For example /home/user/data.csv
  -t HH:MM:SS:AM/PM   add HH:MM:SS:AM/PM of the end meeting. For example 12:00:00:AM
  -o OUTPUT-FILENAME  By default output file name based on date "output-dd-mm-yyyy"
sh-5.1$ python ms-team-timestamp.py -i test/meetingAttendanceList.csv -t 11:20:00:PM
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.
