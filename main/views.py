# https://www.youtube.com/watch?v=Y7OAk7DiLJs
from django.shortcuts import render,redirect
import pandas as pd
from sklearn.cluster import KMeans, DBSCAN
import matplotlib.pyplot as plt
from io import StringIO
from django.contrib.messages import constants as messages
import re
import json
import requests
import numpy as np
from django.http import JsonResponse

# Create your views here.
from django.template.defaultfilters import register

@register.filter(name='is_list')
def is_list(value):
    return isinstance(value, list)

@register.filter(name='isdigit')
def is_list(value):
    return isinstance(value, float)

def main(request):
    # return render(request,"upload.html")
    return render(request,"main.html")

def csv_page(request):
    return render(request,"upload.html")

def block_scan(request):
    return render(request,"blockscan.html")

def block_scan_analysis(request):
    if request.method=='POST' :
        person_address=request.POST.get("person_address")
        contract_add=request.POST.get("contract_address")
        chain= request.POST.get("chain")
        typeof=request.POST.get("type")
        if typeof=="ERC-20":
            normal_list="https://api.etherscan.io/api?module=account&action=tokentx&address="+contract_add+"&startblock=StartBlockNumber&endblock=EndBlockNumber&sort=asc&apikey="+"KQ8CTV715ADWGM62JA2DVZA1V23A9MBHHU"
        elif typeof=="Normal":
            normal_list="https://api.etherscan.io/api?module=account&action=txlist&address="+contract_add+"&startblock=StartBlockNumber&endblock=EndBlockNumber&sort=asc&apikey="+"KQ8CTV715ADWGM62JA2DVZA1V23A9MBHHU"
        print(normal_list)
        y = requests.get(normal_list)
        data = y.json()
        result = data["result"]
        df = pd.DataFrame(result)

        df["value"] = df["value"].astype(float)
        df["tokenDecimal"] = df["tokenDecimal"].astype(int)
        df["value"] = df.apply(lambda row: row["value"] / (10 ** row["tokenDecimal"]), axis=1)
        values_list = df["value"].tolist()
        threshold = 3
        mean = np.mean(values_list)
        std_dev = np.std(values_list)
        values_list = [x for x in values_list if (x - mean) / std_dev < threshold]
        cols = ["value"]

        top_10_dep=df[df["from"].str.lower() == contract_add.lower()]
        top_10_dep_sorted = top_10_dep.sort_values(by="value", ascending=False)
        top_10_deposit_addresses = top_10_dep_sorted["from"].head(10).tolist()
        top_10_deposit_amounts = top_10_dep_sorted["value"].head(10).tolist()
        for i, address in enumerate(top_10_deposit_addresses):
            amount = top_10_deposit_amounts[i]
            print(f"Top {i + 1}: Address/User {address} deposited the maximum amount ({amount})")

        new_col = []
        for item in cols:
            item = item.replace('-', '_')
            item = item.replace("Date",'date')
            item = item.replace(' ', '')
            item = item.replace('&', 'and')
            new_col.append(item)
        
        params={}
        params["value"]= values_list
        params["head"]=new_col
        params["columns"]=len(cols)
        params['mlmodel']=["Regression","SVM","RandomF"]
        params["row"]=len(data)

        # recursive_cols = [col for col in df.columns if df[col].apply(lambda x: isinstance(x, str)).all()]
        recursive_cols=["tokenName","tokenSymbol"]
        params["tokenName"]=df["tokenName"].tolist()
        params["tokenSymbol"]=df["tokenSymbol"].tolist()
        params["recursive"]=recursive_cols


        params['colors']=["#14A44D","red","#E4A11B","#3B71CA","#FBFBFB","#DC4C64","#9966FF","#4BC0C0"]
        # params['stock']=OHLV
        params['message_text']="Addess scaned! Check it out."
        # params['message']=messgage
        # print("nested dic ", params)
        print(params["head"])
        context = {'params': params}

        return render(request,"index.html",context)

def upload_csv(request):
    if request.method=='POST' and request.FILES['mycsv']:
        myfile = request.FILES['mycsv']

        file=request.FILES.get('mycsv')
        # file1=file
        file1=StringIO(file.read().decode('utf-8'))
        data=pd.read_csv(file1,sep='[:;,|]',engine='python')
        date_cols = [col for col in data.columns if re.match(r'.*(date|time|timestamp).*', col, re.IGNORECASE)]
        phone_cols = [col for col in data.columns if re.match(r'.*(phone|tel|mobile).*', col, re.IGNORECASE)]
        OHLV = [col.lower() for col in data.columns if re.match(r'.*(open|high|low|close).*', col, re.IGNORECASE)]
        messgage=False
        message_text="File analysed"
        if len(OHLV)==0:
            OHLV=False
            messgage=True
        else:
            message_text="Detected you have provided Financial file."
            messgage=True
            print("yes financial ")
        print(OHLV)
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
            item = item.replace('-', '_')
            item = item.replace("Date",'date')
            item = item.replace(' ', '')
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
        params['mlmodel']=["Regression","SVM","RandomF"]
        params["row"]=len(data)
        params["recursive"]=recursive_cols
        params['colors']=["#14A44D","red","#E4A11B","#3B71CA","#FBFBFB","#DC4C64","#9966FF","#4BC0C0"]
        params['stock']=OHLV
        params['message_text']=message_text
        params['message']=messgage
        # print("nested dic ", params)
        print(params["head"])
        data.to_csv("user_session.csv")

        context = {'params': params}

        # request.session.flush()
        # request.session['df'] = data
        return render(request,"index.html",context)
        # return render(request,"main.html",param)
    else:
        redirect('/')

def process_form(request):
    print("runnnnnnn")
    if request.method == 'POST':
        data = json.loads(request.body)
        # user_input = data.get('model1', '')
        Dependent = data.get('Dependent', [])
        INDependent = data.get("INDependent",[])
        mlmodel = data.get("mlmodel",[])
        print(Dependent,INDependent,mlmodel)
        response = {
            'message': "You have entered the message : {}".format(user_input),
        }
        x=pd.read_csv("user_session.csv")
        print(x)
        print(user_input)
        return JsonResponse(response)
    else:
        return JsonResponse({'message': 'This endpoint only accepts POST requests.'})


def cluster_and_visualize(df, feature_1, feature_2, algorithm="kmeans", **kwargs):
    """
    Applies clustering on the data and visualizes the clusters on a scatter plot.
    
    Args:
    - df (pandas.DataFrame): Input data.
    - feature_1 (str): Name of the first feature for visualization.
    - feature_2 (str): Name of the second feature for visualization.
    - algorithm (str): The clustering algorithm to use ("kmeans" or "dbscan").
    - **kwargs: Additional arguments for clustering algorithms.
    
    Returns:
    - plt.figure: A scatter plot displaying the clusters.
    """
    data = df[[feature_1, feature_2]].values
    
    if algorithm == "kmeans":
        n_clusters = kwargs.get('n_clusters', 3)  # Default to 3 clusters if not provided
        model = KMeans(n_clusters=n_clusters)
        clusters = model.fit_predict(data)
    elif algorithm == "dbscan":
        eps = kwargs.get('eps', 0.5)
        min_samples = kwargs.get('min_samples', 5)
        model = DBSCAN(eps=eps, min_samples=min_samples)
        clusters = model.fit_predict(data)
    else:
        raise ValueError("Unsupported algorithm. Choose 'kmeans' or 'dbscan'.")
    
    # Visualize the clusters
    plt.figure(figsize=(10, 7))
    plt.scatter(data[:, 0], data[:, 1], c=clusters, cmap='rainbow', edgecolor='k', s=50)
    plt.xlabel(feature_1)
    plt.ylabel(feature_2)
    plt.title(f'{algorithm.upper()} Clustering')
    plt.colorbar()
    return plt

    # Using the same sample data for demonstration
    sample_df_for_clustering = pd.DataFrame(sample_data_for_clustering)

    # Visualize clusters using KMeans
    cluster_and_visualize(sample_df_for_clustering, 'Feature1', 'Feature2', algorithm="kmeans", n_clusters=2).show()
