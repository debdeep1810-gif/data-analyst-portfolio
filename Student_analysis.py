import pandas as pd

df = pd.read_csv(r"D:\DEBDEEP SARKAR\HERITAGE ENGINEERING\6th Semester\Internships and Placements\Student_analysis.csv")

print(df.head())      # to verify file loaded
print(df.corr(numeric_only=True))
