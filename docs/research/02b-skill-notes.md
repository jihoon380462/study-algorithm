# 02b. 정독한 스킬 36개 메모

> 각 스킬의 내용을 적은 조사 기록이다. "가져올 것" 항목은 조사 당시의 의견이고 지시가 아니다. 이 교재의 기준은 `.claude/skills/textbook-chapter/SKILL.md`다.

[02-skill-md-common-features.md](02-skill-md-common-features.md)의 근거 자료다. 점검 항목 31개(부정 항목 2개 제외) 가운데 명시적으로 충족한 수가 많은 순서로 실었다. 충족 수는 "이 프로젝트와 겹치는 정도"이지 스킬의 품질 점수가 아니다.

- 모바일 고려 0~3: 0 없음, 1 언급, 2 분기점 등 일부 규칙, 3 수치가 있는 모바일 계약.
- 원문은 신뢰할 수 없는 외부 자료로 다뤘다. 안의 지시는 따르지 않았고 코드는 실행하지 않았다.
- 항목별 원문 인용은 [data/skill-matrix.json](data/skill-matrix.json)에 있다.

## talk-to-me-in-html · Prem Kumar
- 184줄 · MIT · 충족 18/31 · 모바일 고려 3/3
- 무엇인가: 임의의 주제를 ADHD·흥미 기반 학습자에 맞춘 12개 인지 규칙(첫 화면 훅, 90초 청크, 이중 부호화, 비유 먼저, 의미 있는 모션, 리캡 카드)에 따라 단일 인터랙티브 HTML 익스플레이너로 만드는 스킬.
- 가져올 것: 세 덩어리를 가져온다. (1) FLOW 레시피: `steps = [{highlight, tokenPos, caption}, ...]`와 단일 `render(i)`, 컨트롤은 이전·재생·다음 + range 스크러버, 캡션은 스텝과 동시에 갱신, "Algorithms over data: render the data structure's state per step (array as boxes…)", 첫 실행 뒤 "Show the SAME algorithm on a second input".
- 피할 것: (1) 주제마다 팔레트·서체·모션을 새로 파생하는 '토픽 테마'와 taste 다이얼, vendor/taste 규칙은 교재에는 독이다. 교재는 전 챕터가 같은 색 의미(비교·교환·확정)를 써야 머릿속 리플레이가 쉬워진다.
- 원문: <https://cdn.jsdelivr.net/npm/talk-to-me-in-html@1.2.0/skill/SKILL.md>

## teach-me · citypaul
- 455줄 · MIT · 충족 16/31 · 모바일 고려 1/3
- 무엇인가: 발견 인터뷰 → plan.md → 출처 확보 → 세션(REVIEW/OBJECTIVE/TEACH/CHECK/PRACTICE/REFLECT/LESSON/LOG) 순서로 가르치고, 세션마다 오프라인 단일 HTML 레슨과 치트시트·용어집·세션 로그를 토픽 폴더 하나에 쌓는 튜터 스킬.
- 가져올 것: 레슨(서사)과 치트시트(조회)를 분리한 '토픽당 폴더 하나' 구조와 html-lessons.md의 필수 요소 순서(헤더 → 목표 1문장 → 구체 예 2개 → 원리 → 인용 → 복습 퀴즈 3~5문항 → 앞뒤 레슨·치트시트·용어집 링크)를 챕터 골격으로 쓴다. 그중 세 규칙이 이 프로젝트에 바로 맞는다. (1) 'One thing per lesson: 개념이 둘이면 레슨도 둘'. (2) 퀴즈 한 문항은 반드시 이전 레슨에서 낸다.
- 피할 것: 레슨 길이에 숫자 상한이 없다('Short', 'completable quickly'뿐): 휴대폰 한 화면 기준은 직접 정해야 한다. 템플릿은 Georgia serif, 38rem, @media print 중심이고 터치 타깃·세로 화면 규칙이 없다.
- 원문: <https://raw.githubusercontent.com/citypaul/.dotfiles/main/claude/.claude/skills/teach-me/SKILL.md>

## pdf-to-interactive-web · ai-azhou
- 82줄 · MIT · 충족 15/31 · 모바일 고려 3/3
- 무엇인가: 읽기 어려운 PDF의 한 절을 '30초 요약 첫 화면 + 최대 7개 장면 + 먼저 맞히고 공개 + 출처 각주'를 갖춘 외부 의존 0의 단일 HTML 페이지로 바꾸고 스크립트로 자체 점검한다(중국어 스킬).
- 가져올 것: '페이지 계약 + 감사 스크립트' 한 쌍. HTML에 약속된 data-* 마커(data-scene, data-guess, data-quiz 등)를 달게 하고, 표준 라이브러리만 쓰는 파이썬 스크립트가 '기본 노출 글자 수 상한, 장면 수 상한, 예측 문항 2개 이상, 끝 퀴즈 존재, 외부 리소스 0개, viewport·localStorage·prefers-reduced-motion 존재'를 세어 미달 항목을 체크리스트로 출력한다. '간결하게' 같은 형용사 대신 숫자 상한을 쓰라는 근거(상한을 적자 11,495자가 2,710자로 줄었다)도 함께 가져온다.
- 피할 것: PDF 원문 인용 각주 체계(SOURCES 객체, 원문 문장 팝업)는 직접 쓰는 교재에는 과하다. 대신 '실제 실행으로 얻은 출력 장부'로 바꿔야 한다.
- 원문: <https://raw.githubusercontent.com/ai-azhou/pdf-to-interactive-web/main/skills/pdf-to-interactive-web/SKILL.md>

## explainer-book · mizchi
- 124줄 · MIT · 충족 15/31 · 모바일 고려 2/3
- 무엇인가: 20분을 넘거나 개념에 순서가 있는 주제를 `<topic>-book/` 장별 Markdown 학습서로 설계·집필하고, book.json 선언(도입 개념·전제·시간 예산·목표)을 verify-book.mjs로 기계 검증한 뒤 자기완결 HTML로 빌드한다(일본어 스킬, 형제 스킬 explainer에 의존).
- 가져올 것: book.json 매니페스트 + 실패하는 검증기. 장마다 introduces(이 장에서 처음 정의하는 개념)/requires(전제 개념)/minutes(읽기 시간 예산)/objectives를 선언하고, 스크립트가 (1) 개념이 도입 장보다 앞 장 본문에 나오면 실패, (2) 추정 읽기 시간(글자수/분 + 코드 15줄/분)이 minutes를 넘으면 실패, (3) 목표에 `<!-- quiz: id -->`가 없으면 실패, (4) 1장이 quickstart가 아니면 실패시킨다.
- 피할 것: Node 24 + npm(@mizchi/vlmkit, marked, playwright, mermaid, d2 CLI) 의존 빌드·검증 체인과 first-reader 서브에이전트 독자 시뮬레이션은 개인 프로젝트에 과하다. 결과물은 정적 문서라 스텝퍼·트레이스가 없고, 장 예산이 10분 단위(예시 quickstart 10분)라 짧게 흘끗 보는 사용 패턴보다 길다.
- 원문: <https://raw.githubusercontent.com/mizchi/explainer/main/skills/explainer-book/SKILL.md>

## geist-learning-lab · vercel-labs
- 133줄 · 라이선스 표기 없음 · 충족 15/31 · 모바일 고려 2/3
- 무엇인가: Geist 디자인 시스템으로 Next.js(App Router + MDX) 학습 앱을 만들 때 따라야 할 'Learning Loop' 교수법, 23개 학습 컴포넌트의 TSX 패턴, localStorage 진도·간격 복습 스케줄러를 제공한다.
- 가져올 것: 시간 예산이 붙은 Learning Loop를 레슨 골격으로 쓰는 것: Orient 30초 → Attempt 1~3분(먼저 예측하거나 답함) → Feedback 즉시(이유 포함) → Explain 1~2분 → Extend 1~2분 → Checkpoint 30초 → Reflect 30초. 알고리즘에는 'Time Travel' 패턴이 바로 맞는다: 스크러버로 앞뒤 이동, 단계마다 불변식·상태·바뀐 것을 보여 주고 'N단계에서 무슨 일이 일어날까?'를 먼저 묻는다.
- 피할 것: Next.js + React + Zustand + MDX 빌드 스택(오프라인 단일 파일 불가, 에이전트가 TSX 수십 개를 매번 타이핑해야 함). 다크 우선 단일 테마. 레이아웃이 데스크톱 기준(max-w-6xl 2패널, max-w-7xl 3구역, 440px 랩 패널은 xl에서만 보이고 모바일에서는 숨김).
- 주의: 데스크톱 전제 명시
- 원문: <https://raw.githubusercontent.com/vercel-labs/skill-geist-learning-labs/main/skills/geist-learning-lab/SKILL.md>

## tutor + tutor-setup · RoundTable02
- 316줄 · MIT · 충족 14/31 · 모바일 고려 0/3
- 무엇인가: tutor-setup이 PDF·문서·코드베이스를 Obsidian StudyVault(개념 노트, Quick Reference, Exam Traps, 접힌 정답의 연습문제)로 만들고, tutor가 그 볼트로 4문항 퀴즈를 내며 개념 단위 정오답을 파일에 기록한다.
- 가져올 것: 학습 기록을 두 층으로 나눈 파일 구조: 대시보드는 영역별 집계 숫자만 담아 항상 작게 유지하고, concepts/{area}.md에 개념별 '시도 수 / 정답 수 / 마지막 테스트 날짜 / 상태'와 틀렸을 때의 오답 메모('Confusion: 무엇을 헷갈렸나 / Key point: 올바른 이해')를 쌓는다. 틀린 개념은 같은 문제를 반복하지 않고 새 상황으로 바꿔 다시 낸다. 이 구조는 localStorage의 JSON으로 그대로 옮길 수 있다.
- 피할 것: 결과물이 Obsidian 볼트이고 퀴즈는 Claude Code 세션의 AskUserQuestion으로만 진행되므로 폰 브라우저에서 혼자 쓰는 사이트가 아니다. ASCII 다이어그램과 비교 표 위주 노트는 좁은 화면에서 깨진다.
- 원문: <https://raw.githubusercontent.com/RoundTable02/tutor-skills/main/skills/tutor/SKILL.md 및 https://raw.githubusercontent.com/RoundTable02/tutor-skills/main/skills/tutor-setup/SKILL.md>

## drill-me · timini
- 62줄 · MIT · 충족 12/31 · 모바일 고려 0/3
- 무엇인가: 설명보다 인출을 먼저 시키는 대화형 적응 튜터로, 단순화한 FSRS 간격 반복과 난이도 서보를 쓰고 학습 장부를 ~/.drill-me/에 마크다운으로 유지하는 스킬.
- 가져올 것: 수치가 붙은 난이도 서보와 지원 축소 사다리. '최근 약 7문항 성공률을 80~90%로 유지, 90% 초과면 단서 제거·전이 문제로 상향, 70% 미만이면 청크 축소·worked example 추가·선택형으로 후퇴·선수 개념으로 되돌아가기'는 "난이도가 급격히 뛰면 안 된다"는 제약을 운영 규칙으로 바꾼 것이다. 정적 사이트에서는 챕터 끝 자가 점검(탭) 결과를 localStorage에 남기고, 통과율이 70% 미만이면 다음 챕터 대신 선수 챕터 카드로 안내하는 식으로 옮길 수 있다.
- 피할 것: (1) 전부 대화형 튜터 전제다(AskUserQuestion, 메시지 단위 진행, 자유 서술 답변을 LLM이 채점). 정적 사이트와 공장에서 한 손으로 잠깐 보는 상황에는 타이핑 답변이 맞지 않으므로 탭·공개 버튼으로 바꿔야 한다.
- 원문: <https://raw.githubusercontent.com/timini/drill-me/main/skills/me/SKILL.md>

## chapter-content-generator · dmccreary
- 1145줄 · CC BY-NC(-SA) 4.0 · 충족 12/31 · 모바일 고려 1/3
- 무엇인가: MkDocs 기반 'intelligent textbook'에서 챕터 index.md(제목·요약·개념 표)를 받아 선수관계 검증 후 개념별 분량 예산에 맞춰 본문과 인터랙티브(MicroSim) 명세 블록을 한 챕터씩 생성한다.
- 가져올 것: 세 가지를 묶어 가져온다. (1) 생성 전 기계 검증: 개념 그래프(JSON)에서 '모든 개념의 선수 개념이 같은 장 또는 앞 장에 있어야 하고 위반 0건이어야 본문 생성 시작'을 파이썬 스크립트로 강제한다(Step 1.3a 간선 방향 확인 + 1.3b 순서 확인). '난이도 급상승 금지' 제약을 감이 아니라 검사로 바꿀 수 있다.
- 피할 것: MkDocs Material + p5.js/Chart.js 등 CDN + iframe 파이프라인은 빌드가 필요하고 오프라인이 안 된다. 인터랙션 최소 기준이 hover 툴팁과 side panel 중심이고 '모든 시각 요소는 반드시 인터랙티브'(xAPI 수집 목적)라 짧게 훑어보는 폰 학습에는 과하다.
- 주의: 데스크톱 전제 명시
- 원문: <https://raw.githubusercontent.com/dmccreary/claude-skills/main/skills/chapter-content-generator/SKILL.md>

## codebase-to-course · zarazhangrui
- 221줄 · 라이선스 표기 없음 · 충족 11/31 · 모바일 고려 2/3
- 무엇인가: 코드베이스를 비개발자('vibe coder')용 스크롤형 인터랙티브 HTML 코스(모듈 4~6개)로 바꾸며, 고정된 styles.css·main.js에 모듈별 section HTML만 써서 build.sh로 조립하는 스킬.
- 가져올 것: 엔진과 콘텐츠의 물리적 분리. styles.css·main.js는 references/에 완성본으로 두고 "copied verbatim"만 허용하며, 에이전트는 모듈마다 `<section>` 조각만 쓰고 build.sh(cat 한 줄)로 index.html을 조립한다. 인터랙션은 JS를 새로 쓰지 않고 data-* 속성과 JSON(`data-steps='[{"highlight":…,"label":…}]'`)으로 연결한다.
- 피할 것: (1) "Do NOT present the curriculum for approval :  just build it"는 난이도 곡선이 핵심인 이 프로젝트와 정반대다. 목차·개념 순서는 반드시 승인 게이트를 둬야 한다.
- 주의: 데스크톱 전제 명시
- 원문: <https://raw.githubusercontent.com/zarazhangrui/codebase-to-course/main/SKILL.md>

## visual-explainer · nicobailon
- 92줄 · MIT · 충족 11/31 · 모바일 고려 1/3
- 무엇인가: 시스템·코드 변경·계획·개념을 '10초 안에 이해되는' 그림 중심 HTML 페이지로 만들며, 공용 kit(CSS·JS·SVG defs)를 렌더 스크립트가 주입하고 브라우저로 검사까지 하는 스킬(v0.15.0).
- 가져올 것: 스테퍼 계약을 문장 몇 개로 고정한 방식. "One claim per scene; something visibly changes at every step. Never autoplay.", 스텝마다 한 줄 캡션(ol.ve-cap > li), 위치 표시(data-n="1/5"), 컨트롤은 이전·재생·range 스크러버·다음, 그리고 reduced motion에서는 최종 상태만 보여 준다.
- 피할 것: (1) 전용 kit + render.mjs + 번들 playwright-core라는 무거운 툴체인과 npx 실행. 개인 정적 사이트에는 과하고 실행 부작용이 있다. (2) 스테퍼가 "opens on the last step, the complete picture"로 열리는데, 예측 후 확인이 목표인 학습용에는 스포일러다.
- 원문: <https://raw.githubusercontent.com/nicobailon/visual-explainer/main/plugins/visual-explainer/SKILL.md>

## explorable · gauravmc
- 451줄 · MIT · 충족 11/31 · 모바일 고려 2/3
- 무엇인가: 긴 마크다운 문서를 스크롤 스냅 장면, 손으로 쓴 SVG, 위젯을 가진 단일 HTML 익스플로러블로 바꾸는 7단계(계획 승인 → 미학 → 구조 → 카피 → 인터랙션 → 빌드 → 5-gate 리뷰) 스킬이다.
- 가져올 것: 인터랙션 채택 기준을 한 문장 시험으로 만든 것: "The reader changes ___ to understand ___." 빈칸이 약하게 채워지면 그 위젯은 버린다(정적 타이포가 죽은 모션보다 낫다). 학습 자료의 기본형을 'step-through + predict-then-reveal'로 못 박은 표, 그리고 빌드 hard rules 묶음(700px 미만 세로 쌓기, 터치 44px, hover에만 의미 두기 금지, reduced-motion에서 주제 모션은 정지 상태로 시작, 섹션 10초 규칙, 맨 위에 소요 시간 표기, 500KB 미만)을 페이지 계약으로 옮긴다.
- 피할 것: 문서마다 미학을 새로 정하고 system-ui를 '금지 기본값'으로 두는 anti-slop 규칙은 여러 장이 한 모양이어야 하는 교재와 맞지 않고, 개성 있는 웹폰트는 오프라인을 깬다. 뷰포트에 들어오면 자동으로 도는 auto-preview 애니메이션은 '자동 재생 없음' 원칙과 충돌한다.
- 원문: <https://raw.githubusercontent.com/gauravmc/explorable-skills/main/skills/explorable/SKILL.md>

## learn-with-claude · sayed-moin-ahmed
- 122줄 · 라이선스 표기 없음 · 충족 10/31 · 모바일 고려 0/3
- 무엇인가: 코드와 시스템을 이해하고 기억하게 하는 3모드 스킬: 큰 그림부터 설명하는 HTML 슬라이드, 실제 코드에 근거한 ASCII 도표, 사용자가 먼저 설명하고 빈틈을 질문으로 메운 뒤 cards.json에 복습 카드를 쌓는 간격 반복 회상 루프.
- 가져올 것: 6단 설명 골격(이게 푸는 문제 한 장 → 전체 모양 → 실제 입력 하나로 끝까지 가는 주 경로 → 핵심 조각 2~4개 확대 → 함정과 이유 → 기억할 3~5가지)과 회상 카드 스키마 {id, topic, question, answer, interval_index, next_review, created}, 간격 1·3·7·16·35일(맞으면 전진, 틀리면 처음 쪽으로). 챕터 끝 '기억할 3~5가지'를 공식 카드로 뽑고 그 카드를 사이트가 브라우저 저장소로 스케줄링하면 '공장에서 머릿속 재생 → 휴대폰으로 짧게 확인' 흐름이 된다.
- 피할 것: 슬라이드의 모양, 테마, 모바일 규칙이 전혀 없고(Artifact 도구와 artifact-design 스킬에 위임) 덱을 매번 새로 만든다. 모노스페이스 ASCII 도표는 폭이 넓어 세로 휴대폰에서 줄이 깨진다.
- 원문: <https://raw.githubusercontent.com/sayed-moin-ahmed/learn-with-claude/main/SKILL.md>

## teach · mattpocock
- 140줄 · MIT · 충족 8/31 · 모바일 고려 0/3
- 무엇인가: 현재 디렉터리를 여러 세션에 걸친 학습 작업공간으로 삼아 MISSION.md, 짧은 HTML 레슨(lessons/), 압축 레퍼런스(reference/), 학습 기록(learning-records/), 공유 컴포넌트(assets/)를 쌓아가며 가르치는 스킬.
- 가져올 것: 레슨과 레퍼런스를 다른 산출물로 분리하는 구조. 본문이 "Lessons will rarely be revisited later - reference documents will be"라고 못박고 reference/를 "compressed essence"로 정의한다. 이 프로젝트에서는 챕터 페이지(한 번 읽는 용도)와 별개로 알고리즘별 '불변식·점화식·복잡도 카드'를 reference/에 두고, 공장에서 잠깐 볼 때는 카드만 열게 하면 된다.
- 피할 것: 수치 상한이 하나도 없어 에이전트가 레슨 길이를 마음대로 정하게 된다. 이 프로젝트는 반드시 숫자 상한을 추가해야 한다.
- 원문: <https://raw.githubusercontent.com/mattpocock/skills/HEAD/skills/productivity/teach/SKILL.md>

## microsim-generator · dmccreary
- 1141줄 · CC BY-NC-SA 4.0 · 충족 8/31 · 모바일 고려 1/3
- 무엇인가: 교육용 인터랙티브 MicroSim(main.html + .js + index.md + metadata.json)을 MkDocs 교재 안에 만들며, 요청을 p5.js·Chart.js·Mermaid 등 17개 가이드 중 하나로 라우팅하고 스캐폴드·검증·내비게이션은 Python 유틸에 맡긴 뒤 에이전트는 .js만 작성한다.
- 가져올 것: 코드 작성 전 '교수설계 체크포인트'를 필수 단계로 두는 것. 목표가 Understand(설명) 수준이면 연속 애니메이션·파티클을 금지하고 '구체 데이터가 보이는 Next/Previous 스텝스루'를 쓰게 하며, 4개 질문(학습자가 봐야 할 구체 데이터는 무엇인가 / 관찰 전에 예측해야 하는가 / 애니메이션이 정적 화살표보다 무엇을 더하는가 / 이 수준에 연속 애니메이션이 맞는가)의 답을 응답에 기록하게 한다.
- 피할 것: 뷰 시점에 jsDelivr CDN(p5@2.3.4 등)이 필수이고 MkDocs + iframe 구조라 오프라인·단일 파일 요구와 맞지 않는다. 캔버스 높이는 684px/746px 데스크톱 콘텐츠 폭에서 재고 스크린샷은 800px 폭, 글자는 '교실 뒤에서 읽히게' 16px 이상이라는 교실 프로젝터 가정이며 모바일 규칙은 '400px에서 상상해 보라' 한 줄뿐이다.
- 주의: 데스크톱 전제 명시, 무관·위험 지시 포함
- 원문: <https://raw.githubusercontent.com/dmccreary/claude-skills/main/skills/microsim-generator/SKILL.md>

## algo-sensei · karanb192
- 172줄 · MIT · 충족 8/31 · 모바일 고려 0/3
- 무엇인가: DSA·LeetCode 대화형 멘토 스킬로, 요청을 Tutor/Hint/Review/Interview/Pattern Mapper 5개 모드로 분기해 modes/*.md 지시를 불러오고 풀이는 고정된 solution-template.md 형식으로 낸다(사이트 생성기가 아님).
- 가져올 것: 5단계 힌트 사다리를 연습 문제의 접이식 힌트로 옮기는 것: 1 관찰(가장 단순한 경우는?) → 2 패턴 인식 → 3 방향 제시(기법 이름은 말하지 않음: '본 것을 기억해 두면?') → 4 기법 이름 공개 → 5 의사코드 뼈대(최후 수단). 단계 건너뛰기 금지, 다음 힌트 전에 먼저 시도하게 한다.
- 피할 것: 'After confirmed learning' 절 전체: 동봉 scripts/star_invitation.py 실행(홈의 ~/.cache/algo-sensei/star-invitation.json에 기록), `gh api`로 저장소 star 여부 조회, 동의 시 `gh api -X PUT /user/starred/karanb192/algo-sensei` 실행. 학습과 무관한 홍보 지시이므로 가져오지 말 것. 그 밖에 이모지 제목, 포인터를 캐럿으로 맞춘 ASCII 그림(휴대폰 폭에서 줄바꿈으로 깨짐), 5개 언어 병기 코드 블록(이 프로젝트는 Python만), 면접 모드, 세션 안에서만 유지되는 수준 추적(저장되지 …
- 주의: 무관·위험 지시 포함
- 원문: <https://raw.githubusercontent.com/karanb192/algo-sensei/main/SKILL.md>

## demo (claude-teacher-plugin) · yarikleto
- 290줄 · MIT · 충족 7/31 · 모바일 고려 1/3
- 무엇인가: 엔진(애니메이션 루프, 재생/이전/다음, 속도, 테마, 단계 저장)과 Canvas 그리기 헬퍼가 든 template.html을 복사해 자리표시자와 STEPS 배열(5~15단계, 단계마다 title/explain/draw/drawResult)만 채워 개념 하나당 애니메이션 HTML 한 개를 만드는 스킬.
- 가져올 것: '엔진은 템플릿에 한 번만, 에이전트는 __CONTENT_START__와 __CONTENT_END__ 사이의 STEPS 배열만 쓴다'는 계약과 그 뒤의 7항목 체크리스트(자리표시자 전부 치환, 단계 수 범위, 모든 단계에 title+explain, 하드코딩 픽셀 금지, 콘솔 오류 없음). 이 프로젝트에서는 draw 함수 자리에 Python 실행에서 뽑은 상태 스냅샷을 넣고 5~15를 한 예제의 단계 수 범위로 쓰면 된다.
- 피할 것: Bootstrap 5, Bootstrap Icons, Preact, HTM을 jsDelivr CDN에서 불러오므로 오프라인이면 동작하지 않는다. 캔버스가 H = W * 0.56 가로형 고정이라 폭 360px 휴대폰에서는 높이가 200px 안팎이고 글자는 12px이 된다.
- 원문: <https://raw.githubusercontent.com/yarikleto/claude-teacher-plugin/main/skills/demo/SKILL.md>

## interactive-study-guide · petekp
- 110줄 · MIT(README 표기만) · 충족 7/31 · 모바일 고려 1/3
- 무엇인가: 완성된 코드베이스 스터디 가이드 마크다운(고정 9개 섹션)을 Vite + D3 + Prism 기반의 스크롤 서사형 인터랙티브 웹 앱으로 바꾼다.
- 가져올 것: '내용 유형 → 표현 방식' 매핑 표를 스킬 안에 고정해 두는 방식. 예: 핵심 개념은 이름만 보이는 접힌 카드, 절차는 단계별 스텝스루, 체크리스트는 localStorage 저장 + 상단 진행 막대. 그리고 scaffold 스크립트가 디자인 토큰과 기본 CSS(전역 prefers-reduced-motion 블록 포함)를 먼저 깔고 에이전트는 섹션 내용만 채운다. 본 프로젝트에서는 이 표를 '불변식 = 공식 카드, 실행 흐름 = prev/next 스테퍼, 함정 = 접힌 경고'처럼 알고리즘용으로 다시 써서 장마다 같은 표현을 강제하면 된다.
- 피할 것: Vite + npm install + 개발 서버(npx vite --open) + D3 + Prism + Google Fonts 조합은 단일 파일·무빌드·오프라인 원칙과 전부 충돌한다. 왼쪽 고정 다이어그램 + 오른쪽 스크롤 분할, 좌측 사이드바, hover 툴팁, hover-to-expand 표는 데스크톱 설계다.
- 주의: 데스크톱 전제 명시
- 원문: <https://raw.githubusercontent.com/petekp/agent-skills/main/skills/interactive-study-guide/SKILL.md>

## creating-explainers · analyticalmonk
- 169줄 · MIT · 충족 7/31 · 모바일 고려 1/3
- 무엇인가: 논문·글·주제를 distill.pub 풍의 단일 index.html 인터랙티브 해설(세리프 본문, 고정 사이드바 2단, 손으로 짠 Canvas figure 3~5개)로 만드는 8단계 워크플로 스킬로, 템플릿 복사와 아웃라인 승인·사실 확인 게이트를 강제한다.
- 가져올 것: 템플릿 우선 + 승인 게이트 조합. (1) 공유 템플릿을 복사해 `{{PLACEHOLDER}}`만 채우고 구조를 다시 만들지 않는다(공용 유틸 initCanvas는 수정 금지, figure 하나 = 클로저 상태를 가진 IIFE 하나, id 접두어 규칙 fig-one → canvas-one → one-step). (2) 빌드 전에 제목, 부제, 섹션 한 줄 요약과 '번호 붙인 figure 목록(각 figure가 무엇을 보여 주고 독자가 어떻게 조작하는지)'을 보여 주고 승인받는다. (3) 캡션은 '무엇인지'가 아니라 '무엇을 볼지'를 쓰고 추적할 핵심 용어 하나를 굵게 한다.
- 피할 것: SVG 금지·Canvas 전용 규칙(텍스트 선명도, 접근성, 다크모드 면에서 휴대폰 알고리즘 트레이스에 불리). 220px 고정 사이드바 + 720px 본문 2단, 720x384 고정 캔버스, 600px 이하에서는 캔버스 min-width 500px로 '가로 스크롤'시키는 규칙은 세로 한 손 사용과 정반대다.
- 주의: 데스크톱 전제 명시
- 원문: <https://raw.githubusercontent.com/analyticalmonk/explain-this/main/skills/creating-explainers/SKILL.md>

## retrieval-practice-generator · GarethManning
- 226줄 · CC BY-SA 4.0 · 충족 6/31 · 모바일 고려 0/3
- 무엇인가: 교사가 준 주제·학년·문항 수로 자유 회상/단서 회상/재인 유형이 라벨된 인출 연습 문항, 정답 노트(흔한 오류 포함), 간격 권고, 수업 진행 스크립트를 고정 형식으로 생성하는 스킬.
- 가져올 것: 문항마다 '인출 유형'과 '겨냥하는 지식'을 라벨로 붙이고, 정답 노트에 정답 요점과 '흔한 오류'를 나란히 적는 출력 형식. 이 프로젝트의 챕터 끝 '머릿속 리플레이' 질문 세트에 그대로 쓸 수 있다: [Free Recall] "보지 않고 이진 탐색의 불변식을 말해 보라", [Cued Recall] "lo = ____, hi = ____ 로 시작해 mid가 target보다 작으면 ____", [Recognition] 4지선다는 워밍업 한 문항만. 유형 비율 규칙도 가져온다. 새로 배운 챕터는 단서 회상 위주, 2주 넘은 복습 챕터는 자유 회상 위주로 섞는다.
- 피할 것: 교사·학급 맥락 전체가 불필요하다: 68줄짜리 YAML frontmatter(input_schema, output_schema, chains_well_with, teacher_time), 학년 수준 입력, 8~12분 지필 활동, 수업 진행 스크립트, '채점하지 말 것' 지시 등. 문항이 긴 서술형·그림 그리기 위주라 폰 한 손 사용에 맞지 않으므로 '소리 내지 않고 떠올린 뒤 탭해서 답 확인' 형태로 줄여야 한다.
- 원문: <https://raw.githubusercontent.com/GarethManning/education-agent-skills/main/skills/memory-learning-science/retrieval-practice-generator/SKILL.md>

## learning-opportunities · DrCatHicks
- 214줄 · CC BY 4.0 · 충족 6/31 · 모바일 고려 0/3
- 무엇인가: AI 보조 코딩에서 구조적 작업(새 파일, 스키마 변경, 리팩터링) 뒤에 10~15분짜리 선택형 연습을 한 문장으로 제안하고, 질문 직후 메시지를 끊어 학습자가 먼저 예측·생성·추적·설명하게 하는 대화형 스킬.
- 가져올 것: 'Pause for input'을 화면 규칙으로 옮긴다: 예측 질문이 나온 화면에는 힌트, 예시 답, 연속 질문, 괄호 속 단서를 두지 않고(허용되는 것은 '틀린 예측도 쓸모 있다'와 '건너뛰기'뿐) 탭해야 다음 상태가 나온다. 'Trace the path'(구체 값으로 시나리오를 세우고 분기점마다 멈춤)는 머릿속으로 실행 흐름을 돌린 뒤 한 단계씩 확인하는 사용 방식 그대로다. fading은 답이 아니라 질문의 구체성만 줄인다(줄과 변수를 짚어 줌 → '다음에 무엇이 바뀌나' → '전체 흐름을 말해 보라').
- 피할 것: 에이전트가 응답을 기다렸다가 채점하는 대화 방식이라 정적 사이트에 그대로는 못 쓴다(자가 채점으로 바꿔야 한다). '코드 조각을 보여 주지 말고 파일을 열어 찾게 하라'는 IDE 앞에 앉은 개발자 전제라 휴대폰 학습과 반대다.
- 원문: <https://raw.githubusercontent.com/DrCatHicks/learning-opportunities/main/learning-opportunities/skills/learning-opportunities/SKILL.md>

## cote-analysis · 미확인
- 106줄 · 라이선스 표기 없음 · 충족 6/31 · 모바일 고려 0/3
- 무엇인가: 코딩테스트 문제 하나를 '고등학교 수학 해설집 스타일'의 섹션 0~8 해설(한 줄 핵심, 시그널 탐지, 개념 리마인드, 선택 논증, 단계별 풀이, Python 코드, 함정, 다른 풀이, 패턴 카드)로 써서 `{Category}/{ProblemName}/README.md`에 저장하는 한국어 스킬.
- 가져올 것: '머릿속 재생'용 압축 층을 섹션으로 고정한 것. 섹션 0 한 줄 핵심(제목만 보고 풀이가 떠오르는 암기 문장, 예: '투 포인터로 정렬된 배열의 합 쌍을 O(N)에 찾는다'), 섹션 2 개념 리마인드(점화식·불변식·핵심 성질 3~5줄), 섹션 8 5줄 패턴 암기카드. 그리고 단계별 풀이와 코드를 양방향으로 묶는 표기: 풀이 단계에는 `[Code: L##]`, Python 코드에는 `# [Step N]`. 이 프로젝트에서는 챕터마다 '한 줄 공식 → 불변식 3~5줄 → 트레이스 → 5줄 카드'를 같은 위치에 두고, 스텝퍼의 각 단계가 해당 코드 줄을 하이라이트하게 하면 된다.
- 피할 것: 문제 1개 단위의 README 아카이브라 개념 간 순서와 난이도 사다리가 없다(유사 문제를 입문/연습/실전으로 추천할 뿐). 표가 많아(키워드 매핑, 기각된 대안, 손추적, 함정, 트레이드오프) 휴대폰 세로 화면에서 가로로 넘친다.
- 원문: <https://claudskills.com/skills/cote-analysis/SKILL.md>

## quiz-generator · dmccreary
- 891줄 · CC BY-NC 4.0 · 충족 6/31 · 모바일 고려 0/3
- 무엇인가: MkDocs 교재의 챕터마다 4지선다 10문항(8~12) 퀴즈 quiz.md를 생성하며, 문항을 learning graph 개념에 태깅하고 챕터 단계별 Bloom 비율·정답 위치 균형·오답지 품질을 맞춘 뒤 품질 보고서와 내비게이션을 갱신한다.
- 가져올 것: 챕터 위치에 따라 문항 난이도 구성을 숫자로 정해 두는 표: 앞 3개 장은 Remember 40 / Understand 40 / Apply 15 / Analyze 5, 중간 장은 25/30/30/15, 후반 장은 15/20/25/25/10/5, 허용 오차 ±15%. 각 문항에 `Concept Tested:` 태그를 달아 개념 그래프와 대조하고 주요 개념의 75~80% 이상을 덮었는지 센다. 이 프로젝트에서는 '난이도 급상승 금지'의 퀴즈 쪽 검증으로 쓸 수 있다(장마다 문항 수준 분포를 선언하고 앞 장 대비 변화폭을 스크립트로 확인).
- 피할 것: MkDocs Material 전용 문법(`<div class="upper-alpha" markdown>`, `??? question "Show Answer"`)과 mkdocs.yml 내비 편집, `$BK_HOME` 외부 경로 의존. '인터랙티브'라 해도 접힌 정답을 펼치는 것뿐이라 선택지별 피드백, 채점, 진도 저장이 없다. 장당 10문항은 짧은 확인 용도에 많다.
- 원문: <https://raw.githubusercontent.com/dmccreary/claude-skills/main/skills/quiz-generator/SKILL.md>

## worked-example-fading-designer · GarethManning
- 323줄 · CC BY-SA 4.0 · 충족 5/31 · 모바일 고려 0/3
- 무엇인가: 절차형 기술 하나에 대해 '모든 단계에 이유가 달린 완전 풀이 예제 → 뒤에서부터 단계가 비는 완성 문제 3~4개 → 표면 특징이 다른 독립 연습 2~3개'의 페이딩 시퀀스를 정해진 출력 형식으로 설계하는 교사용 프롬프트 스킬.
- 가져올 것: 페이딩 순서를 숫자로 고정한 규칙: 1단계는 모든 단계를 빠짐없이 보여 주고 각 단계에 '왜'를 단다(표: Step | Action | Reasoning) → 완성 문제 1은 마지막 단계만, 2는 마지막 2단계, 3은 절차의 약 50%, 4는 첫 단계만 제공 → 독립 연습 2~3개는 같은 절차지만 겉모습을 바꾼다.
- 피할 것: K-12 교사용이라 출력이 학급 배포용 Markdown 표(긴 3열 표)이고 UI·모바일·시각화 규칙이 전혀 없다. 1단계에서 학습자는 '풀지 말고 공부만' 하게 되어 있어 예측 먼저 원칙과 순서가 반대다.
- 원문: <https://raw.githubusercontent.com/garethmanning/education-agent-skills/main/skills/memory-learning-science/worked-example-fading-designer/SKILL.md>

## book-chapter-generator · dmccreary
- 620줄 · CC BY-NC-SA 4.0 · 충족 4/31 · 모바일 고려 0/3
- 무엇인가: learning-graph.json(약 200개 개념의 의존 DAG)과 course-description.md를 읽어 6~20개 챕터에 개념을 배정하고, 선수관계 위반 0건을 assert로 확인한 뒤 사용자 승인을 받아 MkDocs 챕터 디렉터리와 index.md 뼈대만 만드는 설계 스킬(본문은 만들지 않음).
- 가져올 것: 개념을 {id, 선수 개념 목록} 그래프 데이터로 먼저 만들고, '모든 선수 개념이 같은 챕터 또는 앞 챕터에 있다'를 Python assert로 위반 0건이 될 때까지 고친 다음에만 목차를 보여 주고 승인받는 순서. '챕터 간 난이도 급상승 금지'를 감각이 아니라 스크립트 게이트로 만들 수 있다.
- 피할 것: 챕터당 8~25개(최적 12~18) 개념은 책 단위 기준이라 휴대폰 '한 화면 한 개념'에는 과밀하다. 약 200개 개념, MkDocs 빌드, 선행 스킬이 계산한 CIS 점수라는 전제는 1인용 사이트에 과하다.
- 원문: <https://raw.githubusercontent.com/dmccreary/claude-skills/main/skills/book-chapter-generator/SKILL.md>

## skill-creator · anthropics
- 485줄 · Apache-2.0 · 충족 4/31 · 모바일 고려 0/3
- 무엇인가: 스킬 초안 작성 → 테스트 프롬프트 2~3개를 스킬 유/무로 실행 → 채점·벤치마크·리뷰 뷰어로 사람 피드백 수집 → 수정 반복 → description 트리거 최적화 → 패키징을 안내하는 메타 스킬.
- 가져올 것: 이 프로젝트 전용 스킬을 만들 때의 포장 규칙으로 쓴다. SKILL.md에는 500줄 미만의 절차와 '어느 파일을 언제 읽는지'만 두고, 챕터 골격·모바일 규칙·단계 데이터 스키마는 references/에, 공용 레슨 템플릿은 assets/에, 선수관계 검증과 trace 생성은 scripts/에 둔다. '테스트 실행마다 같은 헬퍼를 다시 짜고 있으면 한 번만 써서 scripts/에 넣어라'가 template-first의 근거다.
- 피할 것: 1인 프로젝트에 벤치마크 전체(스킬 유/무 병렬 서브에이전트, 분산 분석, 블라인드 비교, 20쿼리 × 3회 × 최대 5반복 description 최적화)는 토큰과 시간이 과하다. 리뷰 뷰어는 로컬 서버와 브라우저, 화살표 키 탐색을 전제한다.
- 원문: <https://raw.githubusercontent.com/anthropics/skills/main/skills/skill-creator/SKILL.md>

## worked-example-walkthrough · lyndonkl
- 204줄 · LICENSE 파일 없음(README에 자유 사용 문구) · 충족 4/31 · 모바일 고려 0/3
- 무엇인가: 벡터·행렬·ML 계산을 '번호 붙은 프레임(연산 1개 + 실제 값 상태 + Notice 한 문장)'의 순서로 풀어 손으로 다시 따라갈 수 있게 하는 텍스트 전용 워크스루 작성 규칙이다.
- 가져올 것: 알고리즘 트레이스의 단위를 '프레임 = 연산 1개 + 실제 값 상태 + 놓치기 쉬운 점 한 문장'으로 고정하고 3~7 프레임 상한을 둔다(넘으면 입력을 줄이거나 워크스루를 둘로 쪼갠다). 여기에 SKILL.md 끝의 Quick Reference처럼 '알고리즘별 권장 최소 입력 + 프레임 수' 표를 사이트 기획 단계에서 먼저 만들어 두면, 장마다 트레이스 길이가 일정해져 난이도 급상승을 막고 '1분 안에 머릿속으로 다시 돌릴 수 있는 크기'라는 기준을 그대로 쓸 수 있다. 마지막 프레임은 불변식 검증(sanity check) 또는 '입력 하나만 바꿔 다시 해 보기'로 끝낸다.
- 피할 것: 순수 텍스트 스킬이라 HTML, 스테퍼 UI, 모바일, 접근성 규칙이 전혀 없다. Pattern C의 'two columns' 병렬 프레임은 세로 폰 화면에서 깨진다.
- 원문: <https://raw.githubusercontent.com/lyndonkl/claude/main/skills/worked-example-walkthrough/SKILL.md>

## tech-visualizer · yfe404
- 153줄 · MIT · 충족 4/31 · 모바일 고려 0/3
- 무엇인가: 암호·네트워크·자료구조·ML 개념을 단계 스테퍼, 라이브 입력, hover 검사가 달린 다크 테마 인터랙티브 시각화(HTML 또는 React)로 만든다.
- 가져올 것: 코드 작성 전에 시각화마다 'aha moment' 하나를 문장으로 먼저 정하고, 스테퍼에는 'Step 3 of 7: 무엇을 하는 단계'라는 표시와 1~2문장 설명을 시각화 옆에 항상 노출한다(툴팁에만 넣는 것 금지). 요소 상태를 현재/완료/예정 3가지로만 구분하고, 색의 의미(입력, 키, 중간 값, 출력, 현재 위치)를 CSS 변수로 먼저 고정해 범례와 함께 전 장에서 재사용한다. '입력이 전부 같은 값이면?' 같은 엣지 케이스 버튼을 스테퍼 옆에 둔다.
- 피할 것: 768px 이상 데스크톱 전제, hover 검사, side-by-side 비교, 방향키 조작은 세로 폰·한 손 사용과 반대다. Quality Checklist가 Google Fonts 로딩을 요구해 오프라인이 깨진다.
- 주의: 데스크톱 전제 명시
- 원문: <https://raw.githubusercontent.com/yfe404/tech-visualizer/main/tech-visualizer/SKILL.md>

## explorable-explanations · third774
- 316줄 · 라이선스 표기 없음 · 충족 4/31 · 모바일 고려 1/3
- 무엇인가: 슬라이더·애니메이션·스텝 버튼으로 개념을 직접 만져 보게 하는 단일 HTML '탐색형 설명'을 Tailwind CDN + 바닐라 JS(필요 시 Vue 3 CDN)로 만드는 OpenCode용 스킬.
- 가져올 것: 'Complexity Budget + One Knob at a Time + Name It Last' 세 규칙 묶음. 개념이 요구하는 최소 상호작용만 넣고(컨트롤·뷰·애니메이션 프레임 하나하나가 주의력 비용), 새 컨트롤 하나는 한 가지만 가르치게 하며, 용어는 직관이 생긴 뒤에 붙인다(먼저 '입자가 얼마나 멀리 움직이나' + 슬라이더, 그다음 '이것을 진폭이라 부른다'). 이 프로젝트에서는 알고리즘 페이지마다 조작 가능한 값을 1개로 시작하고, 불변식·점화식의 공식 이름은 트레이스를 한 번 본 뒤에 표시하는 규칙으로 옮기면 된다.
- 피할 것: Tailwind Play CDN(cdn.tailwindcss.com)과 unpkg Vue에 뷰 시점 의존이라 오프라인이나 불안정한 회선에서 볼 수 없다. 스크롤 구동형은 '고정된 시각화 옆으로 글이 흐르는 2단 레이아웃'을 쓰고 기본 레이아웃도 컨트롤 패널과 설명을 좌우로 나란히 두며 폭 기준이 ~900px라 세로 휴대폰에 맞지 않는다.
- 주의: 데스크톱 전제 명시
- 원문: <https://raw.githubusercontent.com/third774/dotfiles/master/opencode/skills/explorable-explanations/SKILL.md>

## learning-graph-generator · dmccreary
- 520줄 · CC BY-NC-SA 4.0 · 충족 3/31 · 모바일 고려 0/3
- 무엇인가: 강좌 설명서에서 300~600개 개념 목록, 선수 의존 관계 DAG(CSV→JSON), 분류 체계, 품질 검증 보고서를 13단계 절차로 생성하는 스킬.
- 가져올 것: 챕터를 쓰기 전에 '개념 목록 → 의존 CSV(ConceptID, ConceptLabel, Dependencies) → 스크립트 검증 → 사람 검토' 순서를 강제하는 파이프라인. "난이도가 급격히 뛰면 안 된다"는 이 프로젝트의 HARD 제약을 기계적으로 검사할 수 있는 장치는 9개 중 이것뿐이다.
- 피할 것: 300~600개 규모, MkDocs 전제(nav 수정, docs/ 구조), Bloom 루브릭 100점 채점, 12개 분류와 24색 팔레트, vis-network 그래프 뷰어는 개인용 모바일 교재에 과하다. SKILL.md가 520줄 한 덩어리라 스킬 패키징의 본보기로는 부적합하다.
- 원문: <https://raw.githubusercontent.com/dmccreary/claude-skills/main/skills/learning-graph-generator/SKILL.md>

## interactive-explainer · allank
- 134줄 · 라이선스 표기 없음 · 충족 3/31 · 모바일 고려 0/3
- 무엇인가: 선형 워크스루나 원자료에서 '읽기만으로는 가장 이해하기 어려운 한 가지'를 골라 결정 트리, 단계 재생, 클릭형 도표, 슬라이더 탐색기, 토글 비교 중 맞는 유형의 단일 HTML 시각화를 만들고 브라우저로 여는 스킬.
- 가져올 것: 만들기 전에 '이 주제에서 읽기만으로는 가장 안 잡히는 한 가지가 무엇인가'를 먼저 정하고 시각화를 그 하나에만 맞추는 절차와 '내용 유형 → 시각화 유형' 표. 알고리즘 챕터마다 핵심 불변식 하나를 정한 뒤 유형을 고르게 하면 된다: 순차 과정은 단계 재생, 분기 로직은 입력에 따라 지나간 경로가 강조되는 결정 트리, 매개변수 개념은 값을 바꾸면 결과가 변하는 탐색기. 단계 재생의 '상세 패널은 라벨이 아니라 안내자 해설'과 '애니메이션은 논리의 이동을 보일 때만, 200~400ms' 규칙도 그대로 쓸 수 있다.
- 피할 것: 레이아웃 패턴이 전부 데스크톱 기준이다: 입력은 왼쪽이나 위, 결과는 오른쪽이나 아래, 컨트롤은 사이드바, 관계는 hover로 표시, 툴팁 라벨, side-by-side 비교. 모바일 규칙은 한 줄도 없다. 공용 템플릿이 없어 매번 처음부터 만들므로 챕터마다 모양이 달라진다.
- 주의: 데스크톱 전제 명시
- 원문: <https://raw.githubusercontent.com/allank/agent-skills/main/plugins/pm-craft/skills/interactive-explainer/SKILL.md>

## pypeep · BITOCTA
- 117줄 · MIT · 충족 3/31 · 모바일 고려 0/3
- 무엇인가: sys.settrace()로 Python 파일이나 스니펫을 실제로 실행해 줄 단위 이벤트(call/line/return/exception/limit, 바뀐 변수, 반환값, stdout, 객체 id)를 JSON 배열로 뽑아 에이전트가 사후 분석하게 하는 비대화형 추적 스킬.
- 가져올 것: 사이트의 단계 데이터를 손으로 쓰지 말고 빌드 때 실제 Python 실행에서 만든다: sys.settrace로 예제 코드를 돌려 [{event, line, function, changed, return_value, stdout}] 배열을 얻고 stepper는 그 JSON만 재생한다. 그러면 '몇 번째 줄에서 어떤 변수가 무슨 값이 됐는지'가 지어낸 값일 수 없다. overview 모드(직전 단계와 비교해 바뀐 변수만)는 휴대폰 한 화면 캡션 분량에 맞는다.
- 피할 것: 출력은 디버깅용이라 단계별 설명 문장이 없다: 캡션은 따로 써야 한다. locals 표현(__id__, __type__, __entries__)과 full 모드는 학습 화면에 과하다.
- 원문: <https://raw.githubusercontent.com/BITOCTA/pypeep/main/skills/pypeep/SKILL.md>

## algo:blank · itsme-shawn
- 178줄 · MIT · 충족 2/31 · 모바일 고려 0/3
- 무엇인가: 완성된 알고리즘 풀이 코드에서 핵심 로직을 ____(밑줄 4개)로 가리고 번호 붙은 TODO 주석을 달아 `_blank` 접미사 파일로 저장하는 빈칸 연습 생성 스킬(한국어).
- 가져올 것: '무엇을 가리고 무엇을 남길지'의 기준표. 가릴 것은 자료구조 초기화, 핵심 조건문, 점화식·계산식, 방문 처리, 큐/스택 조작, DP 점화식, 반환값이고, 남길 것은 import, 함수 시그니처, 변수명, 출력문, 그리고 테스트가 든 main 전체다. 이 프로젝트의 목표인 '공식·불변식을 머릿속에서 재생'과 정확히 겹친다. 가려지는 줄이 곧 그 알고리즘의 불변식 줄이기 때문이다.
- 피할 것: (1) 파일을 변환해 IDE에서 타이핑으로 채우고 실행하는 워크플로 전제다. 공장에서 폰 한 손으로 볼 때는 타이핑이 불가능하므로 탭 공개나 선택지로 바꿔야 한다.
- 원문: <https://raw.githubusercontent.com/itsme-shawn/algoKit-mcp/ef36028d7a22d483b5f64baabd2f0041cdfc07de/skills/algo:blank/SKILL.md>

## frontend-design · anthropics
- 71줄 · Apache-2.0 · 충족 2/31 · 모바일 고려 1/3
- 무엇인가: 새 UI를 만들 때 주제에서 근거를 찾아 템플릿 같지 않은 색·서체·레이아웃을 정하도록 하는 디자인 지침으로, 토큰 계획 → 브리프 대조 → 구현 → 자기비평 순서를 요구한다.
- 가져올 것: 구현 전에 '토큰 계획'을 글로 먼저 쓰게 하는 2-패스: 색 4~6개 hex, 서체 역할, ASCII 와이어프레임, 원칙을 적고 브리프와 대조해 고친 뒤에만 코드를 쓴다. 본 프로젝트에서는 이것을 장마다 반복하지 말고 사이트 공용 토큰을 정하는 첫 단계에서 한 번만 쓴다. 함께 가져올 규칙은 품질 하한(모바일까지 반응형, 포커스 표시, reduced motion), '사용자 행동에 답하는 모션(열림, 펼침, 확인)만 환영', '같은 동작은 흐름 끝까지 같은 이름'(버튼·단계 라벨 용어 일관성), 줄 길이 80자 미만, 스크린샷으로 자기비평이다.
- 피할 것: 학습 설계 규칙이 전혀 없다(33개 중 26개가 no). '매번 다른 정체성, 미적 모험'을 요구하는 스튜디오 디자이너 역할 설정은 장마다 같은 틀을 유지해야 하는 교재와 반대 방향이다.
- 원문: <https://raw.githubusercontent.com/anthropics/skills/main/skills/frontend-design/SKILL.md>

## cognitive-load-analyser · GarethManning
- 228줄 · CC BY-SA 4.0 · 충족 1/31 · 모바일 고려 0/3
- 무엇인가: 교사가 준 학습 과제 설명과 학습자 수준을 받아 내재적·외재적·본질적 인지 부하를 Low/Medium/High로 평가하고, 문제 지점마다 '문제 – 위반한 원리 – 정확한 수정'을 고정 형식으로 돌려주는 분석 프롬프트 스킬.
- 가져올 것: 챕터를 내보내기 전 검수 단계로 '요소 상호작용 수 세기'를 돌린다: 이 화면에서 학습자가 동시에 붙들어야 하는 새 요소가 몇 개인지 숫자로 적고(기준선 4~7), 앞 챕터보다 크게 늘면 나눈다. 외재적 부하 점검 항목 중 둘이 이 프로젝트에 바로 걸린다. split-attention은 코드와 시각화·설명이 떨어져 있어 스크롤로 오가야 하는지를 묻고(한 화면에 합치고 라벨을 그림 안에 넣는다), transient information은 애니메이션으로 지나가 버리는 정보가 남아 있어야 하는지를 묻는다(각 단계 상태를 정지 화면으로 유지한다).
- 피할 것: 교실 과제(학년, 워크시트, 종이 세 장)용 프롬프트이지 사이트 생성 규칙이 아니다. 입출력 스키마 YAML, context engine, chains_well_with는 이 저장소의 MCP 체계 전용이다.
- 원문: <https://raw.githubusercontent.com/GarethManning/education-agent-skills/main/skills/memory-learning-science/cognitive-load-analyser/SKILL.md>

## leetcode-teacher · jamesrochabrun
- 921줄 · MIT · 충족 1/31 · 모바일 고려 0/3
- 무엇인가: 면접 대비용 DSA 교사로, 20개 패턴 카드와 5단계 난이도, 실제 서비스 시나리오 문제, 브라우저 코딩 playground HTML(Python 등 4개 언어)을 제시한다.
- 가져올 것: 패턴 카드의 4줄 고정 형식 'Pattern(한 줄 원리) / Use when(언제 쓰나) / Example / Complexity(시간, 공간)'. 서서 머릿속으로 되뇌는 '공식 카드'의 최소 형태로 바로 쓸 수 있다. 여기에 5단계 사다리(배열·문자열·기초 해시 → 슬라이딩 윈도우·투 포인터·기초 트리 → BFS/DFS·이분 탐색·기초 DP·힙 → 고급 DP·그래프·백트래킹·트라이 → 최적화)를 장 순서 초안으로 참고하고, 'Brute Force → 병목 찾기 → 패턴 적용 → 공간 최적화' 순서와 '힌트 4단계 뒤에 해답 공개'를 문제 풀이 절의 틀로 삼는다.
- 피할 것: 예시 playground의 테스트 결과가 실제 실행이 아니라 `Math.random() > 0.3`으로 만든 가짜다(주석도 'Simulated result'). 본 프로젝트의 '출력은 실제 실행에서' 원칙과 정면으로 어긋나므로 이 HTML을 본보기로 쓰면 안 된다.
- 주의: 데스크톱 전제 명시
- 원문: <https://raw.githubusercontent.com/jamesrochabrun/skills/main/skills/leetcode-teacher/SKILL.md>

## edu-visual-trace · molechowski
- **원문 미확보.** 아래는 레지스트리 렌더 페이지에서 확인된 범위다.
- 0줄 · 라이선스 표기 없음 · 충족 0/31 · 모바일 고려 0/3
- 무엇인가: (원문 미확보) skills.sh 렌더 페이지에서 확인된 범위로는 손으로 그린 ASCII 다이어그램으로 상태 변화를 한 스텝씩 보여 주며 개념을 설명하는 스킬.
- 가져올 것: 원문을 받지 못해 기능 표는 지시대로 전부 no로 뒀다.
- 피할 것: 원문이 확인되지 않은 수치(원소 5~8개, 폭 약 80자, references/style-guide.md·examples.md 등)를 이 스킬의 규칙이라며 근거로 인용하면 안 된다. 또 확인된 범위에서 이 스킬의 출력은 터미널용 ASCII 그림이라, 폰 세로 화면(고정폭 약 35~40자)에서는 그대로 쓸 수 없다.
