#dissertation 

from pandas_profiling import ProfileReport
import pandas as pd
df = pd.read_excel("Data Uni Dissertation.xlsx")
report = ProfileReport(df)
report.to_file(output_file= "report.html")

