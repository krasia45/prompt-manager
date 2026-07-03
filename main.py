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
def add_prompt():
    print("\n=== 프롬프트 추가 ===")
    title = input("제목: ").strip()
    content = input("내용: ").strip()
    
    if not title or not content:
        print("⚠ 제목과 내용은 비어있을 수 없습니다. 다시 시도해주세요.")
        return

    print("\n카테고리 선택:")
    for idx, cat in enumerate(categories, 1):
        print(f"{idx}) {cat}")
    
    try:
        cat_choice = int(input("선택: "))
        if 1 <= cat_choice <= len(categories):
            category = categories[cat_choice - 1]
        else:
            category = "기타"
    except ValueError:
        category = "기타"

    new_item = {
        "title": title,
        "content": content,
        "category": category,
        "favorite": False
    }
    prompts.append(new_item)
    print("🎉 프롬프트가 성공적으로 추가되었습니다!")

    def show_list():
    print("\n=== 프롬프트 목록 ===")
    if not prompts:
        print("등록된 프롬프트가 없습니다.")
        return

    for idx, p in enumerate(prompts, 1):
        star = "⭐" if p["favorite"] else ""
        print(f"{idx}. [{p['category']}] {p['title']} {star}")
    print(f"\n총 {len(prompts)}개의 프롬프트")

    def show_by_category():
    print("\n=== 카테고리별 조회 ===")
    for idx, cat in enumerate(categories, 1):
        print(f"{idx}) {cat}")
    
    try:
        choice = int(input("선택: "))
        selected_cat = categories[choice - 1]
    except (ValueError, IndexError):
        print("⚠ 잘못된 선택입니다.")
        return

    print(f"\n[{selected_cat}] 카테고리 프롬프트:")
    count = 0
    for idx, p in enumerate(prompts, 1):
        if p["category"] == selected_cat:
            star = "⭐" if p["favorite"] else ""
            print(f"{idx}. {p['title']} {star}")
            count += 1
            
    if count == 0:
        print("해당 카테고리에 등록된 프롬프트가 없습니다.")
    else:
        print(f"\n총 {count}개의 프롬프트")
        def search_prompt():
    print("\n=== 프롬프트 검색 ===")
    keyword = input("검색어 입력: ").strip()
    
    if not keyword:
        print("⚠ 검색어를 입력하셔야 합니다.")
        return

    print("\n검색 결과:")
    count = 0
    for idx, p in enumerate(prompts, 1):
        if keyword in p["title"] or keyword in p["content"]:
            star = "⭐" if p["favorite"] else ""
            print(f"{idx}. [{p['category']}] {p['title']} {star}")
            count += 1
            
    if count == 0:
        print("검색 결과가 없습니다.")
    else:
        print(f"\n{count}개의 프롬프트를 찾았습니다.")
        def show_detail():
    print("\n=== 프롬프트 상세 보기 ===")
    try:
        idx = int(input("조회할 프롬프트 번호 입력: ")) - 1
        if 0 <= idx < len(prompts):
            p = prompts[idx]
            star = "⭐" if p["favorite"] else "없음"
            print("─" * 30)
            print(f"제목: {p['title']}")
            print(f"카테고리: {p['category']}")
            print(f"즐겨찾기: {star}")
            print("─" * 30)
            print(f"내용:\n{p['content']}")
            print("─" * 30)
        else:
            print("⚠ 해당 번호의 프롬프트가 존재하지 않습니다.")
    except ValueError:
        print("⚠ 숫자만 입력해주세요.")
while True:
    show_menu()
    user_choice = input("선택: ").strip()
    if user_choice == "0":
        print("프로그램을 종료합니다. 이용해 주셔서 감사합니다!")
        break
    elif user_choice == "1":
        add_prompt()
      
   elif user_choice == "2":
        show_list()
elif user_choice == "3":
        show_by_category()
elif user_choice == "4":
        search_prompt()
elif user_choice == "5":
        show_detail()
    else:
        print("잘못된 선택입니다. 다시 시도해 주세요.")

        prompt_manager = {
            "categories": categories,
            "prompts": prompts
        }