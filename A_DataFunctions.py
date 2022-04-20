# 
from A_Functions import *

# Membuat fungsi max
def max_length(data,kolom):
    max = length_manual(data[0][kolom])
    for i in range(length_manual(data)):
        if length_manual(data[i][kolom])> max:
            max = length_manual(data[i][kolom])
    return max