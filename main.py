import json
import os

# 이벤트 허브(Event Hub) 맞춤형 카테고리 설정
categories = ["이벤트 기획", "타겟 마케팅", "자동화 스크립트", "성과 분석", "기타"]
DATA_FILE = "prompts.json"

# 초기 기본 데이터 (이벤트 허브 맞춤형 프롬프트 샘플 4개 이상 포함)
default_prompts = [
    {
        "title": "대형 브랜드 및 소상공인 연계 이벤트 기획안 작성",
        "category": "이벤트 기획",
        "content": "당신은 전문 프로모션 기획자입니다. 대형 브랜드의 할인 프로모션과 인근 소상공인의 특가 이벤트를 하나의 플랫폼에서 아우르는 통합 이벤트 기획안의 목차와 핵심 전략을 작성해 주세요.",
        "favorite": True,
        "views": 5
    },
    {
        "title": "외국인 관광객 및 타겟 고객 참여 유도 문구",
        "category": "타겟 마케팅",
        "content": "이벤트 허브 플랫폼에 접속한 외국인 관광객과 로컬 고객들의 시선을 사로잡을 수 있는 직관적이고 매력적인 푸시 알림 및 배너 참여 유도 문구를 각 3가지씩 제안해 주세요.",
        "favorite": False,
        "views": 2
    },
    {
        "title": "이벤트 당첨자 추첨 자동화 파이썬 스크립트",
        "category": "자동화 스크립트",
        "content": "참가자 명단이 담긴 리스트에서 무작위로 당첨자를 공정하게 추첨하는 파이썬 코드를 작성해 주세요. 중복 당첨 방지 로직과 결과 출력 포맷을 포함해 주시기 바랍니다.",
        "favorite": False,
        "views": 8
    },
    {
        "title": "마케팅 프로모션 성과 분석 및 지표 리포팅",
        "category": "성과 분석",
        "content": "이벤트 진행 후 수집된 조회수, 참여율, 전환율 데이터를 바탕으로 프로모션의 효과를 진단하고 개선점을 도출하기 위한 데이터 분석 프레임워크와 체크리스트를 작성해 주세요.",
        "favorite": True,
        "views": 12
    }
]

def load_data():
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            return default_prompts.copy()
    return default_prompts.copy()

prompts = load_data()

def save_data():
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(prompts, f, ensure_ascii=False, indent=4)

def show_menu():
    print("\n=== 이벤트 허브 프롬프트 관리 ===")
    print("1. 프롬프트 추가")
    print("2. 프롬프트 목록")
    print("3. 카테고리별 조회")
    print("4. 프롬프트 검색")
    print("5. 프롬프트 상세 보기 (조회수 증가)")
    print("6. 즐겨찾기 관리")
    print("7. 즐겨찾기 목록")
    print("8. 프롬프트 수정 및 삭제")
    print("9. 조회수 기준 Top 목록 정렬")
    print("10. Markdown 파일로 내보내기")
    print("0. 저장 및 종료")
    print("================================")

def add_prompt():
    print("\n=== 프롬프트 추가 ===")
    title = input("제목: ").strip()
    content = input("내용: ").strip()
    
    if not title or not content:
        print("⚠ 제목과 내용은 비어있을 수 없습니다.")
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
        "favorite": False,
        "views": 0
    }
    prompts.append(new_item)
    save_data()
    print("🎉 프롬프트가 성공적으로 추가되고 저장되었습니다!")

def show_list():
    print("\n=== 프롬프트 목록 ===")
    if not prompts:
        print("등록된 프롬프트가 없습니다.")
        return

    for idx, p in enumerate(prompts, 1):
        star = "⭐" if p["favorite"] else ""
        print(f"{idx}. [{p['category']}] {p['title']} {star} (조회수: {p.get('views', 0)})")
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
            print(f"{idx}. {p['title']} {star} (조회수: {p.get('views', 0)})")
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
            p["views"] = p.get("views", 0) + 1  # 조회수 증가
            save_data()
            star = "⭐" if p["favorite"] else "없음"
            print("─" * 30)
            print(f"제목: {p['title']}")
            print(f"카테고리: {p['category']}")
            print(f"즐겨찾기: {star}")
            print(f"조회수: {p['views']}")
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
            save_data()
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

def update_or_delete_prompt():
    print("\n=== 프롬프트 수정 및 삭제 ===")
    try:
        idx = int(input("작업할 프롬프트 번호 입력: ")) - 1
        if not (0 <= idx < len(prompts)):
            print("⚠ 해당 번호의 프롬프트가 없습니다.")
            return
        
        mode = input("1) 수정 2) 삭제 중 선택: ").strip()
        if mode == "1":
            new_title = input(f"새 제목 (기존: {prompts[idx]['title']}): ").strip()
            new_content = input(f"새 내용 (기존: {prompts[idx]['content']}): ").strip()
            if new_title:
                prompts[idx]["title"] = new_title
            if new_content:
                prompts[idx]["content"] = new_content
            save_data()
            print("🎉 프롬프트가 수정되었습니다!")
        elif mode == "2":
            removed = prompts.pop(idx)
            save_data()
            print(f"🗑 '{removed['title']}' 프롬프트가 삭제되었습니다.")
        else:
            print("⚠ 올바른 번호를 선택해주세요.")
    except ValueError:
        print("⚠ 숫자만 입력해주세요.")

def show_top_views():
    print("\n=== 조회수 기준 Top 목록 ===")
    sorted_prompts = sorted(prompts, key=lambda x: x.get("views", 0), reverse=True)
    for idx, p in enumerate(sorted_prompts, 1):
        print(f"{idx}. [{p['category']}] {p['title']} - 조회수: {p.get('views', 0)}")

def export_to_markdown():
    print("\n=== Markdown 내보내기 ===")
    with open("prompts_export.md", "w", encoding="utf-8") as f:
        f.write("# Event Hub Prompts Export\n\n")
        for cat in categories:
            f.write(f"## 카테고리: {cat}\n\n")
            for p in prompts:
                if p["category"] == cat:
                    f.write(f"### {p['title']}\n")
                    f.write(f"- **즐겨찾기**: {'⭐' if p['favorite'] else '없음'}\n")
                    f.write(f"- **조회수**: {p.get('views', 0)}\n\n")
                    f.write(f"{p['content']}\n\n---\n\n")
    print("🎉 'prompts_export.md' 파일로 성공적으로 내보냈습니다!")

while True:
    show_menu()
    user_choice = input("선택: ").strip()
    
    if user_choice == "0":
        save_data()
        print("데이터를 저장하고 프로그램을 종료합니다.")
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
    elif user_choice == "8":
        update_or_delete_prompt()
    elif user_choice == "9":
        show_top_views()
    elif user_choice == "10":
        export_to_markdown()
    else:
        print("⚠ 잘못된 번호입니다. 0~10 사이의 숫자를 입력해주세요.")