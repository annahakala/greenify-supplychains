# The inputted data is a pre_processed csv file from the original data supplied from the challenge.
# Due to the propiotary nature of the data we have choosen not to upload it to github.
# The pre-process is decribed in the read me.

import pandas as pd
import sys


df = pd.read_csv("data/new_data_calculated.csv")

CO2_cost_by_category = df.groupby(['CategoryL2'])['CO2kg','SpendEUR'].sum()

CO2_cost_by_category.to_csv('CO2_cost_by_category.csv')
