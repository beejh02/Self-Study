import sys

S = sys.stdin.readline().strip()

psum = [[0 for _ in range(len(S))] for _ in range(26)]

for i in range(len(S)):
    if(i > 0):
        for j in range(26):
            psum[j][i] = psum[j][i-1]
    psum[ord(S[i]) - ord('a')][i] += 1

Q = int(sys.stdin.readline())

for _ in range(Q):
    question = list(map(str, sys.stdin.readline().split()))
    char = question[0]
    question[1] = int(question[1])
    question[2] = int(question[2])
    
    idx = ord(char) - ord('a')

    if question[1] > 0:
        print(psum[idx][question[2]] - psum[idx][question[1]-1])
    else:
        print(psum[idx][question[2]])