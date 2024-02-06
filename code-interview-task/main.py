import numpy as np
import pandas as pd

data = np.random.randint(10, size=(2, 3)) 

df=pd.DataFrame(data)
file_name = 'codetask.xlsx'

print(df)

df.to_excel(file_name)


