import pandas as pd
df=pd.read_csv("retail_sales_dataset.csv")
df.drop_duplicates(inplace=True)
new_df=df.dropna()


import matplotlib.pyplot as plt

#1) TOP SELLING PRODUCTS:

tsp=new_df.groupby('Product Category')['Quantity'].sum().sort_values(ascending=False)
print('TOP SELLING PRODUCTS :',tsp)
print()


#2) MONTHLY SALES TREND :

new_df['Date']=pd.to_datetime (new_df['Date'],dayfirst = True)
new_df['month'] = new_df['Date'].dt.month
new_df['month_name'] = new_df['Date'].dt.strftime('%b')
mst=new_df.groupby(['month','month_name'])['Total Amount'].sum().sort_index()
mst.index = mst.index.get_level_values('month_name')
print('MONTHLY SALES TREND :',mst)
print()


#3) CATEGORY WISE REVENUE :

cwr = new_df.groupby('Product Category')['Total Amount'].sum().sort_values(ascending=False)
print('CATEGORY WISE REVENUE :',cwr)
print()


#4) HIGHEST SPENDING CUSTOMERS (TOP 5 CUSTOMERS) :

hsc = new_df.groupby('Customer ID')['Total Amount'].sum().reset_index()
hsc = hsc.sort_values(by = 'Total Amount',ascending = False)
hsc5 = hsc.head(5)
print('HIGHEST SPENDING CUSTOMERS(TOP 5) :',hsc5)
print()


#5) ORDERS BY CATEGORY :

obc = new_df['Product Category'].value_counts()
print('ORDERS BY CATEGORY :',obc)
print()


#6) OVERALL SALES :

os = new_df['Total Amount'].sum()
print('OVERALL  SALES :',os)
print(f"Total Sales : Rs{os}")
print()


#7) AVERAGE ORDER VALUE :

tr = new_df['Total Amount'].sum()
to = new_df.shape[0]
aov = tr/to
print('AVERAGE ORDERS VALUE :',aov)
print()


#8) GENDER BASED ANALYSIS :

gba = new_df.groupby('Gender')['Total Amount'].sum()
print('GENDER BASED ANALYSIS :',gba)
print()


#9) AGE GROUP ANALYSIS\SALES :

bins=[0,18,25,35,50,100]
labels=['0-18','18-25','25-35','35-50','50+']
new_df['Age_Group']=pd.cut(new_df['Age'],bins=bins,labels=labels)
ags= new_df.groupby('Age_Group')['Total Amount'].sum()
print ('AGE GROUP SALES :',ags)
print()


#)CHARTS :

#1)

plt.figure(figsize=(10,6))
tsp.plot(kind ='bar',color ='skyblue')
plt.title('TOP SELLING PRODUCTS')
plt.xlabel('Product')
plt.ylabel('Quantity')
plt.savefig("charts/top selling products_chart.png")
plt.show()


#2)

plt.figure(figsize=(10,6))
mst.plot(kind='line',color='red',linewidth = 3)
plt.title('MONTHLY SALES TREND')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.savefig("charts/monthly sales trend_chart.png")
plt.show()

#3)

plt.figure(figsize=(10,6))
cwr.plot(kind='bar',color='purple')
plt.title('CATEGORY WISE REVENUE')
plt.xlabel('Category')
plt.ylabel('Revenue')
plt.savefig("charts/category wise revenue_chart.png")
plt.show()

#4)

plt.figure(figsize=(10,6))
hsc5.plot(kind='bar',color='orange')
plt.title('HIGHEST SPENDING CUSTOMERS (TOP 5)')
plt.xlabel('Customer ID')
plt.ylabel('Amount')
plt.savefig("charts/highest spending customers_chart.png")
plt.show()

#5)

plt.figure(figsize=(10,6))
obc.plot(kind='bar',color='green')
plt.title('ORDERS BY CATEGORY')
plt.xlabel('Products')
plt.ylabel('Orders')
plt.savefig("charts/orders by category_chart.png")
plt.show()

#6)

plt.figure(figsize=(6,6))
plt.axis('equal')
gba.plot(kind='pie',autopct='%1.1f%%',color=['#4e79a7','#f28e2b'],shadow=True,startangle=90)
plt.title('GENDER BASED SALES')
plt.legend()
plt.savefig("charts/gender based sales_chart.png")
plt.show()

#7)

plt.figure(figsize=(10,6))
plt.bar(ags.index,ags.values)
plt.title('Sales by Age Group')
plt.xlabel('Age Group')
plt.ylabel('Sales')
plt.savefig("charts/sales by age group_chart.png")
plt.show()
































