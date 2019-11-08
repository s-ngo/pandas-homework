import argparse

import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv(filepath_or_buffer='housing.data',
                 sep='\\s+',
                 header=None)

df.columns = ['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS', 'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT', 'MEDV']

print(df.info())
print(df.describe())
print(df.corr())


# parser = argparse.ArgumentParser()
# parser.add_argument('--dataset_path', help='Dataset Path')
# parser.add_argument('--dataset_sep', default=',', help='Dataset separator')
# parser.add_argument('--column_names', help='Column Names')
# args = parser.parse_args()
#
# # We're now creating a dataframe straight from a data file
# df = pd.read_csv(filepath_or_buffer=args.dataset_path,
#                  sep=args.dataset_sep,
#                  header=0)
#
# df.columns = args.column_names.split(',')
#
# print(df.info())
# print(df.describe())
# print(df.corr())
#
# plt.plot(df['CRIM'])
# plt.savefig(f'crime.png')
# plt.clf()
#
# plt.scatter(df['MEDV'], df['CRIM'])
# plt.savefig(f'crime_to_value.png')