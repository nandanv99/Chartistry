# https://www.youtube.com/watch?v=Y7OAk7DiLJs
from django.shortcuts import render,redirect
import pandas as pd
from io import StringIO
import re
# Create your views here.
from django.template.defaultfilters import register

@register.filter(name='is_list')
def is_list(value):
    return isinstance(value, list)

@register.filter(name='isdigit')
def is_list(value):
    return isinstance(value, float)

def main(request):
    return render(request,"upload.html")
    # return render(request,"new_template.html")


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

        cols = []
        for col in data.columns:
            if all(data[col].apply(lambda x: isinstance(x, (int, float)))):
                cols.append(col)
        print("cols are : ",cols)

        # handling unnamed columns 
        count=0
        for i, col in enumerate(data.columns):
            if col.startswith("Unnamed"):
                data = data.rename(columns={col: f"Unnamed{count+i+1}"})

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

        print("new cols is :",new_col)
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
        params['colors']=["#14A44D","red","#E4A11B","#3B71CA","#FBFBFB","#DC4C64","#54B4D3"]
        # print("nested dic ", params)
        print(params["head"])

        context = {'params': params}
        # return render(request,"chartify.html",context)
        return render(request,"index.html",context)
        # return render(request,"main.html",param)
    else:
        redirect('/')
