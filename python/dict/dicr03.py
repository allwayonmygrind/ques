student = {
    'python': 85,
    'javascript': 90,
    'html': 75
}

ft = input('열람하려는 과목을 입력해주십시오 : ')

score = student.get(ft)

if score is None :
    print('없는 과목입니다')
elif score >= 80 :
    print('합격')
else :
    print('불합격')

