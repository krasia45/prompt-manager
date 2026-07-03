def show_menu():
    print("\n=== 나만의 프롬프트 관리 ===")
    print("1. 프롬프트 추가")
    print("2. 프롬프트 목록")
    print("0. 종료")
    print("=============================")

while True:
    show_menu()
    user_choice = input("선택: ").strip()
    if user_choice == "0":
        print("프로그램을 종료합니다. 이용해 주셔서 감사합니다!")
        break
    elif user_choice == "1":
        # TODO: 프롬프트 추가 기능
        pass
    elif user_choice == "2":
        # TODO: 프롬프트 목록 기능
        pass
    else:
        print("잘못된 선택입니다. 다시 시도해 주세요.")