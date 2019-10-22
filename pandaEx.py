import pandas as pd

def question2():
    #turning "?" and "n.a" to NaN
    df = pd.read_csv("Automobile_data.csv", na_values={
        'price': ["?", "n.a"],
        'hoursepower': ["?", "n.a"],
        'average-mileage': ["?", "n.a"]
    })

    #replacing NaN with 0 in all columns
    df.fillna("0", inplace=True)

    #replace some text over something else
    df["text"] = df["text"].str.replace("hell", "beeee", case=None)

    #print(df.head(5))
    #print(df.tail(5))
    print(df.head(40))

#question2()

#find the most expensive car and its company name
def question3():
    df = pd.read_csv("Automobile_data.csv")
    df = df[['company', 'price']][df.price == df['price'].max()]

    print(df)
#question3()


def question4():
    df = pd.read_csv("Automobile_data.csv")

    car_manuf = df.groupby('company')
    get_company = car_manuf.get_group('toyota')

    print(get_company)
#question4()



