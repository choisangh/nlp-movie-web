# driver = webdriver.Chrome('./lec22_chromedriver.exe', options=options)
# driver.implicitly_wait(5)
time.sleep(1)

error_list = []
tot_list = []
for uid in range(2):
    try:
        url = f'http://www.cine21.com/movie/info/?movie_id={uid}'
        print(url)
        # driver.post(url)
        # page_html_source = driver.page_source

        response = requests.get(url)
        if response.status_code == 200:
            page_html_source = response.text
            soup = BeautifulSoup(page_html_source, 'html.parser')
            # print(page_html_source)
            dict['번호'] = i

            try:
                제목 = soup.select_one(
                    "#container > div.movie_detail_top_area.nostill > div > div > div.mov_info > p.tit").text
                dict['제목'] = 제목
            except Exception as e:
                dict['제목'] = np.nan

            try:


            except Exception as e:

            개봉년도 = soup.select_one(
                "#container > div.movie_detail_top_area > div > div > div.mov_info > p:nth-of-type(3) > span:nth-of-type(1)").text
            국가 = soup.select_one(
                "#container > div.movie_detail_top_area > div > div > div.mov_info > p:nth-of-type(3) > span:nth-of-type(2)").text
            관람등급 = soup.select_one(
                "#container > div.movie_detail_top_area.nostill > div > div > div.mov_info > p:nth-of-type(3) > span").text
            장르 = soup.select_one(
                "#container > div.movie_detail_top_area > div > div > div.mov_info > p:nth-of-type(4) > span:nth-of-type(1)").text
            상영시간 = soup.select_one(
                "#container > div.movie_detail_top_area > div > div > div.mov_info > p:nth-of-type(4) > span:nth-of-type(2)").text
            개봉일 = soup.select_one(
                "#container > div.movie_detail_top_area > div > div > div.mov_info > p:nth-of-type(5) > span:nth-of-type(1)").text
            누적관객 = soup.select_one(
                "#container > div.movie_detail_top_area > div > div > div.mov_info > p:nth-of-type(5) > span:nth-of-type(2)").text
            감독 = soup.select_one(
                "#container > div.movie_detail_top_area.nostill > div > div > div.mov_info > p:nth-of-type(6) > a").text
            출연 = soup.select_one(
                "#container > div.movie_detail_top_area > div > div > div.mov_info > p:nth-of-type(7)").text
            평점 = soup.select_one(
                "#container > div.movie_detail_top_area > div > div > ul > li:nth-of-type(2) > span").text
            줄거리 = soup.select_one("#content > div.story_area > div").text
            썸네일 = soup.select_one(
                "#container > div.movie_detail_top_area.nostill > div > div > div.mov_poster > img").get('src')

            # print(개봉년도,국가, 관람등급, 상영시간,개봉일,누적관객,감독,출연,평점,줄거리)

            dict['개봉년도'] = 개봉년도
            dict['국가'] = 국가
            dict['관람등급'] = 관람등급
            dict['상영시간'] = 상영시간
            dict['개봉일'] = 개봉일
            dict['누적관객'] = 누적관객
            dict['감독'] = 감독
            dict['출연'] = 출연
            dict['평점'] = 평점
            dict['썸네일'] = 썸네일
            dict['줄거리'] = 줄거리
            tot_list.append(dict)

        else:
            print("error")
    except Exception as e:
        print(f"에러발생 {uid}")
        error_list.append(uid)
        continue

mvd = pd.DataFrame(tot_list)
mvd.head()