import pandas as pd

df_data=pd.read_csv("PP0006_MULTI.txt", on_bad_lines='skip', sep=' 1 +|0 0 |0 3 |5 3 ', header=None,  encoding = "ISO-8859-1")

df_data[['first', 'second']]=df_data[0].str.split('03APLN', expand=True)
df_data=df_data.drop(0, axis=1)
df_data=df_data.drop('first', axis=1)

df_data['second']=df_data['second'].apply(lambda x: x[2:-3])
df_data[['indeks', 'second']]=df_data['second'].str.split(' ',1, expand=True)
df_data['second']=df_data['second'].apply(lambda x: x.strip())
df_data=df_data.rename(columns={'second':'nazwa'})

df_data['cena']=df_data[1].apply(lambda x: x[:22])
df_data[1]=df_data[1].apply(lambda x: x.split(' ',1)[1].strip() if x[22]!='1' and x[22]!='2' else x.split(' ',1)[1].strip().split(' ',1)[1].strip())
df_data['ilosc_w_opakowaniu']=df_data[1].apply(lambda x: int(x[:5]))
df_data['grupa_rabatowa']=df_data[1].apply(lambda x: x[20:21])
df_data=df_data.drop(1,axis=1)

df_data['cena']=df_data['cena'].apply(lambda x: str(int(x)/100).replace('.',','))
df_data=df_data.reindex(columns=['indeks', 'nazwa', 'cena', 'ilosc_w_opakowaniu', 'grupa_rabatowa'])

df_data.to_csv('task_3_result.csv',index=False,sep="/")