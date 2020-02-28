# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 13:34:57 2020

@author: 212560141
"""

import random

print(random.random())
import pandas as pd
import numpy as np
np.random.seed(1)
data3 = pd.DataFrame({"C" : np.random.random(),
                     "D"  : np.random.random(),
                     "A"  : np.random.random(),
                     "B"  : np.random.random(),
                     }, index=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15,16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32])