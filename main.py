import pandas as pd

# Load the dataset
df = pd.read_csv('./data.csv')

# Convert all values in the 'gender' column to lowercase to ensure consistency (e.g., 'Male' → 'male')
df["Gender"] = df["Gender"].str.lower()

# Clean column names: remove leading/trailing spaces, convert to lowercase, and replace spaces with underscores
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')

# remove duplicates
df.drop_duplicates(inplace=True)

# Convert the 'age' column to integer type to ensure correct data type for numerical analysis
df["age"] = df["age"].astype(int)

# Save the cleaned DataFrame to a new CSV file without including the index column
df.to_csv('final-csv.csv', index=False)
print(df)
