This depository includes two parts:

1) The error coefficient of Polar Codes in files err_coeff.m and err_coeff_full.m
   The MATLAB function err_coeff(I,N) that returns [d_min,A_dmin] where d_min is the minimum Hamming distance (or minimum weight of non-zero codewords) of the polar code with information ste I (constructed with an specific design SNR) and length N, and A_dmin is the number of minimum wieght codewords.
   

2) The set of Python functions provided here are used to modify a polar code with index set I a.k.a $\mathcal{A}$ (here argument profile) and code length N and n=log2(N). 

Note that the main function is modify_profile. As these functions are taken from a user-defined Python class with modifications, if you find any minor error in it, please let me know.

The details of this procedure can be found on https://arxiv.org/abs/2111.08843

****** 
This implementation was added to rate_profile.py in the following repository titled list decoder for polar and PAC codes.
https://github.com/mohammad-rowshan/List-Decoder-for-Polar-and-PAC-Codes
******
