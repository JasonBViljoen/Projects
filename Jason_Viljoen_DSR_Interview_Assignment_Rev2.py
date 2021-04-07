#PALINDROME DATA 
#DATA SCIENCE RESIDENCY INTERVIEW ASSIGNMENT
#by Jason Viljoen

#=============================================================================
#import libraries
import pandas as pd
#=============================================================================
#import data
df = pd.read_excel("pone.0212445.s004.xlsx")#import the dataset
df.columns = df.iloc[0]#rename columns to correct headings
df = df.iloc[1:]#remove the first row, as this is duplicate column headings

# #=============================================================================
#Task 2a)
Survey_Estimate = df[df['Estimate'] == 'Survey'] #only keep those rows with survey estimates
NoPLHIV_Survey_Total = Survey_Estimate['NoPLHIV'].sum() #calculate number of people living with HIV according to the Survey estimate
print('\nTotal number of people living with HIV according to the Survey Estimate:',NoPLHIV_Survey_Total)

#=============================================================================
#Task 2b)
Xhariep_df = df[df['District'] == 'Xhariep'] #Keep only Xhariep's data
Xhariep_mean = Xhariep_df['NoPLHIV'].mean() #Calculate the average of the two estimates for Xhariep
print('\nAverage NoPLHIV of the two estimates for Xhariep:',Xhariep_mean)

#=============================================================================
#Task 2c)
df['NoPNLHIV'] = (df['NoPLHIV']/(df['Prevalence_%']/100))-df['NoPLHIV'] #add column with number of people not living with HIV
print('\n')
print('Number of people not living with HIV for each row:\n')
print(df['NoPNLHIV'])

#=============================================================================
#Task 2d)
City_Districts = df[df['District'].str.contains("City")] #keep only districts with 'city' in the title
Metro_Districts = df[df['District'].str.contains("Metro")] #keep only districts with 'metro' in the title
City_and_Metro_Districts = pd.concat([City_Districts, Metro_Districts], axis=0) #combine the two dataframes into one

Survey_Estimate_City_Metro = City_and_Metro_Districts[City_and_Metro_Districts['Estimate'] == 'Survey'] #only keep those rows with survey estimates
NoPLHIV_Survey_Total_City_Metro = Survey_Estimate_City_Metro['NoPLHIV'].sum() #calculate number of people living with HIV in cities/metros according to the Survey estimate
print('\nTotal NoPLHIV in all the cities (Survey Estimate):',NoPLHIV_Survey_Total_City_Metro)

Fay_Heriott_Estimate_City_Metro = City_and_Metro_Districts[City_and_Metro_Districts['Estimate'] == 'Fay-Heriott'] #only keep those rows with Fay-Heriott estimates
NoPLHIV_Fay_Heriott_Total_City_Metro = Fay_Heriott_Estimate_City_Metro['NoPLHIV'].sum() #calculate number of people living with HIV in cities/metros according to the Fay-Heriott estimate
print('\nTotal NoPLHIV in all the cities (Fay-Heriott Estimate):',NoPLHIV_Fay_Heriott_Total_City_Metro)

#=============================================================================
#Task 3)
df.to_csv('New_Data.csv',index=False) #export original data with extra column to .csv file

#END
#Time taken to complete assignment: ±2.5 hours

