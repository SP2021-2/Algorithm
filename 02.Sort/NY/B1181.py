# 백준 1181 - 단어 정렬
# 후기
# - 더 효과적인 방법이 있나? 흠

N = int(input())

words = []

for i in range (N) :
    word = input()
    words.append((len(word), word))

words = list(set(words))

words.sort()

for i in range (len(words)) :
    print(words[i][1])