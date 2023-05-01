N = int(input())
student_responses = []
answers = []
for i in range(N):
  student_responses.append(input())
for i in range(N):
  answers.append(input())

correct = 0
for i in range(N):
  if student_responses[i] == answers[i]:
    correct += 1

print(correct)
