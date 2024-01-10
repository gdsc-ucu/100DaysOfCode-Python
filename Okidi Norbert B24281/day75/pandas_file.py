import pandas as pd
import numpy as np

original_df = pd.read_csv('dataset_file.csv')

# Generate additional data
bmi_categories_df = {
    'Index': range(1, 200),
    'BMI_Category': np.random.choice(['Normal', 'Overweight', 'Underweight', 'Obese'], size=199)  # Fix the typo here
}

additional_data_df = pd.DataFrame(bmi_categories_df)

# Merge the datasets based on the 'Index' column
merged_df = pd.merge(original_df, additional_data_df, on="Index")

merged_df.columns = merged_df.columns.str.replace('"', '').str.strip()
print("Merged Dataset:")
print(merged_df)
    
average_values_grouped_by_bmi = merged_df.groupby('BMI_Category').agg({
    'Height(Inches)': 'mean',
    'Weight(Pounds)': 'mean'
})

print("\nAverage Height and Weight by BMI Category:")
print(average_values_grouped_by_bmi)

