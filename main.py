
questions = [
    {
        "question": "드라마 《도깨비》에서 김신 역을 맡은 배우는?",
        "choices": ["1. 이민호", "2. 공유", "3. 현빈", "4. 송중기"],
        "answer": 2,
        "hint": "도깨비와 저승사자가 등장하는 드라마의 주인공이야."
    },
    {
        "question": "드라마 《사랑의 불시착》에서 윤세리 역을 맡은 배우는?",
        "choices": ["1. 손예진", "2. 김태희", "3. 박신혜", "4. 수지"],
        "answer": 1,
        "hint": "현빈과 함께 주연으로 출연한 배우야."
    },
    {
        "question": "드라마 《이상한 변호사 우영우》에서 우영우의 직업은?",
        "choices": ["1. 의사", "2. 기자", "3. 변호사", "4. 경찰"],
        "answer": 3,
        "hint": "법정에서 의뢰인을 변호하는 직업이야."
    },
    {
        "question": "드라마 《오징어 게임》 참가자들이 입는 옷의 색깔은?",
        "choices": ["1. 빨간색", "2. 파란색", "3. 검은색", "4. 초록색"],
        "answer": 4,
        "hint": "숲이나 잔디에서 흔히 볼 수 있는 색이야."
    },
    {
        "question": "드라마 《태양의 후예》에서 유시진 역을 맡은 배우는?",
        "choices": ["1. 박서준", "2. 송중기", "3. 이종석", "4. 김수현"],
        "answer": 2,
        "hint": "《빈센조》에도 출연한 배우야."
    }
]

print("==============================")
print("        K-Drama Quiz")
print("==============================")

print("등록된 퀴즈 문제 수:", len(questions))

while True:
    print()
    print("1. 퀴즈 시작")
    print("2. 퀴즈 추가")
    print("3. 퀴즈 목록 보기")
    print("4. 최고 점수 확인")
    print("5. 종료")

    choice = input("메뉴를 선택해 주세요: ").strip()

    if choice == "1":
        score = 0

        for question in questions:
            print()
            print(question["question"])

            for choice_text in question["choices"]:
                print(choice_text)

            while True:
                answer = input("정답 번호를 입력해 주세요: ").strip()

                if answer == "":
                    print("빈칸은 입력할 수 없습니다.")
                elif not answer.isdigit():
                    print("숫자만 입력해 주세요.")
                elif answer not in ["1", "2", "3", "4"]:
                    print("1부터 4까지의 숫자를 입력해 주세요.")
                else:
                    break

            if answer == str(question["answer"]):
                print("정답입니다!")
                score = score + 10
            else:
                print("오답입니다!")

        print()
        print("최종 점수:", score, "점")

    elif choice == "2":
        new_question = input("새로운 문제를 입력해 주세요: ").strip()

        new_choices = []

        for i in range(4):
            choice_text = input(str(i + 1) + "번 보기를 입력해 주세요: ").strip()
            new_choices.append(str(i + 1) + ". " + choice_text)

        while True:
            new_answer = input("정답 번호를 입력해 주세요 (1~4): ").strip()

            if new_answer in ["1", "2", "3", "4"]:
                new_answer = int(new_answer)
                break
            else:
                print("1부터 4까지의 숫자를 입력해 주세요.")

        new_hint = input("이 문제의 힌트를 입력해 주세요: ").strip()

        questions.append({
            "question": new_question,
            "choices": new_choices,
            "answer": new_answer,
            "hint": new_hint
        })

        print("새로운 퀴즈가 추가되었습니다!")

    elif choice == "3":
        print("퀴즈 목록을 보여줍니다!")
    elif choice == "3":
        print("퀴즈 목록을 보여줍니다!")

    elif choice == "4":
        print("최고 점수를 확인합니다!")

    elif choice == "5":
        print("게임을 종료합니다.")
        break

    else:
        print("1부터 5까지의 숫자를 입력해 주세요.")
    
        
    
