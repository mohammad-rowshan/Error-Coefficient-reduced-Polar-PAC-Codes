This depository includes two parts:

1) The error coefficient (or the enumeration of minimum weight codeowrs) of Polar Codes in files err_coeff.m and err_coeff_full.m
   The MATLAB function err_coeff(I,N) that returns [d_min,A_dmin] where d_min is the minimum Hamming distance (or minimum weight of non-zero codewords) of the polar code with information ste I (constructed with an specific design SNR) and length N, and A_dmin is the number of minimum wieght codewords.
   
The difference between the two files is that the file err_coeff_full.m construct polar codes using density evolution with GA method and proviles set I to the enumerator function err_coeff(I,N) while err_coeff.m includes only the enumerator and you need to provide set I to the function.

2) The set of Python functions provided here are used to modify a polar code with index set I a.k.a $\mathcal{A}$ (here argument profile) and code length N and n=log2(N). 

Note that the main function is modify_profile. As these functions are taken from a user-defined Python class with modifications, if you find any minor error in it, please let me know.

The details of this procedure can be found on https://arxiv.org/abs/2111.08843

****** 
This implementation was added to rate_profile.py in the following repository titled list decoder for polar and PAC codes.
https://github.com/mohammad-rowshan/List-Decoder-for-Polar-and-PAC-Codes
******
