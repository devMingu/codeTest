from itertools import combinations

def solution(relation):
    column = len(relation[0])   #key들의 개수
    key_idx = list(range(column)) #리스트의 형태로 키들의 인덱스를 저장
    minimality = [] #유일성 & 최소성을 보장하는 키들의 모임
    for i in range(1, column+1): # i는 가능한 조합을 의미하기때문에 1부터 key들의 개수까지.
        for comb in combinations(key_idx, i): # combinations를 통해 나온 조합을 comb를 통해 접근.
            temp = []
            for key in relation: #relation의 각 tuple에 접근.
                current_key = [key[c] for c in comb]
                #current_key에는 각 tuple에서 나온 조합이 들어가있음.
                if current_key not in temp:
                    temp.append(current_key)
                else: # 중복이 된다면 유일성이 보장이 되지 않는다. --> BREAK
                    break
            #유일성이 보장된다면 최소성을 확인해야함.
            else:
                for mini in minimality: #comb가 이미 존재한다면 최소성이 보장이 안됨.
                    if set(mini) <= (set(comb)):
                        break
                #comb의 최소성이 보장이 된다면 minimality에 삽입.
                else:
                    minimality.append(comb)
    answer = len(minimality)
    return answer

solution([["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]])

