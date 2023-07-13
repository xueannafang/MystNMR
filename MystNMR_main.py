import MystNMR_io
import MystNMR_vld

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
