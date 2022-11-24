# 8기 FINAL 관통 PJT : 영화 추천 알고리즘 기반 커뮤니티 서비스

## 목차

1. [공통 요구 사항](#공통-요구-사항)
2. [필수 요구 사항](#필수-요구-사항)
3.
4.
5.
---

## 공통 요구 사항

### 영화 데이터 기반 추천 서비스 구성
1. 대기열식 추천
  - 좋아하는 장르를 선택시키고, 그것을 기반으로 그 장르 내의 영화들 보여줌
  - 보여준 영화들 중 선택한 영화들을 db에 저장
  - 저장한 영화에서 비슷한 장르 추천
  - 로딩중 만들면 금상첨화
  - 중간중간에 장르는 다르지만 비슷한 배우진, 감독진 등이 포함된 영화를 섞으면 금상첨화

### 영화 추천 알고리즘 구성
- 
### 커뮤니티 서비스 구성
-
### 서비스 관리 및 유지보수
- 

## 개발 환경
 - Python :                 '3.9.13'
 - Django :                 '3.2.13'
 - node.js :               '16.18.0'
 - Django REST Framework:   '3.14.0'
 - Vue 2
---
## 필수 요구 사항
### 개요
- 필수 요구사항은 프로젝트 내에 반드시 포함되어야 합니다.
- 이외의 추가적인 기능 및 반응형 디자인 등은 팀 별로 자유롭게 수행할 수 있습니다.
  - 영화 데이터
  - 영화 추천 알고리즘
  - API
  - 커뮤니티
  - README
  - 기타

### 영화 데이터
- 본 프로젝트는 영화 를 주제로 진행되기 때문에, 영화 정보 데이터를 필수적으로 가지고 있어야 합니다.
- 최소 50 개 이상 존재해야 합니다.
- 데이터는 fixtures 를 사용하여 언제든 load 될 수 있도록 준비합니다.\

### 영화 추천 알고리즘
- 추천 방식은 자유롭게 구성하되 해당 서비스를 이용하는 사용자는 반드시 최소 1 개 이상의 영화를 추천 받을 수 있어야 합니다.
- 어떠한 방식으로 추천 시스템을 구현 했는지 기술적으로 설명할 수 있어야 합니다.

### API
- 사용하는 API 에는 제한이 없습니다.
- 다만 유료 API 서비스는 주의가 필요합니다.

### 커뮤니티
- 유저간 소통 할 수 있는 커뮤니티 기능을 구현해야 합니다. (게시글 댓글 좋아요 팔로우 등)
- 소통 방식은 자유롭게 구성합니다.

### README
- 반드시 아래의 내용이 작성되어 있어야 합니다.
  - 팀원 정보 및 업무 분담 내역
  - 목표 서비스 구현 및 실제 구현 정도
  - 데이터베이스 모델링 (ERD)
  - 영화 추천 알고리즘에 대한 기술적 설명
  - 서비스 대표 기능에 대한 설명
  - 배포 서버 URL ( 배포했을 경우)
  - 기타 느낀 점 후기 등

### 기타
- 최소한 5 개 이상의 URL 및 페이지를 구성해야 합니다.
- HTTP Method와 HTTP response status code 는 상황에 맞게 적절하게 반환되어야 하며, 필요에 따라 적절한 에러 페이지를 구성해야 합니다.
- .gitignore 파일을 사용하여 불필요한 파일 및 폴더는 제출하지 않도록 합니다.
- 프로젝트명
  - final pjt front, final pjt back 두 서버를 모두 사용하는 경우

### 선택 요구사항
- 배포는 선택적으로 진행합니다.
- 배포 진행은 공용 노션의 해당 문서를 참고합니다.
  1. 서버(Django) 배포
  2. 클라이언트 (Vue) 배포


## 문제 해결법
1. dump data 에러 : 한글 코덱의 문제이므로 코드를 다음과 같이 사용
  - python -Xutf8 manage.py dumpdata > data.json
2. 404 에러 
  - URL이 없는 곳에 요청하거나, 데이터 없이 요청한 경우 발생
3. 500 에러 
  - 빼박 장고 문제
4. 400 에러 
  - 장고까지 문제가 안왓을 가능성이 높음, 데이터 없이 요청한 경우에도 발생


## 마지막 날 마무리해야할 구현 정리
1. 팔로우 기능
2. 회원 정보 수정
3. 게시판 페이지네이션
4. 내 댓글만 수정, 삭제 버튼 표현
