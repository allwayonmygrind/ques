student = {
    'name': 'Kim',
    'python': 85,
    'javascript': 90,
    'html': 75
}

ft = input('점수 열람을 원하시는 과목을 입력해주세요 : ')

print(student.get(ft,'없는 과목입니다'))