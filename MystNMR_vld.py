def to_corr(peak_list):

    to_corr  = any(item in ['D', 'EF', 'G'] for item in peak_list)

    return to_corr

def to_pinv(peak_list, prod_list):

    if len(peak_list) == len(prod_list):

        to_pinv = False
    
    else:

        to_pinv = True
    
    return to_pinv

def is_ratio_vld(all_ratio):

    all_ratio_vld = True

    for a, ratio in enumerate(all_ratio):

        if ratio > 1 or ratio < 0:
            all_ratio_vld = False        

    return all_ratio_vld


                



