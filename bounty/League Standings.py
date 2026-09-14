
#####################################################################################################################################################################
#LA_LIGA_STANDING
#####################################################################################################################################################################
 
from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np
pd.set_option("display.max_rows",1000)
url = "https://www.msn.com/en-us/sports/soccer/la-liga/standings" #url
response = requests.get(url)
soup = BeautifulSoup(response.text,'html.parser')
table1 = soup.find(class_= "tableview soccerfullstandings standing")#######################change class other than jquery

#Find all the rows
rowcell = []#all rows
for row in table1.find_all('tr'):
    for cell in table1.find_all('td'):
        c = cell.text.replace('\n','')
        rowcell.append(c)
    break



#find all column names
tcol = ['POS',"TEAM","GP","W","D","L","GD","PTS"]#column names 



tcol = tcol[:11] ###########################change according to the number of columns 
print(tcol)

#remove row cells
rindex = []
for i in range(20):
    z = 1+(11*i)
    gf = 7+(11*i)
    ga = 8+(11*i)
    rindex.append(z)
    rindex.append(gf)
    rindex.append(ga)


rowcell = np.delete(rowcell, rindex)
print(len(rowcell))
        
#make rowcell 2DD
rowcell = np.array(rowcell)
r = int(len(rowcell)/len(tcol))

c = int(len(tcol))
print(c)
rowcell = np.reshape(rowcell,(r,c))

#Making dataframe
from IPython.display import HTML
table= pd.DataFrame(rowcell, columns = tcol)
table = table.rename_axis(None)
q = table.to_html(classes='table table-hover table-bordered', index=False)

text = """<html><style type="text/css">

table, th, td {
border: 2px #2b2b2b solid;
color: #2b2b2b;
}

table { background-color: white; }
th { background-color: silver; }

</style>
<font color="black">""" + q + "</font></body></html>"
#Write in text file
f= open("la_liga_standings.html","w+")
f.write(text)
f.close()
text


#####################################################################################################################################################################
#epl_standing
#####################################################################################################################################################################

from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np
pd.set_option("display.max_rows",1000)
url = "https://www.msn.com/en-us/sports/soccer/premier-league/standings" #url
response = requests.get(url)
soup = BeautifulSoup(response.text,'html.parser')
table1 = soup.find(class_= "tableview soccerfullstandings standing")#######################change class other than jquery

#Find all the rows
rowcell = []#all rows
for row in table1.find_all('tr'):
    for cell in table1.find_all('td'):
        c = cell.text.replace('\n','')
        rowcell.append(c)
    break



#find all column names
tcol = ['POS',"TEAM","GP","W","D","L","GD","PTS"]#column names 



tcol = tcol[:11] ###########################change according to the number of columns 
print(tcol)

#remove row cells
rindex = []
for i in range(20):
    z = 1+(11*i)
    gf = 7+(11*i)
    ga = 8+(11*i)
    rindex.append(z)
    rindex.append(gf)
    rindex.append(ga)

rowcell = np.delete(rowcell, rindex)
print(len(rowcell))
        
#make rowcell 2DD
rowcell = np.array(rowcell)
r = int(len(rowcell)/len(tcol))

c = int(len(tcol))
print(c)
rowcell = np.reshape(rowcell,(r,c))

#Making dataframe
from IPython.display import HTML
table= pd.DataFrame(rowcell, columns = tcol)
table = table.rename_axis(None)
q = table.to_html(classes='table table-hover table-bordered', index=False)

text = """<html><style type="text/css">

table, th, td {
border: 2px #2b2b2b solid;
color: #2b2b2b;
}

table { background-color: white; }
th { background-color: silver; }

</style>
<font color="black">""" + q + "</font></body></html>"
#Write in text file
f= open("epl_standings.txt","w+")
f.write(text)
f.close()
text
#####################################################################################################################################################################
#seriea_standings
#####################################################################################################################################################################
from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np
pd.set_option("display.max_rows",1000)
url = "https://www.msn.com/en-us/sports/soccer/serie-a/standings" #url
response = requests.get(url)
soup = BeautifulSoup(response.text,'html.parser')
table1 = soup.find(class_= "tableview soccerfullstandings standing")#######################change class other than jquery

#Find all the rows
rowcell = []#all rows
for row in table1.find_all('tr'):
    for cell in table1.find_all('td'):
        c = cell.text.replace('\n','')
        rowcell.append(c)
    break



#find all column names
tcol = ['POS',"TEAM","GP","W","D","L","GD","PTS"]#column names 



tcol = tcol[:11] ###########################change according to the number of columns 
print(tcol)

#remove row cells
rindex = []
for i in range(20):
    z = 1+(11*i)
    gf = 7+(11*i)
    ga = 8+(11*i)
    rindex.append(z)
    rindex.append(gf)
    rindex.append(ga)


rowcell = np.delete(rowcell, rindex)
print(len(rowcell))
        
#make rowcell 2DD
rowcell = np.array(rowcell)
r = int(len(rowcell)/len(tcol))

c = int(len(tcol))
print(c)
rowcell = np.reshape(rowcell,(r,c))

#Making dataframe
from IPython.display import HTML
table= pd.DataFrame(rowcell, columns = tcol)
table = table.rename_axis(None)
q = table.to_html(classes='table table-hover table-bordered', index=False)

text = """<html><style type="text/css">

table, th, td {
border: 2px #2b2b2b solid;
color: #2b2b2b;
}

table { background-color: white; }
th { background-color: silver; }

</style>
<font color="black">""" + q + "</font></body></html>"
#Write in text file
f= open("seriea_standings.txt","w+")
f.write(text)
f.close()
text
#####################################################################################################################################################################
#ligue_a_standings
#####################################################################################################################################################################
from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np
pd.set_option("display.max_rows",1000)
url = "https://www.msn.com/en-us/sports/soccer/ligue-un/standings" #url
response = requests.get(url)
soup = BeautifulSoup(response.text,'html.parser')
table1 = soup.find(class_= "tableview soccerfullstandings standing")#######################change class other than jquery

#Find all the rows
rowcell = []#all rows
for row in table1.find_all('tr'):
    for cell in table1.find_all('td'):
        c = cell.text.replace('\n','')
        rowcell.append(c)
    break



#find all column names
tcol = ['POS',"TEAM","GP","W","D","L","GD","PTS"]#column names 



tcol = tcol[:11] ###########################change according to the number of columns 
print(tcol)

#remove row cells
rindex = []
for i in range(20):
    z = 1+(11*i)
    gf = 7+(11*i)
    ga = 8+(11*i)
    rindex.append(z)
    rindex.append(gf)
    rindex.append(ga)


rowcell = np.delete(rowcell, rindex)
print(len(rowcell))
        
#make rowcell 2DD
rowcell = np.array(rowcell)
r = int(len(rowcell)/len(tcol))

c = int(len(tcol))
print(c)
rowcell = np.reshape(rowcell,(r,c))

#Making dataframe
from IPython.display import HTML
table= pd.DataFrame(rowcell, columns = tcol)
table = table.rename_axis(None)
q = table.to_html(classes='table table-hover table-bordered', index=False)

text = """<html><style type="text/css">

table, th, td {
border: 2px #2b2b2b solid;
color: #2b2b2b;
}

table { background-color: white; }
th { background-color: silver; }

</style>
<font color="black">""" + q + "</font></body></html>"
#Write in text file
f= open("ligue_a_standings.txt","w+")
f.write(text)
f.close()
text

#####################################################################################################################################################################
#bundesliga_standings
#####################################################################################################################################################################

from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np
pd.set_option("display.max_rows",1000)
url = "https://www.msn.com/en-us/sports/soccer/bundesliga/standings" #url
response = requests.get(url)
soup = BeautifulSoup(response.text,'html.parser')
table1 = soup.find(class_= "tableview soccerfullstandings standing")#######################change class other than jquery

#Find all the rows
rowcell = []#all rows
for row in table1.find_all('tr'):
    for cell in table1.find_all('td'):
        c = cell.text.replace('\n','')
        rowcell.append(c)
    break



#find all column names
tcol = ['POS',"TEAM","GP","W","D","L","GD","PTS"]#column names 



tcol = tcol[:11] ###########################change according to the number of columns 
print(tcol)

#remove row cells
rindex = []
for i in range(18):
    z = 1+(11*i)
    gf = 7+(11*i)
    ga = 8+(11*i)
    rindex.append(z)
    rindex.append(gf)
    rindex.append(ga)


rowcell = np.delete(rowcell, rindex)
print(len(rowcell))
        
#make rowcell 2DD
rowcell = np.array(rowcell)
r = int(len(rowcell)/len(tcol))

c = int(len(tcol))
print(c)
rowcell = np.reshape(rowcell,(r,c))

#Making dataframe
from IPython.display import HTML
table= pd.DataFrame(rowcell, columns = tcol)
table = table.rename_axis(None)
q = table.to_html(classes='table table-hover table-bordered', index=False)

text = """<html><style type="text/css">

table, th, td {
border: 2px #2b2b2b solid;
color: #2b2b2b;
}

table { background-color: white; }
th { background-color: silver; }

</style>
<font color="black">""" + q + "</font></body></html>"
#Write in text file
f= open("bundesliga_standings.txt","w+")
f.write(text)
f.close()
text

#####################################################################################################################################################################
#UPLOAD
#####################################################################################################################################################################



