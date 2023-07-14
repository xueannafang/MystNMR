import MystNMR_io
import MystNMR_vld
import MystNMR_calc

test_name = 'NMR_20230714.csv'

input_nmr_data = 'MystNMR_input_data.csv'


peak_list = ['A', 'B', 'C']
prod_list = ['S3E0', 'S2E0', 'S2E1']


all_coeff_mat = {
    'A' : [3, 3, 0],
    'B' : [2, 2, 2],
    'C' : [6, 4, 4],
    'D' : [6, 4, 4],
    'EF' : [54, 36, 36],
    'G' : [9, 6, 6]
}

to_corr = MystNMR_vld.to_corr(peak_list)
to_pinv = MystNMR_vld.to_pinv(peak_list, prod_list)
print(to_corr, to_pinv)



NMR_data_df, NMR_data_dict = MystNMR_io.load_input_data(input_nmr_data)

all_calc_rslt = []

for a, sample in enumerate(NMR_data_dict):

    

    sample_id = sample['sample_id']

    print('coeff_mat of ')
    print(sample_id)
    print(': ')
    sample_coeff_mat = MystNMR_io.init_coeff_mat(all_coeff_mat, peak_list) # construct coefficient peak
    print(sample_coeff_mat)
    mat_B = MystNMR_io.init_coeff_mat(sample, peak_list) # read corresponding integral
    print('mat_B: ')
    print(mat_B)

    if to_corr == True:

        pass # correct the sample_coeff_mat

    else:

        coeff_mat = sample_coeff_mat
    
    if to_pinv == True:

        pass # invoke the pinv calculation

    else:

        # invoke the dot calculation
        # prod_ratio = MystNMR_calc.dot_calc(coeff_mat, mat_B)

        stat_vld_rslt = MystNMR_calc.stat_ptb_dot_calc(coeff_mat, mat_B, 10000)
        rslt_mean, rslt_std = MystNMR_calc.rslt_with_error(stat_vld_rslt)
        print(rslt_mean, rslt_std)
        updt_sample_entry = MystNMR_io.write_prod_stat_info(sample, prod_list, rslt_mean, rslt_std)
    

    all_calc_rslt.append(updt_sample_entry)


all_calc_rslt_df = MystNMR_io.list2df(all_calc_rslt)

all_calc_rslt_df.to_csv(test_name)


        # MystNMR_io.decent_ratio(prod_list, prod_ratio)