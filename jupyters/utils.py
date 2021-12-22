# %%
### Import Modules
from datetime import datetime
from sklearn import preprocessing
from scipy import stats
import numpy as np
from sklearn import metrics
import pandas as pd

# %%
### Convert numerical date to datetime formats
def date_conversion(df,column,dt_format = '%d-%m-%Y'):
    df_copy = df.copy()
    date = df_copy[column]                                                                        # Get the actual column
    date = date.astype(str)                                                                       # Convert to string to add the century
    date = '19' + date                                                                            # Add the century value
    df_copy[column] = date.apply(lambda x: (datetime.strptime(x,'%Y%m%d')).strftime(dt_format))   # Convert to the desired date format

    return df_copy


def date_conversion_genders(df,column,dt_format = '%d-%m-%Y'):
    df_copy = df.copy()
    date = df_copy[column]                                            # Get the actual column
    date = date.astype(str)                                      # Convert to string to add the century
    date = '19' + date                                           # Add the century value

    ### Get the monts value with gender
    lst = []
    for item in date:
        lst.append(item[4:6])
        
    months = []
    gender = [] 
    for item in lst:
        if(int(item) > 50):
            months.append(int(item)- 50)
            gender.append('female')
        else:
            months.append(int(item))
            gender.append('male')
            
    ### Replace the old month values
    for i in range(len(date)):
        if gender[i] == 'female':
            date[i] = str(int(date[i])-5000)

    df_copy[column] = date.apply(lambda x: (datetime.strptime(x,'%Y%m%d')).strftime(dt_format))
    df_copy["gender"] = gender

    return df_copy

# %%
def replace_null(df):
    return df.fillna(df.median())

def replace_null_non_numeric(df,column):
    return df[column].fillna(df[column].value_counts().idxmax())

# %%
### Drop columns with percentage of nulls that surpasses the provided limit
def drop_null_columns(df,limit = 0.7):
    return df[df.columns[df.isnull().mean() < limit]]

### Drop rows with percentage of nulls that surpasses the provided limit
def drop_null_rows(df,limit = 0.5):
    return df.loc[df.isnull().mean() < limit]

# %%

### Converts catergorical values to numerical
def category_encoding(df,column):

    copy = df.copy()
    encoder = preprocessing.LabelEncoder()
    encoder.fit(copy[column].unique())
    copy[column] = encoder.transform(copy[column])

    return copy

### Applyes categorical normalization to all non int columns
def full_df_category_enconding(df):
    
    cp = df.copy()
    columns = cp.columns
    
    for column in columns:
        if(cp[column].dtypes != 'int64'\
        and cp[column].dtypes != 'float64'\
        and  cp[column].dtypes != 'int32'\
        and  cp[column].dtypes != 'float32'):
            cp = category_encoding(cp,column)
    
    return cp



# %%
### Outlier removal using the z-score method
def remove_outliers_zscore(df,column,factor = 3):
    return df[(np.abs(stats.zscore(df[column])) < factor)]

### Outlier removel according to percentile
def remove_outliers_percentile(df,column):
    lower_bound = df[column].quantile(.95)
    upper_bound = df[column].quantile(.05)

    return df[(df[column] > lower_bound) & (df[column] < upper_bound)]
    

# %%
def get_auc(y_test,y_predicted,label=-1):
    fpr, tpr, _ = metrics.roc_curve(pd.to_numeric(y_test), pd.to_numeric(y_predicted),pos_label=label)    
    return metrics.auc(fpr, tpr)



# %%
