def eratosthenes(n):
    multiples = set()          # 공백의 set을 정의
    for i in range(2, n + 1):  # 2부터 n까지의 정수에 대해서
        if i not in multiples: # set에 없으면
            yield i            # 함수의 return 값을 i로 출력 (generator) -> 이것이 소수
            multiples.update(range(i * 1, n + 1, i)) # i의 배수를 전부 추가함

print(list(eratosthenes(100)))