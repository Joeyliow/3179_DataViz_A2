import pandas as pd

# Load your dataset
file_path = 'Stacked_Line_Dataset.csv'  # Replace with your actual file path
df = pd.read_csv(file_path)

# Group by Year, Country, and Crop_Type, then sum the Crop_Yield_MT_per_HA
df_grouped = df.groupby(['Year'])['Crop_Yield_MT_per_HA'].sum().reset_index()

# Save the grouped data to a new CSV file
output_file_path = 'Processed_Line_Dataset.csv'  # Replace with your desired output path
df_grouped.to_csv(output_file_path, index=False)

print(f"Processed data saved to: {output_file_path}")