import csv

with open('student.csv','w',newline='')as f:
    w=csv.writer(f)
    header=['sid','sname','city','contact']
    w.writerow(header)

#Insert 5 Records Directly
    row=[[1,'om','kedarnath',9876567890],
         [2,'sai','shirdi',1231231230],
         [3,'ram','ayodhya',1234567865],
         [4,'kishan','vrundavan',2345670763],
         [5,'ravan','lanka',8978655544]]
    w.writerows(row)


#Insert 5 Records Take Input From User 
    for i in range(5):
        sid=int(input("Enter Student id:"))
        sname=input("Enter Student name:")
        city=input("Enter Student city:")
        contact=input("Enter Student contact:")
        row=[sid,sname,city,contact]
        w.writerow(row)


#Read Records From CSV File
with open('student.csv','r') as read:
    r=csv.reader(read)
    for i in r:
        print(i)

