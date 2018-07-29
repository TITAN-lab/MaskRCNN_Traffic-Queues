import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def read_file(path):
    file = pd.read_csv(path)
    return file

def time_shift(time_data, shift):
    time_data = range(0, time_data[-1])
    time_data = list(filter(lambda x: (x % 20 == 0), time_data))
    tos = time_data[shift:]
    froms = time_data[0:len(tos)]
    return [froms, tos]
### read_file are you done? yes
folder = "results/"
csv_files = os.listdir(folder)
cols = ['Q1', 'Q2', 'Q3', 'Q4']
# cols = ['Q1', 'Q2', 'Q3']
output_result = pd.DataFrame(columns=cols)
for csv_file in csv_files:
    if csv_file.endswith(".csv"):
        path = folder + csv_file
        file = read_file(path)
        times = file['time'].unique()
        if (len(times))>0:
            [froms, tos]=time_shift(times, 1)
            for (a, b) in zip(froms, tos):
                cur_data = file[(file['time'] >= a) & (file['time'] <b) ]
                if cur_data.shape[0]>0:
                    data_values= cur_data['queue_length'].values
        #             # print (data_values)
        #             L = sum(i<=100 for i in data_values)/len((data_values))
        #             M = sum(i > 100 and i<= 150 for i in data_values) / len((data_values))
        #             H = sum(i > 150 for i in data_values) / len((data_values))
        #             output_result.loc[len(output_result)] = [L,M,H];
        # output_result.to_csv("results/quartiles/" + os.path.basename(path))

                    data_values = data_values[data_values>100]
                    if len(data_values)>0:
                        out = np.percentile(data_values, [25,50,75,100])
                    else:
                        data_values=[0]
                        out = np.percentile(data_values, [25, 50, 75, 100])
                    output_result.loc[len(output_result)] = out;
        output_result.to_csv("results/quartiles/" + os.path.basename(path))
