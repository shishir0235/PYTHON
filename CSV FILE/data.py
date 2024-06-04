import pandas as pd
df=pd.read_csv(r"C:\Users\Shishir Ranjan\Downloads\industry.csv")  // r is for unicode error and it treats backslashes as literal characters and prevents python from interpreting them as escape sequence 
print(df)