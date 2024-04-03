def find_primes(number: int) -> list:
    # 내가 만든 소수 찾는 알고리즘 코드
    """특정 수 이하의 모든 소수를 찾는 함수

    1. 특정 수 길이의 리스트를 만든다. (에라토스테네스의 체와 동일)
    2. 3부터 시작해 제일 제일 작은 소수를 찾을 때 까지 특정 수의 '절반 이하'의 홀수들을 체크한다. (※ 다른 부분 ※)
    3. 소수가 발견되면 해당 소수의 모든 배수를 소수가 아닌 수로 지정한다. (에라토스테네스의 체와 동일)
    4. 마지막까지 소수로 지정되어 있는 수들만 뽑아내 반환한다. (에라토스테네스의 체와 동일)

    Args:
        number (int): 특정 수

    Returns:
        list: 특정 수 이하의 모든 소수 리스트
    """

    # 특정 수의 길이의 리스트를 생성, False는 소수가 아닌 수를, True는 소수를 나타냄
    # 2의 배수는 소수가 될 수 없으므로 False, True 번갈아가며 생성
    numbers = [False, True] * (number // 2 + 1)
    if number % 2 == 0: del numbers[-1]

    # 위에서 소수인 2가 False로 지정되었으므로 True로 새로 지정
    if number > 1: numbers[2] = True

    # 3부터 특정 수 절반까지의 홀수들을 모두 체크한다
    for i in range(3, number // 2 + 1, 2):
        # 해당 수가 소수인 경우
        if numbers[i]:
            # 해당 수의 모든 배수들을 소수가 아닌 수로 지정한다
            for j in range(i*2, number + 1, i): numbers[j] = False
            
    # 남아있는 소수(True)들을 소수 리스트에 저장한다
    primes = [i for i in range(2, number + 1) if numbers[i]]

    # 소수 리스트 반환
    return primes






def eratosthenes_sieve(n):
    # 인터넷에서 검색한 에라토스테네스의 체 알고리즘을 이용해 만든 코드

    # 2부터 n까지의 모든 수를 포함하는 리스트 생성
    prime_list = [True] * (n+1)
    prime_list[0] = prime_list[1] = False
    
    # 에라토스테네스의 체 알고리즘 적용
    for i in range(2, int(n**0.5)+1): # ----> 왜 루트까지만 계산하는지 모르겠습니다
        if prime_list[i]:
            for j in range(i*i, n+1, i):
                prime_list[j] = False
    
    # 소수만을 담은 리스트 생성
    primes = [i for i in range(2, n+1) if prime_list[i]]
    
    return primes