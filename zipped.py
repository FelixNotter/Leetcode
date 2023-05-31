# Enter your code here. Read input from STDIN. Print output to STDOUT
N_X = input()

N = N_X.split()[0]
X = N_X.split()[1]
subject_scores = []
for i in range(int(X)):
    subject_scores.append(input().split())


for ans in zip(*subject_scores):
    total = 0

    for num in ans:
        total += float(num)
    print(total/int(X))
    
