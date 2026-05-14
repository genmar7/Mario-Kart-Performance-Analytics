"""
Analyzing Mario Kart world records to find most-used drivers, vehicles, tires, and gliders.

- Standardizes multicolored character names (e.g., Blue Yoshi -> Yoshi)
- Creates summary table with mode, count, and percentage for kart parts
- Exports cleaned data and summary table

Requirements: pandas
"""
# %%
import pandas as pd
df = pd.read_csv('mk_world_records.csv')


#standardizing multicolored characters 
#(characters that can be customized as  different colors but have the same stats)
replacements = {}

def decolor(driver):
    for cust_char in df['Character'].unique():
        if driver in cust_char:
            replacements[cust_char] = driver

decolor('Yoshi')
decolor('Heavy Mii')
decolor('Shy Guy')
decolor('Birdo')

df["Character"] = df["Character"].replace(replacements)


#create a new dataframe with modes, including the count and percentages
cols = ["Character", "Vehicle", "Tires", "Glider"]

mdf = []
for col in cols:
    mode = df[col].mode().iloc[0]
    count = df[col].value_counts().loc[mode]
    percent = round(count / len(df) * 100, 2)
    mdf.append({'Kart Part': col, 'Mode': mode, 'Count': count, 'Percentage': f'{percent}%'})

modes = pd.DataFrame(mdf)

#export
modes.to_csv("mk_wr+modes.csv", index=False)
# %%
