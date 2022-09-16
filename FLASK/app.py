import re
import json
import requests
from operator import itemgetter
from urllib.parse import urlparse
from urllib.parse import urlencode
from urllib.request import Request, urlopen
from flask_cors import CORS, cross_origin
from collections import defaultdict, Iterable
from flask import Flask, flash, request, redirect, render_template ,jsonify

app=Flask(__name__)

cors = CORS(app, resources={

    r"/*": {
        "origins": "*"

    }
})

def send_request(payload):
    #mirror query input to clusters 
    url = "http://192.168.8.210:5000/search"
    data = json.dumps(payload)
    request = Request(url, urlencode({'data': data}).encode())
    _son = urlopen(request).read().decode()
    print(_son)
    '''
    headers = {'Content-type': 'application/json'}
    response = requests.post(url, data=json.dumps(payload), headers=headers,timeout=10)
    return response.content
    '''
    return {}

def SEMANTIC_SCHOLAR(query):
    _response ={}
    data = requests.get('http://localhost:9200/idxs2edb/_search?q='+query+'&size='+str(str(request.args.get('limit', None))))
    response = data.json()
    _response_list = []
    elastic_docs = response["hits"]["hits"]
    for num, doc in enumerate(elastic_docs):
        try:
            source_data = doc["_source"]
            res= [n.get('name') for n in  list(eval(source_data["authors"]))]
            source_data["type"]="text"
            source_data["score"]=doc["_score"]
            source_data["license_url"]="https://creativecommons.org/licences/by-nc/4.0"
            source_data["license_name"]="CC BY-SA 4.0"
            source_data["license_disclaimer"]=""

            source_data["authors"]=[{"author":res}]
            urls = eval(source_data["pdfurls"])
            source_data["item"]= urls[0]
            source_data["authors"]=[{"author":urlparse( urls[0]).netloc}]
            source_data["abstract"]=str(str(source_data["description"]).replace("None", "")).replace("None .", "")
            source_data.pop('_meta', None)
            _response_list.append(source_data)
        except TypeError:
            print('TypeError')
    _response_List = [i for n, i in enumerate(_response_list) if i not in _response_list[n + 1:]]
    return _response_List

def TEACHERS_FUTURE(query):
    _response = {}
    data = requests.get('http://localhost:9200/idxtfedb/_search?q='+query+'&size=20')
    response = data.json()
    _response_list = []
    _response_List = []
    elastic_docs = response["hits"]["hits"]
    for num, doc in enumerate(elastic_docs):
        try:
            source_data = doc["_source"]
            #print( source_data)
            _author=source_data["authors"]
            source_data["license_url"]="https://creativecommons.org/licences/by-sa/4.0"
            source_data["license_name"]="CC BY-SA 4.0"
            source_data["license_disclaimer"]=""
            source_data["score"]=doc["_score"]
            source_data["type"]="text"
            source_data["date_updated"]=source_data["date_updated"][-4:]
            source_data["authors"]=[{"author":_author}]
            #print(re.match(r'^.*?\.pdf', doc["_source"]["book_key"]).group(0))
            source_data["item"]="https://sc.coloer.net:3000/docs/"+re.match(r'^.*?\.pdf', doc["_source"]["book_key"]).group(0)
            source_data["abstract"]=str(str(source_data["description"]).replace("None", "")).replace("None .", "")
            source_data.pop('_meta', None)
            _response_list.append(source_data)
        except KeyError:
            print("keyerror")
        except AttributeError:
            print("AttributeError")
    _response_List = [i for n, i in enumerate(_response_list) if i not in _response_list[n + 1:]]
    return _response_List

def TEACHERS_FUTURE_VIDEO(query):
    _response = {}
    data = requests.get('http://localhost:9200/idxtfvedb/_search?q='+query+'&size=20')
    response = data.json()
    _response_list = []
    _response_List = []
    elastic_docs = response["hits"]["hits"]
    #print(elastic_docs)
    for num, doc in enumerate(elastic_docs):
        try:
            source_data = doc["_source"]
            #print( source_data)
            _author=source_data["authors"]
            source_data["license_url"]="https://creativecommons.org/licences/by-sa/4.0"
            source_data["license_name"]="CC BY-SA 4.0"
            source_data["license_disclaimer"]=""
            source_data["score"]=doc["_score"]
            source_data["type"]="video"
            source_data["date_updated"]=source_data["date_updated"][-4:]
            source_data["authors"]=[{"author":_author}]
            #print(re.match(r'^.*?\.pdf', doc["_source"]["book_key"]).group(0))
            source_data["item"]=doc["_source"]["book_key"]
            source_data["abstract"]=str(str(source_data["description"]).replace("None", "")).replace("None .", "")
            source_data.pop('_meta', None)
            _response_list.append(source_data)
        except KeyError:
            print("keyerror")
        except AttributeError:
            print("AttributeError")
    _response_List = [i for n, i in enumerate(_response_list) if i not in _response_list[n + 1:]]
    return _response_List

def X5GON_VIDEOS(query):
    print(query)
    _response ={}
    data = requests.get('http://localhost:9200/idxvedb/_search?q='+query+str(str(request.args.get('limit', None))))
    response = data.json()
    _response_list = []
    elastic_docs = response["hits"]["hits"]
    for num, doc in enumerate(elastic_docs):
        source_data = doc["_source"]
        _author=source_data["authors"]
        source_data["type"]="video"
        source_data["score"]=doc["_score"]
        source_data["authors"]=[{"author":_author}]
        source_data["abstract"]=str(str(source_data["description"]).replace("None", "")).replace("None .", "")
        source_data.pop('_meta', None)
        _response_list.append(source_data)
    _response_List = [i for n, i in enumerate(_response_list) if i not in _response_list[n + 1:]]
    return _response_List

@app.route('/search', methods=['GET'])
def index():
    _response = {}
    request_data = request.get_json()
    end_date=str(request.args.get('end_date', None))

    if str(request.args.get('document', None)) == "All":
        q =str(request.args.get('keyWord', None))
        query = re.sub(r"[^a-zA-Z0-9]+", ' ', q)
        
        TF_LIST=TEACHERS_FUTURE(query)
        S2_LIST=SEMANTIC_SCHOLAR(query)
        XG_VIDEO_LIST=X5GON_VIDEOS(query)
        TF_VIDEO_LIST=TEACHERS_FUTURE_VIDEO(query)
        print(query)
        _response = {}
        data = requests.get('http://localhost:9200/idxtedb/_search?q='+query+str(str(request.args.get('limit', None))))
        response = data.json()
        _response_list = []
        _response_List = []
        elastic_docs = response["hits"]["hits"]
        for num, doc in enumerate(elastic_docs):
            source_data = doc["_source"]
            _author=source_data["authors"]
            source_data["type"]="text"
            source_data["score"]=doc["_score"]
            source_data["authors"]=[{"author":_author}]
            source_data["abstract"]=str(str(source_data["description"]).replace("None", "")).replace("None .", "")
            source_data.pop('_meta', None)
            _response_list.append(source_data)
        _response_List = [i for n, i in enumerate(_response_list) if i not in _response_list[n + 1:]]
        _Response_List=TF_LIST+_response_List+S2_LIST+TF_VIDEO_LIST+XG_VIDEO_LIST
        sorted_List = sorted(_Response_List, key=itemgetter('score'),reverse=True)
        _response = {
        "total_results":  len(_Response_List),
        "time_taken": response["took"],
        "results": sorted_List
        }

    #BOOK FILTER
    if str(request.args.get('document', None)) == "Book":
        q =str(request.args.get('keyWord', None))
        query = re.sub(r"[^a-zA-Z0-9]+", ' ', q)
        print(query)
        _response ={}
        data = requests.get('http://localhost:9200/idxbedb/_search?q='+query+str(str(request.args.get('limit', None))))
        response = data.json()
        _response_list = []
        _response_List = []
        elastic_docs = response["hits"]["hits"]
        for num, doc in enumerate(elastic_docs):
            source_data = doc["_source"]
            _author=source_data["authors"]
            source_data["type"]="book"
            source_data["score"]=doc["_score"]
            source_data["source"]="https://openlibrary.org/"
            source_data["authors"]=[{"author":_author}]
            source_data["item"]="https://openlibrary.org"+source_data["book_key"]
            source_data["abstract"]=str(str(source_data["abstract"]).replace("None .", "")+" . "+str(source_data["description"]).replace("None", "")).replace("None .", "")
            source_data.pop('_meta', None)
            _response_list.append(source_data)
        _response_List = [i for n, i in enumerate(_response_list) if i not in _response_list[n + 1:]]
        _response = {
        "total_results":  len(_response_List),
        "time_taken": response["took"],
        "results": _response_List
        }

    #EMPTY FILTER
    if str(request.args.get('document', None)) == "":
        q =str(request.args.get('keyWord', None))
        query = re.sub(r"[^a-zA-Z0-9]+", ' ', q)
        
        TF_LIST=TEACHERS_FUTURE(query)
        S2_LIST=SEMANTIC_SCHOLAR(query)
        XG_VIDEO_LIST=X5GON_VIDEOS(query)
        TF_VIDEO_LIST=TEACHERS_FUTURE_VIDEO(query)
        print(query)
        _response = {}
        data = requests.get('http://localhost:9200/idxtedb/_search?q='+query+str(str(request.args.get('limit', None))))
        response = data.json()
        _response_list = []
        _response_List = []
        elastic_docs = response["hits"]["hits"]
        for num, doc in enumerate(elastic_docs):
            source_data = doc["_source"]
            _author=source_data["authors"]
            source_data["type"]="text"
            source_data["score"]=doc["_score"]
            source_data["authors"]=[{"author":_author}]
            source_data["abstract"]=str(str(source_data["description"]).replace("None", "")).replace("None .", "")
            source_data.pop('_meta', None)
            _response_list.append(source_data)
        _response_List = [i for n, i in enumerate(_response_list) if i not in _response_list[n + 1:]]
        _Response_List=TF_LIST+_response_List+S2_LIST+TF_VIDEO_LIST+XG_VIDEO_LIST
        sorted_List = sorted(_Response_List, key=itemgetter('score'),reverse=True)
        _response = {
        "total_results":  len(_Response_List),
        "time_taken": response["took"],
        "results": sorted_List
        }

    #VIDEO FILTER
    if str(request.args.get('document', None)) == "Video":
        q =str(request.args.get('keyWord', None))
        query = re.sub(r"[^a-zA-Z0-9]+", ' ', q)
        TF_LIST=TEACHERS_FUTURE_VIDEO(query)
        print(query)
        _response ={}
        data = requests.get('http://localhost:9200/idxvedb/_search?q='+query+str(str(request.args.get('limit', None))))
        response = data.json()
        _response_list = []
        elastic_docs = response["hits"]["hits"]
        for num, doc in enumerate(elastic_docs):
            source_data = doc["_source"]
            _author=source_data["authors"]
            source_data["type"]="video"
            source_data["score"]=doc["_score"]
            source_data["authors"]=[{"author":_author}]
            source_data["abstract"]=str(str(source_data["description"]).replace("None", "")).replace("None .", "")
            source_data.pop('_meta', None)
            _response_list.append(source_data)
        _response_List = [i for n, i in enumerate(_response_list) if i not in _response_list[n + 1:]]
        _Response_List=TF_LIST+_response_List
        sorted_List = sorted(_Response_List, key=itemgetter('score'),reverse=True)
        _response = {
        "total_results":  len(_Response_List),
        "time_taken": response["took"],
        "results": sorted_List
        }

    #AUDIO FILTER
    if str(request.args.get('document', None)) == "Audio":
        q =str(request.args.get('keyWord', None))
        query = re.sub(r"[^a-zA-Z0-9]+", ' ', q)
        _response = {}
        data = requests.get('http://localhost:9200/idxtfaedb/_search?q='+query+str(str(request.args.get('limit', None))))
        response = data.json()
        _response_list = []
        _response_List = []
        elastic_docs = response["hits"]["hits"]
        #print(elastic_docs)
        for num, doc in enumerate(elastic_docs):
            try:
                source_data = doc["_source"]
                #print( source_data)
                source_data["type"]="audio"
                _author=source_data["authors"]
                source_data["license_url"]="https://creativecommons.org/licences/by-sa/4.0"
                source_data["license_name"]="CC BY-SA 4.0"
                source_data["license_disclaimer"]=""
                source_data["score"]=doc["_score"]
                source_data["date_updated"]=source_data["date_updated"][-4:]
                source_data["authors"]=[{"author":_author}]
                #print(re.match(r'^.*?\.pdf', doc["_source"]["book_key"]).group(0))
                source_data["item"]="https://sc.coloer.net:3000/docs/"+doc["_source"]["book_key"]
                source_data["abstract"]=str(str(source_data["description"]).replace("None", "")).replace("None .", "")
                source_data.pop('_meta', None)
                _response_list.append(source_data)
            except KeyError:
                print("keyerror")
            except AttributeError:
                print("AttributeError")
        _response_List = [i for n, i in enumerate(_response_list) if i not in _response_list[n + 1:]]
        _response = {
            "total_results":  len(_response_List),
            "time_taken": response["took"],
            "results": _response_List
            }
    
    #TEXT FILTER
    if str(request.args.get('document', None)) == "Text":
        q =str(request.args.get('keyWord', None))
        print(q)
        query = re.sub(r"[^a-zA-Z0-9]+", ' ', q)
        TF_LIST=TEACHERS_FUTURE(query)
        print(query)
        _response ={}
        data = requests.get('http://localhost:9200/idxs2edb/_search?q='+query+'&size='+str(str(request.args.get('limit', None))))
        response = data.json()
        _response_list = []
        elastic_docs = response["hits"]["hits"]
        for num, doc in enumerate(elastic_docs):
            try:
                source_data = doc["_source"]
                res= [n.get('name') for n in  list(eval(source_data["authors"]))]
                source_data["type"]="text"
                source_data["score"]=doc["_score"]
                source_data["license_url"]="https://creativecommons.org/licences/by-nc/4.0"
                source_data["license_name"]="CC BY-SA 4.0"
                source_data["license_disclaimer"]=""

                source_data["authors"]=[{"author":res}]
                urls = eval(source_data["pdfurls"])
                source_data["item"]= urls[0]
                source_data["authors"]=[{"author":urlparse( urls[0]).netloc}]
                source_data["abstract"]=str(str(source_data["description"]).replace("None", "")).replace("None .", "")
                source_data.pop('_meta', None)
                _response_list.append(source_data)
            except TypeError:
                print('TypeError')
        #res=send_request(_response_list)
        #print(res)
        _response_List = [i for n, i in enumerate(_response_list) if i not in _response_list[n + 1:]]
        _Response_List=TF_LIST+_response_List
        sorted_List = sorted(_Response_List, key=itemgetter('score'),reverse=True)
        _response = {
        "total_results":  len(_Response_List),
        "time_taken": response["took"],
        "results": sorted_List
        }
    return _response
