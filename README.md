# MystNMR
 NMR side product calculation

The aim of this project is to use quantitative ratios among integrals of possible product peaks to estimate the component of corresponding compounds in a reaction mixture.

## Working principles

The project was developed from a multi-step SN2 synthesis, whose extent of conversion is sensitive towards the reaction conditions (such as solvent, temperature and time).

<p>
 <img src=https://github.com/xueannafang/MystNMR/blob/main/fig/rxn_p3.png width=1000>
 </p>

For now we ignore potential side reaction that could lead by solvents. This case can lead to six combinations of products depending on the substituion occurs (S1) or not (S0), and the ester hydrolysised (E1) or not (E0). Our desired product is S3E0, where all substitution sites have been reacted and the ester remain unmodified.

<p>
 <img src=https://github.com/xueannafang/MystNMR/blob/main/fig/potential_sp.png width=1000>
 </p>

Ideally, the NMR of the desired product would follow:

<p>
 <img src=https://github.com/xueannafang/MystNMR/blob/main/fig/s3e0_nmr.png width=1000>
 </p>

However, in undesired cases we have a mixture of partially substituted products.

 A few practical issues were also noticed in this situation. In particular, the peaks in the aliphatic carbon region could overlap with water residue or unreacted substrates, given the high similarity between bromododecane and the dodecyl chain.

 Luckily, with nanospray mass spectroscopy we can get an idea about what are included there. The result says the mixture contains S3E0, S2E0, and S2E1.


 Now, assume each compound exists individually.

 The ratio of peak [A, B, C, D, E+F, G] would be:

 For S3E0: [3, 2, 6, 6, 54, 9];

 For S2E0: [3, 2, 4, 4, 36, 6];

 and for S2E1: [0, 2, 4, 4, 36, 6].

 
Let's set the concentration of S3E0, S2E0 and S2E1 as x, y, z, which together construct the coefficient matrix X.

X = [x, y, z]

The problem is now to find a linear combination of the NMR integral of each compound that adds up to our mixture integrals. (Note the E and F are combined due to significant overlap on spectrum.)

 The unreacted substrate has a distinguished peak on the proton NMR, which can serve as a reference and correct the integral of the rest of the product peaks (C, D, E, F, G) from the mixture spectrum before calculation starts.

<p>
 <img src=https://github.com/xueannafang/MystNMR/blob/main/fig/set_up_eq.png width=1000>
 </p>

 Because C, D, E, F, G are all contributed by the alkyl part, these rows are lienar combination of each other. Therefore, we only need one group to in the linear equation (otherwise the matrix has redundant rows).


The coefficient matrix is obtainable by solving this linear equation using the same method proposed by [SolvPred](https://github.com/xueannafang/hsp_toolkit_solv_pred_v_2.0).

<p>
 <img src=https://github.com/xueannafang/MystNMR/blob/main/fig/solv_x.png width=1000>
 </p>


 ## Run MystNMR

The input can be filled in the spreadsheet [here](https://github.com/xueannafang/MystNMR/blob/main/MystNMR_input_data.csv), where integrals of individual product needs to be filled in columns of peak labels.


Calculation can be done by running ```MystNMR_main.py``` (available [here](https://github.com/xueannafang/MystNMR/blob/main/MystNMR_main.py)) using Python.


The block at the beginning can be modified according to working compounds. Each row in the ```all_coeff_mat``` dictionary is the row vector of potential compounds in the mixture. Peaks to be involved in the linear equation need to be specified in ```peak_list``` variable. The input and output data file name needs to be updated in ```input_nmr_data``` and ```test_name``` variables.

```
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
```

The output will be saved after the calcultion is done.

- [Example.csv](https://github.com/xueannafang/MystNMR/blob/main/NMR_20230713.csv)


## Related project

- [MystMS](https://github.com/xueannafang/MystMS_SP2_20230506)
A side product prediction tool for MS analysis.

