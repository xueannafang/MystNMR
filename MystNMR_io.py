import pandas as pd

def load_input_data(input_csv):

    ip_csv = pd.read_csv(input_csv)
    ip_df = pd.DataFrame(ip_csv)
    print(ip_df)

    return ip_df
