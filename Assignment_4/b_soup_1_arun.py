#assignment_4

from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

html = urlopen('https://www.treasury.gov/resource-center/'
               'data-chart-center/interest-rates/Pages/'
               'TextView.aspx?data=yieldYear&year=2019')

bsyc = BeautifulSoup(html.read(), "lxml")
tc_table_list = bsyc.findAll('table',
                      { "class" : "t-chart" } )
tc_table = tc_table_list[0]
x1 =[] #initiating a list

# just get the contents of each cell
for c in tc_table.children:
    for r in c.children:
        x1.append(r.contents)

#creating an array of result
a1 = np.array(x1)
a2 =a1.reshape(251,13) # reshaping the data in table format
df = pd.DataFrame(a2[1:], columns = a2[0])

# Write the daily yield curves to a file and print it out as nice table
fout = open('daily_yield_curves.txt', 'wt', encoding='utf-8') #open
fout.write(df.to_string(header = True, index = False)) #printdf
fout.close() #close


#preparing for plots
a3 = a2[1:,1:]
a4 = np.array([[1, 2, 3, 6, 12, 24, 36, 60, 84, 120, 240, 360]])#unintelligent method of adding the row
a5 = np.append(a4, a3, axis =0)
z = a5[1:].astype(np.float) #changing to float preparing Z
a5[:1].astype(np.int) #changing to integer
y = range(0,250)
x, y = np.meshgrid(a4, y) #preparing x and y axes


#3D Surface Plot
fig1 = plt.figure()  
ax1 = fig1.add_subplot(111, projection='3d') 
ax1.plot_surface(x, y, z, cmap='coolwarm')  
ax1.set_xlabel('days_since_01/02/19')  
ax1.set_ylabel('month to maturity')
ax1.set_zlabel('rate')
ax1.view_init(40, 30)
fig1.tight_layout()
plt.show()

#Wireframe Plot
fig2 = plt.figure() # figure object
ax2 = fig2.add_subplot(111, projection='3d')
ax2.plot_wireframe(x, y, z) 
ax2.set_xlabel('days since 01/02/19') 
ax2.set_ylabel('month to maturity')
ax2.set_zlabel('rate')
ax2.view_init(40, 30) 
fig2.tight_layout()
plt.show()


