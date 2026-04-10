# 모닥불 (Modakbul)

**2026-Spring Software Engineering Team Project**

**Instructor:** Jaekwon Lee

---

## 👨‍💻 Team Members & Roles

| Name | Role & Responsibilities | GitHub Profile |
| --- | --- | --- |
| **김건우** | Role 1 / ~ | [Github Profile](https://github.com/goukimesatz) |
| **나르지기토브 예르도스** | Role 2 / ~ | [Github Profile](https://github.com/YerdosNar) |
| **전상준** | Role 3 / ~ | [Github Profile](https://github.com/nclsang) |
| **차경호** | Role 4 / ~ | [Github Profile](https://github.com/Homeria) |

---

## 📖 Project Overview

**모닥불 (Modakbul)**는 현재 화제가 되는 이슈에 대해 실시간으로 밀도 있게 소통할 수 있는 익명 커뮤니티 백엔드 API 입니다. 사용자들이 지속적으로 '장작(댓글)'을 추가하지 않으면 게시물의 '화력(HP)'이 줄어들고 결국 파괴(삭제)되는 시스템을 통해, 언제 접속하든 지금 가장 활발하게 논의되는 신선한 주제만 남게 됩니다.

---

## 🎯 Project Vision Statement

- **Target Users:** 영구적인 디지털 발자국이 남는 것을 부담스러워하며 실시간 이슈에 대해 소통하고 싶은 익명 사용자
- **Problem or Need:** 기존 커뮤니티는 한 번 작성된 글이 영구 보존되어 정보의 피로감과 불필요한 흔적을 남김.
- **Product Category:** 실시간 휘발성 익명 커뮤니티 API 서버.
- **Key Benefit & Differentiation:** 게시물에 '화력(HP)'이라는 수명을 부여하여, 사용자의 참여(장작)가 없는 게시물은 데이터베이스에서 영구적으로 자동 소멸됨.

---

## 📌 Project Goals & Scope

- **Business Goals:** 실시간 HP 감소 및 게시물 소멸 로직 처리 시스템 구축.
- **In-Scope (Major Features):**
    - 모닥불(게시물) 생성 및 장작(댓글 등) 추가를 위한 RESTful API 구현
    - ▲ WebSocket을 활용한 실시간 화력(HP) 상태 브로드캐스팅 및 클라이언트 동기
    - 일정 주기로 화력(HP)을 감소시키고 0이 될 경우 데이터를 삭제하는 백그라운드 스케줄러(Background Scheduler)
	- 세션/IP 기반 익명 사용자 기준 화력 관리
- **Out-of-Scope:**
    - 복잡한 프론트엔드 UI/UX 구현
    - 삭제된 게시물의 영구 보존용 아카이빙 시스템
    - 회원가입 및 인증 절차
	- 화력 유지를 위한 악성 행동을 방지하는 보안 체계

---

## 👥 Stakeholders & Users

- **Stakeholders:** 개발 팀(팀원 전체), 교수님 및 조교님.
- **Requirements:** 백엔드 아키텍처가 실시간 데이터 처리와 백그라운드 작업을 얼마나 효율적으로 처리하는지 구조작 타당성 검증.
- **Users:** 휘발성 이슈 토론을 즐기는 익명의 사용자.

---

## 📅 Milestones

- **Milestone 1:** 커뮤니티 기본 API 및 데이터베이스 아키텍처 구축 (Week 1 ~ Week 2)
	- **목표:** 게시물(모닥불) 관리용 기본 REST API 엔드포인트 및 정적 데이터베이스 환경 완성
	- **주요 작업 (Tasks):**
		- 관계형 DB 스키마 설계 (카테고리, 모닥불 모델)
		- 코드 아키텍처 설계
		- FastAPI 서버 초기 환경 세팅 및 라우팅 구조 설계
		- Pydantic을 이용한 클라이언트 요청 데이터(Payload) 검증 로직 추가
		- **GET/POST/DELETE:** 모닥불 목록 조회, 신규 모닥불 및 카테고리 생성, 수동 삭제 API 구현
	- **산출물 (Deliverables):** DB 스키마 명세서, CRUD 기준의 API 라우터, API 명세서
		
- **Milestone 2:** 모닥불(HP) 코어 비즈니스 로직 및 백그라운드 통합 (Week 3 ~ Week 5)
	- **목표:** 시간에 따른 HP 감소 및 자동 소멸 로직
	- **주요 작업 (Tasks):**
		- 비동기 백그라운드 작업(Background Tasks)을 활용한 주기적인 모닥불 HP 감소 스케줄러 구현
		- **PUT:** '장작 넣기(게시물, 댓글 등)' 처리 및 해당 모닥불의 HP 증가 로직 구현
		- 데이터베이스 트랜잭션 및 동시성 제어 (HP 증감 충돌 해결)
	- **산출물 (Deliverables):** 상태 자동 변화 및 소멸 로직이 통합된 백그라운드 스케줄러 코드

- **Milestone 3:** 실시간 통신 최적화 및 최종 배포 (Week 6 ~ Week 7)
	- **목표:** 주기적 폴링(Polling)의 단점을 해결하는 실시간 데이터 동기화 환경 구축 및 배포
	- **주요 작업 (Tasks):**
		- WebSocket 연결을 도입하여 활성화된 모닥불의 남은 HP와 신규 장작 상태를 클라이언트에게 실시간 브로드캐스팅
		- 백엔드 통합 비즈니스 로직 테스트
		- 전체 코드 리팩토링 및 최종 성능 최적화
	- **산출물 (Deliverables):** WebSocket 기반 실시간 통신 서버 및 최종 프로젝트 결과 보고서
	
---

## 🛠 Tech Stack

- **Backend Framework:** FastAPI
- **Database & ORM:** ~
- **Real-time Communication:** WebSocket
- **Deployment & Tools:** ~