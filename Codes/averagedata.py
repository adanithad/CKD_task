"""
This code will import the raw .csv file and take the average for each patient.
"""
import pandas as pd

column_names = ['id', 'value', 'time']
dataframe = pd.read_csv('T_glucose.csv', delimiter=',')

new_table = dataframe.groupby('id').mean()[['value']]

new_table.to_csv('dataglucose.csv')


