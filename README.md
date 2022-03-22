<img width="500" src="https://blog.kakaocdn.net/dn/lD0LP/btrwVb3n7IO/bMsq3NHZNnQweqx3BXkdR0/img.png">
Main Page - Menu, Search bar 
<img width="500" src="https://blog.kakaocdn.net/dn/cscA2x/btrwT0gLj0V/KQWWWUhDaVvnGULsNycvF0/img.png">
메뉴를 통해 장르, 스토리, 배우/감독별 선택 가능
The Movie DB API를 활용해 데이터 수집, 각 메뉴에 해당 되는 비정형 데이터(텍스트)를 자연어 처리하여 추천 알고리즘 구현
텍스트를 벡터화하여(TfidfVectorizer) cosine similarity 측정 후 가장 유사한 영화를 추천
<img width="500" src="https://blog.kakaocdn.net/dn/vQRjt/btrwPbKEX5B/HT00gnl1SiWZ8LHBzPyPu0/img.png">
Search bar를 통해 영화 검색 가능
<img width="500" src="https://blog.kakaocdn.net/dn/cqSXl0/btrwMHbZgLQ/Kdz4sIyGFgsks4CxxpsZwK/img.png">
Result Page
cosine similarity가 높은 순으로 5개 영화 추천
