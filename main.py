def show_menu():
categories = ["텍스트 생성", "이미지 생성", "영상 생성", "페르소나", "자동화", "기타"]

prompts = [
    {
        "title": "블로그 글 작성 도우미",
        "content": "당신은 10년 경력의 블로거입니다. SEO 최적화 글을 작성해주세요.",
        "category": "텍스트 생성",
        "favorite": True
    },
    {
        "title": "제품 썸네일 생성",
        "content": "다음 제품의 매력적인 썸네일 이미지를 3D 스타일로 생성해주세요.",
        "category": "이미지 생성",
        "favorite": False
    },
    {
        "title": "영어 회화 파트너",
        "content": "당신은 친절한 영어 선생님입니다. 일상 대화를 시작해주세요.",
        "category": "페르소나",
        "favorite": False
    }
]    print("\n=== 나만의 프롬프트 관리 ===")
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

        prompt_manager = {
            "categories": categories,
            "prompts": prompts
        }