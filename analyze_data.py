import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt
import seaborn as sns
color = sns.color_palette()

DATA_DIR = "data/"

def main():
    #train_df = pd.read_csv(DATA_DIR + 'train_2016_v2.csv/train_2016_v2.csv', parse_dates=["transactiondate",])
    #sub_df = pd.read_csv(DATA_DIR + 'train_2016_v2.csv/train_2016_v2.csv') 
    prop_df = pd.read_csv(DATA_DIR + 'properties_2016.csv/properties_2016.csv')

    missing_df = prop_df.isnull().sum(axis=0).reset_index()
    missing_df.columns = ['column_name', 'missing_count']
    missing_df = missing_df.ix[missing_df['missing_count']>0]
    missing_df = missing_df.sort_values(by='missing_count')
    
    ind = np.arange(missing_df.shape[0])
    fig, ax = plt.subplots(figsize=(12,18))
    rects = ax.barh(ind, missing_df.missing_count.values, color='blue')
    ax.set_yticks(ind)
    ax.set_yticklabels(missing_df.column_name.values, rotation='horizontal')
    ax.set_xlabel("Count of missing values")
    ax.set_title("Number of missing values in each column")
    plt.show()
    

if __name__ == "__main__":
    main()
    
