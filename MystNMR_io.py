import pandas as pd
import numpy as np

def load_input_data(input_csv):

    ip_csv = pd.read_csv(input_csv)
    ip_df = pd.DataFrame(ip_csv)
    print(ip_df)
    ip_dict = ip_df.to_dict('records')
    print(ip_dict)

    return ip_df, ip_dict


def init_coeff_mat(all_coeff_mat, peak_list):

    coeff_mat_list = []

    for i, peak in enumerate(peak_list):
        crt_peak_coeff = all_coeff_mat[peak]
        coeff_mat_list.append(crt_peak_coeff)
    
    coeff_mat = np.array(coeff_mat_list)

    return coeff_mat

