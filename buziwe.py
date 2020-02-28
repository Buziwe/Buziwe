

import pandas as pd
import numpy as np
np.random.seed(12)
df = pd.DataFrame(np.random.randn(6, 4),
   index= list('abcdef'), columns= list('ABCD'))
                    