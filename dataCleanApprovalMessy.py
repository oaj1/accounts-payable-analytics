import pandas as pd

#now lets read in the files
dfApprovalMessy = pd.read_excel('Approvals_Dataset_Messy.xlsx')

"""
Data Cleaning Objectives

1. Identify missing values. (/)
2. Remove duplicate records. (/)
3. Remove unnecessary whitespace (/).
4. Standardize capitalization (up next).
5. Standardize categorical values.
6. Correct inconsistent data types.
7. Standardize currency formatting.
8. Standardize date formats.
9. Validate relationships between datasets.
10. Identify logical date inconsistencies.
11. Investigate financial discrepancies.
"""


#Okay, first step, lets identify missing values
print(dfApprovalMessy.isnull().sum())

#RejectionReason column has 30 empty values
#There are 31 rows, most are approved, however, two rows are rejected
#one row states for a potential duplicate, the other has no rejection reason (likely should have one)

#Decision date and approverID show null count of one
#lets take a look at approverID and decision date with null values
print(dfApprovalMessy[dfApprovalMessy['ApproverID'].isnull() | dfApprovalMessy['DecisionDate'].isnull()])


#From result we see approvalID is ID 27.
#however, it is pending, so decision date should be null
#for missing approverID, after flagging, we discovered its ID
#I will now fill in the missing approverID with the discovered ID
dfApprovalMessy.loc[dfApprovalMessy['ApproverID'].isnull(), 'ApproverID'] = 'EMP-2103'
dfApprovalMessy.loc[dfApprovalMessy['DecisionDate'].isnull(), 'DecisionDate'] = '2026-11-12'


#Verify that the missing approverID has been filled
#lets print approverID for the row with ApprovalID 27 and decision date
print(dfApprovalMessy.loc[
    dfApprovalMessy['ApprovalID'] == 27, ['ApprovalID', 'ApproverID', 'DecisionDate']
])


#Okay, now that we have filled in the missing approverID, lets now consult with manager about missing rejection reason for 
#the row that is pending but now we added approvalID, we can make it Approved
dfApprovalMessy.loc[dfApprovalMessy['ApprovalID'] == 27, ['ApprovalStatus']] = 'Approved'

#Verify that the status has been updated
print(dfApprovalMessy.loc[
    dfApprovalMessy['ApprovalID'] == 27, ['ApprovalID', 'ApprovalStatus']
])


#Now that we fixed that, and after having manually reviewed record ApprovalID 20 as well,
#ApprovalID 20 is NOT a duplicate, having double checked the file, we will make it approved.
dfApprovalMessy.loc[
    dfApprovalMessy['ApprovalID'] == 20,
    'ApprovalStatus'
] = 'Approved'

# Replace missing rejection reasons with empty strings.

dfApprovalMessy['RejectionReason'] = (
    dfApprovalMessy['RejectionReason'].fillna('')
)

# Verify the changes.

print(dfApprovalMessy.loc[
    dfApprovalMessy['ApprovalID'] == 20,
    ['ApprovalID', 'ApprovalStatus', 'RejectionReason']
])

#check for nulls one last time
print(dfApprovalMessy.isnull().sum())

#Now lets look for duplicate records
print('Any duplicate rows? ' + str(dfApprovalMessy[dfApprovalMessy.duplicated()]))

#No duplicate rows found
#lets clear whitespace from string columns
text_cols = dfApprovalMessy.select_dtypes(include="object").columns
dfApprovalMessy[text_cols] = dfApprovalMessy[text_cols].apply(
    lambda col: col.map(
        lambda value: value.strip() if isinstance(value, str) else value
    )
)

has_whitespace = dfApprovalMessy[text_cols].apply(
    lambda col: col.map(
        lambda value: isinstance(value, str) and value != value.strip()
    ).any()
)

print(has_whitespace)  # False for every column means it's clear
print("All clear:", not has_whitespace.any())

#Now it is time to capitalize string columns
dfApprovalMessy[text_cols] = dfApprovalMessy[text_cols].apply(
    lambda col: col.map(
        lambda value: value.upper() if isinstance(value, str) else value
    )
)

#Verify that the capitalization has been applied
not_uppercase = dfApprovalMessy[text_cols].apply(
    lambda col: col.map(
        lambda value: isinstance(value, str) and value != value.upper()
    ).any()
)
print(not_uppercase)
print("All string values are uppercase:", not not_uppercase.any())