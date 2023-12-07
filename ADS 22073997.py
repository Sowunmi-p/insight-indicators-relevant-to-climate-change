#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Thu Nov 16 12:41:38 2023

@author: apple
"""
#import libraries
import pandas as pd
import matplotlib.pyplot as plt
import stats as st

# Define a function to read my csv file and set index
# created another dataframe and transposed it to make the Country name be the
# the column
def read_csv_and_set_index(file_name):

    """
    Read a CSV file into a DataFrame and set the 'Country Name' column as 
    the index.

    Parameters:
    - file_name (str): The name of the CSV file.

    Returns:
    - pd.DataFrame: The DataFrame with the 'Country Name' column set as the 
    index.
    """

    df1 = pd.read_csv(file_name, index_col='Country Name')
    tranposed_df = df1.T
    
    return df1, tranposed_df


file_name = 'applied3.csv'
df1,tranposed_df = read_csv_and_set_index(file_name)

print(df1)
# display the shape of my data(number of rows and columns)
print("Dataset has {} rows and {} columns".format(df1.shape[0], df1.shape[1]))
print(df1.columns)
# display first few data of my second dataframe
print(tranposed_df)

# Data cleaning/wrangling
# drop columns that are not needed(country code and series code)
df1.drop(columns=['Country Code', 'Series Code'], inplace=True)

# display first few data of my first dataframe
print(df1.head())

# reset the column axis of my first dataframe
df1.set_axis(['Series_Name', '2000', '2001', '2002', '2003', '2004',
              '2005', '2006', '2007', '2008', '2009', '2010', '2011',
              '2012', '2013', '2014', '2015', '2016', '2017', '2018',
              '2019', '2020'], axis=1, inplace=True)

# display first few data of my first dataframe after resetting the axis
print(df1.head())




# reset the column axis of my second dataframe
tranposed_df.drop(['Country Code', 'Series Code'], inplace=True)
tranposed_df.set_axis(['Series_Name', '2000', '2001', '2002', '2003', '2004', '2005',
              '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013',
              '2014', '2015', '2016', '2017',
              '2018', '2019', '2020'], axis=0, inplace=True)

# display first few data of my second dataframe after resetting the axis
print(tranposed_df.head())

# display the information about my first dataframe
print(df1.info())

print("\nSummary Statistics of my first dataframe using pandas:")
print(df1.describe())


# display the sum of duplicated values of my first dataframe
print(df1.duplicated().sum())

# display the sum of null_values of my first dataframe
print(df1.isna().sum())


# display the information about my data
print(tranposed_df.info())

# display the statistical information about my second dataframe
print("\nSummary Statistics of my second dataframe using pandas:")
print(tranposed_df.describe())


# display the sum of duplicated values of my second dataframe
print(tranposed_df.duplicated().sum())

# display the sum of null_values of my second dataframe
print(tranposed_df.isna().sum())


# created a new data frame where series name is Access to electricity (%
# of population) using loc
electricity_df = df1[df1.loc[:, "Series_Name"]
                     == 'Access to electricity (% of population)']
print(electricity_df)



# created a new data frame where series name is Population growth (annual %)
# using loc
pop_df = df1[df1.loc[:, "Series_Name"] == 'Population growth (annual %)']
print(pop_df.head())


# created a new data frame where series name is Agricultural land (sq. km)
# using loc
agric_df = df1[df1.loc[:, "Series_Name"] == 'Agricultural land (sq. km)']
print(agric_df)


# created a new data frame where series name is GDP growth (annual %)
# using loc
gdp_df = df1[df1.loc[:, "Series_Name"] == 'GDP growth (annual %)']
print(gdp_df)


# created a new data frame where series name is Forest area (% of land area)
# using loc
forest_df = df1[df1.loc[:, "Series_Name"] == 'Forest area (% of land area)']
print(forest_df)


# created a new data frame where series name is CO2 emissions (kt) using loc
co2_df = df1[df1.loc[:, "Series_Name"] == 'CO2 emissions (kt)']
print(co2_df)


# display the new dataframe electricity_df
print(electricity_df)

# display the statistical information about electricity_df
print(electricity_df.describe())

print("correlstion", electricity_df.corr())

# Extracting the relevant data for the line plot and transposing
electricity_data = electricity_df.iloc[:, 1:].transpose()

# display my new variable electricity_data
print(electricity_data)

# Plotting the line graph
plt.figure(figsize=(10, 6))
electricity_data.plot(title='Access to Electricity Over the Years',
                      xlabel='Year',
                      ylabel='Access to electricity (% of population)')
plt.legend(title='Country', bbox_to_anchor=(1.05, 1), loc='upper left')

# Display the plot
plt.show()

# created a new variable for data where country name is India and set index
# to be series name and transposed it
india_data = df1.loc['India'].set_index('Series_Name').T
print(india_data)

# Calculating correlation matrix for india
india_corr = india_data.corr()
print(india_corr)
#statistical method to explore nigeria data
print(st.skew(india_data))
# set figsize to 10 by 8
plt.figure(figsize=(10, 8))
# Using the imshow function, this line displays the correlation matrix
# (india_corr) as an image. The colormap is set to 'coolwarm', which reflects
# positive associations with warm colours (reds) and negative correlations with
# cool colours (blues). To avoid smoothing between pixels,
# interpolation='nearest' is utilised.
plt.imshow(india_corr, cmap='coolwarm', interpolation='nearest')
# This line adds a colorbar to the right of the heatmap to help interpret
# the colours.
plt.colorbar()

# Adding annotations
''' for i in range(len(india_corr)) : as well as nested loop: 
    These loops 
iterate across the correlation matrix's rows and columns
'''
for i in range(len(india_corr)):
    for j in range(len(india_corr)):

        '''plt.text('nigeria_corr[i, j]:.2f', ha='center,' va='center,' 
      color='w'): Text annotations are added to the heatmap with this line. 
    It displays the correlation value (formatted to two decimal places) from 
    the correlation matrix in the centre of each cell in the heatmap'''

        plt.text(
            i, j, f'{india_corr.iloc[i, j]:.2f}',
            ha='center', va='center', color='w')

# Set axis labels and title
plt.xticks(range(len(india_corr)), india_corr.columns, rotation=90)
plt.yticks(range(len(india_corr)), india_corr.index)
plt.title('Correlation Matrix for India')
plt.show()

# Extracting the relevant data for the population bar plot
pop_data = pop_df.loc[:, ['2000', '2005', '2010', '2020']]

# Plotting the bar plot
plt.figure(figsize=(10, 6))
pop_data.plot(kind='bar',
              title='Population Growth for every first 5 Years interval',
              xlabel='Countries', ylabel='Annual % Growth')
plt.legend(title='years', bbox_to_anchor=(1.05, 1), loc='upper left')

# Display the plot
plt.show()

# created a new variable for data where country name is Nigeria and set index
# to be series name and transposed it
nigeria_data = df1.loc['Nigeria'].set_index('Series_Name').T
print(nigeria_data)

#statistical method to explore nigeria data
print(st.skew(nigeria_data))
# Calculating correlation matrix
nigeria_corr = nigeria_data.corr()
print(nigeria_corr)

# set figsize to 10 by 8
plt.figure(figsize=(10, 8))
# Using the imshow function, this line displays the correlation matrix
# (nigeria_corr) as an image. The colormap is set to 'coolwarm', which reflects
# positive associations with warm colours (reds) and negative correlations with
# cool colours (blues). To avoid smoothing between pixels,
# interpolation='nearest' is utilised.
plt.imshow(nigeria_corr, cmap='coolwarm', interpolation='nearest')
# This line adds a colorbar to the right of the heatmap to help interpret
# the colours.
plt.colorbar()

# Adding annotations
''' for i in range(len(nigeria_corr)) : as well as nested loop: 
    These loops 
iterate across the correlation matrix's rows and columns
'''
for i in range(len(nigeria_corr)):
    for j in range(len(nigeria_corr)):

        '''plt.text('nigeria_corr[i, j]:.2f', ha='center,' va='center,' 
      color='w'): Text annotations are added to the heatmap with this line. 
    It displays the correlation value (formatted to two decimal places) from 
    the correlation matrix in the centre of each cell in the heatmap'''

        plt.text(
            i, j, f'{nigeria_corr.iloc[i, j]:.2f}',
            ha='center', va='center', color='w')

# Set axis labels and title
plt.xticks(range(len(nigeria_corr)), nigeria_corr.columns, rotation=90)
plt.yticks(range(len(nigeria_corr)), nigeria_corr.index)
plt.title('Correlation Matrix for Nigeria')
plt.show()

# Extracting the relevant data for the gdp bar plot
gdp_data = gdp_df.loc[:, ['2000', '2005', '2010', '2020']]
print(gdp_data.head())
# Plotting the bar plot
plt.figure(figsize=(10, 6))
gdp_data.plot(kind='bar', title='GDP Growth for every first 5 Years interval',
              xlabel='Countries', ylabel='Annual % Growth')
plt.legend(title='years', bbox_to_anchor=(1.05, 1), loc='upper left')

# Display the plot
plt.show()

# Extracting the relevant data for the line plot
co2_df_data = co2_df.iloc[:, 1:].transpose()
print(co2_df_data)
# Plotting the line graph
plt.figure(figsize=(10, 6))
co2_df_data.plot(title='CO2 emissions (kt) over the years',
                 xlabel='Year', ylabel='CO2 emissions (kt)')
plt.legend(title='Country', bbox_to_anchor=(1.05, 1), loc='upper left')

# Display the plot
plt.show()

# created a new variable for data where country name is china and set index
# to be series name and transposed it
china_data = df1.loc['China'].set_index('Series_Name').T
# display my new variable (china_data)
print(china_data)

# Calculating correlation matrix
china_corr = china_data.corr()

# Display the correlation matrix
print(china_corr)



# set figsize to 10 by 8
plt.figure(figsize=(10, 8))
# Using the imshow function, this line displays the correlation matrix
# (china_corr) as an image. The colormap is set to 'coolwarm', which reflects
# positive associations with warm colours (reds) and negative correlations with
# cool colours (blues). To avoid smoothing between pixels,
# interpolation='nearest' is utilised.
plt.imshow(china_corr, cmap='coolwarm', interpolation='nearest')
# This line adds a colorbar to the right of the heatmap to help interpret
# the colours.
plt.colorbar()


''' for i in range(len(china_corr)) : as well as nested loop: 
    These loops 
iterate across the correlation matrix's rows and columns
'''
# Adding annotations
for i in range(len(china_corr)):
    '''plt.text('china_corr.iloc[i, j]:.2f', ha='center,' va='center,' 
  color='w'): Text annotations are added to the heatmap with this line. 
It displays the correlation value (formatted to two decimal places) from 
the correlation matrix in the centre of each cell in the heatmap'''
    for j in range(len(china_corr)):
        plt.text(i, j, f'{china_corr.iloc[i, j]:.2f}', ha='center',
                 va='center', color='w')

# Set axis labels and title
plt.xticks(range(len(china_corr)), china_corr.columns, rotation=90)
plt.yticks(range(len(china_corr)), china_corr.index)
plt.title('Correlation Matrix for China')

# Display the plot
plt.show()


#created a new pivot table called forest
forest = df1[df1["Series_Name"] == "Forest area (% of land area)"][[
    '2000', "2010", "2020"]].round()
#created a new column (diff_20) for the subtraction of forest value for 
#between the year 2020 and year 2000
forest['diff_20'] = forest['2020'] - forest['2000']
#display the pivot table
print(forest.sort_values('diff_20', ascending=False))

