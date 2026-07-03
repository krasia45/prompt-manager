categories = ["테스트 생성", "이미지 생성", "영상 생성", "페르소나", "자동화", "기타"]

prompts = [
    {
        "title": "노코드 자동화 워크플로우 설계 도우미",
        "category": "자동화",
        "content": "당신은 업무 자동화 전문가입니다. '매일 아침 특정 키워드가 포함된 이메일을 확인하고, 이를 구글 스프레드시트에 자동으로 기록한 뒤, 슬랙(Slack) 팀 채널에 요약본을 공유하는 루틴'이 있습니다. 이 반복 업무를 Make나 Zapier 같은 노코드 툴을 활용해 자동화할 수 있도록 Trigger(시작 이벤트)와 Action(처리 동작)을 단계별로 시각적 워크플로우 구조를 설계해 주세요. 추가로 조건 분기가 필요한 지점과 팁도 함께 알려주세요.",
        "favorite": False
    },
    {
        "title": "Make vs Zapier 도구별 장단점 비교 분석",
        "category": "자동화",
        "content": "노코드 자동화 파이프라인을 구축하려고 합니다. 동일한 자동화 워크플로우(예: 이메일 수신 시 데이터 추출 및 메신저 알림)를 구현할 때, Make(과거 Integromat)와 Zapier 두 가지 플랫폼의 작동 원리상 차이점과 각각의 뚜렷한 장단점을 근거를 들어 비교 분석해 주세요. 특히 비용, 사용 편의성, 조건 분기 설정의 자유도 측면을 중심으로 비교해 주시기 바랍니다.",
        "favorite": False
    },
    {
        "title": "업무 프로세스 분석 및 자동화 가능성 진단",
        "category": "자동화",
        "content": "현재 팀 내에서 수작업으로 진행 중인 업무 리스트를 분석하여 자동화 파이프라인을 설계하고자 합니다. '단순히 돌아가기만 하면 된다'를 넘어, 어떤 수동 업무가 자동화하기에 가장 적합한지 판단하는 기준(예: 반복 빈도, 데이터 형식의 일관성, 소요 시간 등)을 제시해 주고, 수작업 루틴을 Trigger와 Action 구조로 변환할 때 체크해야 할 핵심 질문 5가지를 작성해 주세요.",
        "favorite": False
    }
]

def show_menu():
    print("\n=== 나만의 프롬프트 관리 ===")
    print("1. 프롬프트 추가")
    print("2. 프롬프트 목록")
    print("3. 카테고리별 조회")
    print("4. 프롬프트 검색")
    print("5. 프롬프트 상세 보기")
    print("6. 즐겨찾기 관리")
    print("7. 즐겨찾기 목록")
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

def manage_favorite():
    print("\n=== 즐겨찾기 관리 ===")
    try:
        idx = int(input("즐겨찾기 설정/해제할 번호 입력: ")) - 1
        if 0 <= idx < len(prompts):
            prompts[idx]["favorite"] = not prompts[idx]["favorite"]
            status = "추가" if prompts[idx]["favorite"] else "해제"
            print(f"'{prompts[idx]['title']}' 프롬프트를 즐겨찾기에 {status}했습니다!")
        else:
            print("⚠ 해당 번호의 프롬프트가 없습니다.")
    except ValueError:
        print("⚠ 숫자만 입력해주세요.")

def show_favorites():
    print("\n=== 즐겨찾기 목록 ===")
    count = 0
    for idx, p in enumerate(prompts, 1):
        if p["favorite"]:
            print(f"{idx}. [{p['category']}] {p['title']} ⭐")
            count += 1
            
    if count == 0:
        print("즐겨찾기된 프롬프트가 없습니다.")
    else:
        print(f"\n총 {count}개의 즐겨찾기")

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
    elif user_choice == "6":
        manage_favorite()
    elif user_choice == "7":
        show_favorites()
    else:
        print("⚠ 잘못된 번호입니다. 0~7 사이의 숫자를 입력해주세요.")