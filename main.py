import pandas as pd

data = {
    "name": ["John", "Carlos", "Pepe", "Martha"],
    "age": [18, 19, 42, 26],
    "gender": ["Male", "Male", "Male", "Female"],
}


def main():
    # create data frame
    df = pd.DataFrame(data)
    # print data frame
    print(df)

    # Read a CSV
    csv_df = pd.read_csv('data/test_data.csv').head()
    
    # print the dataframe
    print(csv_df)
    
   
if __name__ == "__main__":
    main()
