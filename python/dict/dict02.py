student = {
    'name': 'Kim',
    'python': 85,
    'javascript': 90,
    'html': 75
}

ft = input('열람하실 과목의 이름을 입력해주세요 : ')
ftScore = int(input('해당 과목의 변경할 점수를 입력해주세요 : '))

student[ft] = ftScore
print(ft, '과목의 점수는 :' , student.get(ft))