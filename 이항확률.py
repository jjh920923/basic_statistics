import math

def binomial_probability(n, X, p):
    prob = (math.factorial(n) / (math.factorial(n-X) * math.factorial(X))) * math.pow(p, X) * math.pow(1-p, n-X)
    prob = float(format(prob, ".3f"))
    return prob

binomial_probability(10, 3, 1/5)

# 예제 5-19 (한 밤중 집에 혼자 있을 때 느끼는 공포에 대한 조사)
# 미국인의 5%는 한 밤중에 집에 혼자 있을 때 공포를 느낀다고 한다.
# 20명의 미국인을 확률적으로 선택할 때, 다음의 확률을 구하시오.
# a. 한 밤중에 집에 혼자 있을 때 공포를 느끼는 사람이 5명인 경우
# b. 한 밤중에 집에 혼자 있을 때 공포를 느끼는 사람이 많아야 3명인 경우
# c. 한 밤중에 집에 혼자 있을 때 공포를 느끼는 사람이 최소한 3명인 경우

# 문제 a
binomial_probability(20, 5, 0.05)

# 문제 b
result = 0
for i in range(4):
    result = result + binomial_probability(20, i, 0.05)
print(result)

# 문제 c
result = 0
for i in range(3):
    result = result + binomial_probability(20, i, 0.05)
answer = float(format(1 - result, ".3f"))
print(answer)
