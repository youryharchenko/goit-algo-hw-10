# Обчислення визначенного інтеграла методом Монте-Карло

import random
import math

import pandas as pd

def main():
       
    S = math.pi / 2

    iters = 100000
    count = 0
    rs = []
    n_iter = []
    err = []
    for i in range(1, iters+1):
        x = random.uniform(-1, 1)
        y = random.uniform(0, 1)
        r = abs(math.sqrt(x**2+y**2))
  
        if r <= 1:
            count += 1
        
        if not i%2000:
            n_iter.append(i) 
            rs.append(2*count/i)
            err.append(abs(S-2*count/i))

    df = pd.DataFrame({
        "Ітерацій": n_iter,
        "Площа": rs,
        "Помилка": err   
    })

    print(df)
    