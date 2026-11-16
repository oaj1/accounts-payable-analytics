import pandas as pd

#now lets read in the files
dfApproval = pd.read_excel('Approvals_Dataset.xlsx')
dfInvoice = pd.read_excel('Invoice_Dataset.xlsx')
dfPayment = pd.read_excel('Payment_Dataset.xlsx')
dfVendor = pd.read_excel('Vendor_Dataset.xlsx')

#Now lets examine the dataframes
#print(dfApproval.head())
#print(dfInvoice.head())
#print(dfPayment.head())
#print(dfVendor.head())

#Lets take a look to see any null values

#print(dfApproval.isnull().sum())
#print(dfInvoice.isnull().sum())
#print(dfPayment.isnull().sum())
#print(dfVendor.isnull().sum())

#of the four dataframes, only Approvals has null values
#lets verify
#print(dfApproval['ApprovalStatus'].value_counts())

#based on the results, 
# 27 Approved → likely have DecisionDate and no RejectionReason
#2 Rejected → should have both DecisionDate and RejectionReason
#1 Pending → should have no DecisionDate and no RejectionReason

#lets confirm

print(
    dfApproval[dfApproval['ApprovalStatus'] == 'Pending']
)

#confirmed, only one Pending approval exists, approvalID 27


#Now lets look for any duplicates