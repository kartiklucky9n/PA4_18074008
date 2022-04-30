from tests import *

# Value of parameters
a,b,c=10007,25247,40639

# BlumBlumShub Implementation random number generator class
class BBS:
  # Constructor of class BBS to initialize the parameters of BBS Generator
  def __init__(self,a,b,c):
    # a and b are two large prime number leaving remainder 3 when divided by 4
    # c is chosen to be relatively prime to a and b
    self.a=a    
    self.b=b
    # Calculate m = a x b
    self.m=a*b
    # Calculate X_0 = (c^2)mod(m)
    self.x=(c*c)%(self.m)
  
  # Function to generate one random bit
  def get_next_one_random_bit(self):
    # Calculate X[i] =  (X[i-1] ^ 2)mod(n)
    self.x=(self.x*self.x)%(self.m)
    # Calculate B[i] = X[i] mod 2, givin 0,1 as random value
    random_bit= (self.x%2)
    return random_bit

  # Function to generate num random bits
  def get_next_num_random_bits(self,num):
    randomized_bits=[]
    for i in range(num):
      # generate one random bit and append it to the list of random bits
      Bi=self.get_next_one_random_bit()
      randomized_bits.append(Bi)
    return randomized_bits


# Generate and print random bits
bbs=BBS(a,b,c)
random_bits=bbs.get_next_num_random_bits(100)
print("Random bits genrated are:", random_bits, end="\n\n")

# Apply freuency test
test_of_frequency(random_bits)

# Apply runs test
test_of_runs(random_bits)


