import pandas as pd

# Adjust path if needed – based on your folder structure
female_path = 'data/vocadiab/vocadiab_females_dataset.pkl'
male_path = 'data/vocadiab/vocadiab_males_dataset.pkl'

female_data = pd.read_pickle(female_path)
male_data = pd.read_pickle(male_path)

print("Female data shape:", female_data.shape)
print(female_data.head())

print("Male data shape:", male_data.shape)
print(male_data.head())
