#https://pynative.com/python-pandas-exercise/

import pandas as pd
df = pd.read_csv("Automobile_data.csv")

def data_cleaning(df):
    # view unique values and counts on a specific column
    result = df["body-style"].value_counts()
    print(result)

    df.columns = [col.lower() for col in df]
    print(df.columns)
    print(df[["company"]].info())

    #Find total number of missing values(nulls) in the file:
    print(df.isnull().sum())

    # turning "?" and "n.a" to NaN
    df = pd.read_csv("Automobile_data.csv", na_values={
        'price': ["?", "n.a"],
        'hoursepower': ["?", "n.a"],
        'average-mileage': ["?", "n.a"]
    })

    # replacing NaN with the 0 in all columns
    df.fillna(0, inplace=True)

    # fillna with the price's mean in specific columns
    # df[['price']] = df[['price']].fillna(df[['price']].mean())
    df[['price']] = df[['price']].replace(0, df[['price']].mean())

    # replace some text over something else
    df["text"] = df["text"].str.replace("hell", "beeee", case=None)

    # df.to_csv("new_Automobile_data.csv")
    # print(df.head(5))
    # print(df.tail(5))
    print(df[['company', 'price', 'horsepower']].head(40))
    print(df.isnull().sum())
data_cleaning(df)


###--------------------------------------------------------------------------
def speed_function(x):
    df = pd.read_csv("Automobile_data.csv")
    if x >= 110:
        return "Fast"
    else:
        return "Slow"
#The .apply() method passes every value in the horsepower column through
#the speed_function and the returns a new Series. This Series is then
#assigned to a new column called Speed.
def print_speed():
    df["Speed"] = df["horsepower"].apply(speed_function)
    print(df.head(10))
#print_speed()
###--------------------------------------------------------------------------

###--------------------------------------------------------------------------
#Imbedding matplotlib in pandas to show graphs
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size': 10, 'figure.figsize': (10, 8)})
#df.plot(kind='scatter', x='horsepower', y ='price', title="Price vs Speed");
#df['price'].plot(kind="box")
#df.boxplot(column='horsepower', by='company')
#plt.show()
###--------------------------------------------------------------------------

#find the most expensive car and its company name
def question3():
    df = pd.read_csv("Automobile_data.csv")
    #Retrieve the max value in the sub-dict
    fetch = df[['company', 'price']][df.price == df['price'].max()]

    print(fetch)
#question3()

def question4():
    df = pd.read_csv("Automobile_data.csv")

    car_manuf = df.groupby('company')
    get_company = car_manuf.get_group('toyota')
    #print(get_company)

    #or----------------------------------------------------
    #Think of this way...SELECT * FROM df WHERE df[company] = toyota
    #fetch = df[df['company'] == "toyota"]
    #example...
    fetch = df[
        (df['price'] >= 5000) & (df['price'] <= 7000) &
        (df['company'] == "toyota")
    ]
    print(fetch)
#question4()

def question5():
    print(df['company'].value_counts())
#question5()
def question6():
    car_company_df = df.groupby('company')
    get_max_price_df = car_company_df['company', 'price'].max()
    print(get_max_price_df)
#question6()
