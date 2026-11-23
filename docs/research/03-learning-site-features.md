# 03. 학습 사이트·교재·앱의 공통 기능

조사일 2026-11-23. 페이지와 문서를 읽은 조사다. 실제 폰으로 열어 본 것은 아니다.

## 1. 조사 대상

- **알고리즘 시각화 사이트 24곳**: VisuAlgo, USFCA(David Galles), CSVisTool, Algorithm Visualizer, Python Tutor, memory_graph, Thonny, Recursive, staying.fun, alg0.dev, Toptal 정렬 애니메이션, Pathfinding Visualizer, W3Schools DSA, Programiz DSA, Hello Algo, See Algorithms, Red Blob Games, OpenDSA, codedive.in, Algorithms: Explained and Animated(앱), AlgoMonster, NeetCode, LeetCode Explore, SortVisualizer
- **시각 교재·에세이 22곳**: Hello Algo, Grokking Algorithms, Runestone pythonds, Wengrow의 Common-Sense Guide, Red Blob Games, Sam Rose, Ciechanowski, Josh Comeau, Bret Victor, Nicky Case, TheAlgorithms/Python, Interview Cake, Tech Interview Handbook, roadmap.sh, Open Data Structures, CS50, Algorithms Illuminated, MIT 6.006, Allen Downey, Brilliant, Educative, 알고리즘 도감
- **모바일 학습 앱·형식 19개**: Brilliant, Duolingo, Mimo, Sololearn, Enki, Grasshopper, Py, Fibu, Codecademy Go, Khan Academy, Anki/AnkiDroid, Mochi, RemNote, Algorithms: Explained and Animated, Imprint, Headway, LeetCode 모바일, Google Web Stories, Readwise
- **한국 커리큘럼 14개**: 이코테(나동빈), 바킹독 실전 알고리즘, 백준 단계별, solved.ac CLASS, 프로그래머스 고득점 Kit 등([04](04-curriculum.md)에서 다룬다)

## 2. 요약

1. 시각화 사이트는 두 계열이다. 미리 만든 애니메이션 목록(VisuAlgo, USFCA, Toptal)과 코드 추적기(Python Tutor, memory_graph, Recursive)다. 둘 다 "한 스텝 앞뒤 이동, 코드 줄 강조, 변수 상태, 스텝 설명, 복잡도"를 갖춘다.
2. **Python과 모바일은 둘 다 뒷전이다.** VisuAlgo와 CSVisTool은 의사코드를 쓰고, USFCA는 코드가 없고 캔버스가 1000×500 고정이며, Algorithm Visualizer는 JS·C++·Java다. VisuAlgo는 작은 터치 화면용이 아니라고 스스로 밝힌다.
3. **기기 없이 떠올리도록 설계된 자료는 없다.** 교재는 읽는 동안, 시각화는 보는 동안만 돕는다. 이 프로젝트의 차별점은 "재생 카드"다([01](01-blind-spots.md) 1번).

## 3. 본보기로 삼을 것

### Hello Algo — 장 골격의 기준
- 골격: 한 줄 정의 → 일상 비유 → 그림 → 연산·복잡도 표 → 번호 붙은 단계 프레임 → 코드 → 장단점과 응용 → 요약 → 연습.
- "애니메이션"은 실제로는 탭 `<1>`~`<n>`에 정적 SVG 한 장씩이다(원본 마크다운으로 확인). 애니메이션 엔진 없이 정지 프레임만으로 충분하다는 뜻이다.
- 코드는 테스트되는 소스 파일에서 본문으로 주입한다. 본문과 코드가 어긋나지 않는다.
- 한국어판이 저장소에 있다(`ko/`, 버전 1.3.0, 문서 118개, 영한 용어표 포함).
- **글·코드·그림 전부 CC BY-NC-SA 4.0이다.** 구조와 용어 선택만 참고하고 문장·코드·그림은 가져오지 않는다.
- 따라 하지 않을 것: Python Tutor iframe(온라인 필요, 높이 549px 고정, 데스크톱 화면), MkDocs Material 스택([05](05-tech-and-workflow.md)).

### 그 밖
- **Red Blob Games**: 10줄짜리 Python 루프 하나를 단계마다 조금씩 바꿔 BFS → 경로 복원 → 조기 종료 → 다익스트라 → 탐욕 최선 우선 → A*로 간다. "뼈대 코드 하나를 변형"은 난이도를 완만하게 만드는 좋은 장치다. 다만 원본에서도 BFS → 다익스트라는 한 번에 9줄이 바뀌는 가장 큰 도약이다. 한 줄만 바뀌는 것은 다익스트라 → A*뿐이다. 이 구간은 2~3장으로 쪼개야 한다.
- **Wengrow**(Python판 1권, 20개 장): Big-O를 3~7장 다섯 장에 나누고, 그중 세 장은 정렬 하나씩(버블, 선택, 삽입)에 얹는다. 재귀는 읽기(10장) → 쓰기(11장) → DP(12장) → 퀵 정렬(13장)로 이어진다. 병합 정렬은 1권에 없다.
- **바킹독**: 큐·스택으로 하는 격자 BFS·DFS를 재귀보다 앞에 둔다. 다만 저자 스스로 BFS를 "첫 번째 고비"라고 부른다. 쉬워서 앞에 둔 것이 아니므로, 큐·2차원 배열·방향 배열·방문 표시를 앞 장에서 하나씩 익힌 뒤에 합쳐야 한다. 재귀는 가장 쉬운 예만 한 번 따라가 보이고 그 뒤로는 귀납적으로 읽게 한다. DP는 "테이블 정의 → 점화식 → 초기값" 순서로 가르친다.
- **알고리즘 도감 앱**: 모바일에서 프레임을 탭으로 넘긴다. 한국어를 지원한다. 코드는 없다.
- **모바일 학습 앱들**: 2~5분 단위, 탭으로 넘기는 카드, 하단의 큰 버튼, "다음에 할 것"이 하나뿐인 경로.

## 4. 공통 기능과 1판 판정

조사에서 "필수"로 평가된 기능도 혼자 쓰는 1판 기준으로 다시 걸렀다. 뺀 이유는 [01](01-blind-spots.md) 5부에 있다.

### 1판에 넣는다

| 기능 | 주로 본 곳 |
|---|---|
| 한 스텝 앞뒤 이동(탭 한 번에 한 스텝) | VisuAlgo, Python Tutor, Hello Algo |
| 실행 중인 코드 줄 강조 | Python Tutor, Recursive, alg0.dev |
| 변수·포인터 상태(i, j, lo, hi) | Python Tutor, memory_graph |
| 스텝마다 한 줄 설명 | VisuAlgo, W3Schools DSA |
| 보조 구조(큐·스택·표)를 항상 표시 | Python Tutor, Recursive |
| 작은 입력의 전체 추적표(정지 화면) | Programiz, Hello Algo, Toptal |
| 비교·교환 횟수 카운터 | W3Schools DSA, Programiz |
| 모든 장이 같은 골격 | Hello Algo, Runestone, Wengrow |
| 첫머리 질문 훅 | Hello Algo, Grokking |
| 먼저 맞히고 나서 공개 | Brilliant, Mimo, VisuAlgo 훈련 모드 |
| 불변식 한 줄과 복잡도 한 줄 | Toptal, Programiz |
| 함정 하나(주로 Python 함정) | Hello Algo, Tech Interview Handbook |
| 하단 고정 큰 버튼과 k/N 표시 | AnkiDroid, Duolingo, Mimo |
| 한 화면에 들어가는 짧은 코드 | Mimo, Grasshopper |
| 하나뿐인 다음 단계, 이어서 보기 | Brilliant, Duolingo |
| 핵심만 담은 복습 카드 | Codecademy Go, Imprint, Anki |
| 고정 간격 복습("오늘 돌릴 3개") | Anki, Readwise |
| 용어집 한 페이지 | Runestone, Hello Algo 부록 |

### 조건에 따라 넣는다

| 기능 | 조건 |
|---|---|
| 오프라인(최소 캐시) | 작업장에서 통신이 안 될 때 |
| 인쇄용 포켓 카드 | 폰을 작업장에 못 들고 갈 때 |
| 진도 내보내기·가져오기 | iPhone이면 1판 필수 |

### 12장 이후로 미룬다

| 기능 | 미루는 이유 |
|---|---|
| 입력 프리셋(전형·최악·경계) | 빌드에서 굽는 방식으로 나중에 추가 |
| 트리·그래프·호출 트리 렌더러 | 1판은 배열 렌더러 하나로 충분 |
| 빈칸 채우기, 순서 맞추기 | 통과율 자료를 보고 결정 |
| 형제 알고리즘 비교, 응용 절 | 한 화면 분량이 우선 |
| 검색, 전체 지도 | 목차 한 페이지로 대체 |
| FSRS 같은 적응형 복습 | 카드 100장 전에는 차이가 작음 |

### 넣지 않는다

| 기능 | 이유 |
|---|---|
| 자동 재생, 속도 조절 | 수동적으로 보는 것은 효과가 없다 |
| 스크러버 드래그, 스와이프, 좌우 탭 존 | 장갑 낀 손에서 실패, 브라우저 뒤로 가기와 충돌 |
| 브라우저 안 Python 실행 | Pyodide만 약 6MB 전송 |
| 의사코드, 여러 언어 탭 | Python 하나만 |
| 계정, 동기화, 댓글 | 사용자가 한 명 |
| 점수, 배지, 연속 기록, 알림 | 유지 비용만 든다 |
| 수동 다크 모드 토글 | OS 설정을 따르면 충분 |
| hover 툴팁 | 터치에서 동작하지 않는다 |
| 오디오, 영상 | 이어폰 허용 여부 미확인, 잠금 화면에서 불안정 |

## 5. 장 골격(제안)

섹션 하나가 한 화면이다.

1. **질문 훅** 한 줄
2. **직관 그림** 한 장(정식 입력 사용)
3. **코드**(15줄 이하)
4. **스테퍼**: 다음 스텝을 예측 → 탭 → 확인
5. **불변식 한 줄, 복잡도 한 줄**
6. **함정** 하나
7. **변형 질문** 하나("이 줄을 바꾸면?")
8. **재생 카드**: 머릿속 과제 3개, 가벼움·무거움 표시, 숫자로 대조할 정답

## 6. 수치 규칙

| 항목 | 값 | 근거 |
|---|---|---|
| 기준 화면 | 폭 360px 세로, 가로 스크롤 0 | 가장 좁은 흔한 폰 |
| 실제 높이 | 주소창 때문에 줄어든다(844 → 약 664px) | 직접 측정 |
| 터치 타깃 | 최소 44~48px, 장갑이면 56px 이상 | Apple 44pt, Android 48dp |
| 코드 줄 길이 | 36자 권장, 40자 상한 | 360px에 14px 글꼴이면 여백 포함 36자, 코드 블록을 화면 끝까지 넓히면 40자 |
| 코드 분량 | 핵심 함수 15줄 이하, 중첩 3단 이하 | 한 화면 |
| 들여쓰기 | 4칸 유지 | 외운 모양이 실제 관례와 같아야 한다 |
| 한글 주석 | 코드 밖 설명으로 뺀다 | 한글은 영문 폭의 약 2배 |
| 머릿속 카드 예제 | 원소 5개 이하, 변수 3개 이하, 12스텝 이하 | 작업 기억 한계([01](01-blind-spots.md)) |
| 화면 스테퍼 예제 | 원소 8개 이하 | 버블 정렬 n=6이 줄 단위로 54스텝 |
| 한 단위 시간 | 2~5분 | 모바일 학습 앱 공통 |
| 카드 싣기, 확인 | 각 1분 이내 | 휴식 시간 기준 |
| 화면당 글 | 2~3문장 | codebase-to-course, Web Stories |
| 모션 | 상태가 바뀔 때만, 약 200ms | 모션 줄이기 설정 존중 |
| 글꼴 | 시스템 글꼴 | 한글 웹폰트는 0.5~2MB |
| 한글 줄바꿈 | `word-break: keep-all` | 어절 단위 줄바꿈 |
| 색 | 의미 3~4개 고정, 모양·테두리와 함께 | 색만으로 구분하지 않는다 |
| 상태 저장 시점 | 화면이 가려질 때(`visibilitychange`) | 갑자기 폰을 넣는 상황 |

## 7. 화면 스케치

```
┌──────────────────────────┐
│ 3. 선택 정렬       4/11  │ 장 제목, 스텝 k/N
├──────────────────────────┤
│  [5][2][4][1][3]         │ 배열(정식 입력)
│      i     m             │ 포인터 이름표
│  비교 3 · 교환 0         │ 카운터
├──────────────────────────┤
│ 2   for j in range(...): │ 코드
│ 3 ▶     if a[j] < a[m]:  │ 현재 줄 강조
│ 4           m = j        │
├──────────────────────────┤
│ a[3]=1 < a[1]=2 → m = 3  │ 한 줄 설명
├──────────────────────────┤
│ [  ◀ 이전  ] [  다음 ▶ ] │ 하단 고정, 56px
└──────────────────────────┘
```

스케치의 숫자는 배치를 보이려는 예시다. 실제 값은 실행 추적에서 만든다.
