<img width="800" src="https://blog.kakaocdn.net/dn/lD0LP/btrwVb3n7IO/bMsq3NHZNnQweqx3BXkdR0/img.png"><br>
Main Page - Menu, Search bar <br><br>

<img width="800" src="https://blog.kakaocdn.net/dn/cscA2x/btrwT0gLj0V/KQWWWUhDaVvnGULsNycvF0/img.png"><br>

메뉴를 통해 장르, 스토리, 배우/감독별 선택 가능<br>

The Movie DB API를 활용해 데이터 수집, 각 메뉴에 해당 되는 비정형 데이터(텍스트)를 자연어 처리하여 추천 알고리즘 구현<br>

텍스트를 벡터화(TfidfVectorizer)하여 Cosine Similarity 측정 후 가장 유사한 영화를 추천<br>

<img width="800" src="https://blog.kakaocdn.net/dn/vQRjt/btrwPbKEX5B/HT00gnl1SiWZ8LHBzPyPu0/img.png"><br>

Search bar를 통해 영화 검색 가능<br>

<img width="800" src="https://blog.kakaocdn.net/dn/cqSXl0/btrwMHbZgLQ/Kdz4sIyGFgsks4CxxpsZwK/img.png"><br>

Result Page<br>

Cosine Similarity가 높은 순으로 5개 영화 추천<br>
