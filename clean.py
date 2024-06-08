
import pandas as pd

input_file = 'Output.csv'
df = pd.read_csv(input_file)

print("Original DataFrame:")
print(df)

df_cleaned = df.dropna()
print("\nDataFrame after removing rows with at least one blank value:")

print(df_cleaned)
output_file = 'output_merged_cleaned.csv'
df_cleaned.to_csv(output_file, index=False)

print(f"\nCleaned DataFrame saved to {output_file}")


