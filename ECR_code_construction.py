# Polar/RM Code Modification for reducing the error-coefficient #######################
#
# Copyright (c) 2021, Mohammad Rowshan
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without modification, 
# are permitted provided that:
# the source code retains the above copyright notice, and te redistribtuion condition.
# 
# Freely distributed for educational and research purposes
########################################################################################

def supp_bin(bnry):
	indices_of_1s = set()
	for x in range(len(bnry)): 
		if bnry[x]==1:
			indices_of_1s |= {x}
	return indices_of_1s

def supp(i):
	bnry = [x for x in list(bin(i).replace("0b", ""))]
	bnry.reverse()
	indices_of_1s = set()
	for x in range(len(bnry)): 
		if bnry[x]=='1':
			indices_of_1s |= {x}
	return indices_of_1s

def bitreversed(num: int, n) -> int:
  return int(''.join(reversed(bin(num)[2:].zfill(n))), 2)

def dec2bin(d, n):
	bnry = [int(x) for x in list(bin(d)[2:].zfill(n))]
	bnry.reverse()
	return bnry

def bin2dec(binary): 
	decimal = 0
	for i in range(len(binary)): 
		decimal = decimal + binary[i] * pow(2, i) 
	return decimal

def countOnes(num:int):
	ones = 0
	binary = bin(num)[2:]
	len_bin = len(binary)
	for i in range(len_bin):
		if binary[i]=='1':
			ones += 1
	return(ones)

def row_wt(N): #Retruens the weight of all the rows of G_N
	w = np.zeros(N, dtype=int)
	for i in range(N):
		w[i] = self.countOnes(i)
	return w

def min_row_wt(profile,N,n): #Returns the minimum weight
	w = row_wt(N)
	min_w = n
	for i in range(N):
		if profile[i] == 1 and w[i] < min_w:
			min_w = w[i]
	return min_w
	
def rows_wt(profile,wt,N,n): #Retruns the indices of all the rows with weight wt
	w = row_wt(N)
	rows = []
	for i in range(N):
		if profile[i] == 1 and w[i] == wt:
			rows.append(bitreversed(i, n))
	return rows

def rows_wt_indices(profile,wt,N): #Forming set B, Bc and W
  bitrev_indices = [bitreversed(j, n) for j in range(N)]
	w = row_wt(N)
	B = []
	Bc = []
	W = []
	profile = profile[bitrev_indices]
	for i in range(N):
		if profile[i] == 1 and w[i] == wt:
			B += [i]
		elif profile[i] == 0 and w[i] == wt:
			Bc += [i]
		elif profile[i] == 0 and w[i] > wt:
			W += [i]
	return B, Bc, W


def leftSW_add(index,N,n): #Forming set Ki
	supp_index = supp(index)
	supp_size = len(supp_index)
	Ki = n - supp_size
	N_1 = N - 1
	for x in supp_index:
		Ki += sum(dec2bin(N_1^index,n)[x+1:n]) 
	return Ki

def rightSW(index,N,n): #Forming set Dj
	supp_index = supp(index)
	Dj = 0 
	N_1 = N - 1
	zros = dec2bin(N_1^index,n)
	for x in supp_index:
		Dj += sum(zros[0:x]) 
	return Dj

def E_set(index,N,n): #Forming set Ej, backward rightswapping
	supp_index = supp(index)
	E = [index]
	N_1 = N - 1
	zros = dec2bin(N_1^index,n)
	index_bin = dec2bin(index,n)
	for x in supp_index:
		spaces, fliping = sum(zros[0:x]), list(supp_bin(zros[0:x]))
		for y in range(spaces-1,-1,-1):
			member_bin = copy.deepcopy(index_bin)
			member_bin[x] = 0
			member_bin[fliping[y]] = 1
			E += [bin2dec(member_bin)]
	return E


def modify_profile(profile,N,n):  #Set I >> Profile, N: code length, n : log2(N)
	bitrev_indices = [bitreversed(j, n) for j in range(N)]
	profile = profile[bitrev_indices]
	w_min = min_row_wt(profile,N,n)
	B, Bc, W = rows_wt_indices(profile,w_min,N)
	cnt_sw = 0
	while True:

		B_rsw_size = []
		for x in B:
			B_rsw_size += [rightSW(x,N,n)]
		if len(B_rsw_size)==0:
			break
		cand_to_freeze = B[::-1][B_rsw_size[::-1].index(max(B_rsw_size))]
			
		E = E_set(cand_to_freeze,N,n) #Right swap
		Bc_lsw_size = []
		paired = False
		B_diff_E =  set(B) - set(E)
		E_cap_B = (set(B) & set(E))- {cand_to_freeze}
		
		reduction = 2**leftSW_add(cand_to_freeze,N,n)
		for x in E_cap_B:
			reduction += 2**(leftSW_add(x,N,n)-1)
		E_cap_Bc = list(set(Bc) & set(E))
		if len(W)>0:
			cand_to_unfreeze = max(W)
			W.remove(cand_to_unfreeze)
			addition = 0
			paired = True
		elif len(E_cap_Bc)>0:
			for x in E_cap_Bc:
				Bc_lsw_size += [leftSW_add(x,N,n)]
			cand_to_unfreeze = E_cap_Bc[::-1][Bc_lsw_size[::-1].index(min(Bc_lsw_size))]
			addition = 2**(leftSW_add(cand_to_unfreeze,N,n)-1)
			if addition<reduction:
				Bc.remove(cand_to_unfreeze)
				paired = True
		elif len(Bc)>0: 
			for x in Bc:
				Bc_lsw_size += [leftSW_add(x,N,n)]
			cand_to_unfreeze = Bc[::-1][Bc_lsw_size[::-1].index(min(Bc_lsw_size))]
			addition = 2**(leftSW_add(cand_to_unfreeze,N,n))
			if addition<reduction:
				Bc.remove(cand_to_unfreeze)
				paired = True
		if paired == True and cnt_sw<3: #You can sepcify the max pi here, e.g., 3. By putting zero, you will avoid any code modifications.
			B.remove(cand_to_freeze)
			profile[cand_to_freeze] = 0
			profile[cand_to_unfreeze] = 1
		else:
			break
	profile = profile[bitrev_indices]        
	return profile
