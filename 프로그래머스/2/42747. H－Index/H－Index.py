def solution(citations):
    citations.sort(reverse=True)  # 내림차순 정렬
    h_index = 0

    for i in range(len(citations)):
        # 현재 인용 수가 i+1 이상인 경우 H-Index 후보
        if citations[i] >= i + 1:
            h_index = i + 1  # H-Index 업데이트

    return h_index
