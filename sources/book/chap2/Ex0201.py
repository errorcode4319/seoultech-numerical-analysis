import math
import numpy as np 

def deposit(pay, rate, nyear):
    rt = 1.0 + rate 
    sn = int(pay * rt * (math.pow(rt, nyear) - 1.0) / rate)
    return sn 



if __name__ == "__main__":
    a = 100000
    r = 0.05
    n = 10
    print(f"납입액: {a}원")
    print(f"연이율: {r}")
    print(f"기간: {n}년")

    sn = deposit(a, r, n)
    print(f"원리합계: {sn}원")