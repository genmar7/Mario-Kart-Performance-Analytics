"""
Analyzing Mario Kart world records to find most-used drivers, vehicles, tires, and gliders.

- Standardizes multicolored character names (e.g., Blue Yoshi -> Yoshi)
- Creates summary table with mode, count, and percentage for kart parts
- Exports cleaned data and summary table

Requirements: 
- pandas
- mk_world_records.csv with columns:
    - Track
    - Character  
    - Vehicle
    - Tires
    - Glider
"""
# %%
#load data
import pandas as pd
df = pd.read_csv('mk_world_records.csv')


#standardizing multicolored characters 
replacements = {}

def decolor(driver):
    for cust_char in df['Character'].unique():
        if driver in cust_char:
            replacements[cust_char] = driver

for driver in ["Yoshi", "Heavy Mii", "Shy Guy", "Birdo"]:
    decolor(driver)

df["Character"] = df["Character"].replace(replacements)


#create modes summary df
cols = ["Character", "Vehicle", "Tires", "Glider"]
mdf = []

for col in cols:
    mode = df[col].mode().iloc[0]
    count = df[col].value_counts().loc[mode]
    percent = round(count / len(df) * 100, 2)
    mdf.append({
        'Kart Part': col, 
        'Mode': mode, 
        'Count': count, 
        'Percentage': f'{percent}%'
    })

modes = pd.DataFrame(mdf)


#export
modes.to_csv("mk_wr_modes.csv", index=False)

print("Modes summary:\n", modes)
# %%
