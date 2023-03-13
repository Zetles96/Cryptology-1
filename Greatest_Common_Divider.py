# -*- coding: utf-8 -*-
"""
Created on Wed Dec  1 09:10:21 2021

@author: madsn
"""
# imported libraries numpy because reason pandas because looks nice
import numpy as np
import pandas as pd


# Euclidisk extended allegoritme
# made by Mads Legard Nielsen
# input the a and b from you assignment thingy
# Euclidisk extended allegoritme
# made by Mads Legard Nielsen
def euclidall(a, b):
    a = np.abs(a)
    b = np.abs(b)
    i = [-1, 0]
    r_i = np.array([a, b], dtype=np.int64)
    q_i = np.array([0, 0], dtype=np.int64)
    s_i = np.array([1, 0], dtype=np.int64)
    t_i = np.array([0, 1], dtype=np.int64)
    while b != 0:
        r = a % b
        q = int(a / b)
        q_i = np.append(q_i, q)
        s = s_i[-2] - q_i[-1] * s_i[-1]
        t = t_i[-2] - q_i[-1] * t_i[-1]
        a = b
        b = r
        i = np.append(i, (i[-1]) + 1)
        r_i = np.append(r_i, r)
        s_i = np.append(s_i, s)
        t_i = np.append(t_i, t)
        d = {"ri": r_i, "qi": q_i, "si": s_i, "ti": t_i}
        df = pd.DataFrame(data=d, index=i)
        # latex = df.to_latex()
    return df


print(euclidall(65537,4294967317))
