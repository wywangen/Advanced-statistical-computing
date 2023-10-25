import numpy as np
import pandas as pd

p1=np.load("estimated_p1.npy")
pi_list=np.load("estimated_pi.npy")
column_gender=np.load("column of gender.npy")

pd1 = pd.DataFrame({"height": column_gender[0], "expected gender":column_gender[1]})
pd1.to_csv("expected_gender.csv")