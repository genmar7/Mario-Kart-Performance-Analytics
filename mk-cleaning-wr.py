
"""
Cleaning Mario Kart 8 Deluxe world record data 
(World Records as of January 31, 2026)

Reads wr_history.csv, cleans columns, fixes race speed values,
and writes mk_world_records.csv.

Requirements: Pandas
"""
# %%
# load data
df = pd.read_csv('wr_history.csv')

# drop unneeded columns & totals
df = df.drop(columns=['Unnamed: 0', 'Nation', 'Splits', 'Player','Date','Duration'])
df = df.iloc[:-3]

# rename & clean columns  
df = df.rename(columns={'Unnamed: 2':'Race Speed','Time+Video':'Time'})
df["Track"] = df["Track"].str.replace("150cc  200cc", "")

# fix 'race speed' pattern (handles tie at rows 57-58)
df.loc[:57, 'Race Speed'] = ['150cc', '200cc'] * (58//2)
df.loc[58:, 'Race Speed'] = ['200cc'] + ['150cc', '200cc'] * ((192-58)//2)

# export
df.to_csv("mk_world_records.csv", index=False)
