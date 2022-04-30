import math

def test_of_frequency(nums_array):
  s=0
  for x in nums_array:
    if x==1: s+=1 #add 1 to s for every 1 bit in list of numbers
    else: s-=1  #subtract 1 to s for every 0 bit in list of numbers

  n= len(nums_array) # number of pseudo random numbers generated
  sqrt_n = math.sqrt(n)
  s_observed= abs(s)/sqrt_n # calculate absolute value of observed sum divided by square root of n

  p_value= math.erfc(s_observed/math.sqrt(2)) # calculate P-value using error function

  if p_value<0.01: 
    print(f"The sequence does not appear random in FREQUENCY TEST since p-value : {p_value} < 0.01.") # if P-value if less than 0.01 then sequence is not random
  else:
    print(f"The sequence appears random FREQUENCY TEST since p-value : {p_value} >= 0.01.") # if P-value if more than 0.01 then sequence is random

def test_of_runs(nums_array):
  num = len(nums_array)  # size of the array of of pseudo random numbers

  # Calculate the number of runs in the list
  rhuns=0 
  for i in range(num-1):
    if nums_array[i]!=nums_array[i+1]: rhuns+=1

  # Calculate the fraction of 1's in the bit list
  frac=0
  for x in nums_array: 
    if x==1: frac+=1
  frac/=num

  numrtr= abs(rhuns-2*num*frac*(1-frac))  # |runs-2Nfrac(1-frac)|
  denotr= 2*math.sqrt(2*num)*frac*(1-frac) # (2*sqrt(2N)*frac(1-frac))

  p_value= math.erfc(numrtr/denotr) # p_value = erfc(|V_N(obs)-2Nπ(1-π)|/(2*sqrt(2N)*π(1-π)))

  if p_value<0.01: 
    print(f"The sequence does not appear random in RUNS TEST since p-value : {p_value} < 0.01. ") # if P-value if less than 0.01 then sequence is not random
  else:
    print(f"The sequence appears random in RUNS TEST since p-value : {p_value} >= 0.01. ") # if P-value if more than 0.01 then sequence is random