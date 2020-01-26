import pandas as pd
import numpy as np
import timeit

mysetup = ""

mycode2 = ''' 
import pandas as pd
import numpy as np
t = pd.Series(np.random.randint(0, 1000, 100000000))
summary = np.sum(t)
'''

print(timeit.timeit(setup=mysetup, stmt=mycode2, number=3))


mycode = ''' 
import pandas as pd
import numpy as np
s = pd.Series(np.random.randint(0, 1000, 100000000))
summary = 0
for item in s:
    summary+=item
'''

print(timeit.timeit(setup=mysetup, stmt=mycode, number=3))

