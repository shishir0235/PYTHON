import pandas as pd
sales_data={
    'customer ID':[1,2,3],
    'product category':['electronics','clothing','home good'],
    'purchase amount':[50,20,75],
    'age':[40,70,20]
}

     # Create a dataframe of sales_data

df=pd.DataFrame(sales_data)

     # Descriptive Statistics

print("descriptive ststistics:")
print(df.describe())    // The describe() method returns description of the data in the DataFrame. 
print()

     # Data Visualisation (requires matplotlib or seaborn)

import matplotlib.pyplot as plt

    # Sales distribution by product category     

sales_by_category=df.groupby('product category')['purchase amount'].sum()
sales_by_category.plot(kind='bar',xlabel='Product Category',ylabel='Total Sales',title='Sales Distribution by Product Ctaegory')
plt.show()

    # Segmentation Analysis

print("segmentation analysis:")

    # Segment customers by age for simplicity

bins=[20,30,40]
labels=['20-30','31-40','41-50']
df['age group']=pd.cut(df['age'],bins=bins,labels=labels)
segment_counts=df['age group'].value_counts   //value_counts() method is a convenient way to count the number of occurrences of each unique value in a pandas Series or DataFrame column
print(segment_counts)