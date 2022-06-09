import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
#import matplotlib.marker as marker
import numpy as ny
import matplotlib.pyplot as plt

po_df = pd.read_csv(('data/po.csv'),parse_dates=['Order Date', 'Shipment Date'])
po_df.head()

po_df= po_df[['Order Date', 'Order ID', 'Carrier Name & Tracking Number', 'Order Status','Subtotal','Tax Charged',
              'Shipping Charge','Total Charged']]
po_df.head()

po_df.columns = po_df.columns.str.replace(' ', '')  # overwrtting the columns

po_df = po_df.rename(
    columns={
        'CarrierName&TrackingNumber': 'Carrier',

    }
)
po_df.head()

# counting the Nan occurences
po_df.isna().sum()
po_df = po_df.rename(
    columns={

        'CarrierName&TrackingNumber': 'Carrier'

    }
)
po_df.Carrier=po_df.Carrier.str.split('(').str[0]
po_df['TotalCharged'] = po_df['TotalCharged'].str.replace('$','')
po_df.head()

po_df['QUARTER'] = pd.PeriodIndex(po_df['OrderDate'], freq='Q')
#Exercise greather 10
po_df['TotalCharged'] = po_df['TotalCharged'].astype(float)
#o=po_df.loc[po_df['TotalCharged'] > 10].count()

print((po_df['TotalCharged'] >10).count())
df1=po_df[po_df['TotalCharged']>10]
df1.shape[0]

df_bc=po_df.loc[(po_df['year'] == 2019 ), 'TotalCharged'].sum()
df_bc

df_20=po_df.loc[(po_df['year'] == 2020 ), 'TotalCharged'].sum()
df_20

df_21=po_df.loc[(po_df['year'] == 2021 ), 'TotalCharged'].sum()
df_21

df_c=df_20+df_21
df_c

#Hist graph
po_df['TotalCharged'].plot.hist(title='Purchase by year ')


#Scatter
x=po_df['TotalCharged']
y=po_df['year']
plt.scatter(x,y)
plt.xlabel('year')
plt.ylabel('TotalCharged')



#total charged
df_year=po_df.groupby('year').sum()
df_year=df_year.astype({'TotalCharged':'float'})
df_year






