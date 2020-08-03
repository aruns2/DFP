# -------------------------------------------------- #
# DATA-FOCUSED PYTHON — HOMEWORK 4:
# Pandas Series and DataFrame and Matplotlib
# -------------------------------------------------- #
# Team 14:
# Saumweber Andrea, asaumweb@andrew.cmu.edu
# Sharma Arun, aruns2@andrew.cmu.edu


# -------------------------------------------------- #
# MODULE IMPORTS
# -------------------------------------------------- #
from urllib.request import urlopen  # b_soup_1.py
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import pandas as pd

# -------------------------------------------------- #
# 1A BEAUTIFULSOUP MODULE / WEBSITE SCRAPING
# -------------------------------------------------- #
# Open the web page
html = urlopen(
    'https://www.treasury.gov/resource-center/data-chart-center/'
    'interest-rates/Pages/TextView.aspx?data=yieldYear&year=2019')

# Create BeautifulSoup object
bsyc = BeautifulSoup(html.read(), "lxml")

# Find the right table class and grab the correct t-chart table (it is the only one)
tc_table_list = bsyc.findAll('table', {"class": "t-chart"})
tc_table = tc_table_list[0]


# Define conversion functions
# Rates should be float values
# The time to maturity should be integers representing month
def type_conversion(var):
    try:
        var = float(var)  # converts Strings to floats (if possible)
    except:
        var = cn_to_nm(var)  # converts all other values
    return var


def cn_to_nm(var):
    if 'mo' in var:
        var = int(var.split(' ')[0])  # for monthly denotation
    elif 'yr' in var:
        var = int(var.split(' ')[0]) * 12  # for yearly denotation
    elif 'Date' in var:
        var = ''  # Delete tag Date because it must be empty or 'Date / Month to maturity'
    else:
        pass  # keep variable otherwise
    return var


# Get the data and convert it to a list of list using list comprehension
daily_yield_curves = [[type_conversion(r.contents[0]) for r in c.children] for c in tc_table.children]

# Write the daily yield curves to a file and print it out as nice table
output = open('./daily_yield_curves.txt', 'wt', encoding='utf-8')

for i in range(len(daily_yield_curves)):
    table = "\t".join(str(item).ljust(8) for item in daily_yield_curves[i])
    output.write(table + "\n")
    print(table)

# Close the file to make resources free
output.close()

# -------------------------------------------------- #
# 1B MATPLOTLIB MODULE / PLOTTING DATA
# -------------------------------------------------- #
# Create np.arrays from the list of lists
np_daily_yield_curves = np.array(daily_yield_curves)
y, x = np.meshgrid(np_daily_yield_curves[0, 1:].astype(np.int), range(0, 250))
z = np.array(np_daily_yield_curves[1:, 1:].astype(np.float))

# Create a 3D Surface Plot
fig1 = plt.figure()  # figure object
ax1 = fig1.add_subplot(111, projection='3d')  # set axes
ax1.plot_surface(x, y, z, cmap='coolwarm')  # add surface/data
ax1.set_xlabel('trading days since 01/02/19')  # set axes labels
ax1.set_ylabel('month to maturity')
ax1.set_zlabel('rate')
ax1.view_init(40, 30)  # orientate
plt.show()

# Create a Wireframe Plot
fig2 = plt.figure() # figure object
ax2 = fig2.add_subplot(111, projection='3d')  # set axes
ax2.plot_wireframe(x, y, z) # add wireframe/data
ax2.set_xlabel('trading days since 01/02/19') # set axes labels
ax2.set_ylabel('month to maturity')
ax2.set_zlabel('rate')
ax2.view_init(40, 30) # orentate
plt.show()


# -------------------------------------------------- #
# 1B PANDAS MODULE / USING DATA FRAMES
# -------------------------------------------------- #
# Create a pandas data frame using slices and comprehension
yield_curve_df = pd.DataFrame([ls[1:13] for ls in daily_yield_curves[1:]],
                              columns=daily_yield_curves[0][1:],
                              index=[ls[0] for ls in daily_yield_curves[1:]])

# Create a plot with dates on the x-axis, rates on the y-axis;
# maturities are distinguished by color
yield_curve_df.plot()
plt.legend(title='month to maturity')
plt.show()

# Create a transposed version of the plot
# Transpose the data frame
by_day_yield_curve_df = yield_curve_df.transpose()
# Slice the data frame for sake of clarity (only use every 20th trading day)
by_day_yield_curve_df = by_day_yield_curve_df[by_day_yield_curve_df.columns[::20]]
# Create the plot with maturities on the x-axis, rates on the y-axis;
# trading days are distinguished by color
by_day_yield_curve_df.plot()
plt.legend(title='trading days')
plt.show()
