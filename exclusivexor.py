# Implementation of Exclusive OR Generator class
from tests import test_of_frequency, test_of_runs

# 127 length seed bit sequence
bit_sequence =  [0,0,0,1,0,1,1,0,1,1,0,1,1,0,0,1,0,0,0,1,\
                 0,1,1,1,1,0,0,1,0,0,1,0,1,0,0,1,1,0,1,1,\
                 1,0,1,1,0,1,0,0,0,1,0,0,0,0,0,0,1,0,1,0,\
                 1,1,1,1,1,1,1,0,1,0,1,0,0,1,0,0,0,0,1,0,\
                 1,0,1,1,0,1,1,0,0,0,0,0,0,0,0,0,0,1,0,0,\
                 1,1,0,0,0,0,1,0,1,1,1,0,0,1,1,1,1,1,1,1,1,1,0,0,1,1,1]

class EXclusiveORGenerator:
  def __init__(self, bit_sequence):
    # bit sequence is a 127-bit long seed 
    self.bs=bit_sequence
    # Number of bits in the bit sequence
    self.num=len(bit_sequence)
  
  # Function to generate num random bits
  def give_next_num_random_bits(self,num):
    random_bits=[]
    for i in range(num):
      # in the list of random bots one bit is genrated and appended
      Bi=self.give_next_one_random_bit()
      random_bits.append(Bi)
    return random_bits
  
  # Function to generate one random bit
  def give_next_one_random_bit(self):
    # Calculate X[i] = X[i-127] XOR X[i-1] 
    random_bit= (self.bs[self.num-127]^self.bs[self.num-1])
    # The next bit is appended to the list of bit sequence
    self.bs.append(random_bit)
    # The number of bits are incremented
    self.num+=1
    return random_bit

  



# Generate and print random bits
eog=EXclusiveORGenerator(bit_sequence)
random_bits=eog.give_next_num_random_bits(100)
print("random bits genrated are:", random_bits, end="\n\n")

# Apply freuency test
test_of_frequency(random_bits)

# Apply runs test
test_of_runs(random_bits) 