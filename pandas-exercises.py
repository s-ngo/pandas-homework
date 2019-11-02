import pandas as pd
import numpy as np


def pretty_print(name, to_print):
    print(f'{name}:')
    print(f'{to_print}\n\n')


insurance = pd.read_csv(filepath_or_buffer='insurance.csv',
                        sep=',',  # optional
                        header=0)  # optional

# Getting DataFrames information
# pretty_print("Insurance dataframe", insurance.to_string())
# pretty_print("Insurance columns", insurance.columns)
# pretty_print("Insurance index", insurance.index)
# pretty_print("Insurance dtypes", insurance.dtypes)
# pretty_print("Insurance shape", insurance.shape)
# pretty_print("Insurance info", insurance.info())
# pretty_print("Insurance describe", insurance.describe())
#
# pretty_print("Age column", insurance['age'])
# pretty_print("Age, Children, Charges", insurance[['age', 'children', 'charges']])

# 5. Print only the first 5 lines and only the columns age,children and charges
# pretty_print("5 lines of Age, Children, Charges", insurance[['age', 'children', 'charges']].head(n=6))

# 6. What is the average, minimum and maximum charges ?
# pretty_print("Mean of Charges column", insurance['charges'].mean())
# pretty_print("Min of Charges column", insurance['charges'].min())
pretty_print("Max of Charges column", insurance['charges'].max())

# 7. What is the age and sex of the person that paid 10797.3362. Was he/she a smoker?
# pretty_print("Age and Sex of person who paid 10797.3362", insurance['charges'] == "10797.3362")
# "Age and Sex of person who paid 10797.3362",
# pretty_print(insurance['age', 'sex'].where(insurance['charges'] == 10797.3362)
# pretty_print(insurance[insurance['charges'] == 10797.3362]['age'])
pretty_print(insurance.loc[10797.3362])

# 8. What is the age of the person who paid the maximum charge?


# 9. How many insured people do we have for each region?
# 10. How many insured people are children?
# 11. What do you expect to be the correlation between charges and age, bmi and children?
# 12. Using the method corr(), check if your assumptions were correct.
