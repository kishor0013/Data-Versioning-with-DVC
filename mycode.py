import pandas as pd
import os

data={
    'name':['abc','xyz','pqr'],
    'age':[10,20,30],
    'gender':['M','F','M']
}

df=pd.DataFrame(data)

#adding new row of data for data version 2
new_row={'name':'ghi','age':40,'gender':'F'}
df.loc[len(df.index)]=new_row

data_dir='data'
os.makedirs(data_dir,exist_ok=True)
filepath=os.path.join(data_dir,'mydata.csv')
df.to_csv(filepath,index=False)
print(f"Data saved to {filepath}")