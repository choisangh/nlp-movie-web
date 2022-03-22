import json

import pandas as pd
from flask import Flask, make_response, jsonify, request, render_template
import cx_Oracle
import sqlalchemy as sa
# from flask_cors import CORS, cross_origin
import requests
from bs4 import BeautifulSoup
from movie_search_util import *
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
    return render_template("index.html",)





@app.route('/com_search_ajax', methods=['post'])
def com_search_ajax():

    str = request.form.get('search_str')
    print(str)


    #-----------웹에서 입력한 검색어와 관련된 업체만 가져오기 -----------------
    temp = mdf[(mdf['title'].str.lower().contains(str))|(mdf['title'].str.lower().contains(str.lower()))]['title'].head()

    return json.dumps(  temp.values.tolist()  )



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

    url1 = "https://api.themoviedb.org/3/movie/"+str(id_list[0])+"?api_key=08cf79d69ff8a9b33dcc4595d9608330&language=ko-KR"
    url2 = "https://api.themoviedb.org/3/movie/" + str(id_list[1]) + "?api_key=08cf79d69ff8a9b33dcc4595d9608330&language=ko-KR"
    url3 = "https://api.themoviedb.org/3/movie/" + str(id_list[2]) + "?api_key=08cf79d69ff8a9b33dcc4595d9608330&language=ko-KR"
    url4 = "https://api.themoviedb.org/3/movie/" + str(id_list[3]) + "?api_key=08cf79d69ff8a9b33dcc4595d9608330&language=ko-KR"
    url5 = "https://api.themoviedb.org/3/movie/" + str(id_list[4]) + "?api_key=08cf79d69ff8a9b33dcc4595d9608330&language=ko-KR"
    def get_json(url):
        r = requests.get(url)
        data = json.loads(r.text)
        poster_path=data["poster_path"]
        title=data["title"]
        overview=data["overview"]
        if len(overview)>200:
            overview=overview[:200]
            overview+="..."

        return poster_path,title,overview
    img1,t1,v1 = get_json(url1)
    img2,t2,v2 = get_json(url2)
    img3,t3,v3 = get_json(url3)
    img4,t4,v4 = get_json(url4)
    img5,t5,v5 = get_json(url5)



    res = [[t1, 'https://image.tmdb.org/t/p/original'+img1, v1],
    [t2, 'https://image.tmdb.org/t/p/original'+img2, v2],
    [t3, 'https://image.tmdb.org/t/p/original'+img3, v3],
    [t4, 'https://image.tmdb.org/t/p/original'+img4, v4],
    [t5, 'https://image.tmdb.org/t/p/original'+img5, v5]]

    return render_template(redirect_url, MY_INFO=res)




# @app.route('/result')
# def result():
#     return render_template("result.html", )


if __name__ == '__main__':
    app.debug = True
    app.run(host='127.0.0.1', port=9898)