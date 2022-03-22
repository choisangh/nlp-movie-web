import json

import pandas as pd
from flask import Flask, make_response, jsonify, request, render_template
import cx_Oracle
import sqlalchemy as sa
# from flask_cors import CORS, cross_origin
import requests
from bs4 import BeautifulSoup
from movie_search_util_not_json import *
import sys




# ------------------------------------
#pip install flask_cors
# import flask_cors CORS, cross_origin
# CORS(app)
# CORS(app, resources={r'*': {'origins': '*'}})
# ------------------------------------



app = Flask(__name__, template_folder="template", static_folder="static")
# CORS(app)


@app.route('/')
def index():
    print('=======================================hi')
    print('=======================================hi')
    print('=======================================hi')
    return render_template("index.html",)



@app.route('/com_search_ajax', methods=['post'])
def com_search_ajax():
    str = request.form.get('search_str')
    print(str)
    mdf['title']=mdf['title'].str.lower()
    # -----------웹에서 입력한 검색어와 관련된 업체만 가져오기 -----------------
    temp = mdf[(mdf['title'].str.contains(str)) | (mdf['title'].str.contains(str.upper()))][['id','title']].head()

    return json.dumps(temp.values.tolist())









@app.route('/search', methods=['GET'])
def search():

    search_gubun = request.args.get('search_gubun')
    search_str = request.args.get('search_str')
    print("서치구분",search_gubun)
    print("서치STR",search_str)
    redirect_url = "result.html"


    if search_gubun == 'genres':
        id_list = my_search_by_genres(search_str, 0.97)
        print(id_list)  #제목,포스터,리뷰

    elif search_gubun == 'story':
        id_list = my_search_by_review(search_str, 5)
        print(id_list)   #제목,포스터,리뷰
    elif search_gubun == 'actor':
        id_list = my_search_by_meta(search_str, 5)  # Batman Forever
        print(id_list)   #제목,포스터,리뷰
    else:
        print(search_gubun)
        redirect_url = "index.html"

    res=[]
    for id in id_list:
        title=mdf[mdf['id']==id]['title2'].values[0]
        img=mdf[mdf['id']==id]['poster_path2'].values[0]
        overview=mdf[mdf['id']==id]['overview2'].values[0]
        print(overview,type(overview))

        if pd.isnull(overview): #한글 overview가 없을 경우
            overview=mdf[mdf['id']==id]['overview'].values[0]
        if len(str(overview))>200:
            overview=str(overview)[:200]+"..."
        res.append([title,'https://image.tmdb.org/t/p/original'+img,overview])

    return render_template(redirect_url, MY_INFO=res)




# @app.route('/result')
# def result():
#     return render_template("result.html", )


if __name__ == '__main__':
    app.debug = True
    app.run(host='127.0.0.1', port=9898)