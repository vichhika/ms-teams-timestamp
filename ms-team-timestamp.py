import csv
import re
import os
import argparse
import datetime
import time as TIME

def is_csv(parser, arg):
    status = False
    if not os.path.exists(arg):
        parser.error("\"%s\" does not exist !" % arg)
    else:
        if re.findall("\.csv$",arg):
            status = True
        else:
            parser.error("\"%s\" does not support !" % arg)
    return status

def is_end_meeting_valid(parser,arg):
    status = False
    if re.findall("^([0-9]{1,2}:){3}(AM|PM)$",arg):
        timeList = re.split(":",arg)
        status = True if 12 - int(timeList[0]) >= 0 and 60 - int(timeList[1]) >= 0 and 60 - int(timeList[2]) >= 0 else False
    if not status: parser.error("\"%s\" is invalid !" % arg)
    return status
        

def extract_csv(arg):
    csv_file = open(arg,'r',encoding='utf-16')
    dataset = list(csv.reader(col.replace('\t',',') for col in csv_file))
    header = ['Full Name', 'User Action', 'Duration of participation (min)']
    del dataset[0]
    body = dataset
    return header,body

def datetime_to_epoch(date,time):
    date = re.split("/",date)
    time = re.split(":",re.sub("^:","",time.replace(" ",":")))
    date_time = date+time
    date_time = '-'.join(j for j in ['0'+date_time[i] if len(date_time[i]) == 1 else date_time[i] for i in range(0,len(date_time))])
    return TIME.mktime(TIME.strptime(date_time,"%m-%d-%Y-%I-%M-%S-%p"))

if __name__ == '__main__':
    dataset_output = []
    students = []
    parser = argparse.ArgumentParser(description="Calculate Timestamp that student has joined meeting.")
    parser.add_argument("-i", dest="filepath", required=True, help="add csv file location. For example /home/user/data.csv", metavar="CSV-FILE-PATH")
    parser.add_argument("-t", dest="endmeeting", required=True, help="add HH:MM[AM/PM] of the end meeting. For example 12:00AM", metavar="HH:MM[AM/PM]")
    parser.add_argument("-o", dest="output", required=False, help="By default output file name based on date \"output-dd-mm-yyyy\"", metavar="OUTPUT-FILENAME")
    args = parser.parse_args()
    args.endmeeting = args.endmeeting[:-2]+":00:"+args.endmeeting[-2:]
    if is_csv(parser,args.filepath) and is_end_meeting_valid(parser,args.endmeeting):
        header,body = extract_csv(args.filepath)
        [students.append(i[0]) for i in body]
        students = list(dict.fromkeys(students))
        for student in students:
            total_joined = 0
            join_time = 0
            leave_time = 0
            end_time = 0
            for i in body:
                if student == i[0]:
                    if join_time == 0 and "Joined" in i[1]:
                        join_time = datetime_to_epoch(i[2],i[3])
                    else:
                        leave_time = datetime_to_epoch(i[2],i[3])
                        total_joined +=(leave_time - join_time)/60
                        join_time = 0
                        leave_time = 0
            if join_time != 0:
                end_time = datetime_to_epoch(i[2],args.endmeeting)
                total_joined +=(end_time - join_time)/60
                join_time = 0
            total_joined = int(total_joined)
            dataset_output.append([student,"joined",str(total_joined)])
        dataset_output.sort()
        output_file = args.output+".csv" if args.output else "output-"+body[0][2].replace("/","-")+"-"+str(TIME.strftime("%H%M%S",TIME.localtime()))+".csv" 
        if not os.path.exists("output"): os.mkdir("output")
        with open("output/"+output_file,'w', encoding='utf-16') as csv_file:
            w = csv.writer(csv_file)
            w.writerow(header)
            w.writerows(i for i in dataset_output)
