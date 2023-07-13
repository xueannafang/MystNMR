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

def decent_ratio(prod_list, prod_ratio_array):

    all_prod_info_list = []

    for i, prod in enumerate(prod_list):
        prod_info = {}
        prod_info['name'] = prod
        prod_info['ratio'] = prod_ratio_array[i]
        all_prod_info_list.append(prod_info)
    
    print(all_prod_info_list)


def write_prod_stat_info(old_dict, prod_list, mean_list, std_list):

    new_dict = old_dict

    for i, prod in enumerate(prod_list):
        mean_name = str(prod) + "_mean"
        std_name = str(prod) + "_std"
        new_dict[mean_name] = mean_list[i]
        new_dict[std_name] = std_list[i]
    
    return new_dict

def list2df(old_list):
    df = pd.DataFrame(old_list)
    return df