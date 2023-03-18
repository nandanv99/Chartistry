# https://www.youtube.com/watch?v=Y7OAk7DiLJs
from django.shortcuts import render,redirect
import pandas as pd
from io import StringIO
import re
# Create your views here.

def main(request):
    return render(request,"upload.html")


def upload_csv(request):
    if request.method=='POST' and request.FILES['mycsv']:
        myfile = request.FILES['mycsv']

        file=request.FILES.get('mycsv')
        # file1=file
        file1=StringIO(file.read().decode('utf-8'))
        data=pd.read_csv(file1,sep='[:;,|_]',engine='python')
        date_cols = [col for col in data.columns if re.match(r'.*(date|time|timestamp).*', col, re.IGNORECASE)]
        phone_cols = [col for col in data.columns if re.match(r'.*(phone|tel|mobile).*', col, re.IGNORECASE)]
        cols_to_drop = date_cols + phone_cols
        data = data.drop(cols_to_drop, axis=1)

        # recursive_cols = []
        # for col in data.columns:
        #     if data[col].dtype == 'object' and data[col].duplicated().any():
        #         recursive_cols.append(col)

        

        cols=data.columns[data.dtypes != 'object'].tolist()
        recursive_cols=data.columns[data.dtypes == 'object'].tolist()
        print("recursive cols: ",recursive_cols)
        new_col = []
        for item in cols:
            # replace '-' with '_'
            item = item.replace('-', '_')
            item = item.replace("Date",'date')
            item = item.replace(' ', '')
            # replace '&' with 'and'
            item = item.replace('&', 'and')
            new_col.append(item)


        params={}
        for col in data.columns:
            col_dict = data[col].tolist()
            col = col.replace('-', '_')
            col = col.replace(' ', '')
            # replace '&' with 'and'
            col = col.replace('&', 'and')
            params[col] = col_dict
        params["head"]=new_col
        params["columns"]=len(cols)
        params["row"]=len(data)
        params["recursive"]=recursive_cols
        # print("nested dic ", params)
        print(params["head"])

        context = {'params': params}
        return render(request,"chartify.html",context)
        # return render(request,"main.html",param)
    else:
        redirect('/')
