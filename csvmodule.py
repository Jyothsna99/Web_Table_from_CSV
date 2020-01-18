'''using csv module we can read the contents of the csv
This program reads the data from csv file and create a table in the web page using the data that is red from csv file'''
import csv
def csv_to_html_table(fname,headers=None,delimiter=","):
    f=open(fname,'r')
    content=csv.reader(f)
    rows = list(content)
    table = "<center><h1>Student Table</h1></center><table align='center' border='3'>"
    #creating HTML header row if header is provided 
    if headers is not None:
        table+= "".join(["<th>"+cell+"</th>" for cell in headers.split(delimiter)])
    else:
        table+= "".join(["<th>"+cell+"</th>" for cell in rows[0].split(delimiter)])
        rows=rows[1:]
    #Converting csv to html row by row
    for row in rows:
        table+="<tr>"
        for i in row:
            table+="<td>"+i+"</td>"
        table+="</tr>"
    table+="</table><br>"
    return table
if __name__=='__main__':
    myheader='roll no,name,marks'
    w=csv_to_html_table("E://table.csv",myheader)
    #table.csv is the name of the  csv file in which the information is stored 
    f=open("table.html","w")
    f.write(w)
    f.close()