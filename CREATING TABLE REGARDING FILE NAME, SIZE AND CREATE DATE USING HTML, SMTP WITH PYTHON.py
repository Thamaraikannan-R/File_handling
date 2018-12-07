# CREATING TABLE REGARDING FILE NAME, SIZE AND CREATE DATE USING HTML, SMTP WITH PYTHON
import datetime
import os, sys
import os.path, time
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# THIS IS FILE READING AND WORKING PART
file_incoming_path = "C:\\Users\\lotus\\Desktop\\new"  # Puting Path of your Files
org = {'1.txt', '2.txt', '3.txt', '4.txt', '5.txt', '6.txt'}
ls = (os.listdir(file_incoming_path))
ls = set(ls)
not_present = set(org.difference(ls))
ls = list(org.intersection(ls))
file_name = list()
TimeArrived = list()
file_size_found = list()
# print(not_present)
ls.sort()
for i in ls:
    s = ''
    s = file_incoming_path
    s = s.__add__('\\')
    s = s.__add__(i)  # i is file name to read size and time of creation
    file_name.append(i)
    TimeArrived.append(time.ctime(os.path.getmtime(s)))
    file_size_found.append(str(os.path.getsize(s)))
# THIS IS HTML PART
html = """\
<!DOCTYPE html>
<html>
<head>
<style>
table, th, td {
    border: 1px solid black;
    border-collapse: collapse;
}
th, td {
    padding: 10px;
    text-align: centre;
}
</style>
</head>
<body>
<center>
<h2><center>File Access Using List</center></h2>
<p>This program having:\n1. Read all files from Dir.\n2. Check wether recommended Files and\n3. Get File name, File size, File created time and Received or not.4. Show Green If received else show Red</p>
<table style="width:65%">
  <caption> File Date and Time </caption>
  <tr>
    <th>File Name</th>
    <th>File Size</th>
    <th>Date and Time</th>
    <th>Received</th>
  </tr>

 """
for (j, k, l) in zip(file_name, file_size_found, TimeArrived):
    html = html + "<tr><td>" + j + "</td><td>" + str(
        int(int(k) / 1024)) + "Kb</td><td>" + l + "</td><td td style=""background-color:Green;""></td></tr>"
for i in not_present:
    html = html + "<tr><td>" + i + "</td><td>" + "null" + "</td><td>" + "null" + "</td><td td style=""background-color:Red;""></td></tr>"
html = html + """
</table>
</center>
</body>
</html>
"""
print(html)
# THIS IS EMAIL PART
f = open('helloworld.html', 'w')
f.write(html)
f.close()
me = "rtkcse2@gmail.com"
you = "rtkcse@gmail.com"
msg = MIMEMultipart('alternative')
msg['Subject'] = "Subject"
msg['From'] = me
msg['To'] = you
part1 = MIMEText(html, 'html')
msg.attach(part1)
mail = smtplib.SMTP('smtp.gmail.com', 587)
mail.ehlo()
mail.starttls()
mail.login('rtkcse2@gmail.com', 'kannankannan')
#mail.sendmail(me, you, msg.as_string())
print("Sucessfully email Sent")
