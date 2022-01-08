import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

folder = "C:/private/src/python/experiment/DataAnalysysForHospitals/test/"
pd.set_option('display.max_columns', 8)
general = pd.DataFrame(pd.read_csv(folder + 'general.csv'))
prenatal = pd.DataFrame(pd.read_csv(folder + 'prenatal.csv'))
sports = pd.DataFrame(pd.read_csv(folder + 'sports.csv'))

prenatal = prenatal.rename(columns={'HOSPITAL':'hospital',	'Sex':'gender'})
sports = sports.rename(columns={'Hospital':'hospital',	'Male/female':'gender'})
df = pd.concat([general, prenatal, sports], ignore_index=True)
df = df.drop(columns='Unnamed: 0')
df.dropna(axis=0, how='all', inplace=True)
df.gender.replace('male', 'm', inplace=True)
df.gender.replace('female', 'f', inplace=True)
df.gender.replace('man', 'm', inplace=True)
df.gender.replace('woman', 'f', inplace=True)
df['gender'].fillna('f', inplace=True)
df['bmi'].fillna(0, inplace=True)
df['diagnosis'].fillna(0, inplace=True)
df['blood_test'].fillna(0, inplace=True)
df['ecg'].fillna(0, inplace=True)
df['ultrasound'].fillna(0, inplace=True)
df['mri'].fillna(0, inplace=True)
df['xray'].fillna(0, inplace=True)
df['children'].fillna(0, inplace=True)
df['months'].fillna(0, inplace=True)

df.plot(y='age', kind='hist', bins=[0, 15, 35, 55, 70, 80], grid=True)
# plt.show()
df.diagnosis.value_counts().plot.pie()
# plt.show()
sns.catplot(x='hospital', y='height', data=df, kind='violin')
# plt.show()

ans1 = '15-35'
ans2 = 'pregnancy'
ans3 = 'because athleates are taller than non athleates.'

print(f'The answer to the 1st question: {ans1}')
print(f'The answer to the 2nd question: {ans2}')
print(f'The answer to the 3rd question: {ans3}')

pass