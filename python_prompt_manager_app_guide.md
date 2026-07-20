# 📘 [심화] 파이썬 프롬프트 관리자 & 앱 개발 완벽 가이드

본 문서는 실제 동작하는 GenAI 프롬프트 관리 콘솔 앱을 직접 구현하며, 파이썬 기초 및 앱 개발 필수 개념, Git 버전 관리를 체계적으로 마스터하기 위한 통합 실습 가이드입니다.

---

## 1. 🚀 프로젝트 개요 및 앱 아키텍처

### 1) 목적
* **실무형 코딩 역량 강화:** 단순 문법 학습을 넘어, 사용자의 입력을 받고 데이터를 가공·저장하며 상태를 관리하는 **완전한 구조의 소프트웨어**를 직접 구축합니다.
* **앱 개발 사고방식 체득:** 데이터 구조 설계, 예외 방어, 파일 기반 영속성(Persistence), 기능 모듈화 등 실제 앱 개발에 필수적인 아키텍처 패턴을 익힙니다.

### 2) 앱의 필수 구현 기능 (CRUD + α)
1. **Create (생성):** 새로운 프롬프트(제목, 내용, 카테고리, 즐겨찾기 여부) 추가
2. **Read (조회):** 전체 프롬프트 목록 출력 및 상세 내용 확인
3. **Update (수정):** 기존 프롬프트의 내용 또는 즐겨찾기 상태 변경
4. **Delete (삭제):** 불필요한 프롬프트 제거
5. **Search & Filter (검색 및 필터링):** 키워드 검색 및 카테고리별 필터링
6. **Data Persistence (파일 입출력):** 프로그램이 종료되어도 데이터가 유지되도록 JSON 파일 저장/불러오기 연동

---

## 2. 🐍 파이썬 및 앱 개발 필수 문법 레퍼런스

실제 애플리케이션 개발에서 가장 빈번하게 사용되는 핵심 파이썬 문법과 자료구조입니다.

### 1) 자료구조 및 데이터 모델링 (Data Modeling)
* **변수 (Variable):** 앱의 설정이나 상태를 담는 메모리 이름표
  ```python
  app_name = "PromptHub"
  is_running = True
  ```
* **리스트 (List) & 딕셔너리 (Dictionary):** 앱의 상태(State)와 데이터베이스 역할을 하는 핵심 구조
  * 리스트: 순서가 있는 데이터의 모음 (`[]`)
  * 딕셔너리: 속성(Key)과 값(Value)을 매핑하여 하나의 객체를 표현 (`{}`)
  ```python
  # List of Dictionaries 구조 (프롬프트 데이터베이스 모델)
  prompts = [
      {"id": 1, "title": "번역", "content": "영어로 번역해줘", "category": "텍스트", "fav": True},
      {"id": 2, "title": "코드리뷰", "content": "버그를 찾아줘", "category": "개발", "fav": False}
  ]
  ```
* **집합 (Set):** 중복을 허용하지 않는 데이터 모음 (등록된 카테고리 종류 추출 등에 활용)
  ```python
  categories = {"텍스트", "개발", "업무", "개발"}  # 결과: {'텍스트', '개발', '업무'}
  ```

### 2) 제어문과 흐름 제어 (Control Flow)
* **조건문 (`if` / `elif` / `else`):** 사용자의 메뉴 선택이나 예외 상황 분기 처리
  ```python
  if menu == "1":
      show_list()
  elif menu == "2":
      add_item()
  else:
      print("잘못된 입력입니다.")
  ```
* **반복문 (`while` / `for`):**
  * `while True`: 사용자가 종료를 선택할 때까지 앱의 메인 루프(Main Loop) 유지
  * `for ... in ...`: 리스트나 딕셔너리를 순회(Iteration)하며 목록 출력 및 검색 수행
  ```python
  # enumerate를 활용한 인덱스 번호 부여 출력
  for idx, p in enumerate(prompts, start=1):
      print(f"{idx}. {p['title']}")
  ```

### 3) 함수와 모듈화 (Functions & Modularization)
* 코드를 기능별로 분리하여 유지보수성을 높이고 가독성을 극대화합니다.
  ```python
  def get_favorite_count(prompt_list):
      """즐겨찾기된 프롬프트 개수를 계산하여 반환하는 함수"""
      return sum(1 for p in prompt_list if p["fav"])
  ```

### 4) 예외 처리 (Error Handling - Try / Except)
* 사용자의 잘못된 입력(예: 숫자를 입력해야 하는데 문자를 입력)으로 인해 앱이 강제 종료(Crash)되는 것을 방지합니다.
  ```python
  try:
      menu_num = int(input("메뉴 선택: "))
  except ValueError:
      print("⚠️ 숫자만 입력할 수 있습니다.")
  ```

### 5) 파일 입출력 및 모듈 (JSON 영속성)
* 앱이 종료되어도 데이터가 날아가지 않도록 외부 파일(`json`)로 저장하고 불러오는 기술입니다.
  ```python
  import json
  import os

  DATA_FILE = "prompts.json"

  def save_data(data):
      with open(DATA_FILE, "w", encoding="utf-8") as f:
          json.dump(data, f, ensure_ascii=False, indent=4)
  ```

---

## 3. 🌿 Git & GitHub 버전 관리 전략 (App Dev Workflow)

실무 개발 환경에서는 코드를 안전하게 관리하고 협업하기 위해 Git 브랜치 전략을 사용합니다.

### 1) 핵심 명령어 요약
* `git init`: 현재 프로젝트 폴더를 Git 저장소로 변환
* `git status`: 현재 변경된 파일 상태 확인
* `git add .`: 변경된 파일을 스테이징(Stage) 영역에 올림
* `git commit -m "메시지"`: 변경 이력을 스냅샷으로 기록
* `git branch [이름]`: 새로운 브랜치 생성
* `git checkout [이름]` 또는 `git switch [이름]`: 브랜치 이동
* `git merge [이름]`: 다른 브랜치의 작업을 현재 브랜치에 병합
* `git push origin [브랜치명]`: 원격 GitHub 저장소에 업로드

### 2) 미션 필수: Git 브랜치 워크플로우 실습
기능별로 브랜치를 나누어 개발하는 습관은 앱 개발의 기본입니다.
```bash
# 1. 메인 브랜치에서 시작
git checkout main

# 2. 기능 개발용 브랜치 생성 및 이동 (예: 목록 조회 기능)
git checkout -b feature/list-view

# 3. 코드 작성 및 커밋
git add .
git commit -m "feat: 프롬프트 목록 조회 및 상세 보기 기능 추가"

# 4. 메인 브랜치로 복귀 후 병합
git checkout main
git merge feature/list-view

# 5. 최종 원격 저장소에 반영
git push origin main
```

---

## 4. 🏗 완성된 앱 소스코드 구조 예시 (Python Prompt Manager)

아래 코드는 위에서 다룬 파이썬 기초, 예외 처리, 함수, 그리고 파일 입출력(JSON)을 모두 통합한 콘솔 앱 완성본입니다.

```python
import json
import os

DATA_FILE = "prompts.json"

def load_prompts():
    """파일에서 프롬프트 데이터를 불러옵니다. 파일이 없으면 기본 샘플 반환"""
    if not os.path.exists(DATA_FILE):
        return [
            {"title": "번역기", "content": "영어로 번역해줘", "category": "텍스트", "fav": False},
            {"title": "코드리뷰", "content": "버그를 찾아줘", "category": "개발", "fav": True}
        ]
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError:
        return []

def save_prompts(prompts):
    """프롬프트 데이터를 JSON 파일로 저장합니다."""
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(prompts, f, ensure_ascii=False, indent=4)

def show_list(prompts):
    print("
--- [ 📋 프롬프트 전체 목록 ] ---")
    if not prompts:
        print("저장된 프롬프트가 없습니다.")
        return
    for idx, p in enumerate(prompts, 1):
        fav = "★" if p["fav"] else "☆"
        print(f"{idx}. [{p['category']}] {p['title']} {fav}")

def add_prompt(prompts):
    print("
--- [ ➕ 새 프롬프트 추가 ] ---")
    title = input("제목: ").strip()
    content = input("내용: ").strip()
    category = input("카테고리 (예: 텍스트/개발/업무): ").strip()
    
    if not title or not content:
        print("⚠️ 제목과 내용은 필수 입력 항목입니다.")
        return
    
    new_item = {
        "title": title, 
        "content": content, 
        "category": category or "기타", 
        "fav": False
    }
    prompts.append(new_item)
    save_prompts(prompts)
    print("✅ 성공적으로 추가 및 저장되었습니다!")

def search_prompts(prompts):
    keyword = input("
검색할 키워드 입력: ").strip().lower()
    results = [p for p in prompts if keyword in p["title"].lower() or keyword in p["content"].lower()]
    
    print(f"
--- [ 🔍 검색 결과 ({len(results)}건) ] ---")
    if not results:
        print("검색 결과가 없습니다.")
        return
    for idx, p in enumerate(results, 1):
        print(f"{idx}. [{p['category']}] {p['title']} - {p['content'][:30]}...")

def main():
    prompts = load_prompts()
    
    while True:
        print("
==================================")
        print(" 💡 PromptHub - 프롬프트 관리 앱")
        print("==================================")
        print("1. 전체 목록 조회")
        print("2. 프롬프트 추가")
        print("3. 프롬프트 검색")
        print("4. 프로그램 종료")
        
        choice = input("메뉴 선택 (1-4): ").strip()
        
        if choice == "1":
            show_list(prompts)
        elif choice == "2":
            add_prompt(prompts)
        elif choice == "3":
            search_prompts(prompts)
        elif choice == "4":
            print("💾 데이터를 저장하고 프로그램을 종료합니다. 안녕히 가세요!")
            break
        else:
            print("⚠️ 잘못된 입력입니다. 1에서 4 사이의 숫자를 입력해주세요.")

if __name__ == "__main__":
    main()
```

---

## 5. 🎯 학습 및 개발 체크리스트 (Self-Check)

- [ ] Python 3.10+ 및 Git 환경 세팅이 완료되었는가?
- [ ] 리스트와 딕셔너리의 구조를 이해하고 앱의 데이터 상태를 모델링했는가?
- [ ] `try-except` 예외 처리를 적용하여 잘못된 입력으로부터 앱의 안정성을 높였는가?
- [ ] `json` 모듈과 파일 입출력(`open`, `dump`, `load`)을 통해 데이터 영속성을 구현했는가?
- [ ] Git 브랜치 전략(`git checkout -b` -> 작업 -> `git merge`)을 실천했는가?
- [ ] GitHub 저장소에 최소 10개 이상의 의미 있는 커밋 이력을 푸시했는가?
