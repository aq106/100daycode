import pandas as pd
#creating pd df...
df = pd.DataFrame({

    'brand': ['Yum Yum', 'Yum Yum', 'Indomie', 'Indomie', 'Indomie'],

    'style': ['cup', 'cup', 'cup', 'pack', 'pack'],

    'rating': [4, 4, 3.5, 15, 5]

})
#from postgre rds cluster... = pd.read_sql("sql",con=psycopg2 conn works...) = awswrangler = sqlalchemy engine for write...
#https://www.geeksforgeeks.org/different-ways-to-create-pandas-dataframe/ = parsing as data_dict or data/cols...)
print(df)

#iterating pandas df...and updating
df.at[2,'style']="new style"
for index,row in df.iterrows():
    print(index,row['style'],end=";")

#removing dupicates...
i=0
for dup in df.duplicated(subset=['brand']):
    if dup is True:
        df.at[i,'brand']=df.at[i,'brand']+str(i)
    i+=1
df['rating']='5'
df['rating'][df['style']=='pack']='1'
df['rating'][(df['style']=='cup') & (df['brand']=='Indomie')]='2'
print(df)
