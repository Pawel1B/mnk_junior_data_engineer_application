import pandas as pd


df_data=pd.read_csv("data.csv", on_bad_lines='skip', sep='\t')
df_prices=pd.read_csv("prices.csv", on_bad_lines='skip', sep='\t')
df_quantity=pd.read_csv("quantity.csv", on_bad_lines='skip', sep='\t', header=None, names=['part_number', 'quantity'])
df_prices=df_prices.dropna()


df_data=df_data.drop_duplicates()
df_prices=df_prices.drop_duplicates()

df_prices=df_prices[df_prices['price'].apply(lambda x: float(x.replace(',','.'))>0.0)]
df_quantity=df_quantity[df_quantity['quantity'].apply(lambda x: x=='>10' or int(x)>0)]

first_combined=pd.merge(df_prices, df_quantity, on='part_number', how='right')
combined=first_combined.merge(df_data, on='part_number', how='left')

combined=combined.dropna(subset=['price', 'quantity'])

combined=combined[['part_number', 'manufacturer', 'price', 'quantity']]
combined.to_csv('task_1_result.csv',index=False,sep="\t")

def provide_report(dataframe):
    values=dict(dataframe['manufacturer'].value_counts())
    output_raport=""
    for key in values.keys():
        output_raport+=f'{key} - {values[key]} rows,\n'
    with open('report.txt', "w", encoding="utf-8") as f:
        f.write(output_raport)
provide_report(combined)