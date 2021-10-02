# Microsoft Teams Student Timestamp

ms-team-timestamp.py is a Python script that calculate timestamp of student has joined meeting.

## Usage

```sh
❯ python ms-team-timestamp.py -h
usage: ms-team-timestamp.py [-h] -i CSV-FILE-PATH -t HH:MM[AM/PM] [-o OUTPUT-FILENAME]

Calculate Timestamp that student has joined meeting.

optional arguments:
  -h, --help          show this help message and exit
  -i CSV-FILE-PATH    add csv file location. For example /home/user/data.csv
  -t HH:MM[AM/PM]     add HH:MM[AM/PM] of the end meeting. For example 12:00AM
  -o OUTPUT-FILENAME  By default output file name based on date "output-dd-mm-yyyy"
❯ python ms-team-timestamp.py -i test/meetingAttendanceList.csv -t 11:20PM
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.
