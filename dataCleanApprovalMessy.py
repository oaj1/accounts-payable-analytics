import pandas as pd

#now lets read in the files
dfApprovalMessy = pd.read_excel('Approvals_Dataset_Messy.xlsx')

"""
Data Cleaning Objectives

1. Identify missing values. (/)
2. Remove duplicate records. (up next)
3. Remove unnecessary whitespace.
4. Standardize capitalization.
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
#one for reject states potential duplicate, the other has no rejection reason

#Decision date and approverID show null count of one
#lets take a look at approverID and decision date with null values
print(dfApprovalMessy[dfApprovalMessy['ApproverID'].isnull() | dfApprovalMessy['DecisionDate'].isnull()])


#From result we see approvalID is ID 27.
#however, it is pending, so decision date should be null
#for missing approverID, after flagging, we discovered its ID
#I will now fill in the missing approverID with the discovered ID
dfApprovalMessy.loc[dfApprovalMessy['ApproverID'].isnull(), 'ApproverID'] = 'EMP-2103'


#Verify that the missing approverID has been filled
#lets print approverID for the row with ApprovalID 27
print(dfApprovalMessy.loc[
    dfApprovalMessy['ApprovalID'] == 27, ['ApprovalID', 'ApproverID']
])