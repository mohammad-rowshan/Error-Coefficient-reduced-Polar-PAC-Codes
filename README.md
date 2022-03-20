The set of Python functions provided here are used to modify a polar code with index set I a.k.a $\mathcal{A}$ (here argument profile) and code length N and n=log2(N). 

Note that the main function is modify_profile. As these functions are taken from a user-defined Python class with modifications, if you find any minor error in it, please let me know.

The details of this procedure can be found on https://arxiv.org/abs/2111.08843

Moreover, there is a MATLAB function that returns the minmum Hamming weight d_min of a prolar code (defined with index set I) and the error coefficient (the total number of codewors minimum Hamming weight, A_dmin).

****** 
This implementation was added to rate_profile.py in the other repository titled list decoder for polar and PAC codes. Please see how it performs there.
https://github.com/mohammad-rowshan/List-Decoder-for-Polar-and-PAC-Codes
******
