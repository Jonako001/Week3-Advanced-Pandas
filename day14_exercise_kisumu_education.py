"""
Day 15: Kisumu County Education - Attendance vs Infrastructure
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(15)

schools_base = ['Kisumu Boys High', 'Kisumu Girls', 'St Marys Ahero', 'Maseno School', 
                'Nyabondo Boys', 'Kisumu Day Secondary', 'Ahero Girls', 'Chulaimbo Boys',
                'Kisumu County Academy', 'Nyangori High', 'Lela Secondary', 'Sawagongo High']

attendance_data = []
for s in schools_base:
    attendance_data.append([s, round(np.random.uniform(68, 96),1), 'Kisumu'])
attendance_data.append(['Kisumu Boys High', 88.5, 'Kisumu']) # duplicate

df_attendance = pd.DataFrame(attendance_data, columns=['school', 'average_attendance_pct', 'county'])

infra_data = [
    ['Kisumu Boys High School', 18, 'Yes'],
    ['Kisumu Girls High', 16, 'Yes'],
    ["St Mary's Ahero", 10, 'No'],
    ['Maseno School', 22, 'Yes'],
    ['Nyabondo Boys', 12, 'No'],
    ['Kisumu Day Secondary', 14, 'Yes'],
    ['Ahero Girls', 11, 'No'],
    ['Chulaimbo Boys', 13, 'Yes'],
    ['Kisumu County Academy', 20, 'Yes'],
    ['Nyangori High', 15, 'Yes'],
    ['Lela Secondary', 9, 'No'],
    ['Sawagongo High', 19, 'Yes'],
]
df_infra = pd.DataFrame(infra_data, columns=['school_name', 'num_classrooms', 'water_access'])
df_infra.loc[5, 'num_classrooms'] = np.nan

print(f"BEFORE: Attendance {len(df_attendance)} rows, Infra {len(df_infra)} rows")

# --- CLEANING FIX ---
def clean_name(name):
    name = str(name).lower().strip()
    name = name.replace("'","").replace(".","")
    name = name.replace("  ", " ").replace("ahero"," ahero") # FIX for St MarysAhero typo
    name = name.replace(" high school","").replace(" high","").replace(" secondary","")
    name = name.strip()
    return name

df_attendance_clean = df_attendance.drop_duplicates(subset=['school'])
df_attendance_clean['school_key'] = df_attendance_clean['school'].apply(clean_name)
df_infra['school_key'] = df_infra['school_name'].apply(clean_name)

median_rooms = df_infra['num_classrooms'].median()
df_infra['num_classrooms'] = df_infra['num_classrooms'].fillna(median_rooms)

merged = pd.merge(df_attendance_clean, df_infra, on='school_key', how='inner')
print(f"AFTER: Merged {len(merged)} schools")

# --- FIXED LINE HERE - ADDED COMMA ---
print(merged[['school', 'school_name', 'average_attendance_pct', 'num_classrooms']].head())

correlation = merged['num_classrooms'].corr(merged['average_attendance_pct'])
print(f"\nCorrelation: {correlation:.2f}")

plt.figure(figsize=(8,5))
plt.scatter(merged['num_classrooms'], merged['average_attendance_pct'], s=80, alpha=0.7)
for i, row in merged.iterrows():
    plt.text(row['num_classrooms']+0.1, row['average_attendance_pct']+0.1, row['school'][:12], fontsize=7)
plt.title('Kisumu County: Attendance vs Number of Classrooms')
plt.xlabel('Number of Classrooms')
plt.ylabel('Average Attendance (%)')
plt.grid(alpha=0.3)
plt.tight_layout()
plt.savefig('kisumu_attendance_vs_classrooms.png', dpi=150)
print("Saved kisumu_attendance_vs_classrooms.png")