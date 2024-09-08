#S = 특정문자열
#Q = 질문의 수

#S = input()
#Q = int(input())

S = 'seungjaehwang'
question = list(map(str, input().split()))
question[1] = int(question[1])
question[2] = int(question[2])

psum = [0 for i in range(len(S))]
temp = 0

for i in range(len(S)):
    if(S[i] == question[0]):
        temp += 1
    psum[i] = temp

print(question)
print(psum)
print(S)

print(psum[question[2]] - psum[question[1]])