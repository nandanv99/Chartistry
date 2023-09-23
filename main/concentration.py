# def concetrate(d):
#     def get_bal(data_IN,data_OUT):
#         list_address = list(data_OUT.txhash_OUT.unique())+list(data_IN.txhash_IN.unique())
#         list_address = list(set(list_address))
#         d = pd.DataFrame()
#         list_bal = []
#         list_addresses = []
#         for i in list_address:

#             if data_OUT.loc[data_OUT['txhash_OUT']==i].shape[0]!=0:
#                 bal1 = data_OUT.loc[data_OUT['txhash_OUT']==i].balance.sum()#astype(int)
            
#             else:
#                 bal1=0


#             if data_IN.loc[data_IN['txhash_IN']==i].shape[0]!=0:
#                 bal2 = data_IN.loc[data_IN['txhash_IN']==i].balance.sum()#.astype(int)
#             else:
#                 bal2=0

                
#             net_bal = bal2-bal1
#             list_addresses.append(i)
#             list_bal.append(net_bal)
#         d['address']=list_addresses
#         d['balance'] = list_bal
#         return d
#     d = get_bal(data_IN,data_OUT)
#     range_dic={
#             '0-500':0,
#             '500-1000':0,
#             '1000-2000':0,
#             '2000-3000':0,
#             '3000-4000':0,
#             '4000-5000':0,
#             '5000-10000':0,
#             '10000-20000':0,
#             '20000-30000':0,
#             '30000-40000':0,
#             '40000-50000':0,
#             '50000-100000':0,
#             '100000-200000':0,
#             '200000-300000':0,
#             '300000-400000':0,
#             '400000-500000':0,
#             '500000-1000000':0,
#             '1000000-MAX':0,
#             }

#     amnt_dic={
#                 '0-500_amount':0,
#                 '500-1000_amount':0,
#                 '1000-2000_amount':0,
#                 '2000-3000_amount':0,
#                 '3000-4000_amount':0,
#                 '4000-5000_amount':0,
#                 '5000-10000_amount':0,
#                 '10000-20000_amount':0,
#                 '20000-30000_amount':0,
#                 '30000-40000_amount':0,
#                 '40000-50000_amount':0,
#                 '50000-100000_amount':0,
#                 '100000-200000_amount':0,
#                 '200000-300000_amount':0,
#                 '300000-400000_amount':0,
#                 '400000-500000_amount':0,
#                 '500000-1000000_amount':0,
#                 '1000000-MAX_amount':0,
#             }


#     list_balance=[]
#     for i in range(d.shape[0]):
#         list_balance.append(d.iloc[i,1])
#         # print(list_balance)
#     for j in list_balance:
#         if 0<=j<=500:
#             range_dic['0-500']+=1
#             amnt_dic['0-500_amount']+=j
#         if 500<j<=1000:
#             range_dic['500-1000']+=1
#             amnt_dic['500-1000_amount']+=j
#         if 1000<j<=2000:
#             range_dic['1000-2000']+=1
#             amnt_dic['1000-2000_amount']+=j
#         if 2000<j<=3000:
#             range_dic['2000-3000']+=1
#             amnt_dic['2000-3000_amount']+=j
#         if 3000<j<=4000:
#             range_dic['3000-4000']+=1
#             amnt_dic['3000-4000_amount']+=j
#         if 4000<j<=5000:
#             range_dic['4000-5000']+=1
#             amnt_dic['4000-5000_amount']+=j
#         if 5000<j<=10000:
#             range_dic['5000-10000']+=1
#             amnt_dic['5000-10000_amount']+=j
#         if 10000<j<=20000:
#             range_dic['10000-20000']+=1
#             amnt_dic['10000-20000_amount']+=j
#         if 20000<j<=30000:
#             range_dic['20000-30000']+=1
#             amnt_dic['20000-30000_amount']+=j
#         if 30000<j<=40000:
#             range_dic['30000-40000']+=1
#             amnt_dic['30000-40000_amount']+=j
#         if 40000<j<=50000:
#             range_dic['40000-50000']+=1
#             amnt_dic['40000-50000_amount']+=j
#         if 50000<j<=100000:
#             range_dic['50000-100000']+=1
#             amnt_dic['50000-100000_amount']+=j
#         if 100000<j<=200000:
#             range_dic['100000-200000']+=1
#             amnt_dic['100000-200000_amount']+=j
#         if 200000<j<=300000:
#             range_dic['200000-300000']+=1
#             amnt_dic['200000-300000_amount']+=j
#         if 300000<j<=400000:
#             range_dic['300000-400000']+=1
#             amnt_dic['300000-400000_amount']+=j
#         if 400000<j<=500000:
#             range_dic['400000-500000']+=1
#             amnt_dic['400000-500000_amount']+=j
#         if 500000<j<=1000000:
#             range_dic['500000-1000000']+=1
#             amnt_dic['500000-1000000_amount']+=j
#         # if 1000000<=j:
#         # if 1000000<j<=10000000:
#         if 1000000 <= j <= 10000000:
#             range_dic['1000000-MAX']+=1
#             amnt_dic['1000000-MAX_amount']+=j