# 🪵 모닥불 (Modakbul) 요구사항 명세서

**버전:** 1.0.0  
**최근 수정일:** 2026-04-10  
**프로젝트 성격:** 실시간 휘발성 익명 커뮤니티 백엔드 API

---

## 1. User Stories

### Epic 1: 사용자 인증 및 권한 (Auth)
- Goal: 방문자가 회원가입을 하고 로그인하여 서비스의 인증된 사용자가 된다.

**US-01** : 사용자는 서비스에 회원가입을 할 수 있다.
- Description:
    - As a : 방문자
    - I want to : ID와 Password 등의 정보를 입력하여 회원가입을 하여
    - So that : 자신만의 계정을 생성하고 모닥불 서비스에 참여할 수 있다.
- Acceptance Criteria:
    - ID, Password, Nickname이 누락 없이 입력되어야 한다.
    - 이미 존재하는 아이디로 가입 시도 시, 409 Conflict 에러를 반환한다.
    - 비밀번호는 DB에 평문으로 저장되지 않고 해싱(예: bcrypt) 처리되어야 한다.
    - 성공 시 201 Created와 함께 가입 완료 응답을 반환한다.

**US-02** : 사용자는 생성한 계정으로 로그인을 할 수 있다.
- Description:
    - AS a : 가입된 회원
    - I want to : 본인의 계정 정보로 로그인하여
    - So that : 모닥불 피우기, 장작 넣기 등의 인증된 사용자 권한을 얻을 수 있다.
- Acceptance Criteria:
    - 가입되지 않은 ID거나 Password가 틀릴 경우, 401 Unauthorized를 반환한다.
    - 올바른 자격 증명 시, 서버는 인증 토큰(또는 세션)을 발급하여 반환한다.

**US-03** : 사용자는 로그인된 계정을 로그아웃할 수 있다.
- Description:
    - As a : 로그인한 회원
    - I want to : 서비스에서 안전하게 로그아웃하여
    - So that : 내 기기나 환경에서 다른 사람이 내 계정을 도용하지 못하도록 보호할 수 있다.
- Acceptance Criteria:
    - 서버는 클라이언트의 인증 토큰(또는 세션)을 무효화 처리한다.
    - 성공적으로 처리되면 200 OK 응답을 반환한다.

### Epic 2: 모닥불(게시물) 관리
- Goal: 사용자가 핫이슈를 생산하고, 살아있는 이슈의 피드를 조회한다.

**US-04** : 사용자는 새로운 모닥불(Topic)을 피울 수 있다.
- Description:
    - As a : 로그인한 회원
    - I want to : 새로운 주제나 이슈를 텍스트로 작성하여
    - So that : 사람들의 관심과 반응을 모을 수 있다.
- Acceptance Criteria:
    - 서버는 요청 시 인증된 사용자인지 검증해야 하며, 미인증 시 요청을 차단한다.
    - 게시물 저장 시, 작성자의 User ID를 외래키로 함께 매핑하여 저장한다.
    - 초기 상태값으로 적절한 만료일(예: 생성 후 +1시간)을 자동 설정한다.

**US-05** : 사용자는 현재 가장 뜨거운 모닥불 피드(전체 목록)를 볼 수 있다.
- Description:
    - As a : 비로그인 방문자를 포함한 모든 사용자
    - I want to : 살아있는 게시물 목록을 확인하여
    - So that : 현재 사람들이 가장 많이 다루는 이슈가 무엇인지 알 수 있다.
- Acceptance Criteria:
    - 로그인 여부와 상관없이 누구나 조회(GET)할 수 있어야 한다.
    - 만료일시가 지나지 않은 데이터만 필터링하여 반환하며, 지연 삭제 로직을 적용한다.
    - 남은 수명이 긴 순서대로 정렬하여 반환한다.
    - 한 번에 반환하는 게시물의 수(예: 20개)를 제한하거나 페이징(커서/오프셋) 처리하여 반환한다.

**US-06** : 사용자는 특정 모닥불의 상세 내용과 장작들을 볼 수 있다.
- Description:
    - As a : 비로그인 방문자를 포함한 모든 사용자
    - I want to : 특정 모닥불에 달린 댓글 목록을 함께 조회하여
    - So that : 다른 사람들의 구체적인 반응을 읽고 흐름을 파악할 수 있다.
- Acceptance Criteria:
    - 만료일시가 지난 게시물의 ID로 접근 시 404 Not Found 또는 403 Forbidden을 반환한다.
    - 유효한 게시물일 경우, 본문 데이터와 함께 해당 모닥불에 속한 댓글 리스트를 반환한다.


### Epic 3: 장작(댓글) 관리
- Goal: 사용자가 기존 모닥불에 참여하여 의견을 남기고 수명을 연장시킨다.

**US-7** : 사용자는 모닥불에 장작(Comment)을 넣어 불씨를 살릴 수 있다.
- Description:
    - As a : 로그인한 회원
    - I want to : 특정 게시물에 댓글을 달아
    - So that : 의견을 나누고 해당 모닥불이 꺼지지 않게 수명을 연장할 수 있다.
- Acceptance Criteria (인수 조건):
    - 서버는 요청 시 인증된 사용자인지 검증해야 한다.
    - 댓글 저장 시, 작성자의 User ID와 속한 모닥불의 Topic ID를 모두 매핑한다.
    - 이미 만료일이 지난 모닥불에는 댓글 작성을 거부(404/403)해야 한다.
    - 댓글 저장 성공 즉시, 해당 모닥불(Topic)의 만료일을 일정 시간(예: +10분) 연장한다.



## 2. System Stories (Functional Requirements)

### [F-01] 데이터 조회 지연 평가 (Lazy Evaluation)
- **설명:** 백그라운드 삭제 여부와 상관없이, 모든 조회 요청 시 서버 시간과 `expires_at`을 비교한다.
- **상세:**
  - `GET /modakbul`: 쿼리 레벨에서 `WHERE expires_at > NOW()` 필터링 수행.
  - `GET /modakbul/{id}`: DB에서 객체 로드 후 `if obj.expires_at < NOW(): raise HTTPException(404)`.

### [F-02] 데이터베이스 연동 및 캡슐화
- **설명:** SQLite 및 SQLAlchemy를 사용하여 데이터를 영구 저장하되, 라우터는 직접 DB 쿼리를 날리지 않는다.
- **상세:**
  - `crud/` 폴더 내 독립 함수로 구현.
  - 모든 날짜 처리는 파이썬 `datetime.utcnow()`를 기준으로 통일.

### [F-03] (추후 구현) 가비지 컬렉터 (Garbage Collector)
- **설명:** 시스템 자원 최적화를 위해 만료된 데이터를 물리적으로 삭제한다.
- **상세:**
  - 주기적으로 `DELETE FROM modakbul WHERE expires_at < NOW()` 수행.

---

## 3. 기술 스택 (Tech Stack)

- **언어 및 프레임워크:** Python 3.11+, FastAPI
- **데이터베이스:** SQLite (파일 기반)
- **ORM:** -
- **개발 환경:** VSCode, venv (가상환경)

---

## 4. 디렉토리 구조 (Directory Structure)

```text
modakbul_backend/
├── docs/                   # 비코드 문서 (기획, 설계)
│   ├── requirements/       # User Story, 명세서
│   └── architecture/       # ERD, Sequence Diagram
├── api/                    # API 라우터 (FastAPI Endpoint)
├── crud/                   # DB 접근 함수 (Create, Read, Update, Delete)
├── db/                     # DB 연결 및 모델 (SQLAlchemy Models)
├── schemas/                # 데이터 검증 모델 (Pydantic Schemas)
├── core/                   # 설정 및 공통 유틸리티
└── main.py                 # 앱 실행 엔트리 포인트