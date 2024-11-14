# solved_ac api 써보기
import requests
import json
# 유저 기본 정보 받아오기
def get_profile(user_id):
    url = f"https://solved.ac/api/v3/user/show?handle={user_id}"
    request_get_profile = requests.get(url)
    if request_get_profile.status_code == 200:
        print("연결 성공")
        profile = json.loads(request_get_profile.content.decode('utf-8'))
        user_nick = profile['handle']
        user_tier = profile['tier']
        user_class = profile['class']
        user_rating = profile['rating']
        # 필요한 정보 4개 추출
        print("귀하의 id는 %s 입니다." %(user_nick))
        print("귀하의 tier는 %s 입니다."%(tier_list[user_tier]))
        print("귀하의 tier는 %s 입니다."%(str(user_class)))
        print("귀하의 현재 레이팅은 %d 입니다."%(user_rating))
    else:
        if(request_get_profile.status_code) == 404:
            print("연결 실패, id를 확인하세요")
        else:
            print("현재 다른 문제가 있어 사용이 불가능합니다.")

def get_solved_problem(user_id):
    url = f"https://solved.ac/api/v3/search/problem?query=s%40"+user_id
    request_get_profile = requests.get(url)
    if request_get_profile.status_code == 200:
        print("연결 성공")
        solved_problem_list = []
        solved_problem_json = json.loads(request_get_profile.content.decode('utf-8'))
        solved_problem_items = solved_problem_json['items']
        # problem : 해당 query에서 다음 페이지로 어떻게 넘겨야 할 것인가? 이 부분을 구현해야 함.
        for cur_problem in solved_problem_items:
            solved_problem_list.append(cur_problem['problemId'])
        return solved_problem_list
    else:
        if(request_get_profile.status_code) == 404:
            print("연결 실패, id를 확인하세요")
        else:
            print(request_get_profile.status_code)
            print("현재 다른 문제가 있어 사용이 불가능합니다.")
        return

tier_list = {0 : 'Unranked',
             1 : 'Bronze 5', 2 : 'Bronze 4', 3 : 'Bronze 3', 4 : 'Bronze 2', 5 : 'Bronze 1',
             6 : 'Silver 5', 7 : 'Silver 4', 8 : 'Silver 3', 9 : 'Silver 2', 10 : 'Silver 1',
             11 : 'Gold 5', 12 : 'Gold 4', 13 : 'Gold 3', 14 : 'Gold 2', 15 : 'Gold 1',
             16 : 'Platinum 5', 17 : 'Platinum 4', 18 : 'Platinum 3', 19 : 'Platinum 2', 20 : 'Platinum 1',
             21 : 'Diamond 5', 22 : 'Diamond 4', 23 : 'Diamond 3', 24 : 'Diamond 2', 25 : 'Diamond 1',
             26 : 'Ruby 5', 27 : 'Ruby 4', 28 : 'Ruby 3', 29 : 'Ruby 2', 30 : 'Ruby 1'}
user_id = str(input())
#get_profile(user_id) # 유저 연결 성공시 프로필 보여주기 위해 기능 개발 필요
solved_problem_list = get_solved_problem(user_id)
print(solved_problem_list)
print(len(solved_problem_list))