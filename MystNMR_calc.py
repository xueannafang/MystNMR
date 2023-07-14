import numpy as np
import MystNMR_vld

def corr_brak(brak_alpha):

    D_rm = brak_alpha
    EF_rm = brak_alpha * 9
    G_rm = brak_alpha * 1.5

    return D_rm, EF_rm, G_rm

def pinv_coeff(coeff_mat):

    coeff_pinv = np.linalg.pinv(coeff_mat)

    return coeff_pinv

def inv_coeff(coeff_mat):

    coeff_inv = np.linalg.inv(coeff_mat)

    return coeff_inv

def ptb_coeff_inv(coeff_inv):

    ptb_on_inv = np.random.normal(0, 0.1, coeff_inv.T.shape)
    err_on_inv = np.dot(coeff_inv, ptb_on_inv)
    ptbted_inv = coeff_inv + err_on_inv

    return ptbted_inv

def norm_coeff(ndarray):
    
    sum_array = np.sum(ndarray)
    norm_list = []
    
    for i, item in enumerate(ndarray):
        norm_item = item/sum_array
        norm_list.append(norm_item)
    
    norm_array = np.array(norm_list)
    
    return norm_array

def dot_result(ptbted_inv, mat_B):

    before_norm = np.dot(ptbted_inv, mat_B)
    after_norm = norm_coeff(before_norm)

    return after_norm

def dot_calc(coeff_inv, mat_B):

    ptbted_inv_mat = ptb_coeff_inv(coeff_inv)
    prod_ratio_mat = dot_result(ptbted_inv_mat, mat_B)

    return prod_ratio_mat


def stat_ptb_dot_calc(coeff_mat, mat_B, rpt_time = 10):

    vld_rslt = []

    coeff_inv = inv_coeff(coeff_mat)

    for i in range(rpt_time):

        prod_ratio_mat = dot_calc(coeff_inv, mat_B)
        all_ratio_vld = MystNMR_vld.is_ratio_vld(prod_ratio_mat)
        
        if all_ratio_vld is True:
            vld_rslt.append(prod_ratio_mat)
        
    if len(vld_rslt) > 0:
        pass
        # print(vld_rslt)
    
    else:
        print('no valid results.')
    
    return vld_rslt

def rslt_with_error(vld_rslt):

    vld_rslt_list = list(np.array(vld_rslt).T)
    # print(vld_rslt_list)

    vld_rslt_mean = []
    vld_rslt_std = []

    for each, prod_array in enumerate(vld_rslt_list):

        vld_mean = np.mean(prod_array)
        vld_std = np.std(prod_array)

        vld_rslt_mean.append(vld_mean)
        vld_rslt_std.append(vld_std)


    # vld_rslt_mean = np.mean(vld_rslt_array)
    # vld_rslt_std = np.std(vld_rslt_array)

    return vld_rslt_mean, vld_rslt_std

        


