# 07. 출처와 검증 상태

> 사실 확인 기록이다. "계획에 주는 영향" 항목은 폐기된 계획을 기준으로 쓰였으니 따르지 않는다. 이 교재의 기준은 `.claude/skills/textbook-chapter/SKILL.md`다.

조사일 2026-11-23. 1차 조사에서 나온 주장 가운데 계획을 좌우하는 것을 골라, 1차 자료(공식 문서, 저장소 원문, 레지스트리, 논문)를 다시 받아 반증을 시도했다.

## 1. 검증 결과 요약

| 판정 | 건수 | 뜻 |
|---|---|---|
| 확인 | 32 | 1차 자료가 숫자·날짜·이름까지 뒷받침 |
| 부분 확인 | 10 | 핵심은 맞지만 고칠 부분이 있음 |
| 반증 | 0 | 1차 자료와 어긋남 |
| 확인 불가 | 0 | 1차 자료에 닿지 못함 |

"확인"으로 판정된 항목에도 표현을 고친 것이 많다. 판정보다 "확인한 내용"을 읽는다. 모두 그날 읽은 자료 기준이고, 버전과 서비스 상태는 바뀐다.

## 2. 주장별 판정

### 기술(T)

**T1 · 확인**

- 주장: Material for MkDocs는 2025-11경 유지보수 모드에 들어갔고 중요 수정만 2027-05-05까지 제공하며, MkDocs 2.0과 호환되지 않는다(후속: Zensical).
- 확인한 내용: 2025-11-05 Zensical 발표와 함께 Material for MkDocs는 maintenance mode가 됐다(기능 개발 종료). 수정 범위는 'critical bugs and security vulnerabilities'뿐이고 기한은 2027-05-05다. 이 날짜는 2026-09-16에 발표된 6개월 연장의 결과이며 README는 이를 'end of life'라고 부른다. 최신 버전은 9.8.2(2026-11-19, privacy 플러그인 보안 수정)이고, 9.8.0(2026-10-24)부터 Python 3.11 이상을 요구하며 의존성은 `mkdocs<2,>=1.6`이다. MkDocs 2.0은 아직 정식 릴리스가 아니다(PyPI 2.0.dev0은 2026-08-28, 최신 2.0.dev6은 2026-09-15, 안정판은 1.6.1/2024-08-30). 'MkDocs 2.0과 비호환, 플러그인 시스템 없음, TOML 설정'은 이해당사자인 squidfunk가 프리릴리스를 평가한 내용이다. Zensical은 0.1.0이 2026-11-05에 실제로 나왔고 최신은 0.1.3(2026-11-20)이다.
- 계획에 주는 영향: 결론은 그대로다. 수명 종료까지 약 5.5개월 남은 Material for MkDocs로 새 프로젝트를 시작하면 안 된다. Python 단일 툴체인을 원하면 Zensical 0.1.x가 후보지만 나온 지 3주 된 0.1 라인이라 플러그인 의존 없이 순수 Markdown과 커스텀 엘리먼트 범위에서만 써야 한다. Hello Algo의 스택(MkDocs Material)을 그대로 따라 하는 계획은 폐기한다.
- 출처: <https://squidfunk.github.io/mkdocs-material/blog/2025/11/05/zensical/> · <https://squidfunk.github.io/mkdocs-material/blog/2026/02/18/mkdocs-2.0/> · <https://raw.githubusercontent.com/squidfunk/mkdocs-material/master/CHANGELOG> · <https://raw.githubusercontent.com/squidfunk/mkdocs-material/master/README.md>

**T2 · 확인**

- 주장: Pyodide 현재 릴리스는 '314.0.8' 방식 버전이고 코어 다운로드는 원본 약 13.4MB, 전송 약 6MB이며, Pyodide에서 sys.settrace가 동작한다.
- 확인한 내용: npm latest는 pyodide 314.0.8(2026-11-13)이고 next 태그는 315.0.0-alpha.2다. 버전은 Python 버전을 따른다(314.x는 Python 3.14, 0.29.x는 Python 3.13, 연 1회 메이저). 오늘 jsDelivr에서 잰 코어 크기는 pyodide.asm.wasm 9,597,892B(brotli 3,439,687 / gzip 3,600,730), python_stdlib.zip 2,545,550B(추가 압축 없음), pyodide.asm.mjs 1,250,259B(brotli 207,278 / gzip 261,261), pyodide.mjs 17,758B, pyodide-lock.json 119,077B다. 합계는 원본 13.53MB(앞의 세 파일만 13.39MB), 전송 brotli 약 6.22MB, gzip 약 6.44MB다. 스윕의 'brotli 5.9MB'(wasm 3,106,498B)는 재현되지 않아 '약 6.2~6.4MB'가 맞다. sys.settrace는 Pyodide에서 지원된다(직접 실행해 보지는 않았고 변경 기록으로 확인).
- 계획에 주는 영향: 계획은 바뀌지 않는다. 폰 기본 로딩에는 넣지 않고, 넣더라도 버튼을 눌렀을 때만 지연 로딩하며 서비스워커 프리캐시에서 뺀다. GitHub Pages는 gzip만 주므로 실제 전송은 약 6.4MB로 잡는다. Pyodide 314는 Python 3.14라 heapq의 *_max 함수가 있고, 빌드 타임 CPython 추적기와 같은 settrace 코드를 쓸 수 있다.
- 출처: <https://registry.npmjs.org/pyodide> · <https://blog.pyodide.org/posts/314-release/> · <https://raw.githubusercontent.com/pyodide/pyodide/main/docs/project/changelog.md> · <https://data.jsdelivr.com/v1/packages/npm/pyodide@314.0.8>

**T3 · 부분 확인**

- 주장: MicroPython WebAssembly 빌드는 원본 약 450KB(brotli 약 170KB)이고 settrace 빌드가 따로 있으며, 공식 npm 패키지 @micropython/micropython-webassembly-pyscript에서 sys.settrace를 쓸 수 있다.
- 확인한 내용: 크기는 맞다. @micropython/micropython-webassembly-pyscript@1.29.0-6(2026-08-24, npm latest)에서 micropython.wasm은 449,553B(brotli 170,998 / gzip 197,580), micropython.mjs는 110,120B(brotli 26,981 / gzip 30,912), micropython-settrace.wasm은 492,490B(brotli 180,349 / gzip 209,596)다. 다만 세 가지를 바로잡아야 한다. (1) 기본 micropython.wasm에는 sys.settrace가 없다. 패키지에 함께 든 micropython-settrace.wasm만 지원하며, 이 파일은 1.28.0-6(2026-04-06)부터 들어갔고 1.27.0에는 없다. 전용 mjs가 없어 같은 micropython.mjs로 그 wasm을 지정해 불러와야 한다. (2) 스윕이 인용한 README 문장('a -settrace build with sys.settrace support for debuggers')은 pyscript 패키지가 아니라 새 패키지 @micropython/micropython-webassembly-browser(1.30.0-preview.302, 2026-11-17, JSPI 필요)를 설명한다. (3) MicroPython의 settrace 프레임 객체는 f_back, f_code, f_globals, f_lasti, f_lineno만 제공하고 f_locals가 없다. 그래서 줄 번호와 전역은 얻어도 지역 변수 스냅샷은 얻지 못한다.
- 계획에 주는 영향: '나중에 MicroPython settrace 빌드로 브라우저에서 같은 추적기를 돌린다'는 계획은 성립하지 않는다. f_locals가 없어 지역 변수(i, j, lo, hi)를 스텝마다 찍는 Python Tutor식 추적기를 그대로 옮길 수 없다. 정답 trace는 CPython 빌드 타임 산출물로 확정하고, MicroPython은 '내 입력으로 결과만 실행'하는 용도로만 검토한다. 브라우저 추적이 꼭 필요하면 Pyodide(지연 로딩)나 코드 계측 방식이 필요하다. 표준 라이브러리 차이(bisect, lru_cache 등)도 교재 코드와 어긋날 수 있다.
- 출처: <https://registry.npmjs.org/@micropython%2Fmicropython-webassembly-pyscript> · <https://data.jsdelivr.com/v1/packages/npm/@micropython/micropython-webassembly-pyscript@1.29.0-6> · <https://raw.githubusercontent.com/micropython/micropython/master/ports/webassembly/README.md> · <https://raw.githubusercontent.com/micropython/micropython/master/ports/webassembly/Makefile>

**T4 · 부분 확인**

- 주장: ts-fsrs 최신은 6.x이고 기본 알고리즘은 FSRS-7(또는 FSRS-6)이며 압축 약 11KB이고, API가 createEmptyCard/repeat에서 바뀌었다.
- 확인한 내용: ts-fsrs 최신은 6.0.1(2026-11-22)이고 6.0.0은 2026-10-28에 나왔다. `DefaultScheduler()`는 version을 생략하면 FSRS-7을 쓴다. 새 API는 `await DefaultScheduler()`, `scheduler.newCard({ now })`, `scheduler.preview({ card, now })`, `scheduler.review({ card, grade: Rating.Good, now })`이고 결과의 card와 revlog를 둘 다 저장한다. 구 API는 삭제되지 않았다. `createEmptyCard`, `fsrs()`, `FSRS`는 v6에서도 export되지만 deprecated이고 FSRS-6으로 동작한다. 크기 '약 11KB'는 진입 파일 dist/index.mjs(43,128B, gzip 10,590 / brotli 10,968) 하나만 잰 값이다. 이 파일은 middlewares(32,070B), fsrs-6(10,957B) 같은 청크와 의존성 @open-spaced-repetition/srs-kit@1.0.1을 정적으로 가져오고 모델(fsrs-7.mjs 12,975B)을 동적으로 가져온다. 전부 묶인 UMD는 196,175B이고 압축하면 약 40KB다. 실제 번들은 트리 셰이킹에 따라 25~40KB(gzip)로 보는 것이 맞다. engines는 node >=24.0.0이다.
- 계획에 주는 영향: 번들 예산을 11KB가 아니라 약 40KB로 잡아야 하고, 빌드 환경에 Node 24 이상이 필요하다. 6.0.x는 나온 지 한 달도 안 됐고 FSRS-7은 카드 상태 필드가 다르다(stabilityFast 등). 그래서 카드 수십~수백 장짜리 개인 교재는 Leitner나 반감기 방식으로 직접 구현해 시작하고 ts-fsrs는 뒤로 미루는 쪽이 더 타당하다. 쓰게 되면 SKILL.md에 'ts-fsrs@6, DefaultScheduler API, llms.txt 참조'를 못박는다.
- 출처: <https://registry.npmjs.org/ts-fsrs> · <https://cdn.jsdelivr.net/npm/ts-fsrs@6.0.1/README.md> · <https://cdn.jsdelivr.net/npm/ts-fsrs@6.0.1/CHANGELOG.md> · <https://cdn.jsdelivr.net/npm/ts-fsrs@6.0.1/dist/index.mjs>

**T5 · 확인**

- 주장: Python 3.14에서 heapq.heapify_max, heappush_max, heappop_max가 공개 함수로 추가됐다. 2026년 말 안정 버전은 무엇이고, 줄 이벤트 기록에는 sys.monitoring(PEP 669)이 sys.settrace보다 나은가.
- 확인한 내용: Python 3.14에서 max-heap 함수 5개가 추가됐다. heapify_max, heappush_max, heappop_max, heappushpop_max, heapreplace_max이며 모두 'Added in version 3.14'다. 2026-11-23 기준 최신 안정판은 Python 3.15.2(2026-10-25)이고 3.15.0은 2026-10-09에 나왔다. 3.14는 bugfix 단계(3.14.10), 3.13은 security 전용(3.13.18), 3.10은 end-of-life다. sys.monitoring의 LINE 콜백은 `func(code: CodeType, line_number: int)`라 프레임을 받지 않으므로 지역 변수는 sys._getframe(1)로 읽어야 한다. 장점은 위치별로 이벤트를 끌 수 있어(sys.monitoring.DISABLE) 오버헤드가 낮다는 것이다. 3.14부터 `bdb.Bdb(skip=None, backend='settrace')`에 'monitoring' 백엔드가 생겼지만 기본값은 settrace다. 수십 스텝짜리 고정 예제의 모든 줄을 기록하는 용도에는 settrace(또는 bdb)가 더 단순하고 이식성이 좋다.
- 계획에 주는 영향: 교재의 기준 Python을 3.14 이상으로 명시해야 heapq의 *_max 함수를 쓸 수 있다. 현재 작업 환경의 python3는 3.13.18이라 빌드 타임 trace 생성과 테스트에서 실패한다. CI와 로컬에 3.14 이상을 설치하거나, 본문은 부호 반전 관용구로 쓰고 *_max는 '3.14+' 상자에만 둔다. Python Tutor(3.11)에서도 실행되지 않는다. 추적기는 sys.settrace 하나로 유지한다.
- 출처: <https://docs.python.org/3/library/heapq.html> · <https://www.python.org/downloads/> · <https://docs.python.org/3/library/sys.monitoring.html> · <https://docs.python.org/3/library/bdb.html>

**T6 · 확인**

- 주장: iOS/iPadOS Safari는 사이트와 상호작용 없이 Safari를 7일 쓰면 스크립트 쓰기 가능 저장소(localStorage, IndexedDB, 서비스워커 등록과 캐시)를 지우며, 홈 화면에 추가한 웹앱은 예외이고 Safari와 저장소가 분리된다.
- 확인한 내용: WebKit ITP는 사이트와 사용자 상호작용이 없는 채로 'Safari 사용일' 기준 7일이 지나면 그 사이트의 스크립트 쓰기 가능 저장소를 전부 지운다. 달력 날짜가 아니라 Safari를 쓴 날 수다. 대상은 IndexedDB, LocalStorage, Media keys, SessionStorage, Service Worker 등록과 캐시, JS로 만든 쿠키다. 홈 화면 웹앱의 1차 도메인은 이 7일 상한에서 면제되고 데이터가 Safari와 격리된다. 2024~2026년에 이 규칙이 바뀌었다는 1차 자료는 찾지 못했다(Safari 26.0 기능 글은 502로 읽지 못함). 달라진 점은 iOS/iPadOS 26부터 홈 화면에 추가한 모든 사이트가 기본으로 웹앱으로 열린다는 것이다('Open as Web App' 토글, manifest 불필요). Safari 17 이후 저장소 정책은 브라우저 앱 기준 오리진 쿼터가 디스크의 최대 60%, 전체 80%이고 LRU로 축출하며, persist() 승인은 홈 화면 웹앱 여부 같은 휴리스틱을 따른다.
- 계획에 주는 영향: iPhone이라면 첫날 '홈 화면에 추가'를 하고 그 아이콘으로만 여는 것이 필수다. Safari 탭에서 쌓은 진도는 설치본으로 넘어가지 않는다. iOS 26 이상에서는 manifest가 없어도 웹앱으로 열리므로 설치 안내 문구가 단순해진다. 기기와 무관하게 진도 JSON 내보내기·가져오기와 navigator.storage.persist() 요청은 유지한다. 사용자의 폰이 Android인지 iPhone인지 아직 확인되지 않았다.
- 출처: <https://webkit.org/blog/10218/full-third-party-cookie-blocking-and-more/> · <https://webkit.org/tracking-prevention/> · <https://webkit.org/blog/14403/updates-to-storage-policy/> · <https://webkit.org/blog/16993/news-from-wwdc25-web-technology-coming-this-fall-in-safari-26-beta/>

**T7 · 확인**

- 주장: GitHub Pages는 gzip만 제공하고 brotli는 없으며 cache-control max-age=600을 보낸다. GitHub Free에서는 public 저장소에서만 Pages가 되고(private은 Pro/Team/Enterprise), private 저장소에서 게시해도 사이트는 공개된다. 대안인 Cloudflare Pages 무료 티어의 사실관계(private 저장소, brotli).
- 확인한 내용: GitHub 문서 기준으로 Pages는 GitHub Free에서 public 저장소만, Pro/Team/Enterprise에서 public과 private 저장소에서 쓸 수 있다. private 저장소에서 게시해도 사이트는 인터넷에 공개되고, 비공개 게시는 Enterprise Cloud 조직만 가능하다. 한도는 사이트 1GB, 대역폭 월 100GB(소프트), 시간당 10빌드(소프트, 커스텀 Actions 워크플로 제외), 배포 타임아웃 10분이다. 오늘 측정에서 `Accept-Encoding: br, gzip, zstd` 요청에는 `content-encoding: gzip`, br만 보낸 요청에는 무압축(content-length 78359)이 왔고 `cache-control: max-age=600`이었다. 이 두 동작은 문서에 없는 관측값이다. Cloudflare Pages 무료 티어는 월 500빌드(동시 1개), 사이트당 20,000파일, 파일당 25MiB, _headers 규칙 100개이고 gzip과 brotli를 제공하며 기본 캐시 헤더는 `public, max-age=0, must-revalidate`다. GitHub 앱 연동에서 저장소를 선택하는 방식이라 private 저장소를 연결할 수 있다(문서가 private을 제한하지 않음). 다만 Cloudflare는 이제 새 프로젝트를 Pages가 아닌 Workers(Static Assets, 무료 20,000파일/25MiB)로 시작하라고 안내한다.
- 계획에 주는 영향: GitHub Free 계정이면 저장소를 public으로 둬야 Pages를 쓸 수 있다. 그러면 저장소와 사이트가 모두 공개되므로 Hello Algo 같은 CC BY-NC-SA 자료를 옮겨 쓰면 라이선스 의무가 따른다. 저장소를 비공개로 두려면 Cloudflare를 쓰되 Pages가 아니라 Workers Static Assets를 1순위로 본다. 어느 쪽이든 사이트 자체는 공개 URL이다. max-age=600과 gzip 전용은 보장된 계약이 아니므로 오프라인과 재방문 속도는 서비스워커에 맡긴다.
- 출처: <https://docs.github.com/en/pages/getting-started-with-github-pages/what-is-github-pages> · <https://docs.github.com/en/pages/getting-started-with-github-pages/creating-a-github-pages-site> · <https://docs.github.com/en/pages/getting-started-with-github-pages/changing-the-visibility-of-your-github-pages-site> · <https://docs.github.com/en/pages/getting-started-with-github-pages/github-pages-limits>

**T8 · 확인**

- 주장: Hello Algo(krahets/hello-algo) 저장소에 한국어판이 있다(ko/ 디렉터리, 0~16장, Python 코드 포함). 버전은 약 1.3.0이고 글의 라이선스는 CC BY-NC-SA 4.0이다.
- 확인한 내용: main 브랜치에 ko/가 있다. ko/mkdocs.yml은 `INHERIT: ../mkdocs.yml`, site_name 'Hello 알고리즘', `version: 1.3.0`, Noto Sans KR이다. nav는 머리말, 제0장(들어가며)~제16장(부록), 참고 문헌이며 nav에 걸린 118개 md 파일이 모두 있고 본문은 한국어다(코드 블록을 뺀 한글 140,741자, 한자 88자). 2~15장에는 '요약'과 '연습 문제(exercises.md)' 절이 있다. ko/codes/python/에 한국어 docstring과 주석이 달린 Python 코드와 test_all.py가 있다. 라이선스는 글만이 아니라 저장소 전체에 적용된다. 글, 코드, 그림, 사진, 영상이 모두 CC BY-NC-SA 4.0이고 코드에 별도의 MIT 같은 라이선스는 없다. 번역 주체와 방식(사람인지 기계인지)과 품질은 저장소에 적혀 있지 않아 확인하지 못했다. 한국어 PDF/EPUB 제공 여부도 확인하지 못했다(릴리스 페이지 403).
- 계획에 주는 영향: 코드도 CC BY-NC-SA 4.0이므로 Hello Algo의 Python 코드를 베껴 공개 저장소나 사이트에 올리면 출처 표시, 비영리, 동일조건 의무가 생긴다. 구조, 장 순서, 한국어 용어는 참고하되 코드와 문장과 그림은 새로 쓰는 것이 안전하다. 가져다 쓴다면 사이트 전체를 CC BY-NC-SA로 공개해야 한다. 한국어 번역 품질은 사용자가 직접 한두 절을 읽어 판단해야 한다.
- 출처: <https://raw.githubusercontent.com/krahets/hello-algo/main/ko/mkdocs.yml> · <https://raw.githubusercontent.com/krahets/hello-algo/main/ko/README.md> · <https://raw.githubusercontent.com/krahets/hello-algo/main/README.md> · <https://raw.githubusercontent.com/krahets/hello-algo/main/LICENSE>

**T9 · 확인**

- 주장: Hello Algo의 '애니메이션'은 번호 붙은 정적 스텝 프레임 묶음(탭 <1>..<n>)이고, 코드 실행 시각화는 Python Tutor를 임베드한다.
- 확인한 내용: 챕터 원본 마크다운은 pymdownx.tabbed 문법 `=== "<1>"` … `=== "<7>"`의 탭마다 정적 SVG 한 장(binary_search_step1.svg ~ step7.svg)을 넣는다. 본문 코드는 ```` ```src ```` 블록의 `[file]{binary_search}-[class]{}-[func]{binary_search}` 자리표시자로 소스 파일에서 주입한다. 빌드 결과물(docs 브랜치)에는 코드 블록 아래 `??? pythontutor "可视化运行"` 접이식 블록이 있고, 그 안에 높이 549px의 `<iframe class="pythontutor-iframe" src="https://pythontutor.com/iframe-embed.html#code=...">`가 들어간다. 코드를 URL에 인코딩해 pythontutor.com에 맡기는 온라인 iframe이고 자체 추적기는 없다.
- 계획에 주는 영향: 계획은 그대로다. 알고리즘당 5~9장의 번호 붙은 정적 프레임과 캡션이면 충분하고 애니메이션 엔진은 필요 없다. Python Tutor iframe 방식은 네트워크가 필요하고 높이 549px 고정에 데스크톱 UI이며 Python 3.11이라 공장, 오프라인, 폰 세로 화면에 맞지 않는다. 빌드 타임 trace와 자체 변수 표로 대체한다.
- 출처: <https://raw.githubusercontent.com/krahets/hello-algo/main/ko/docs/chapter_searching/binary_search.md> · <https://raw.githubusercontent.com/krahets/hello-algo/main/ko/docs/chapter_preface/suggestions.md> · <https://raw.githubusercontent.com/krahets/hello-algo/docs/docs/chapter_searching/binary_search.md>

**T10 · 확인**

- 주장: Python Tutor 백엔드(pg_logger)는 bdb/sys.settrace로 실행 trace를 JSON으로 기록하고 JS 프런트엔드가 재생한다. 저장소 문서, 라이선스, 명시된 한계(스텝 제한 등).
- 확인한 내용: 구조는 맞다. pg_logger.py의 `class PGLogger(bdb.Bdb)`가 코드를 bdb(내부적으로 sys.settrace) 아래에서 실행해 {code, trace[]} JSON을 만든다. 프런트엔드(pytutor.js)는 각 execution point만 보고 그리며 백엔드를 다시 호출하지 않는다. `line`은 '곧 실행될 줄'이다. 한계는 `MAX_EXECUTED_LINES = 1000`(2016-05-01에 300에서 상향), `#break` 주석 브레이크포인트, 공식 문서의 '> 1,000 steps', 칠판이나 슬라이드 한 장 분량, 외부 라이브러리 미지원이다. 현재 사이트는 실행 최대 10초, Python 3.11(및 3.6)이다. 주의할 점이 있다. 원 저장소 pgbovine/OnlinePythonTutor는 raw에서 404이고, 공식 저장소 pythontutor-dev/pythontutor에는 unsupported-features.md와 board.jpg만 있다. 코드, 문서, 라이선스(MIT 문안, 'Original work Copyright (C) Philip J. Guo')는 2019년 포크 pathrise-eng/pathrise-python-tutor로만 확인했다. 현재 운영 중인 코드는 공개돼 있지 않다.
- 계획에 주는 영향: trace 포맷(스텝마다 완결된 스냅샷, line은 실행 전 줄, #break 키프레임)은 설계 참고로 그대로 쓸 수 있다. 다만 Python Tutor 코드를 가져다 쓰는 것은 권하지 않는다. 공식 최신 코드가 비공개이고 남은 것은 2019년 포크다. 100줄 안팎의 자체 settrace 추적기를 새로 쓰는 것이 맞다. '칠판 한 장, 수십 스텝'이라는 크기 기준은 그대로 채택한다.
- 출처: <https://raw.githubusercontent.com/pathrise-eng/pathrise-python-tutor/master/v5-unity/pg_logger.py> · <https://raw.githubusercontent.com/pathrise-eng/pathrise-python-tutor/master/v3/docs/opt-trace-format.md> · <https://raw.githubusercontent.com/pathrise-eng/pathrise-python-tutor/master/v3/docs/developer-overview.md> · <https://raw.githubusercontent.com/pathrise-eng/pathrise-python-tutor/master/LICENSE.txt>

**T11 · 확인**

- 주장: 폭 360~390 CSS px 폰에서는 13~14px 고정폭 글꼴로 약 36~42자(18px에서는 약 32자)가 들어간다.
- 확인한 내용: 글자 폭 0.6em, 한쪽 여백을 페이지 16px + 코드 블록 패딩 12px(내용 폭 = 뷰포트 − 56px)로 계산하면 다음과 같다. 360px(내용 304px)에서 12px 42자, 13px 38자, 14px 36자, 16px 31자, 18px 28자. 375px(319px)에서 44, 40, 37, 33, 29자. 390px(334px)에서 46, 42, 39, 34, 30자. 412px(356px)에서 49, 45, 42, 37, 32자. 코드 블록을 화면 끝까지 넓히고 패딩 12px만 두면(뷰포트 − 24px) 360px에서 46, 43, 40, 35, 31자이고 390px에서 50, 46, 43, 38, 33자다. 따라서 '13~14px에서 36~42자'는 현실적인 여백 기준으로 맞다. '18px에서 32자'는 ctrl.blog가 360px에 좌우 10px 여백으로 계산한 값이고, 0.6em으로 다시 계산하면 31.5자라 31~32자다. 스윕 계산 중 360px/13px '약 39자'는 38자가 맞다(304 ÷ 7.8 = 38.97). 줄 번호 거터(약 32px)를 두면 4~5자가 더 줄고, 한글은 글자당 약 1em이라 한글 주석은 같은 폭에 절반만 들어간다.
- 계획에 주는 영향: 코드 규칙 '한 줄 36자 이하(최악 조건 360px/14px 기준), 들여쓰기 깊이 3단 이하'는 타당하다. 40자까지 허용하려면 코드 블록을 화면 끝까지 넓히거나 13px로 내려야 한다. 4칸 들여쓰기 3단이면 12자를 쓰므로 실제 코드에 남는 폭은 24자 안팎이다. 긴 조건식은 변수로 쪼개고, 한글 주석은 코드 밖 캡션으로 뺀다. 린터 line-length를 36으로 두고 빌드에서 검사한다.
- 출처: <https://www.ctrl.blog/entry/mobile-code-blocks.html>

**T12 · 부분 확인**

- 주장: 2026년 말 Starlight(Astro)와 VitePress의 상태: 현재 메이저 버전, GitHub Pages 정적 출력과 base 경로 지원, PWA/오프라인 선택지(vite-plugin-pwa, @vite-pwa/astro), 알아 둘 지원 중단 사항.
- 확인한 내용: 두 도구 모두 정적 출력, GitHub Pages base 경로, vite-pwa 통합을 지원한다. 다만 스윕에 없는 변화가 있다. (1) Astro는 7.4.13(2026-11-18)이다. 6.0.0이 2026-03-10, 7.0.0이 2026-06-22에 나왔고 Node >=22.23.4, Vite 8이다. Astro 7부터 기본 Markdown 처리기가 remark/rehype가 아닌 자체 'Sätteri'라서 remark/rehype 플러그인을 쓰려면 @astrojs/markdown-remark를 설치하고 `markdown.processor: unified()`로 되돌려야 한다. @astrojs/db는 제거됐다. (2) Starlight는 0.43.1(2026-11-13)로 여전히 0.x다. peer가 astro ^7.2.10이고, 0.43.0에 breaking change(scopedStyleStrategy)가 있었다. (3) VitePress 안정판은 1.6.4(2025-08-05)에서 15개월째 멈춰 있고 vite ^5.4.14에 묶여 있다. 2.0은 2.0.0-alpha.21(2026-10-25)로 아직 alpha다. (4) base는 Astro가 `site` + `base: '/my-repo'`이고 공식 액션은 withastro/action@v6이다. 본문 내부 링크에 base를 직접 붙여야 한다. VitePress는 `base: '/repo/'`다. (5) PWA는 vite-plugin-pwa 2.0.0(2026-10-03, Node >=20.19, vite ^3~^8), @vite-pwa/astro 2.0.4(2026-11-20, astro ^5/^6/^7, Node >=22.14), @vite-pwa/vitepress 2.0.5(vitepress ^1 || ^2.0.0-0)다. 기본 프리캐시는 css, js, html뿐이다.
- 계획에 주는 영향: '2순위 VitePress(가장 단순)'는 위험이 커졌다. 안정판이 Vite 5에 멈춰 있고 2.0은 alpha라, 새로 시작하면 낡은 안정판이나 불안정한 alpha 중 하나를 골라야 한다. Astro가 1순위라는 판단은 유지되지만 조건이 붙는다. 9개월 사이 메이저가 두 번 바뀌었고 Starlight는 0.x에서 breaking change가 잦다. 버전을 package.json에 정확히 고정하고(astro 7.x, starlight 0.43.x, Node 22 이상), 학습 데이터가 Astro 4/5 시절인 에이전트를 위해 SKILL.md에 'Astro 7, Sätteri 기본, remark 플러그인 금지, 순수 Markdown + 커스텀 엘리먼트'를 명시한다. Starlight 없이 얇은 커스텀 레이아웃만 쓰면 Starlight의 변동을 피할 수 있다. 본문 링크의 base 접두는 빌드 검사로 잡는다.
- 출처: <https://registry.npmjs.org/astro> · <https://registry.npmjs.org/@astrojs%2Fstarlight> · <https://registry.npmjs.org/vitepress> · <https://registry.npmjs.org/vite-plugin-pwa>

**T13 · 확인**

- 주장: Pagefind는 한국어 어간 추출과 분절을 잘 지원하지 않는다.
- 확인한 내용: Pagefind 1.6.0(2026-11-01) 문서에서 한국어(ko)는 UI 번역이 ✅, 어간 추출이 ❌다. 띄어쓰기 없는 언어의 분절은 중국어, 일본어, 태국어에만 적용된다(extended 빌드). 스윕은 '중국어·일본어만'이라고 했지만 태국어도 포함된다. 한국어는 공백으로 나뉜 어절 단위로 색인된다. 다만 스윕이 확인하지 못한 접두 일치는 존재한다. 색인 단어가 검색어로 시작하면 일치하므로 '정렬'을 검색하면 '정렬을', '정렬은', '정렬하면'이 든 페이지가 나온다. 반대로 '정렬을'로 검색하면 '정렬은'은 안 나오고, '버블정렬' 같은 붙여 쓴 복합어는 '정렬'로 찾지 못한다.
- 계획에 주는 영향: 스윕의 우려('정렬을' 같은 어절이 '정렬' 검색에서 빠진다)는 틀렸다. 명사 원형으로 검색하면 조사가 붙은 어절도 잡히므로 개인 교재 검색으로는 Pagefind 기본값으로 충분하다. 보완책은 두 가지다. 용어를 띄어 쓰고('버블 정렬'), 영문 별칭을 프런트매터나 본문에 넣는다. 검색보다 '공식 카드 색인' 페이지를 우선한다는 판단은 유지한다.
- 출처: <https://pagefind.app/docs/multilingual/> · <https://pagefind.app/docs/ranking/> · <https://raw.githubusercontent.com/Pagefind/pagefind/main/pagefind_web/src/search.rs> · <https://raw.githubusercontent.com/Pagefind/pagefind/main/CHANGELOG.md>

**T14 · 부분 확인**

- 주장: 백준 온라인 저지(acmicpc.net)가 2026년에 서비스 종료를 발표했다(스윕은 바킹독 블로그의 2026-04-19 공지를 인용). 실제 경과와 현재 상태.
- 확인한 내용: 종료 발표는 사실이지만 현재는 다시 운영 중이다. 2026-04-15 15:14(KST)에 운영자 최백준(startlink)이 BOJ 공지 게시판에 '서비스 종료 안내'를 올려 2026-04-28 종료를 알렸고, 2026-04-28에 'Goodbye' 글이 올라왔다. 바킹독 블로그의 'BOJ 서비스 종료에 따른 안내'는 2026-04-19 10:43에 쓴 2차 글이다. 2026-06-11 디지털타임스는 데이원컴퍼니(제로베이스)가 자산 양수도 계약으로 BOJ를 인수했다고 보도했다. 2026-11-20 11:13(KST)에 day1company 계정이 '백준 온라인 저지 서비스 재오픈 안내'를 올렸다. 운영 주체가 스타트링크에서 데이원컴퍼니로 바뀌었고, 개정 이용약관 시행일은 2026-11-20이며, 유료서비스는 종료하고 무료 중심으로 운영한다. 2026-11-23 현재 acmicpc.net 첫 화면, /step(74단계), /problem/1000이 정상 응답하고 첫 화면에 '34552 전체 문제'로 표시된다. solved.ac의 현재 상태는 403으로 확인하지 못했다.
- 계획에 주는 영향: 'BOJ가 닫혔으니 외부 문제 링크를 쓰지 말라'는 전제는 낡았다. 문제 번호 링크와 74단계 '단계별로 풀어보기'는 다시 참고 자료로 쓸 수 있다. 다만 7개월 동안 서비스가 사라졌다가 운영사가 바뀌어 돌아온 사건은 플랫폼 종속 위험을 그대로 보여 준다. 교재의 핵심 경로는 자체 예제와 자체 서술로 두고 BOJ 링크는 '더 풀어보기' 선택 항목으로만 넣는다는 결론은 유지한다. 공장에서는 어차피 채점 사이트를 쓰지 못한다.
- 출처: <https://www.acmicpc.net/board/view/165799> · <https://www.acmicpc.net/board/view/165922> · <https://www.acmicpc.net/board/view/166446> · <https://www.acmicpc.net/board/list/notice>

### 학습과학·스킬·문헌(S)

**S1 · 확인**

- 주장: Hundhausen, Douglas & Stasko (2002) 메타연구: 시각화가 '무엇을 보여 주느냐'보다 '어떻게 쓰이느냐'가 중요하다. 스윕 수치: 더 능동적인(노력이 큰) 조건이 있는 14개 실험 중 10개가 유의.
- 확인한 내용: Hundhausen, Douglas & Stasko, "A Meta-Study of Algorithm Visualization Effectiveness", Journal of Visual Languages and Computing (2002) 13, 259-290. 통제 실험 24개를 다뤘다. 결과 분포는 유의 11개(46%), 비유의 10개(42%), 유의하지만 AV 기여 불확실 2개(8%), 반대 방향으로 유의 1개(4%)다. 비교 집단 간 노력이 다른 14개 중 10개(71%)에서 노력이 큰 집단이 유의하게 앞섰고, 노력이 동등한 9개 중 6개는 비유의였다(유의 33%). 이론별로는 Cognitive Constructivism(학습자 활동 조작) 14개 중 10개(71%), Epistemic Fidelity(표현 조작) 10개 중 30%가 유의했다. 한계가 세 가지 있다. (1) 통계적 메타분석이 아니라 실험마다 1표를 주는 집계다. (2) '노력 동등' 분류는 저자 판단이다. (3) 논문 내부 불일치가 있다. 본문은 9+14=23개인데 Table 5에는 노력 동등 10개가 나열되고 Hansen Study VII이 양쪽 열에 중복된다.
- 계획에 주는 영향: 계획 변경 없음. '탭해서 예측 후 공개' 스테퍼와 입력 바꾸기를 핵심으로 두는 방향은 원문이 지지한다. 다만 71%는 표본 14개의 득표 집계이므로 문서에는 '방향성 근거'로만 쓰고 효과 크기처럼 인용하지 말 것. 각주 b에 따라 트레이스 자체의 정확성(실제 Python 실행에서 생성)이 능동 활동의 전제 조건이다.
- 출처: <https://www.cc.gatech.edu/~stasko/papers/jvlc02.pdf>

**S2 · 확인**

- 주장: Naps 외 (2002) engagement taxonomy의 단계(no viewing, viewing, responding, changing, constructing, presenting)와 거기에 붙은 가설.
- 확인한 내용: Naps, Rößling 외, "Exploring the Role of Visualization and Engagement in Computer Science Education"(ITiCSE 2002 워킹그룹 보고서). 6개 형태는 1. No viewing, 2. Viewing, 3. Responding, 4. Changing, 5. Constructing, 6. Presenting이다. 저자들은 이것이 서열 척도가 아니라고 명시한다(Viewing이 전체 집합이고 3~6은 서로 겹칠 수 있는 벤 다이어그램). 가설은 6개다. I. Viewing은 No viewing과 학습 성과가 동등하다. II. Responding > Viewing. III. Changing > Responding. IV. Constructing > Changing. V. Presenting > Constructing. VI. 여러 형태를 섞을수록 좋다("More is better"). 이 가설들은 다기관 실험을 제안하려고 세운 것이며 이 보고서가 검증한 결과가 아니다. 보고서가 인용하는 선행 집계는 21개 실험 기준으로 학습자 참여 조작 12개 중 10개(83%) 유의, 표현 조작 9개 중 3개(33%) 유의다. Hundhausen 논문의 24개/71%와는 다른 숫자다.
- 계획에 주는 영향: 단계 이름은 그대로 챕터 활동 태그로 써도 된다. 다만 '단계가 높을수록 효과가 크다'는 가설이지 확인된 사실이 아니다. Responding(예측·질문)과 Changing(입력 바꾸기)을 목표로 하되, Constructing과 Presenting을 못 넣는다고 설계가 열등하다고 볼 근거는 없다. 가설 I에 따라 자동재생 애니메이션만 있는 화면은 만들 가치가 낮다.
- 출처: <https://typeset.io/pdf/exploring-the-role-of-visualization-and-engagement-in-bhelf2687d.pdf>

**S3 · 확인**

- 주장: Roediger & Karpicke (2006): 1주 뒤 반복 시험 집단 61% 대 반복 학습 집단 40%, 그리고 학습만 한 집단이 더 자신만만했다(실험 2: SSSS vs SSST vs STTT).
- 확인한 내용: Roediger & Karpicke (2006), Psychological Science 17(3), 249-255. 실험 2는 N=180(6칸 각 30명)이고, 산문 지문(256/275단어, 채점 단위 30개)을 썼으며, 피드백 없는 자유 회상이었다. 학습 구간은 5분, 시험은 10분이다. 5분 뒤 회상은 SSSS 83%, SSST 78%, STTT 71%로 학습만 한 쪽이 우세했다. 1주 뒤는 STTT 61%, SSST 56%, SSSS 40%로 역전됐다. 지문 통독 횟수는 SSSS 14.2회, SSST 10.3회, STTT 3.4회다. 1주간 비례 망각은 52%, 28%, 14%다. 자신감은 학습 직후 7점 척도('1주 뒤 얼마나 잘 기억할 것 같은가')로 측정했고 SSSS 4.8, SSST 4.2, STTT 4.0이었다(F(2,177)=6.09). 실험 1(학습 2회 vs 학습 1회+시험 1회)은 5분 81% 대 75%, 2일 54% 대 68%, 1주 42% 대 56%다.
- 계획에 주는 영향: '먼저 떠올리고 나서 공개' 게이트와 자신감 입력은 근거가 유지된다. 주의점이 둘 있다. (1) 자료가 산문 지문의 자유 회상이므로 알고리즘 추적 같은 절차 자료에 61/40 수치를 그대로 약속하면 안 된다. (2) 직후에는 다시 읽기가 더 높게 나온다(83% 대 71%). 그래서 사이트에서 '방금 본 것' 기준 체감은 인출 쪽이 더 나쁘게 느껴진다. 이를 안내 문구에 넣을 것.
- 출처: <https://gwern.net/doc/psychology/spaced-repetition/2006-roediger.pdf>

**S4 · 확인**

- 주장: 은밀한(머릿속) 인출은 단순 자료에서는 소리 내는/쓰는 인출과 비슷하게 효과적이지만 복잡한 자료에서는 약하거나 불완전하다(Tauber 외 2018, Smith, Roediger & Karpicke 2013).
- 확인한 내용: Smith, Roediger & Karpicke (2013, JEP:LMC 39(6), 1712-1725)는 범주화된 단어 목록(18개 범주, 90단어)으로 4개 실험을 했다. covert와 overt 인출의 testing effect가 동등했고(실험 3은 2일 지연), 실험 4에서 covert는 재학습보다 우수했다. Tauber, Witherby, Dunlosky, Rawson, Putnam & Roediger (2018, JARMAC 7(1), 106-115)는 핵심 용어 '정의'로 2개 실험을 했고 최종 시험은 2일 뒤였다. overt 인출의 최종 회상이 covert 인출이나 재학습보다 높았다(pooled d = 0.43). 즉 정의 수준 자료에서 covert는 '약해진' 정도가 아니라 재학습과 차이가 없었다. 후속 교실 연구인 Witherby, Northern & Tauber (2025, Behavioral Sciences, 8학년 과학)도 covert가 재학습과 비슷하고 둘 다 overt보다 낮았다. 반면 Rivers & Northern (2025)은 두 형식 모두 재학습보다 높되 overt가 covert보다 높고 그 차이가 정의에서 더 컸다고 보고한다. 설명 가설은 retrieval dynamics다(복잡한 자료는 속으로 떠올릴 때 끝까지 인출하지 않고 멈춘다). 알고리즘 추적 같은 절차 자료로 covert와 overt를 비교한 연구는 이번에도 찾지 못했다.
- 계획에 주는 영향: 이 프로젝트의 핵심 가정(공장에서 머릿속 재생 = 효과적 인출 연습)이 스윕 표현보다 더 위험하다. 여러 단위로 된 자료에서 covert 인출은 다시 읽기 수준에 그칠 수 있다. 대응은 세 가지다. (1) 머릿속 과제의 답을 한 덩어리로 줄인다(최종 배열, 숫자 하나, 다음 한 단계). (2) 폰을 볼 때 답을 탭으로 고르거나 입력하게 해서 overt 응답으로 마무리한다. (3) 불변식 문장은 '속으로 전부 말한 뒤 대조'하도록 빈칸형 확인 화면을 둔다. '머릿속 재생만으로 충분'이라는 문구는 쓰지 말 것.
- 출처: <https://pcllab.github.io/downloads/2013/2013_Smith_Roediger_Karpicke_JEPLMC.pdf> · <https://profiles.wustl.edu/en/publications/does-covert-retrieval-benefit-learning-of-key-term-definitions/> · <https://pmc.ncbi.nlm.nih.gov/articles/PMC12292154/> · <https://scholarcommons.scu.edu/psych/434>

**S5 · 확인**

- 주장: 코드 추적 정답률은 학생이 추적을 스케치하거나 적을 때 훨씬 높다(스윕: 82% 대 61%). 실제 출처와 수치 확인.
- 확인한 내용: 출처는 Cunningham, Blanchard, Ericson & Guzdial, "Using Tracing and Sketching to Solve Programming Problems: Replicating and Extending an Analysis of What Students Draw", ICER 2017이다. Table 2는 무작위 부분표본 N=65, CS1 중반, Python, 객관식 코드 읽기 문제 기준이다. 스케치 유형별 정답률은 Trace 82.1%(n=95), Computation 78.7%(61), Loop Variables 77.3%(44), Position 66.7%(9), Number 65.3%(118), Rewrite 60.7%(56), Blank 60.7%(135), Odd Trace 55.6%(9)이고 전체 평균은 66.8%다. n은 학생 수가 아니라 문항 응답 수다. 원 연구(Lister 외 2004, Leeds Working Group)에서는 Blank가 50%였다. 이것은 실험 조작이 아니라 학생이 스스로 고른 전략과 정답의 상관이다. 모든 스케치가 유리한 것도 아니다(Rewrite는 빈 종이와 동일). 4번 문항(n=135) 분석에서는 불완전한 trace가 스케치를 안 한 것만큼 낮았다.
- 계획에 주는 영향: '종이 없는 머릿속 추적은 불리하다'는 설계 전제는 유지된다. 다만 '적지 않으면 82%에서 61%로 떨어진다'는 인과 문장은 문서에서 빼고 '완전한 추적을 적은 응답 82.1%, 아무것도 안 적은 응답 60.7%(상관)'로 쓸 것. 불완전한 추적이 무추적만큼 나쁘다는 결과가 더 직접적인 설계 근거다. 머릿속 트레이스는 끝까지 갈 수 있는 크기(원소·변수 수 상한)여야 하고, 중간에 끊기는 크기라면 '집·종이 전용'으로 분류해야 한다.
- 출처: <https://gvu.gatech.edu/sites/default/files/related_project_files/p164-cunningham.pdf>

**S6 · 확인**

- 주장: 작업기억 용량은 약 4(3~5) 청크(Cowan 2001)이고, element interactivity가 인지부하이론에서 내재적 난이도의 척도다(Sweller).
- 확인한 내용: Cowan (2001), "The magical number 4 in short-term memory", Behavioral and Brain Sciences 24(1), 87-114는 되뇌기와 장기기억 청킹을 막은 조건에서 중심 용량 한계가 평균 약 4청크(3~5)라고 주장한다. Cowan (2010, Current Directions in Psychological Science)은 젊은 성인 기준 '의미 있는 항목 3~5개'로 요약하고, 조음 억제 시 약 3단위라고 한다. Sweller (2010, Educational Psychology Review 22(2), 123-138)는 element interactivity가 intrinsic load를 정의하는 기본 기제이며 extraneous load의 바탕이기도 하다고 본다. Chen, Paas & Sweller (2023, Educational Psychology Review 35, 63)에 따르면 element interactivity는 자료 구조와 학습자의 장기기억 지식을 동시에 고려해야 정해진다. 상호작용 요소 수는 셀 수 있지만 학습자 지식은 교사 판단이나 지식 검사로 추정할 수밖에 없다. 따라서 '챕터의 요소 수'는 자료만의 고정값이 아니다.
- 계획에 주는 영향: '동시 추적 변수 3개 이하, 배열 5원소 이하' 상한은 근거와 맞는다(억제 조건의 약 3단위가 더 보수적인 기준). 난이도 급변 방지용 '새 상호작용 요소 수' 메타데이터는 써도 되지만 계산 방식을 바꿔야 한다. '이전 챕터들로 이미 스키마가 된 요소는 1개로 센다'는 규칙을 넣고, 선수 챕터를 실제로 통과했는지(복습 기록)에 따라 값이 달라진다고 명시할 것. 선수 지식이 무너지면 같은 챕터의 요소 수가 다시 커지므로 복습 게이트가 난이도 통제의 일부가 된다.
- 출처: <https://www.cambridge.org/core/journals/behavioral-and-brain-sciences/article/magical-number-4-in-shortterm-memory-a-reconsideration-of-mental-storage-capacity/44023F1147D4A1D44BDC0AD226838496> · <https://pmc.ncbi.nlm.nih.gov/articles/PMC2864034/> · <https://api.semanticscholar.org/graph/v1/paper/DOI:10.1007/s10648-010-9128-5?fields=title,abstract,year,venue> · <https://api.openalex.org/works/doi:10.1007/s10648-023-09782-w>

**S7 · 확인**

- 주장: Strayer 외 (AAA Foundation 2013) 인지 분산 척도에서 OSPAN(수학+기억)이 최고 범주(5.0)의 앵커였고, 인지 분산은 반응 지연, 터널 시야/탐색 감소, 단서 놓침을 유발한다. 산업 현장/기계 작업 중 의도적 머릿속 과제를 다룬 연구가 있는지도 확인.
- 확인한 내용: Strayer, Cooper, Turrill, Coleman, Medeiros-Ward & Biondi (2013), Measuring Cognitive Distraction in the Automobile, AAA Foundation(2013년 6월). 실험실, 운전 시뮬레이터, 계측 차량의 3개 실험에서 8개 조건을 측정했다. 척도는 비분산 단일 과제 운전을 1.0, OSPAN을 5.0으로 범위 보정해 만든 것이다. 즉 OSPAN의 5.0은 측정 순위가 아니라 설계상 상단 앵커다. 나머지는 라디오 1.21, 오디오북 1.75, 핸즈프리 통화 2.27, 동승자 대화 2.33, 손에 든 통화 2.45, 음성-문자 이메일 3.06이다. 여기서 OSPAN은 실험자가 읽어 주는 청각 과제로, 수식 참·거짓 판정 2~5개 사이에 낀 단어를 순서대로 회상하는 것이다. 보고된 장해는 운전 관련 뇌 활동 억제, 반응 시간 증가, 단서 놓침과 정확도 저하, 시각 탐색 감소다. 산업·기계 작업 중 '의도적 학습용 머릿속 과제'를 직접 측정한 연구는 이번에도 찾지 못했다. 인접 근거는 엇갈린다. Wiener, Poock & Steele (1964)는 48분 계기 감시에 한 자리 덧셈(분당 3회)을 추가했을 때 탐지율 차이는 없고 오경보만 유의하게 늘었다고 보고했다. Atchley & Chan (2011)은 단조로운 시뮬레이터 운전에서 부가 언어 과제가 경계 최저 시점의 차선 유지를 개선했다고 보고했다. Biondi 외 (Human Factors 63(5), 813-820)는 실험실 LEGO 조립 중 2-back 과제가 완료 시간을 평균 약 10초 늘리고 근활성도와 주관적 부하를 높였으나 정확도 차이는 없었다고 보고했다.
- 계획에 주는 영향: 안전 등급(가벼움/무거움)과 30~60초 중단 가능 구조는 유지한다. 다만 근거 서술을 고쳐야 한다. '머릿속 추적 = OSPAN = 최고 등급'은 유추이지 측정된 사실이 아니다. 머릿속 추적은 자기 속도로 하고 언제든 멈출 수 있어 OSPAN(외부 진행, 운전 중)보다 부하가 낮을 수도 있고, 변수가 많으면 비슷할 수도 있다. 실증 근거가 없으므로 0장 안전 규칙은 '설비 조작, 이동, 감시 판단이 필요한 순간에는 하지 않는다. 대기 중 정지 상태에서만 한다'처럼 행동 규칙으로 쓰고, 연구 수치로 안전을 보증하는 문구는 넣지 말 것. Wiener 결과(탐지율은 유지, 오경보 증가)는 감시 업무 중 암산이 '놓침'보다 '잘못된 반응'을 늘릴 수 있음을 시사한다.
- 출처: <https://aaafoundation.org/measuring-cognitive-distraction-automobile/> · <https://aaafoundation.org/wp-content/uploads/2026/01/MeasuringCognitiveDistractionsReport.pdf> · <https://api.openalex.org/works/doi:10.2466/pms.1964.19.2.435> · <https://api.openalex.org/works/doi:10.1177/0018720810391215>

**S8 · 확인**

- 주장: 최적 학습의 '85% 규칙'(Wilson 외 2019, Nature Communications): 최적 훈련 정확도 약 85%. 적용 대상과 한계 확인.
- 확인한 내용: Wilson, Shenhav, Straccia & Cohen, "The Eighty Five Percent Rule for optimal learning", Nature Communications 10, 4646 (2019). 이진 분류 과제를 확률적 경사하강 계열 학습 규칙으로 배우는 경우, 가우시안 잡음 가정에서 학습 속도를 최대화하는 훈련 오류율이 약 15.87%(정확도 약 85%)라는 이론 도출이다. 검증은 Perceptron, MNIST 2층 신경망, 원숭이 지각 학습 모델의 시뮬레이션뿐이고 사람 대상 실험은 없다. 잡음 분포가 달라지면 최적값도 달라진다(Laplacian 82%, Cauchy 75%). 배치 학습, 3개 이상 범주, 다지선다, 다른 학습 알고리즘으로는 일반화되지 않았다. 완전 기억의 베이지안 학습자에는 최적 난이도 자체가 없다. 사람의 기억 인출이나 절차 학습의 장기 보존에 대한 주장이 아니다. 스윕이 인용한 drill-me 스킬의 '85% rule'은 '최근 약 7문항 성공률을 80~90%로 유지'하는 휴리스틱이다.
- 계획에 주는 영향: 85%를 '과학적으로 증명된 최적 정답률'로 사이트나 SKILL.md에 적으면 안 된다. 쓸 수 있는 형태는 '대략 70~90% 구간이면 유지, 90% 초과가 이어지면 다음 챕터나 전이 문제로, 70% 미만이면 브리지 챕터를 삽입'하는 운영 휴리스틱이다. 표본 7문항에서는 1문항이 약 14%p이므로 창을 넓히거나 연속 정답·오답 규칙과 함께 쓸 것. 간격 복습의 목표 유지율(FSRS 기본 90%)과는 별개의 숫자이므로 혼용하지 말 것.
- 출처: <https://www.nature.com/articles/s41467-019-12552-4.pdf> · <https://raw.githubusercontent.com/timini/drill-me/main/skills/me/reference/teaching-playbook.md>

**S9 · 부분 확인**

- 주장: 간격 반복: FSRS가 Anki 23.10(또는 그 이후)부터 기본 스케줄러이고 SM-2보다 성능이 좋다. 2026년 현재 상태와 최신 FSRS 버전 확인.
- 확인한 내용: (1) '기본 스케줄러'는 틀렸다. Anki 23.10은 FSRS(당시 FSRS v4)를 선택 옵션으로 내장했을 뿐이다. 2026-11-23 현재 최신 안정 태그 26.09.4와 베타 26.11b1 소스에서도 FSRS 토글의 기본값은 false이고, 공식 문서는 SM-2 계열을 'Anki's default algorithm'으로, FSRS를 'alternative'로 부른다. FSRS는 덱 옵션에서 전역으로 켜야 하며, 켰을 때의 목표 유지율 기본값이 90%다. (2) Anki 26.09.4와 26.11b1에 들어 있는 것은 FSRS-6이다(fsrs 크레이트 6.6.2, 파라미터 21개). (3) 최신 FSRS는 FSRS-7이다(파라미터 34개, 그중 11개가 망각 곡선 형태, 소수 간격과 당일 복습 예측 지원). fsrs-rs 7.0.0이 2026-11-10에 나왔고, ts-fsrs 6.0.1(2026-11-22)은 기본 모델이 FSRS-7이다. (4) 'SM-2보다 낫다'는 회상 확률 예측 정확도 기준으로 지지된다. srs-benchmark(Anki 사용자 약 1만 명, 평가 복습 349,923,850건)의 Log Loss는 FSRS-7 0.3401, FSRS-6 0.3460, FSRS-4.5 0.3625, FSRS v4 0.3726이다. 현재 README 표에는 SM-2 행이 없다. 저장소 result 파일로 직접 계산하면 사용자 평균 Log Loss가 SM2 0.722, SM2-trainable 0.581, Anki 0.513이고, FSRS-6-recency가 SM2보다 Log Loss가 낮은 컬렉션은 99.7%(Anki 대비 98.8%)다. 'SM-2 대비 복습 20~30% 감소'는 FSRS 위키 스스로 오래된 시뮬레이션이라고 경고한다. 학습 성과를 직접 비교한 무작위 실험은 확인하지 못했다.
- 계획에 주는 영향: 'Anki도 기본이 FSRS이니 우리도 FSRS'라는 논리는 쓸 수 없다. 이 프로젝트는 카드가 챕터당 1~3장 수준이고 개인 복습 기록이 없어 FSRS의 이점(개인 파라미터 최적화)이 거의 없다. 1장 단계는 Leitner나 고정 확장 간격으로 시작하고, 복습 로그(날짜, 등급)를 처음부터 남겨 나중에 FSRS로 옮길 수 있게만 해 두면 된다. FSRS를 쓴다면 ts-fsrs 버전을 고정하고(6.0.1은 어제 배포, 기본 FSRS-7은 배포 2주차, Anki 안정판은 아직 FSRS-6), 모델 버전을 명시적으로 지정할 것. 에이전트가 구버전 API나 'Anki 기본 = FSRS' 같은 낡은 지식으로 코드를 쓰지 않도록 SKILL.md에 버전과 날짜를 적어 둘 것.
- 출처: <https://docs.ankiweb.net/releases/changes/changes/23.10.md> · <https://docs.ankiweb.net/faqs/what-spaced-repetition-algorithm.md> · <https://docs.ankiweb.net/deck-options.html> · <https://raw.githubusercontent.com/ankitects/anki/26.09.4/rslib/src/config/bool.rs>

**S10 · 확인**

- 주장: mattpocock/skills의 teach 스킬이 존재하고 작업공간 구조가 MISSION.md, lessons/, reference/, learning-records/, assets/, NOTES.md이며, skills.sh 설치 수가 약 98만이다.
- 확인한 내용: teach 스킬은 mattpocock/skills 저장소의 skills/productivity/teach/SKILL.md에 있다(140줄, 9,733바이트). 작업공간 항목은 6개가 아니라 7개다: MISSION.md, ./reference/*.html, RESOURCES.md(스윕에서 빠짐), ./learning-records/*.md(0001-<dash-case-name>.md), ./lessons/*.html(0001-<dash-case-name>.html), ./assets/*, NOTES.md. 형식 파일 3개(MISSION-FORMAT.md, RESOURCES-FORMAT.md, LEARNING-RECORD-FORMAT.md)가 스킬 폴더에 함께 있다. frontmatter는 name: teach, disable-model-invocation: true, argument-hint 이므로 사용자가 /teach로 직접 호출할 때만 실행된다. skills.sh 표시 설치 수는 스킬 페이지 980.5K, 저장소 목록 페이지 980.7K이고 First seen은 May 27, 2026이다. 다만 이 수치는 teach 자체의 인기 지표로 보기 어렵다: 같은 저장소의 56개 스킬이 8.1K~1.6M에 분포하고 teach는 12위이며, 교육과 무관한 migrate-to-shoehorn(554.2K), scaffold-exercises(558.4K)도 비슷한 규모다(저장소 합계 34.1M). 저장소 단위 일괄 설치가 반영된 숫자로 보인다(이 해석은 추론).
- 계획에 주는 영향: 구조는 그대로 참고할 수 있으나 RESOURCES.md(신뢰 출처 목록)를 추가해야 원본과 같아진다. 설치 수 98만을 '검증된 품질'의 근거로 쓰면 안 된다. teach는 대화형 튜터 작업공간이고 모바일 규칙이 전혀 없으며 레퍼런스를 인쇄용으로 규정하므로, 세로 화면·한 손·짧은 확인이라는 요구는 자체 스킬에 직접 수치로 써야 한다. 가져올 가치가 있는 것은 '레슨과 레퍼런스(공식 카드) 분리', 'assets 재사용 기본', 'learning-records로 다음 레슨 난이도 결정' 세 가지다.
- 출처: <https://raw.githubusercontent.com/mattpocock/skills/HEAD/skills/productivity/teach/SKILL.md> · <https://raw.githubusercontent.com/mattpocock/skills/main/skills/productivity/teach/RESOURCES-FORMAT.md> · <https://raw.githubusercontent.com/mattpocock/skills/main/README.md> · <https://skills.sh/mattpocock/skills/teach>

**S11 · 부분 확인**

- 주장: dmccreary/claude-skills의 book-chapter-generator는 '모든 선수개념이 같은 또는 이전 챕터'를 프로그램 검사로 강제하고 챕터당 개념 8~25개를 제시한다. learning-graph-generator는 개념 의존 CSV를 만들고 DAG 검증과 품질 점수를 낸다.
- 확인한 내용: book-chapter-generator(v1.1.2) 부분은 정확하다. SKILL.md에 파이썬 코드 조각이 들어 있고 에이전트가 이를 실행해 위반 0건을 만들어야 한다(별도 스크립트 파일이 아니라 본문 내 스니펫). 챕터 크기는 Optimal 12-18, Acceptable 8-25, Avoid <8 또는 >25이며, 챕터 수는 최소 6, 최적 10-15, 최대 20, 평균 10-20개 개념을 목표로 한다. learning-graph-generator(v1.07)는 300-600개 개념을 대상으로 learning-graph.csv(열: ConceptID, ConceptLabel, Dependencies, 이후 TaxonomyID 추가; Dependencies는 "1|3|7" 같은 파이프 구분)를 만들고 analyze-graph.py가 Kahn 위상정렬로 DAG 여부, 순환, 고립 노드, 단절 서브그래프, 최대 의존 체인 길이, indegree 분포를 quality-metrics.md로 출력한다. 그러나 품질 점수는 스크립트가 계산하지 않는다. analyze-graph.py(379줄)에는 'score'라는 문자열이 한 번도 없고, SKILL.md가 에이전트에게 1~100 점수를 주관적으로 매기라고 지시할 뿐이다(그래프 점수용 채점 기준표 없음; 채점 기준표는 Step 1의 강좌 설명 품질 점수에만 있다). 저장소는 dmccreary/ibook-skills로 이름이 바뀌었고(이전 raw 주소도 응답함) 라이선스는 CC BY-NC-SA 4.0이다.
- 계획에 주는 영향: '선수개념 위반 0건 assert'는 그대로 가져올 수 있는 검증된 선례다. 반면 '자동 품질 점수'는 실재하지 않으므로 난이도 완만함을 재는 지표(챕터당 신규 개념 수, 최대 의존 체인 길이, 인접 챕터 간 신규 개념 수 차이)는 직접 숫자 기준으로 정의하고 스크립트로 계산해야 한다. 8~25개라는 범위는 300~600개 개념, 6~20개 챕터짜리 교과서용 수치라 모바일 짧은 확인용 챕터에는 너무 크다. 이 프로젝트는 챕터당 신규 개념 1~3개 같은 자체 상한을 써야 한다. 라이선스가 비상업·동일조건이므로 스크립트를 복사하지 말고 같은 검사를 파이썬으로 새로 짜는 편이 안전하다.
- 출처: <https://raw.githubusercontent.com/dmccreary/claude-skills/main/skills/book-chapter-generator/SKILL.md> · <https://raw.githubusercontent.com/dmccreary/claude-skills/main/skills/learning-graph-generator/SKILL.md> · <https://raw.githubusercontent.com/dmccreary/claude-skills/main/skills/learning-graph-generator/analyze-graph.py> · <https://raw.githubusercontent.com/dmccreary/claude-skills/main/skills/chapter-content-generator/SKILL.md>

**S12 · 확인**

- 주장: mizchi/explainer의 explainer-book은 book.json에 챕터별 introduces/requires/minutes를 두고, verify-book 스크립트가 도입 전 사용과 읽기 시간 예산 초과(500자/분 + 코드 15줄/분)를 실패로 처리한다.
- 확인한 내용: 정확하다. skills/explainer-book/scripts/verify-book.mjs가 book.json을 읽어 6가지(chapters, objectives, concepts, budget, exercises, map)를 검사하고 실패가 하나라도 있으면 종료 코드 1을 낸다. 읽기 시간 추정식은 est = (공백 제외 본문 글자 수)/charsPerMinute + (코드 블록 줄 수)/codeLinesPerMinute 이고 기본값이 500과 15이며 book.json에서 바꿀 수 있다. 본문 글자 수는 코드 블록, HTML 주석, <details> 내용을 뺀 것이다. est > minutes이면 실패다. minutes에는 연습 시간을 넣지 않아도 된다. 개념 검사는 단순 부분 문자열 일치(text.includes)이며 aliases로 별칭을 등록한다. 뒤 챕터가 introduces하는 용어가 앞 챕터 본문에 나오면 실패, requires가 어느 챕터에서도 도입되지 않았거나 같은 챕터 또는 뒤 챕터에서 도입되면 실패(assumed에 있으면 통과), introduces로 선언하고 본문에 없으면 실패다. 500자/분은 일본어 묵독 기준으로 정한 값이다. 플러그인 버전은 0.5.3(2026-10-10), 라이선스는 MIT다.
- 계획에 주는 영향: curriculum 파일 + 검증 스크립트 구조를 그대로 채택할 수 있다. 다만 세 가지를 바꿔야 한다. (1) 500자/분은 일본어 묵독값이므로 한국어와 폰 화면 기준으로 직접 재서 정한다. (2) 원본 예산은 10~15분 단위인데 이 프로젝트는 '짧게 확인'이므로 분 단위 예산을 훨씬 작게 잡고, 화면 수나 스텝 수 같은 예산을 추가한다. (3) 부분 문자열 일치라 동의어는 aliases에 등록해야 잡힌다(한국어는 조사가 붙어도 일치하지만 '재귀'와 '되부름' 같은 표기 차이는 못 잡는다). 스크립트는 Node용이므로 파이썬으로 다시 쓰는 편이 프로젝트 스택과 맞다.
- 출처: <https://raw.githubusercontent.com/mizchi/explainer/main/skills/explainer-book/SKILL.md> · <https://raw.githubusercontent.com/mizchi/explainer/main/skills/explainer-book/scripts/verify-book.mjs> · <https://raw.githubusercontent.com/mizchi/explainer/main/skills/explainer-book/references/book-json.md> · <https://raw.githubusercontent.com/mizchi/explainer/main/docs/inductive-invariant-book/book.json>

**S13 · 확인**

- 주장: Jay Wengrow의 A Common-Sense Guide to Data Structures and Algorithms는 Big O를 초반 여러 장에 걸쳐 정렬 하나씩에 붙여 가르치고 재귀를 여러 장으로 나눈다. 2판과 Python판의 실제 목차.
- 확인한 내용: 2판(2020년 8월, 506쪽, ISBN 9781680507225, 예제는 JavaScript·Python·Ruby)과 Python판 Volume 1(2023년 12월, 502쪽, ISBN 9798888650356, 전부 Python)의 20개 장 제목은 같다: 1 Why Data Structures Matter / 2 Why Algorithms Matter(Ordered Arrays, Binary Search) / 3 O Yes! Big O Notation / 4 Speeding Up Your Code with Big O(Bubble Sort) / 5 Optimizing Code with and Without Big O(Selection Sort, Ignoring Constants) / 6 Optimizing for Optimistic Scenarios(Insertion Sort, The Average Case) / 7 Big O in Everyday Code / 8 Blazing Fast Lookup with Hash Tables / 9 Crafting Elegant Code with Stacks and Queues / 10 Recursively Recurse with Recursion / 11 Learning to Write in Recursive / 12 Dynamic Programming / 13 Recursive Algorithms for Speed(Partitioning, Quicksort, Quickselect) / 14 Node-Based Data Structures(Linked Lists) / 15 Speeding Up All the Things with Binary Search Trees / 16 Keeping Your Priorities Straight with Heaps / 17 It Doesn't Hurt to Trie / 18 Connecting Everything with Graphs(DFS, BFS, Dijkstra) / 19 Dealing with Space Constraints / 20 Techniques for Code Optimization. Big O는 3~7장 5개 장에 걸치고 4·5·6장이 각각 정렬 하나를 운반체로 쓴다. 재귀는 10장(읽기, 호출 스택), 11장(쓰기), 12장(DP: memoization → bottom-up), 13장(퀵 정렬)로 이어진다. Python판 Volume 2도 있다(2025년 9월, 500쪽, ISBN 9798888651322, 13개 장): 1 Mergesort / 2 Benchmarking Code / 3 How Random Is That? / 4 Cache Is King / 5 Red-Black Trees / 6 Randomized Treaps / 7 B-Trees(External-Memory Algorithms) / 8 M/B-Way Mergesort / 9 Monte Carlo Algorithms / 10 Hash Tables with Randomization / 11 Rabin-Karp / 12 Bit Vectors(Saving Space) / 13 Bloom Filters. 병합 정렬은 Volume 1에 없고 Volume 2 1장에 있다. 3판은 pragprog에서 찾지 못했다(jwdsal3 주소는 404).
- 계획에 주는 영향: '복잡도 개념 하나를 단순 정렬 하나에 얹어 여러 장에 나눈다'와 '재귀 읽기 → 재귀 쓰기 → 메모이제이션 → 퀵 정렬' 분해는 실제 목차로 뒷받침되므로 계획에 그대로 쓸 수 있다. 주의할 점: (1) Wengrow는 해시 테이블(8장)을 스택·큐(9장)보다 앞에, 연결 리스트(14장)를 재귀·DP 뒤에 둔다. (2) 병합 정렬과 균형 트리는 1권에 없으므로 이 둘의 위치 근거는 다른 교재에서 가져와야 한다. (3) 장 내부 본문은 읽지 못했으므로 확인된 것은 목차와 절 제목까지다.
- 출처: <https://pragprog.com/titles/jwdsal2/a-common-sense-guide-to-data-structures-and-algorithms-second-edition/> · <https://pragprog.com/titles/jwpython/a-common-sense-guide-to-data-structures-and-algorithms-in-python-volume-1/> · <https://pragprog.com/titles/jwpython2/a-common-sense-guide-to-data-structures-and-algorithms-in-python-volume-2/>

**S14 · 부분 확인**

- 주장: Red Blob Games의 Introduction to A*는 짧은 Python 루프 하나를 한두 줄씩 고쳐 BFS → Dijkstra → A*로 올라간다.
- 확인한 내용: 뼈대 루프 하나를 단계적으로 변형한다는 점은 맞지만 '매번 한두 줄'은 일부 단계에서만 맞고, 중간 단계 하나가 빠져 있다. 실제 순서는 (1) Breadth First Search: frontier와 reached로 된 10줄 루프 → (2) reached 집합을 came_from 딕셔너리로 바꿈(줄 수 그대로, 4줄 수정) → (3) 경로 복원용 별도 7줄 루프 → (4) Early exit: `if current == goal: break` 2줄 추가 → (5) Movement costs(Dijkstra): Queue를 PriorityQueue로 교체, cost_so_far 추가, new_cost 계산, 조건 변경, priority 추가로 9줄을 건드림(신규 5줄, 변경 4줄; 코드 12줄 → 17줄) → (6) Heuristic search(Greedy Best First Search): 3줄짜리 heuristic 함수 추가, priority = heuristic(goal, next), cost_so_far 없음 → (7) A*: Dijkstra 코드에서 `priority = new_cost` 한 줄만 `priority = new_cost + heuristic(goal, next)`로 바뀜. 코드는 타입 힌트가 붙은 Python이고, Queue와 PriorityQueue는 표준 라이브러리가 아니라 구현 페이지에 정의된 래퍼(collections.deque, heapq 기반, put(element, priority))다. 구현 페이지 클래스는 `class Queue[Element]:` 문법을 쓰므로 Python 3.12 이상이 필요하다. 저자는 이 Dijkstra·A*가 교과서 버전과 다르고 Uniform Cost Search에 가깝다고 명시한다. 페이지 최종 수정일은 2026-09-29다.
- 계획에 주는 영향: '뼈대 코드 하나를 장마다 조금씩 변형' 전략은 유효하다. 다만 BFS → Dijkstra는 원본에서도 한 번에 9줄이 바뀌는 가장 큰 도약이므로, 난이도 급변 금지 조건을 지키려면 이 구간을 2~3개 챕터로 쪼개야 한다(예: 큐 → 우선순위 큐만 교체, cost_so_far 기록 추가, '더 싼 경로면 다시 넣기' 조건 변경). Greedy Best First Search를 Dijkstra와 A* 사이의 대조 단계로 넣으면 A*가 한 줄 변화로 끝난다. 교재 코드는 heapq를 직접 쓰는 형태로 다시 써야 하고, 교과서식 Dijkstra(방문 확정 집합)와 다른 변형이라는 점을 챕터에 적어 두어야 다른 자료와 혼동하지 않는다.
- 출처: <https://www.redblobgames.com/pathfinding/a-star/introduction.html> · <https://www.redblobgames.com/pathfinding/a-star/implementation.html>

**S15 · 확인**

- 주장: 바킹독 실전 알고리즘은 큐와 스택으로 BFS/DFS를 재귀보다 먼저 가르치고, 재귀 호출을 따라가는 것을 '무간지옥'이라 부르며 귀납적으로 생각하라고 하고, DP를 테이블 정의 → 점화식 → 초기값으로 설명한다.
- 확인한 내용: 세 가지 모두 원문으로 확인된다. 순서: 0x09 BFS(2020-05-09) → 0x0A DFS(2020-05-27) → 0x0B 재귀(2020-06-14) → 0x0C 백트래킹, README FAQ에 "강의의 배치는 난이도순입니다". 단서 네 가지. (1) 0x09와 0x0A는 일반 그래프가 아니라 다차원 배열(격자) Flood Fill에서의 BFS/DFS다. 그래프 자료구조는 0x18(2021-12-01)에서 나오고 재귀 DFS도 거기서 처음 나온다. (2) 저자는 BFS를 쉬운 단원이 아니라 "첫 번째 고비"라고 부른다. (3) 0x0A DFS는 'BFS 코드에서 큐만 스택으로 바꾼 것'으로만 소개하고 "다차원 배열에서 굳이 BFS 대신 DFS를 써야하는 일이 없습니다"라며 연습 문제를 두지 않는다. (4) '무간지옥'은 하노이 탑 함수 호출을 따라가는 맥락의 표현이고, 그 앞에서 가장 쉬운 예(func1(3))는 절차적으로 한 번 따라가 보인 뒤 귀납적 사고로 넘어간다. DP는 재귀 메모이제이션이 아니라 배열을 앞에서부터 채우는 bottom-up 방식으로만 가르친다. 강의 본문 코드는 C++이지만 2026-01-27 공지 이후 0x11강까지 모든 문제의 파이썬 풀이가 hanXen/basic-algo-lecture-python 저장소로 안내되고 있다.
- 계획에 주는 영향: '재귀 앞에 큐 BFS를 둔다'는 선택지는 실제 선례가 있지만, 그 선례의 저자도 BFS를 첫 고비라고 하므로 '재귀보다 쉬우니 앞에 둔다'는 근거로 쓰면 안 된다. 격자 BFS를 재귀 앞에 두려면 큐, 2차원 배열, 방향 배열, 방문 표시를 각각 앞 챕터에서 따로 익힌 뒤에 합쳐야 급경사가 생기지 않는다. 스택 DFS는 이 단계에서는 '큐를 스택으로 바꾸면 방문 순서가 달라진다' 정도의 짧은 대조로만 두고, 본격적인 DFS는 재귀 뒤 그래프 단원에서 다시 다루는 2단 구성이 원본과 같다. 재귀 챕터의 암기 카드는 '함수가 하는 일 + base condition + k에서 k+1로 가는 한 줄' 형식이 원문 취지와 맞고, DP 카드는 '테이블 정의 → 점화식 → 초기값' 3줄 형식이 원문 그대로다.
- 출처: <https://raw.githubusercontent.com/encrypted-def/basic-algo-lecture/master/README.md> · <https://blog.encrypted.gg/941> · <https://blog.encrypted.gg/942> · <https://blog.encrypted.gg/943>

**S16 · 확인**

- 주장: Agent Skills 규격·모범 사례: SKILL.md 본문 500줄 미만(및 약 5000토큰) 권장, description 1024자 제한, name 64자 이하 소문자·하이픈, references를 통한 점진적 공개. 프로젝트 스킬 위치(.claude/skills/<name>/SKILL.md)와 새 frontmatter 필드.
- 확인한 내용: 2026-11-23 기준으로 모두 확인된다. agentskills.io 규격: name은 필수, 1-64자, 소문자 a-z와 0-9와 하이픈만, 하이픈으로 시작·끝 불가, 연속 하이픈(--) 불가, 부모 디렉터리 이름과 일치해야 함. description은 필수, 1-1024자. 선택 필드는 license, compatibility(최대 500자), metadata(문자열 → 문자열 맵), allowed-tools(공백 구분, Experimental). 점진적 공개는 Metadata 약 100토큰, Instructions 5000토큰 미만 권장, Resources는 필요할 때 로드. 500줄과 5000토큰은 권장이지 강제 한도가 아니다. 파일 참조는 SKILL.md에서 한 단계 깊이. Anthropic 플랫폼 문서는 여기에 name과 description에 XML 태그 금지, name에 예약어 anthropic·claude 금지, description은 3인칭으로 쓰라는 규칙을 더한다. Claude Code 문서: 프로젝트 스킬은 `.claude/skills/<skill-name>/SKILL.md`, 개인 스킬은 `~/.claude/skills/<skill-name>/SKILL.md`, 하위 디렉터리의 `<subdir>/.claude/skills/`도 인식한다. Claude Code에서는 frontmatter 필드가 전부 선택이고(name 생략 시 디렉터리 이름, description은 권장) 모르는 필드는 오류 없이 무시된다. description과 when_to_use를 합친 글이 스킬 목록에서 1,536자에서 잘리고, 목록 전체 예산은 컨텍스트 윈도의 1%다. Claude Code 전용 필드는 when_to_use, argument-hint, arguments, disable-model-invocation, user-invocable, allowed-tools, disallowed-tools, model, effort, context(fork), agent, background, hooks, paths, shell이며, 이 필드들은 claude.ai 업로드·Skills API·package_skill.py에서는 하드 에러로 거부된다(허용 필드는 name, description, license, compatibility, metadata, allowed-tools 6개). 자동 압축 후에는 호출된 스킬마다 앞 5,000토큰만 다시 붙고 합계 예산은 25,000토큰이다.
- 계획에 주는 영향: 자체 스킬은 `.claude/skills/<이름>/SKILL.md`에 두고 폴더 이름과 name을 같게, 소문자·하이픈으로, claude나 anthropic이 들어가지 않게 짓는다. description은 핵심 용도를 맨 앞에 쓴다(목록에서 1,536자에서 잘리고 스킬이 많으면 설명이 통째로 빠질 수 있다). 압축 후 앞 5,000토큰만 유지되므로 모바일 규격과 난이도 검사 같은 어기면 안 되는 규칙은 SKILL.md 맨 위에 두고, 챕터 템플릿과 문체 가이드는 references/로 한 단계만 내려 둔다. Claude Code에서만 쓸 프로젝트 스킬이라면 disable-model-invocation, paths, allowed-tools, context: fork 같은 전용 필드를 써도 되지만, 다른 사람의 SKILL.md를 볼 때 이런 필드가 있으면 Claude Code 전용이라는 뜻으로 읽어야 한다.
- 출처: <https://agentskills.io/specification> · <https://raw.githubusercontent.com/agentskills/agentskills/main/docs/specification.mdx> · <https://code.claude.com/docs/en/skills.md> · <https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices.md>

### 보완 조사에서 나온 사실(C)

**C1 · 확인**

- 주장: 백준(acmicpc.net)은 데이원컴퍼니가 스타트링크로부터 운영 자산 일부를 양수해 서비스를 재개했고(회원·제출·문제 데이터 이관, 유료서비스 종료, 개정 약관 2026-11-20 시행), 이전 스윕은 2026-04-19 종료 공지를 인용했다.
- 확인한 내용: 실제 타임라인(모두 KST): (1) 2026-04-15 15:14 BOJ 공지 '서비스 종료 안내'에서 2026-04-28 종료를 발표. 스윕의 '2026-04-19'는 BOJ 공지일이 아니라 바킹독 블로그 글(blog.encrypted.gg/1108, 2026-04-19 10:43) 날짜다. (2) 2026-04-28 14:35 'Goodbye' 글과 함께 종료. (3) 2026-05-29 데이원컴퍼니와 자산 양수도계약 체결(개정 약관 부칙). (4) 2026-06-11 디지털타임스가 인수 보도(사내 브랜드 '제로베이스'가 운영). (5) 2026-11-20 11:13 공지 '백준 온라인 저지 서비스 재오픈 안내'로 재개, 같은 날 개정 이용약관·개인정보 처리방침 시행. 운영 주체는 (주)데이원컴퍼니(공동대표 신해동·김동혁, 문의 help-tech@day1company.co.kr). 유료서비스는 종료, 무료 중심 운영. 재개는 '당초 안내드린 일정이 연기'된 뒤였다. 2026-11-23 현재 첫 화면·/step(74단계)·/problem/1000 모두 200 응답. solved.ac: 2026-04-15 공지로 'BOJ와 솔브드의 연동은 올해 4월 28일을 기하여 종료'를 알렸고, help.solved.ac 업데이트 목록의 최신 글이 그 공지다(재연동 공지 없음). solved.ac 본 사이트는 이 환경에서 Cloudflare 403으로 차단되어 현재 동작 여부는 확인 불가.
- 계획에 주는 영향: '백준 종료'를 전제로 한 서술은 '2026-04-28 종료 → 2026-11-20 데이원컴퍼니가 재개(사흘 전)'로 고쳐야 한다. 다만 7개월 중단 이력, 운영 주체 교체 직후, solved.ac 연동 상태 불명, 약관상 문제 복제 제한 때문에 '교재는 자체 예제로 완결하고 BOJ 번호는 선택 부록으로만 건다'는 결론은 그대로 유지된다. solved.ac 티어/CLASS를 난이도 사다리의 근거로 쓰는 계획은 현재 검증할 수 없으니 넣지 않는다.
- 출처: <https://www.acmicpc.net/> · <https://www.acmicpc.net/board/view/165799> · <https://www.acmicpc.net/board/view/165922> · <https://www.acmicpc.net/board/view/166421>

**C2 · 확인**

- 주장: @dodona/trace-component(npm ~1.7.x, MIT, 의존성 lit뿐)는 Python Tutor 시각화를 재구현한 <tc-trace> 웹 컴포넌트로 Python Tutor trace 포맷을 받으며, dodona-json-tracer(PyPI ~1.1.0, MIT)가 Python 스크립트에서 그 JSON trace를 만든다.
- 확인한 내용: @dodona/trace-component: latest 1.7.2, 게시 2026-10-14T18:18:58Z(레지스트리 modified가 2026-10-19라서 '10-19 갱신'은 릴리스일이 아님), 첫 릴리스 1.0.0 2023-12-08, 58개 버전, package.json license MIT, dependencies는 lit ^3.3.3 하나(lit 자체는 BSD-3-Clause), ESM 전용, dist JS 합계 약 115KB(비압축). 노출 API: 속성 trace·selectedFrame·translations, 메서드 addFrame(frame), 이벤트 frame-change, 슬롯 picker, CSS 변수. 주의: frame-change는 내장 picker만 보낸다. picker 슬롯을 자체 버튼으로 채우면 이벤트가 오지 않고 selectedFrame을 직접 설정해야 하며, 슬롯은 스텝을 렌더링할 때만 존재한다. translations 키는 16개이고 영어 기본값만 들어 있다(한국어는 직접 넘겨야 함). Python Tutor 포맷 호환은 'for now'라는 단서가 붙는다. dodona-json-tracer: 1.1.0(2026-08-07, 1.0.0은 2026-08-05), MIT(Copyright (c) 2023 Team Dodona), requires-python >=3.12, 의존성 없음, import 이름은 tracer, bdb 기반. 옵션 frame_format full/delta, max_steps, module_name, heap_primitives, frame_callback. 구 패키지 json-tracer는 0.1.0(2023-10-06)~0.7.0(2025-01-29), 23개 릴리스, 더 이상 유지되지 않는다. GitHub 저장소(dodona-edu/trace-component, json-tracer)는 이 환경에서 raw 404라 저장소의 LICENSE 파일 자체는 읽지 못했다(레지스트리 메타데이터와 배포 README로 확인).
- 계획에 주는 영향: 참조·호출 스택 장에 그대로 쓸 수 있는 유지보수 중인 MIT 부품이라는 판단은 유효하다. 계획에 반영할 점: 하단 큰 버튼으로 picker 슬롯을 바꾸면 frame-change를 못 받으므로 현재 줄 하이라이트는 자체 상태(selectedFrame)에서 구동한다. 한국어 번역 객체 16키를 직접 만든다. 빌드 Python은 3.12 이상(클라우드 VM은 3.13.18이라 충족). 포맷 호환이 바뀔 수 있으니 버전을 고정한다.
- 출처: <https://registry.npmjs.org/@dodona%2Ftrace-component> · <https://cdn.jsdelivr.net/npm/@dodona/trace-component@1.7.2/README.md> · <https://cdn.jsdelivr.net/npm/@dodona/trace-component@1.7.2/dist/trace_types.d.ts> · <https://data.jsdelivr.com/v1/packages/npm/@dodona/trace-component@1.7.2>

**C3 · 확인**

- 주장: memory_graph(PyPI memory-graph, bterwijn)는 BSD-2-Clause이고 2026년에도 활발히 릴리스되며, Graphviz로 빌드 시점에 Python 객체·참조 그래프를 SVG로 렌더링할 수 있다(mg.render(locals(), 'x.svg')).
- 확인한 내용: memory-graph 0.3.92(2026-11-09 게시), license_expression BSD-2-Clause(저장소 LICENSE.txt도 BSD 2-Clause, 저작권 표기는 'Copyright (c) 2017, pyexample'), 릴리스 총 126개 중 2026년에 27개(최근 0.3.88~0.3.92가 2026-10-15~11-09), requires-python >=3.7, Development Status 4 - Beta. mg.render(data, 'my_graph.svg')가 README에 명시돼 있고 pdf/png/gv도 된다. pip 의존성 graphviz(파이썬 래퍼) 외에 Graphviz 바이너리를 따로 설치해야 한다. 이 클라우드 VM에는 dot이 설치돼 있지 않았다(직접 확인).
- 계획에 주는 영향: 1장 '이름표(참조)' 그림을 빌드 시점 SVG로 뽑는 계획은 유지. 단 클라우드 세션과 CI에 Graphviz가 기본으로 없으므로 setup script와 CI에 apt install -y graphviz를 넣어야 한다(문서상 setup script는 root로 apt 사용 가능, archive.ubuntu.com은 기본 허용 목록). Graphviz 레이아웃은 버전에 따라 좌표가 달라질 수 있어 'trace 재생성 후 git diff' 검사 대상에서 SVG는 빼거나 버전을 고정한다(이 부분은 추론).
- 출처: <https://pypi.org/pypi/memory-graph/json> · <https://raw.githubusercontent.com/bterwijn/memory_graph/main/LICENSE.txt> · <https://raw.githubusercontent.com/bterwijn/memory_graph/HEAD/README.md>

**C4 · 부분 확인**

- 주장: Claude Code 클라우드 세션은 저장소를 새로 clone하고 저장소의 CLAUDE.md와 .claude/skills·agents·commands를 읽으며, .claude/settings.json의 훅·권한 규칙이 적용되고, ~/.claude 사용자 설정과 사용자 스킬은 전달되지 않는다. VM에는 Python 3.x, Node, Chrome for Testing이 있고 기본 네트워크는 Limited(패키지 레지스트리 허용)이며, 모바일 앱으로 세션을 시작·조종할 수 있다.
- 확인한 내용: 대부분 문서와 일치하지만 조건 두 가지가 빠져 있다. (1) .claude/settings.json의 훅·권한 규칙은 'Yes, in a session with one repository'다. 저장소가 여러 개인 세션은 enabledPlugins·extraKnownMarketplaces 키만 읽고, 'project'의 클라우드 스레드에서는 권한 규칙·훅·env가 전혀 적용되지 않는다. (2) ~/.claude/skills·agents·commands, ~/.claude/CLAUDE.md, ~/.claude/settings.json, .claude/settings.local.json은 전달되지 않지만, claude.ai 계정에서 켠 스킬은 클라우드 세션에 자동 로드된다. 그 밖: VM은 Ubuntu 24.04 x86_64, Python 3.x(pip, poetry, uv, black, mypy, pytest, ruff), Node 20·21·22(PATH 기본 22), Chrome for Testing(/usr/bin/google-chrome, CHROME_PATH 설정). 이 세션 실측은 Python 3.13.18, Node v22.23.5, Chrome for Testing 153. 새 환경은 Limited + 'Allow package managers' 체크 상태로 시작하며 npm·PyPI·GitHub·Ubuntu apt 미러가 기본 허용 목록에 있다. setup script는 root로 실행되고 약 5분 안에 끝나야 캐시되며 캐시는 약 7일 뒤 만료된다. 모바일 앱 Code 탭에서 저장소·브랜치를 골라 세션을 시작하고 진행 확인·질문 응답·방향 전환이 가능하며, 모바일에서 클라우드 세션 권한 모드는 Accept edits·Plan·Auto다. 이용 가능 플랜은 Pro, Max, Ultra, Team, Enterprise(해당 좌석).
- 계획에 주는 영향: 챕터 생성 스킬·규칙·검증 훅은 반드시 저장소의 .claude/와 CLAUDE.md에 커밋한다. Stop/PostToolUse 훅으로 검증을 강제하려면 '저장소 1개짜리 일반 클라우드 세션'으로 작업하고 project 스레드는 쓰지 않는다(그 경우 훅이 돌지 않으므로 CI가 유일한 안전망). 개인용 스킬을 저장소에 넣기 싫으면 claude.ai 계정 스킬로 올리는 길도 있다. 한글 폰트와 Graphviz는 setup script(apt)로 설치하되 5분 제한을 지킨다.
- 출처: <https://code.claude.com/docs/en/cloud-environments.md> · <https://code.claude.com/docs/en/settings.md> · <https://code.claude.com/docs/en/skills.md> · <https://code.claude.com/docs/en/mobile.md>

**C5 · 확인**

- 주장: GitHub Pages: GitHub Free에서는 public 저장소만 가능, 저장소가 private이어도 Pages 사이트는 공개(Enterprise Cloud 비공개 게시 제외), 한도는 사이트 1GB·월 100GB 소프트 대역폭·시간당 10빌드(커스텀 Actions 워크플로에는 미적용).
- 확인한 내용: 그대로 맞다. 정확한 문구 기준 추가 사항: 시간당 10빌드도 'soft' 한도이고, 배포는 10분을 넘으면 타임아웃, 소스 저장소 권장 한도 1GB, 계정당 user/organization 사이트는 1개, 초과 시 429 응답이 올 수 있다. 플랜: GitHub Free·Free for organizations는 public 저장소만, private 저장소 Pages는 GitHub Pro·Team·Enterprise Cloud·Enterprise Server. 비공개 게시(접근 제어)는 Enterprise Cloud 조직의 project site만 가능하다.
- 계획에 주는 영향: 무료 계정이면 교재 저장소를 public으로 두거나 GitHub Pro로 올려야 Pages를 쓸 수 있고, 어느 쪽이든 사이트 URL은 공개다. 사이트에 개인정보·학습 기록을 넣지 않고(진도는 localStorage), 타인 저작물(Hello Algo 그림·BOJ 지문)을 싣지 않는다는 원칙이 더 중요해진다. 규모 한도는 개인 교재에 충분하다.
- 출처: <https://docs.github.com/en/pages/getting-started-with-github-pages/github-pages-limits> · <https://docs.github.com/en/pages/getting-started-with-github-pages/what-is-github-pages> · <https://docs.github.com/en/pages/getting-started-with-github-pages/creating-a-github-pages-site> · <https://docs.github.com/en/enterprise-cloud@latest/pages/getting-started-with-github-pages/changing-the-visibility-of-your-github-pages-site>

**C6 · 확인**

- 주장: Cloudflare Pages: 브랜치·PR마다 <branch>.<project>.pages.dev 미리보기 URL이 생기고, 미리보기는 기본 공개(X-Robots-Tag noindex)이며 Cloudflare Access로 제한할 수 있고, 무료 플랜에서 private GitHub 저장소를 지원하며, Cloudflare는 신규 프로젝트를 Workers 정적 자산으로 유도한다.
- 확인한 내용: 모두 1차 문서로 확인된다(비평가가 2차 자료로만 적은 'Workers 권장'도 Pages 문서 첫 화면에 명시). 세부: 배포마다 <hash>.<project>.pages.dev가 생기고 브랜치 별칭은 소문자화하고 영숫자가 아닌 문자를 하이픈으로 바꾼다. 따라서 claude/foo 브랜치는 claude-foo.<project>.pages.dev가 된다. PR 미리보기는 같은 저장소에서 온 PR에만 생긴다. Access 정책(Settings > General > Enable access policy)은 미리보기 배포만 보호하고 <project>.pages.dev 본 도메인은 따로 설정해야 한다. 무료 한도: 월 500빌드, 동시 1빌드, 빌드 타임아웃 20분, 사이트당 파일 20,000개, 파일당 25MiB, 프로젝트당 커스텀 도메인 100개, 계정당 프로젝트 100개. 배포 보존은 30일이며 최근 100개와 현재 프로덕션 배포는 항상 유지(문서 수정일 2026-11-19). 대안인 Workers: 정적 자산 요청은 무료·무제한, Workers Builds 무료 3,000 빌드분/월·동시 1빌드, 브랜치 Preview는 npx wrangler preview(Wrangler 4.135.0 이상), Preview URL도 Access로 보호 가능.
- 계획에 주는 영향: private 저장소를 유지하면서 본인만 보는 브랜치 미리보기가 필요하면 Cloudflare가 GitHub Pages보다 맞다. 다만 Cloudflare 스스로 신규 프로젝트는 Workers로 시작하라고 하므로, 새로 붙인다면 Workers 정적 자산 + Workers Builds Preview를 1순위로 보고 Pages는 차선으로 둔다. 미리보기 URL 규칙(claude/… → claude-…)을 CLAUDE.md에 적어 에이전트가 PR 본문에 정확한 링크를 달게 한다.
- 출처: <https://developers.cloudflare.com/pages/> · <https://developers.cloudflare.com/pages/configuration/preview-deployments/> · <https://developers.cloudflare.com/pages/platform/limits/> · <https://developers.cloudflare.com/pages/get-started/git-integration/>

**C7 · 확인**

- 주장: Simon Willison의 TIL(2026-01)은 GitHub Pages 'Deploy from a branch'를 claude/... 브랜치로 지정해 Claude Code 브랜치를 폰에서 미리 보는 방법을 설명한다.
- 확인한 내용: 글 제목은 'Previewing Claude Code for web branches with GitHub Pages', 작성 시각 2026-01-22T08:43:41-08:00. 절차: private 저장소 생성(빈 README 포함) → Claude Code 작업 시작('self-contained HTML file, vanilla JavaScript, no build step, load any dependencies from a CDN') → 저장소 Settings의 Pages에서 'Deploy from a branch'의 브랜치를 Claude가 만든 claude/... 로 선택 → 약 1분 뒤 https://your-username.github.io/your-repo/index.html 로 확인. 글에 적힌 단서: 새 브랜치마다 수동으로 다시 선택해야 하고, PR을 머지하면 Pages 설정을 main으로 되돌려야 하며, URL은 '(secret)'이라고 부르지만 공개다. 글에 없는 전제: 그는 private 저장소에 Pages를 쓰므로 GitHub Free가 아닌 유료 플랜이 필요하다(GitHub 문서 기준). 무료 계정이면 public 저장소에서만 같은 방법이 된다. 또 미리보기 브랜치를 가리키는 동안에는 '정식' 사이트가 미리보기로 대체된다(저장소당 Pages 소스는 하나).
- 계획에 주는 영향: 이 방법은 '빌드 없는 정적 산출물'과 '매번 설정 화면에서 브랜치 수동 전환'이 전제라, trace JSON을 빌드로 굽는 구조와는 그대로 맞지 않는다(구운 산출물을 브랜치에 커밋해야 함). 매일 쓰는 학습 사이트 주소가 미리보기 중에 바뀌는 문제도 있으므로, 상시 사이트와 미리보기를 분리하는 방식(Cloudflare 브랜치 미리보기 또는 pr-preview 경로 방식)이 이 프로젝트에는 더 맞다. 초기 프로토타입 한두 번에는 이 방법이 가장 싸다.
- 출처: <https://til.simonwillison.net/claude-code/preview-github-pages> · <https://docs.github.com/en/pages/getting-started-with-github-pages/what-is-github-pages> · <https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site>

**C8 · 확인**

- 주장: CSS @page { size: ... }는 Safari에서 18.2부터만 지원된다(Chrome 15+, Firefox 95+).
- 확인한 내용: MDN browser-compat-data 기준 @page size 기술자: Chrome 15, Firefox 95, Safari 18.2(iOS Safari 동일), Android WebView 37, Samsung Internet 1.5. 추가로 알아야 할 점: (1) BCD는 @page 규칙 자체도 Safari 18.2로 적는다(impl_url webkit.org/b/15548). (2) size의 landscape·portrait 키워드는 Safari 미지원(version_added false), page-orientation도 Safari 미지원. (3) Safari 18.2 릴리스 노트에는 'Added support for @page margin descriptors.'와 'Fixed the size property of @page to parse as a descriptor, not a global CSS property.'가 있다. 즉 18.2 이전 Safari는 @page 여백·크기를 믿을 수 없다. (4) @page 여백 상자(top-center 등)는 Chrome 131+만 지원.
- 계획에 주는 영향: A7 세로 카드(74×105mm) 8장은 A4 가로(297×210, 4열×2행)에만 들어가는데, Safari는 'size: A4 landscape' 키워드를 지원하지 않는다. 가장 안전한 설계는 @page size에 의존하지 않는 것이다: 기본 A4 세로에 가로형 카드(105×74mm) 2열×4행(210×296mm)을 mm 단위 그리드로 깔고, 여백만 @page margin으로 지정하며, 인쇄는 Chrome(데스크톱 또는 Android)을 권장한다. 프린터의 비인쇄 여백 때문에 잘리는지는 실제 출력으로 확인해야 한다(이 문장은 추론, 출처 없음).
- 출처: <https://raw.githubusercontent.com/mdn/browser-compat-data/main/css/at-rules/page.json> · <https://developer.apple.com/documentation/safari-release-notes/safari-18_2-release-notes>

**C9 · 확인**

- 주장: Katy Jordan(2015, IRRODL)은 MOOC 221개에서 수료율 중앙값 12.6%(범위 0.7%~52.1%)를 보고했고, 과정이 길수록 수료율이 낮았다.
- 확인한 내용: Jordan, K. (2015). Massive open online course completion rates revisited: Assessment, length and attrition. IRRODL 16(3), 2015-06-19 게시, DOI 10.19173/irrodl.v16i3.2112. 초록 그대로: 221개 MOOC, 수료율(등록자 중 수료 비율)은 0.7%~52.1%, 중앙값 12.6%. 수료율은 과정 길이(길수록 낮음), 시작일(최근일수록 높음), 평가 방식(자동 채점만 쓰는 과정이 높음)에 따라 유의하게 달랐다. 활동 데이터가 있는 일부 과정에서는 첫 1~2주가 참여 유지에 결정적이었다. 한계: 등록자 기준 수료율이고 다중회귀의 상관 결과이며, 대상은 2010년대 초 공개 MOOC다. 혼자 쓰는 개인 교재에 수치를 그대로 옮길 수는 없다.
- 계획에 주는 영향: '79장 전체를 한 번에 약속하지 말고 1판을 12장 이하로 잡는다'는 권고의 근거로 쓸 수 있다. 다만 인과 근거가 아니라 방향성 근거로만 인용하고, 같은 초록의 '첫 1~2주가 결정적'을 반영해 1~3장의 완성도와 폰 사용성을 최우선으로 검증한다.
- 출처: <https://www.irrodl.org/index.php/irrodl/article/view/2112> · <https://api.crossref.org/works/10.19173/irrodl.v16i3.2112>

**C10 · 확인**

- 주장: Hello Algo README는 글·코드·그림·사진·영상 전부가 CC BY-NC-SA 4.0이라고 밝히며(코드도 MIT 아님), 한국어판은 ko/docs/chapter_appendix/terminology.md에 용어 표가 있다.
- 확인한 내용: krahets/hello-algo main 브랜치의 README.md(94행)·en/README.md·ko/README.md(96행) 모두 같은 문장으로 글·코드·그림·사진·영상에 CC BY-NC-SA 4.0을 적용한다. 루트 LICENSE 파일도 'Attribution-NonCommercial-ShareAlike 4.0 International' 전문이며 코드에 대한 별도 MIT 표기는 없다. ko/docs/chapter_appendix/terminology.md는 존재하고 136행, 표 줄 130개(머리·구분선 제외 용어 128개), English | 한국어 2열이다. 예: recursion 재귀, hash table 해시 테이블, load factor 적재율, heapify 힙 재정렬, binary search 이진 탐색, dynamic programming 동적 계획법, greedy algorithm 탐욕 알고리즘, backtracking algorithm 백트래킹 알고리즘, pruning 가지치기, state-transition equation 상태 전이 식.
- 계획에 주는 영향: Hello Algo의 코드·그림·문장을 가져오면 저장소 전체에 비영리·동일조건 의무가 걸린다. 구조와 용어 선택만 참고하고 코드·그림·글은 전부 새로 만든다는 권고(B안)가 맞다. 용어집은 표를 복제하지 않고 대조용으로만 쓰며, 자체 glossary 파일을 단일 원천으로 둔다.
- 출처: <https://raw.githubusercontent.com/krahets/hello-algo/main/README.md> · <https://raw.githubusercontent.com/krahets/hello-algo/main/ko/README.md> · <https://raw.githubusercontent.com/krahets/hello-algo/main/LICENSE> · <https://raw.githubusercontent.com/krahets/hello-algo/main/ko/docs/chapter_appendix/terminology.md>

**C11 · 부분 확인**

- 주장: Web Speech API speechSynthesis는 Android WebView에서 지원되지 않아 인앱 브라우저에서는 소리가 나지 않고, iOS·Android에서 화면이 잠기면 신뢰할 수 없다.
- 확인한 내용: 확인된 부분: MDN 호환성 데이터상 SpeechSynthesis와 SpeechSynthesisUtterance 및 모든 멤버가 Android WebView에서 미지원(version_added false, crbug.com/40417848)이다. 지원: Chrome 33(Android 동일), Safari 7(iOS 동일), Firefox Android 62, Samsung Internet 3.0, Opera Android 미지원. 또 Chrome Android에서 pause()는 cancel()처럼 현재 발화를 끝낸다. 범위 한정: '인앱 브라우저 무음'은 Android System WebView 기반 인앱 브라우저에만 해당한다. iOS 인앱(WKWebView)은 BCD상 Safari와 같게 표시된다. 확인되지 않은 부분: 화면 잠금 중 웹 음성 합성 동작에 대한 1차 근거는 찾지 못했다. 인용된 WebKit 버그 250665는 잠금과 무관한 'getVoices()에서 Kyoko(ja-JP)가 사라짐' 보고이고(상태 NEW, WebKit 측은 재현 실패), Apple 포럼 849627은 네이티브 AVSpeechSynthesizer(expo-speech)가 잠금 순간 멈춘다는 답글 0개짜리 단일 보고다. 따라서 '잠금 시 불안정'은 그럴듯한 추정이지 확인된 사실이 아니며, 사용자의 실제 기기에서 5분 시험으로 판정해야 한다.
- 계획에 주는 영향: '1판에서 오디오 제외' 결론은 유지해도 된다(WebView 미지원과 pause 동작만으로도 Web Speech는 불안정한 기반). 다만 근거 문장은 '잠금 시 멈춘다'가 아니라 '잠금 중 동작을 보장하는 근거가 없다'로 써야 한다. 오디오가 꼭 필요하면 빌드 시점에 만든 mp3를 <audio>로 재생하는 쪽이 검증 가능한 경로다. 사이트 링크는 카카오톡 인앱이 아니라 Chrome·Samsung Internet·Safari나 홈 화면 PWA로 열도록 안내한다.
- 출처: <https://raw.githubusercontent.com/mdn/browser-compat-data/main/api/SpeechSynthesis.json> · <https://raw.githubusercontent.com/mdn/browser-compat-data/main/api/SpeechSynthesisUtterance.json> · <https://bugs.webkit.org/show_bug.cgi?id=250665> · <https://developer.apple.com/forums/thread/849627>

**C12 · 부분 확인**

- 주장: sys.settrace 추적의 함정: 'line' 이벤트는 그 줄이 실행되기 전에 발생하므로 단순 기록은 상태 변화를 한 스텝 늦게 귀속하고, 지역 변수는 기록 시점에 deep copy해야 한다. Python Tutor pg_logger가 둘을 어떻게 처리하는지 확인.
- 확인한 내용: (1) 이벤트 시점은 문서로 확정된다: 'line' 이벤트는 인터프리터가 새 줄을 실행하기 직전(또는 루프 조건을 다시 실행하기 직전)에 발생한다. 따라서 그 시점 스냅샷은 '직전 줄까지 실행한 결과'이고, 마지막 줄의 효과는 'return' 이벤트에서만 잡힌다. (2) Python Tutor는 스텝을 밀지 않는다. pg_logger는 bdb.Bdb 서브클래스로 user_line에서 event 'step_line'을 기록하고, trace의 line은 '곧 실행될 줄'이라고 포맷 문서가 정의한다. 방금 실행한 줄은 이전 스텝의 line으로 표현한다. return 이벤트도 기록하며 __return__ 값을 넣는다. (3) 'deep copy 필수'는 과하게 좁은 표현이다. 필요한 것은 '기록 시점 스냅샷'이고, Python Tutor는 copy.deepcopy가 아니라 매 스텝 encoder.reset_heap() 뒤 pg_encoder로 값을 JSON용 구조로 직렬화하며 복합 객체를 ['REF', id]로 참조해 별칭(같은 객체를 가리키는 두 이름)을 보존한다. 변수별 deepcopy는 별칭 관계를 잃는다(한 번의 deepcopy 호출로 전체를 복사하거나 id 기반 직렬화가 필요). (4) Python 3.13부터 frame.f_locals는 최적화된 스코프에서 write-through proxy를 돌려주므로 프록시를 그대로 저장하면 안 되고 그 자리에서 값으로 풀어야 한다. (5) settrace 동작은 CPython 구현 세부사항이라 빌드 Python 버전을 고정해야 한다. 원 저장소 pgbovine/OnlinePythonTutor는 이 환경에서 raw 404였고, pg_logger는 Philip Guo 저작권 머리말이 붙은 포크(pathrise-eng/pathrise-python-tutor)에서 읽었다.
- 계획에 주는 영향: 추적기 설계 규칙을 이렇게 고정한다: line과 return 이벤트를 모두 기록한다. 화면 표기는 Python Tutor식 '방금 실행한 줄 / 다음에 실행할 줄' 두 표시 중 하나로 통일하고 스킬에 명문화한다(학습자가 머릿속으로 재생할 기준이 흔들리면 안 됨). 스냅샷은 id 기반 직렬화로 만들어 별칭을 보존한다(1장 참조 그림에 필수). .python-version으로 버전을 고정한다. 자체 100줄 추적기 대신 같은 규칙을 이미 구현한 dodona-json-tracer(bdb 기반, MIT)를 쓰는 선택지도 유효하다. 검증 테스트로 'x = 1 다음 스텝에서 x가 보이는가', 'b = a 뒤 b.append가 a에도 반영돼 보이는가'를 CI에 넣는다.
- 출처: <https://docs.python.org/3/library/sys.html#sys.settrace> · <https://docs.python.org/3/reference/datamodel.html#frame.f_locals> · <https://raw.githubusercontent.com/pathrise-eng/pathrise-python-tutor/master/v5-unity/pg_logger.py> · <https://raw.githubusercontent.com/pathrise-eng/pathrise-python-tutor/master/v5-unity/pg_encoder.py>

## 3. 1차 조사에서 바로잡은 것

원자료([data/sweep/](data/sweep/))에는 고치기 전 문장이 그대로 남아 있다. 아래가 우선한다.

- korean-community.json findings[12]: 낡은 정보다. BOJ는 2026-11-20에 데이원컴퍼니 운영으로 재오픈했다. 공식 종료 공지일은 2026-04-15이고 2026-04-19는 바킹독 블로그 글의 날짜다. '현재 운영 형태는 확인하지 못했다'는 부분은 BOJ 공지(board/view/166446)로 해소됐다.
- tech-implementation.json findings[4]: README 인용문 'a -settrace build with sys.settrace support for debuggers'는 @micropython/micropython-webassembly-pyscript가 아니라 새 패키지 @micropython/micropython-webassembly-browser(1.30.0-preview.302, JSPI 필요)를 설명하는 문장이다. pyscript 패키지에도 micropython-settrace.wasm이 들어 있긴 하다(1.28.0-6부터).
- tech-implementation.json findings[4]와 [23]: 'settrace 프레임에서 지역 변수를 읽을 수 있는지 미확인'이라고 했는데 답은 '읽을 수 없다'이다. MicroPython py/profile.c의 frame 객체는 f_back, f_code, f_globals, f_lasti, f_lineno만 제공하고 f_locals가 없다. 그래서 'sys.settrace 하나로 짜 두면 CPython 빌드 타임과 브라우저 런타임에서 같은 코드를 쓴다'(findings[2]의 implication)는 MicroPython에는 해당하지 않고 Pyodide에만 해당한다.
- tech-implementation.json findings[3]: pyodide.asm.wasm의 brotli 3,106,498B는 재현되지 않았다. 오늘 jsDelivr에서 3회 모두 3,439,687B였다. 코어 전송량은 'brotli 5.9MB'가 아니라 약 6.2MB다. gzip 6.4MB는 일치한다. 'sys.settrace 동작의 근거가 2차 자료(Trasee)'라는 부분은 Pyodide changelog 314.0.6이라는 1차 근거로 바꿀 수 있다.
- tech-implementation.json findings[20]: ts-fsrs '압축 약 11KB'는 진입 파일 dist/index.mjs 하나만 잰 값이다. 정적 import 청크와 의존성 @open-spaced-repetition/srs-kit, 동적 import 모델을 합치면 UMD 기준 196KB이고 압축하면 약 40KB다. 'createEmptyCard와 fsrs().repeat는 구버전(v4, v5) API'라는 서술도 부정확하다. v6에서도 deprecated 상태로 export되며 FSRS-6으로 동작한다.
- tech-implementation.json findings[8]: 'Material 9.7.5'는 최신이 아니다. 최신은 9.8.2(2026-11-19)이고 9.8.0부터 Python 3.11 이상을 요구한다. 'Zensical 0.1이 2026-11-05로 예정돼 있었다'는 이미 지난 일이다. 0.1.0이 2026-11-05에 나왔고 현재 0.1.3이다. MkDocs 2.0은 아직 프리릴리스(2.0.dev6)다. 2027-05-05는 2026-09-16에 6개월 연장된 기한이라는 맥락도 빠져 있다.
- tech-implementation.json findings[9]: VitePress를 '2순위(가장 단순)'로 추천하지만 안정판 1.6.4가 2025-08-05 이후 멈춰 있고 Vite 5에 묶여 있으며 2.0은 alpha.21이라는 사실이 빠졌다. Astro 7(2026-06-22)의 기본 Markdown 처리기가 Sätteri로 바뀌어 remark/rehype 플러그인이 기본 동작하지 않는다는 점, Starlight가 여전히 0.x(0.43.1)라는 점, Node 22 이상 요구도 빠졌다.
- tech-implementation.json findings[11]: 'Pagefind 분절은 중국어·일본어만'은 낡았다. 태국어도 포함된다. implication의 "'정렬을' 같은 어절은 '정렬' 검색에서 빠질 수 있다"는 틀렸다. Pagefind는 접두 일치(search.rs의 key.starts_with(term))를 하므로 '정렬'로 검색하면 '정렬을'과 '정렬은'이 잡힌다.
- tech-implementation.json findings[18]: 'Cloudflare Pages가 대안'은 낡았다. Cloudflare Pages 문서 첫 화면이 'Start new projects with Workers'라고 안내하므로 대안은 Workers Static Assets다. 'GitHub Free는 public만 가능'은 기억 기반으로 적혀 있었지만 GitHub 문서로 확인됐다. max-age=600과 gzip 전용은 문서에 없는 관측값이라 보장되지 않는다.
- tech-implementation.json findings[15]: 360px 뷰포트에 13px이면 '약 39자'가 아니라 38자다(304 ÷ 7.8 = 38.97, 39번째 글자가 넘친다). 다른 수치(390px에서 39, 42, 46자, 360px/14px에서 36자)는 맞다.
- tech-implementation.json findings[1]: trace 실험을 Python 3.13.18로 했는데 3.13은 이제 security 전용 브랜치이고 최신 안정판은 3.15.2(2026-10-25)다. curriculum-sequence가 권하는 heapq의 *_max 함수는 3.14 이상에만 있어서 현재 환경(3.13.18)에서는 빌드 타임 trace와 테스트가 실패한다. 교재의 기준 Python 버전을 먼저 정해야 한다.
- tech-implementation.json findings[0], viz-sites.json findings[9]: Python Tutor 코드와 trace 포맷의 출처가 2019년 포크(pathrise-eng/pathrise-python-tutor)다. 원 저장소 pgbovine/OnlinePythonTutor는 raw에서 404이고, 공식 저장소 pythontutor-dev/pythontutor에는 unsupported-features.md와 board.jpg만 있다. 현재 운영 코드는 공개돼 있지 않고 라이선스(MIT 문안)도 포크 스냅샷 기준이다. 현재 사이트는 Python 3.11을 쓴다.
- visual-textbooks.json findings[1], korean-community.json findings[11]: Hello Algo의 CC BY-NC-SA 4.0은 글뿐 아니라 코드, 그림, 사진, 영상 전체에 적용된다(README: 'The texts, code, images, photos, and videos'). korean-community의 '라이선스는 확인하지 못했다'는 해소됐다. 스윕이 놓친 사실로, 한국어판 2~15장에 '연습 문제(exercises.md)' 절이 있다.
- mobile-microlearning.json findings[14]: '홈 화면 웹앱은 자체 카운터를 가져 삭제되지 않을 것으로 기대'는 2020년 블로그 표현이다. 현행 WebKit Tracking Prevention 문서는 홈 화면 웹앱의 1차 도메인을 7일 상한에서 명시적으로 면제한다고 쓴다. iOS/iPadOS 26부터 홈 화면에 추가한 모든 사이트가 기본으로 웹앱으로 열린다는 변화도 빠져 있다. 7일은 달력 날짜가 아니라 'Safari 사용일' 기준이다.
- curriculum-sequence.json findings[11]: Python 3.14에서 추가된 max-heap 함수는 3개가 아니라 5개다(heapify_max, heappush_max, heappop_max, heappushpop_max, heapreplace_max). 스윕 문장에 '등'이 붙어 있어 틀린 서술은 아니다.
- tech-implementation.json findings[4]: micropython.wasm의 gzip 크기 200,412B는 오늘 측정값 197,580B와 다르다(brotli 170,998B는 일치). 결론에는 영향이 없다.
- mobile-microlearning.json findings[6] (및 summary): Roediger & Karpicke의 서로 다른 실험 수치를 한 문장에 섞었다. '5분 뒤 81% 대 75%'는 실험 1(학습 2회 vs 학습+시험)이고 '1주 뒤 61% 대 40%'는 실험 2(STTT vs SSSS)다. 실험 2의 5분 뒤 수치는 SSSS 83%, SSST 78%, STTT 71%이고, 실험 1의 1주 뒤 수치는 56% 대 42%다. 과신(자신감 4.8 vs 4.0, 7점 척도)은 실험 2에서만 측정됐다.
- learning-science.json summary의 '간격 복습과 누적 인터리빙이 없으면 1주 안에 대부분 잊는다'와 commonFeatures의 '복습 일정이 없으면 1주 안에 절반 가까이 잊는다': 원문 근거는 실험 2의 1주 비례 망각 SSSS 52%, SSST 28%, STTT 14%다. '대부분'은 지지되지 않는다. '절반'은 산문 지문을 읽기만 한 조건에만 해당하고, 한 번이라도 인출한 조건은 14~28%였다.
- learning-science.json findings[0]: '24개 통제 실험을 메타 분석'이라는 표현은 과하다. 원문은 실험마다 동일 가중치를 주는 득표 집계다("Under the assumption that each experimental study has equal weight"). 노력 동등 여부도 저자 판단이다. 논문 내부 불일치도 있다. 본문은 9+14=23개인데 Table 5는 노력 동등 10개를 나열하고 Hansen Study VII이 양쪽 열에 중복된다. Lawrence 데이터 크기도 본문은 '9 vs. 24 vs. 41', 표는 '9, 25, or 41'이다.
- learning-science.json summary, findings[20], blindSpots[0]: 'OSPAN이 인지분산 척도에서 최고 등급(5)이었다'를 측정 결과처럼 썼다. 원문에서 5.0은 범위 보정으로 OSPAN에 부여한 설계상 앵커다. 실제 측정된 일상 과제의 최고치는 음성-문자 이메일 3.06이고 핸즈프리 통화는 2.27이다. '머릿속 추적은 OSPAN과 구조가 같다'는 조사자의 유추이며 검증된 바 없다. unreachable에 적힌 원 보고서는 현재 https://aaafoundation.org/wp-content/uploads/2026/01/MeasuringCognitiveDistractionsReport.pdf 에서 받을 수 있다(2018/01 경로는 404).
- learning-science.json summary, findings[7], blindSpots: '종이에 추적을 적지 않으면 정답률이 82%에서 61%로 떨어진다'는 인과 서술이다. Cunningham 외 2017은 자기 선택 전략과 정답의 상관을 본 것이고, n=95와 n=135는 학생 수가 아니라 문항 응답 수다(학생은 부분표본 65명). 82.1%는 'Trace' 유형만의 값이다. Rewrite(60.7%)와 Odd Trace(55.6%)는 빈 종이와 같거나 낮았다.
- learning-science.json findings[5]: Tauber 외 2018을 '복잡한 자료에서는 효과가 줄 수 있다'로 약하게 요약했다. 초록 원문은 overt가 'covert retrieval practice or restudy'보다 높았다는 것이고(pooled d = 0.43), 후속 논문(PMC12292154)은 이를 'covert retrieval did not differ from restudy'로 정리한다. 즉 정의 수준 자료에서 covert는 재학습과 구별되지 않았다. 스윕이 '검색 요약으로만 확인'이라고 적은 부분은 이번에 초록 원문으로 확인했다.
- viz-sites.json openQuestions[7], unreachable[12]와 visual-textbooks.json findings[17]: 기억에 의존했다는 Naps taxonomy는 원문으로 확인됐다. 다만 viz-sites는 5단계(보기, 응답, 변경, 구성, 발표)만 적었고 첫 범주 'No viewing'이 빠졌다(원문은 6개). 원문은 이 분류가 서열 척도가 아니라고 명시한다("we do not consider this to be an ordinal scale"). '적극 참여 학습자가 더 잘한다'는 것은 이 보고서의 결과가 아니라 검증을 제안한 가설 I~VI이다.
- Naps 보고서와 Hundhausen 논문의 수치를 섞지 말 것. Naps 보고서 본문은 21개 실험 기준으로 참여 조작 12개 중 10개(83%), 표현 조작 9개 중 3개(33%)가 유의했다고 쓴다. Hundhausen 논문은 24개 실험 기준으로 노력 비동등 14개 중 10개(71%), 노력 동등 9개 중 3개(33%)다.
- skills-registries.json summary, commonFeatures[16]의 'drill-me의 85% 성공률 규칙': 스킬 본문의 실제 규칙은 '최근 약 7문항 성공률 80~90% 유지(Hard는 0.5로 계산)'이고 제목만 '85% rule'이다. 이름의 출처인 Wilson 외 2019는 이진 분류, 경사하강 학습 모델, 가우시안 잡음에 대한 이론·시뮬레이션이며 사람의 인출 연습을 다루지 않는다. '검증된 수치'가 아니라 운영 휴리스틱으로 표기해야 한다.
- mobile-microlearning.json subjects[10] (Anki): 'SM-2와 FSRS(기본 목표 기억률 90%)'는 틀리지 않았지만 오독하기 쉽다. 90%는 FSRS를 켰을 때의 desired retention 기본값이다. FSRS 자체는 Anki 26.09.4와 26.11b1에서도 기본 꺼짐이고, 내장 버전은 FSRS-6이다(FSRS-7 아님).
- tech-implementation.json findings[20]: 'ts-fsrs 6.0.1, 기본 FSRS-7'은 확인됐다(README "It defaults to FSRS-7"). 다만 6.0.1은 2026-11-22 배포, 6.0.0은 2026-10-28 배포, fsrs-rs 7.0.0은 2026-11-10 배포로 매우 최신이다. Anki 안정판은 아직 FSRS-6이므로 버전을 고정하고 모델 버전을 명시해야 한다.
- learning-science.json findings[1]: Naps 원문은 관련 모범 사례를 "the following eleven points"로 제시하므로 '11개 모범 사례'는 맞다. findings[7]의 Xie, Nelson & Ko 2018 수치(24명, 5~10분, +15%, 변동 46% 감소, 중간고사 +7%)도 원문 PDF로 확인했다. 수정할 것 없음.
- skills-registries.json findings[3]: 'analyze-graph.py로 품질 지표와 100점 점수 산출'은 틀렸다. analyze-graph.py에는 score 계산이 없고(문자열 'score' 0건), 1~100 점수는 SKILL.md가 에이전트에게 주관적으로 매기라고 지시한 것이다. 스크립트가 내는 것은 DAG 여부, 순환, 고립 노드, 단절 서브그래프, 최대 체인 길이, indegree·outdegree 분포와 권고 문구뿐이다.
- skills-registries.json findings[4]와 all_skill_candidates.json[0]: teach 작업공간 목록에서 RESOURCES.md와 형식 파일 3개(MISSION-FORMAT.md, RESOURCES-FORMAT.md, LEARNING-RECORD-FORMAT.md)가 빠졌다. '설치 수 기준 최대 교육 스킬'이라는 표현도 오해를 부른다. skills.sh의 mattpocock/skills 56개 스킬이 8.1K~1.6M에 분포하고(teach 980.7K는 12위, 저장소 합계 34.1M) 교육과 무관한 스킬도 55만 안팎이어서 저장소 일괄 설치가 반영된 수치로 보인다.
- teach SKILL.md 자체에 상반된 문장이 있다. Lessons 절은 "since the user will return to these later to review", Reference Documents 절은 "Lessons will rarely be revisited later - reference documents will be." 스윕은 뒤 문장만 인용했다.
- visual-textbooks.json summary는 Wengrow가 '재귀를 3개 장으로' 쪼갠다고 쓰고 같은 파일 findings[4]는 '4개 장(10~13장)'이라고 써서 서로 다르다. 실제 목차상 제목에 재귀가 들어간 장은 10, 11, 13장이고 12장은 Dynamic Programming이다.
- curriculum-sequence.json findings[0]의 '쉬운 O(n²) 정렬이 병합·퀵보다 먼저다(Wengrow 4~6장 → 13장)'에서 Wengrow가 뒷받침하는 것은 퀵 정렬뿐이다. Wengrow Volume 1에는 병합 정렬이 없고 Volume 2(2025년 9월) 1장 'Getting Things in Order with Mergesort'에 있다. 스윕은 Volume 2의 존재와 목차를 다루지 않았다.
- Wengrow 2판은 Python 전용이 아니다. 출판사 설명은 "with examples in JavaScript, Python, and Ruby"다. Python 전용은 2023년 12월 Volume 1과 2025년 9월 Volume 2다.
- visual-textbooks.json findings[5]: Red Blob Games가 '한 줄씩 바꿔 가며 BFS → 경로 복원 → 조기 종료 → Dijkstra → A*'로 간다는 서술은 Greedy Best First Search 단계(Heuristic search 절)를 빠뜨렸고, 조기 종료 → Dijkstra 구간은 한 줄이 아니라 9줄(신규 5, 변경 4)이 바뀐다. 한 줄만 바뀌는 것은 Dijkstra → A*뿐이다.
- korean-community.json findings[0]의 '강의 코드는 C++이다 ... 파이썬으로 다시 써야 한다'는 일부 낡았다. 2026-01-27 공지(blog.encrypted.gg/1106, docs/other-languages.md)에 따르면 0x11강까지 모든 문제의 파이썬 풀이가 hanXen/basic-algo-lecture-python에 공개돼 있고 나머지는 LLM 포팅을 예고했다. 강의 본문과 슬라이드의 코드는 여전히 C++이다.
- korean-community.json findings[0]은 바킹독의 BFS 선행 배치를 '난이도 곡선이 완만해진다'의 근거로 쓰지만, 원문은 BFS를 "첫 번째 고비"라고 부르고 0x09·0x0A는 일반 그래프가 아닌 격자 Flood Fill이며 0x0A DFS에는 연습 문제가 없다. 재귀 DFS는 0x18 그래프 강의에서 처음 나온다.
- korean-community.json findings[12]: BOJ 운영 상태를 '확인하지 못했다'고 했는데, 2026-11-23에 acmicpc.net 첫 화면이 정상 응답하고 '33440 채점 가능한 문제'와 하단 '상호 : (주)데이원컴퍼니'가 표시된다. 즉 종료 공지(바킹독 2026-04-19 글) 이후 운영 주체가 바뀌어 서비스가 재개된 상태다. 2026-06-11자 '데이원컴퍼니, BOJ 인수' 기사는 검색 결과 제목만 확인했고 본문은 읽지 못했다. 바킹독은 2026-05-08 글에서 강의용 유료 서비스를 만들고 있다고 밝혔다.
- all_skill_candidates.json[4] (mizchi explainer)의 pageUrl이 skills.sh/mizchi/explainer/explanatory-animation인데, CHANGELOG 0.5.0(2026-10-02)에서 explain-with-anim과 explanatory-animation 스킬 및 @mizchi/vlmkit-anim이 삭제됐다("nothing is animated"). 현재 skills/ 아래는 d2-diagram, d2-slides, explainer, explainer-book, first-reader 5개다. mizchi/explainer를 애니메이션 시각화 선례로 인용한 부분이 있다면 낡은 정보다.
- tech-implementation.json findings[21]: 'name은 필수'는 agentskills.io 규격 기준이고 Claude Code에서는 "All fields are optional"이다(name 생략 시 디렉터리 이름). 스윕이 나열한 Claude Code 필드에는 disallowed-tools, effort, background, shell, arguments, user-invocable, hooks, agent, model이 빠져 있고, name에 anthropic·claude 예약어 금지와 XML 태그 금지(플랫폼 문서)도 빠져 있다.
- dmccreary 저장소는 dmccreary/ibook-skills로 이름이 바뀐 것이 맞다(이전 주소 raw URL도 같은 내용을 돌려준다). 스윕은 라이선스를 언급하지 않았는데 CC BY-NC-SA 4.0(비상업, 동일조건)이므로 스크립트나 본문을 복사해 쓰면 조건이 따라온다. mizchi/explainer는 MIT다.
- skills-algo-viz-site.json findings[5]와 skills-registries.json findings[3]은 '위반 0건 assert'를 각각 chapter-content-generator Step 1.3b와 book-chapter-generator에 귀속시키는데, 둘 다 맞다. 같은 검사가 두 스킬에 각각 들어 있다.
- korean-community.json: '바킹독은 2026-04-19 공지에서 …'의 4월 19일은 바킹독 블로그 글 날짜다. BOJ 공식 '서비스 종료 안내'는 2026-04-15 15:14(KST)에 올라왔고 실제 종료일은 2026-04-28이다. 같은 파일 blindSpots의 '현재 상태는 미확인'과 findings의 '정적 백업인지 재개인지 확인하지 못했다'는 낡았다: 2026-11-20 11:13에 (주)데이원컴퍼니가 서비스를 재개했다.
- korean-community.json: solved.ac CLASS 구성은 여전히 확인 불가(solved.ac 본 사이트가 Cloudflare 403). solved.ac 공식 공지(2026-04-15)는 BOJ 연동을 2026-04-28에 종료한다고 했고 이후 공지가 없어, 재개된 BOJ와의 연동 상태는 알 수 없다. 기억 기반 CLASS 서술은 계획 근거로 쓰면 안 된다.
- 보완 조사 메모: '@dodona/trace-component 1.7.2, 2026-10-19 갱신'에서 10-19는 npm 레지스트리 modified 시각이고 1.7.2 게시일은 2026-10-14다.
- 보완 조사 메모: 'picker 슬롯으로 하단 큰 버튼 교체 가능'과 'frame-change 이벤트 제공'을 함께 적었지만, README에 따르면 picker 슬롯을 채우면 frame-change가 발생하지 않는다('Only the built-in picker sends this event'). 두 기능은 동시에 쓸 수 없고 selectedFrame을 직접 관리해야 한다.
- 보완 조사 메모: 'Cloudflare가 Workers 정적 자산을 권한다'를 2차 자료(flaviocopes.com) 전언으로만 적었는데, Cloudflare Pages 공식 문서 첫 화면에 'Start new projects with Workers.'로 명시돼 있다. 또 '<branch>.<project>.pages.dev'는 브랜치명을 그대로 쓰지 않는다: claude/xyz 브랜치는 claude-xyz.<project>.pages.dev가 된다. 미리보기 배포는 30일 뒤 삭제된다(최근 100개와 현재 프로덕션 제외).
- 보완 조사 메모: Simon Willison 방식의 전제 하나가 빠졌다. 그는 private 저장소에 Pages를 쓰는데 GitHub Free는 public 저장소에서만 Pages를 허용한다. 무료 계정이면 저장소를 공개해야 하고, 어느 경우든 사이트 URL은 공개다.
- 보완 조사 메모: '모바일 앱에는 사이트 미리보기가 없다'는 불완전할 수 있다. 공식 문서에 Artifacts 기능이 있다: 'a live, interactive web page that Claude Code publishes from your session to a private URL on claude.ai'. 제약은 자기완결 단일 페이지, 렌더 크기 16 MiB 이하, 엄격한 CSP(외부 스크립트는 cdnjs·unpkg·jsDelivr npm 경로·Tailwind·jQuery CDN만, 외부 이미지 차단, 백엔드·다중 경로 없음). 문서의 Surface 행은 CLI·데스크톱 앱·remote-control을 명시하고 클라우드 세션은 명시하지 않지만, 이 조사 세션(클라우드)에는 Artifact 게시 도구가 실제로 제공돼 있었다(게시는 실행하지 않음). 한 챕터짜리 프로토타입의 비공개 미리보기 경로로 사용자 플랜에서 되는지 확인할 가치가 있다.
- 보완 조사 메모: '한글 폰트 apt 설치 가능 여부는 미확인'은 문서로 해결된다. cloud-environments 문서: 'Scripts run as root on Ubuntu 24.04, so `apt install` and most language package managers work.' 기본 허용 도메인에 archive.ubuntu.com·security.ubuntu.com이 있다. 이 VM에서 fc-list :lang=ko는 WenQuanYi Zen Hei와 Unifont만 나왔고 Graphviz(dot)도 없었다. 둘 다 setup script로 설치해야 한다(실제 설치는 해 보지 않음).
- 보완 조사 메모(인쇄 카드): 'A7(74×105mm)을 A4에 8장'은 A4 가로 방향(4×2)에서만 성립한다. BCD상 Safari는 @page size의 landscape 키워드를 지원하지 않으므로 기본 A4 세로에 가로형 카드 105×74mm를 2×4로 배치하는 편이 안전하다.
- 보완 조사 메모(오디오): WebKit 버그 250665는 WebKit 측이 재현하지 못한 미해결 보고('we can not')이고 Apple 포럼 849627은 답글 0개인 네이티브 앱 보고다. 둘 다 '웹 음성이 잠금 화면에서 멈춘다'의 근거가 아니다. 보완 조사 본문은 '근거를 찾지 못했다'고 정확히 썼으나, 이를 요약한 주장(C11)의 '잠금 시 불안정'은 확인된 사실이 아니다.
- tech-implementation.json: 'GitHub Free에서는 public 저장소만 Pages를 쓸 수 있다는 것은 기억 및 검색 요약 기반'이라고 했는데, GitHub 공식 문서로 확인됐다(C5 참조).
- tech-implementation.json: 'Material 9.7.5는 mkdocs<2로 고정'의 버전이 낡았다. PyPI 최신은 mkdocs-material 9.8.2(2026-11-19)이고 zensical 0.1.3(2026-11-20)이 이미 올라와 있다. mkdocs 최신은 여전히 1.6.1(2024-08-30)이다. '중요 수정은 2027-05-05까지'는 공식 홈('End of life on May 5, 2027')과 일치한다. 9.8.2의 mkdocs 버전 고정 여부는 다시 확인하지 않았다.
- tech-implementation.json·viz-sites.json: Python Tutor 원 저장소 경로(pgbovine/OnlinePythonTutor의 v5-unity/pg_logger.py)는 이 환경에서 raw 404였고, pythontutor-dev/pythontutor에는 문서 2개(board.jpg, unsupported-features.md)만 있다. 스윕이 읽은 pg_logger는 포크(pathrise-eng/pathrise-python-tutor) 사본이다. 'Python Tutor를 포크한다'는 선택지는 원본이 아닌 포크 기준이라는 점을 명시해야 한다.
- tech-implementation.json: '스냅샷은 반드시 deepcopy 또는 직렬화, 스텝 설명은 한 칸 밀어 붙여야 한다'에서 '밀기'는 유일한 방법이 아니다. Python Tutor는 밀지 않고 line을 '곧 실행될 줄'로 정의하며 return 이벤트를 따로 기록한다. 또 Python 3.13+에서 frame.f_locals가 write-through proxy라는 점(공식 문서)이 스윕에 빠져 있다. 현재 docs.python.org/3 기본 문서는 3.15.2이고 클라우드 VM의 Python은 3.13.18이라, '최신 Python'을 전제로 한 서술은 버전을 명시해야 한다.
- 보완 조사 메모: Hello Algo 용어집을 '130행'이라고 했는데 파일은 136행이고 표 줄이 130개(머리·구분선 포함)라 실제 용어는 128개다. 사소한 수치 차이다.

## 4. 조사 대상

스킬 36개의 원문 주소는 [02b-skill-notes.md](02b-skill-notes.md)에 있다.

### 알고리즘 시각화 사이트

- VisuAlgo: <https://visualgo.net/en>
- USFCA Data Structure Visualizations (David Galles): <https://www.cs.usfca.edu/~galles/visualization/Algorithms.html>
- CSVisTool (Georgia Tech CS 1332 Visualization Tool): <https://csvistool.com/>
- Algorithm Visualizer: <https://algorithm-visualizer.org/>
- Python Tutor: <https://pythontutor.com/>
- memory_graph / Memory Graph Web Debugger: <https://memory-graph.com/>
- Thonny: <https://thonny.org/>
- Recursive (oilater): <https://recursive.oilater.com/en>
- staying.fun: <https://staying.fun/en>
- alg0.dev (Algorithm Visualizer): <https://alg0.dev/>
- Toptal Sorting Algorithms Animations: <https://www.toptal.com/developers/sorting-algorithms>
- Pathfinding Visualizer (Clement Mihailescu): <https://clementmihailescu.github.io/Pathfinding-Visualizer/>
- W3Schools DSA: <https://www.w3schools.com/dsa/dsa_algo_bubblesort.php>
- Programiz DSA: <https://www.programiz.com/dsa/bubble-sort>
- Hello Algo: <https://github.com/krahets/hello-algo>
- See Algorithms: <https://see-algorithms.com/>
- Red Blob Games - Introduction to A*: <https://www.redblobgames.com/pathfinding/a-star/introduction.html>
- OpenDSA: <https://opendsa-server.cs.vt.edu/home/about>
- codedive.in (LeetCode 시각화): <https://dev.to/rajan_shukla_b4cde34c3c21/i-built-a-free-leetcode-visualizer-heres-what-i-learned-making-207-problems-animate-line-by-line-5g7n>
- Algorithms: Explained and Animated (모바일 앱): <https://algorithm.wiki/en/app/>
- AlgoMonster (Flowchart, Templates): <https://algo.monster/flowchart>
- NeetCode: <https://neetcode.io/roadmap>
- LeetCode Explore cards: <https://leetcode.com/explore/>
- SortVisualizer: <https://www.sortvisualizer.com/bubblesort/>

### 시각 교재와 에세이

- Hello Algo (krahets/hello-algo): <https://github.com/krahets/hello-algo>
- Grokking Algorithms, Second Edition (Aditya Bhargava): <https://www.manning.com/books/grokking-algorithms-second-edition>
- Problem Solving with Algorithms and Data Structures using Python (Miller & Ranum, Runestone): <https://github.com/RunestoneInteractive/pythonds>
- A Common-Sense Guide to Data Structures and Algorithms in Python, Volume 1 (Jay Wengrow): <https://pragprog.com/titles/jwpython/a-common-sense-guide-to-data-structures-and-algorithms-in-python-volume-1/>
- Red Blob Games (Amit Patel): <https://www.redblobgames.com/pathfinding/a-star/introduction.html>
- Sam Rose (samwho.dev) 시각 에세이: <https://samwho.dev/big-o/>
- Bartosz Ciechanowski (ciechanow.ski): <https://ciechanow.ski/gps/>
- Josh W. Comeau: <https://www.joshwcomeau.com/css/interactive-guide-to-flexbox/>
- Bret Victor: Learnable Programming / Explorable Explanations: <https://worrydream.com/LearnableProgramming/>
- Nicky Case / explorabl.es: <https://blog.ncase.me/how-i-make-an-explorable-explanation/>
- TheAlgorithms/Python: <https://github.com/TheAlgorithms/Python>
- Interview Cake: <https://www.interviewcake.com/concept/python/binary-search>
- Tech Interview Handbook: Algorithms study cheatsheets: <https://www.techinterviewhandbook.org/algorithms/study-cheatsheet/>
- roadmap.sh: Data Structures & Algorithms: <https://roadmap.sh/datastructures-and-algorithms>
- Open Data Structures (Pat Morin), pseudocode/Python판: <https://opendatastructures.org/ods-python/>
- CS50x Week 3 Algorithms + Shorts: <https://cs50.harvard.edu/x/weeks/3/>
- Algorithms Illuminated (Tim Roughgarden): <https://www.algorithmsilluminated.org/>
- MIT 6.006 Introduction to Algorithms (Spring 2020): <https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/resources/lecture-notes/>
- Think Data Structures / Data Structures and Information Retrieval in Python (Allen Downey): <https://allendowney.github.io/DSIRP/>
- Brilliant: Computer Science Algorithms: <https://brilliant.org/courses/computer-science-algorithms/>
- Educative: Grokking the Coding Interview Patterns: <https://www.educative.io/courses/grokking-coding-interview>
- Algorithms: Explained&Animated 앱 / 알고리즘 도감(アルゴリズム図鑑, Ishida & Miyazaki): <https://apps.apple.com/us/app/algorithms-explained-animated/id1047532631>

### 모바일 학습 앱과 형식

- Brilliant: <https://brilliant.org>
- Duolingo: <https://www.duolingo.com>
- Mimo: <https://mimo.org>
- Sololearn: <https://www.sololearn.com>
- Enki: <https://www.enki.com>
- Grasshopper (Google Area 120): <https://en.wikipedia.org/wiki/Grasshopper_(mobile_app)>
- Py: <https://www.ghacks.net/2017/08/09/py-for-android-learn-programming-and-it-skills/>
- Programming Hero (현재 App Store 명칭: Fibu): <https://apps.apple.com/us/app/programming-hero-coding-fun/id1478201849>
- Codecademy Go: <https://apps.apple.com/us/app/codecademy-go/id1376029326>
- Khan Academy 모바일: <https://www.khanacademy.org/downloads>
- Anki / AnkiDroid: <https://docs.ankidroid.org/>
- Mochi: <https://mochi.cards/docs/>
- RemNote: <https://help.remnote.com/en/articles/6026144-the-remnote-spaced-repetition-algorithm>
- Algorithms: Explained and Animated: <https://algorithm.wiki/en/app/>
- Imprint: <https://apps.apple.com/us/app/imprint-learn-visually/id1482780647>
- Headway: <https://apps.apple.com/us/app/headway-daily-book-summaries/id1457185832>
- LeetCode 모바일: <https://leetcode.com>
- Google Web Stories (탭-스루 스토리 포맷): <https://amp.dev/documentation/guides-and-tutorials/start/create_successful_stories/>
- Readwise Daily Review: <https://docs.readwise.io/readwise/docs/faqs/reviewing-highlights>

### 커리큘럼(목차를 읽은 것)

- CLRS — Introduction to Algorithms 4판 (2022): <https://mitp-content-server.mit.edu/books/content/sectbyfn/books_pres_0/3923/11599-transition-guide.pdf>
- Sedgewick & Wayne — Algorithms 4판: <https://algs4.cs.princeton.edu/home/>
- Skiena — The Algorithm Design Manual 3판 (Part I): <https://paulbatchelor.github.io/brain/TADM>
- Grokking Algorithms 2판 (Bhargava): <https://www.manning.com/books/grokking-algorithms-second-edition>
- Wengrow — A Common-Sense Guide to DS&A in Python, Vol. 1: <https://pragprog.com/titles/jwpython/a-common-sense-guide-to-data-structures-and-algorithms-in-python-volume-1/>
- pythonds — Problem Solving with Algorithms and Data Structures using Python (Miller & Ranum): <https://raw.githubusercontent.com/RunestoneInteractive/pythonds/master/_sources/index.rst>
- Hello Algo (krahets/hello-algo, 영어판 mkdocs nav): <https://raw.githubusercontent.com/krahets/hello-algo/main/en/mkdocs.yml>
- Goodrich, Tamassia, Goldwasser — Data Structures and Algorithms in Python: <https://www.zybooks.com/catalog/data-structures-algorithms-python/>
- MIT 6.006 Introduction to Algorithms (OCW Spring 2020): <https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/pages/calendar/>
- Stanford CS106B Programming Abstractions (Autumn 2026 사이트): <https://web.stanford.edu/class/cs106b/>
- Stanford CS161 Design and Analysis of Algorithms (Winter 2025): <https://stanford-cs161.github.io/winter2025/lectures/>
- Princeton COS226 Algorithms and Data Structures (Fall 2024): <https://www.cs.princeton.edu/courses/archive/fall24/cos226/lectures.php>
- UC Berkeley CS61B Data Structures (Spring 2025): <https://sp25.datastructur.es/>
- NeetCode 로드맵 / NeetCode 150 카테고리: <https://neetcode.io/roadmap>
- roadmap.sh — Data Structures & Algorithms: <https://roadmap.sh/pdfs/roadmaps/datastructures-and-algorithms.pdf>
- Tech Interview Handbook — 학습 계획 (1~4주 주제 순): <https://www.techinterviewhandbook.org/coding-interview-study-plan/>
- LeetCode Explore 'Learn' 카드: <https://leetcode.com/explore/learn/>
- USACO Guide (Bronze → Silver → Gold → Platinum → Advanced): <https://raw.githubusercontent.com/cpinitiative/usaco-guide/master/content/ordering.ts>
- CSES Problem Set + Competitive Programmer's Handbook (Laaksonen): <https://cses.fi/book/book.pdf>
- CP-Algorithms (navigation.md): <https://raw.githubusercontent.com/cp-algorithms/cp-algorithms/main/src/navigation.md>
- Khan Academy — Algorithms (Cormen·Balkcom 협업): <https://www.khanacademy.org/computing/computer-science/algorithms>
- freeCodeCamp — Coding Interview Prep: <https://raw.githubusercontent.com/freeCodeCamp/freeCodeCamp/main/curriculum/structure/superblocks/coding-interview-prep.json>
- Codecademy — Learn Data Structures and Algorithms with Python: <https://www.codecademy.com/learn/learn-data-structures-and-algorithms-with-python>
- AlgoExpert 문제 카테고리: <https://www.algoexpert.io/questions>
- BaaaaaaaarkingDog 실전 알고리즘 강좌 (encrypted-def/basic-algo-lecture): <https://github.com/encrypted-def/basic-algo-lecture>
- 이것이 취업을 위한 코딩 테스트다 with 파이썬 (ndb796): <https://github.com/ndb796/python-for-coding-test>
- 바킹독의 실전 알고리즘 (C++, 블로그·유튜브 무료 강의): <https://github.com/encrypted-def/basic-algo-lecture>
- 이것이 취업을 위한 코딩 테스트다 with Python (나동빈, 한빛미디어): <https://github.com/ndb796/python-for-coding-test>
- 백준 단계별로 풀어보기: <https://www.acmicpc.net/step>
- 코딩 테스트 합격자 되기 - 파이썬 편 (박경록, 골든래빗): <https://www.yes24.com/Product/Goods/123272392>
- 파이썬 알고리즘 인터뷰 (박상길, 책만): <https://github.com/onlybooks/python-algorithm-interview>
- Do it! 자료구조와 함께 배우는 알고리즘 입문: 파이썬 편 (시바타 보요, 이지스퍼블리싱): <https://www.yes24.com/Product/Goods/91219874>
- 프로그래머스 알고리즘 고득점 Kit: <https://school.programmers.co.kr/learn/challenges?tab=algorithm_practice_kit>
- Hello 알고리즘 한국어판 (krahets/hello-algo, ko/): <https://github.com/krahets/hello-algo/tree/main/ko>
- Hello Coding 그림으로 개념을 이해하는 알고리즘 (Grokking Algorithms 번역, 한빛미디어): <https://www.yes24.com/Product/Goods/37885448>
- 그림으로 배우는 알고리즘 (Yes24 상품 29032375): <https://www.yes24.com/Product/Goods/29032375>
- 인프런: 파이썬 알고리즘 문제풀이 입문(코딩테스트 대비) (김태원): <https://www.inflearn.com/course/파이썬-알고리즘-문제풀이-코딩테스트>
- 인프런: 38군데 합격 비법, 코딩테스트 필수 알고리즘 (딩코딩코, Python): <https://www.inflearn.com/course/38군데-합격비법-코테-필수-알고리즘>
- 인프런: 그림으로 쉽게 배우는 자료구조와 알고리즘 (기본편) (감자, JavaScript): <https://www.inflearn.com/course/자료구조-알고리즘-기본>
- solved.ac CLASS (미검증): <https://solved.ac/class>
- Hello Algo (mkdocs.yml nav, 한국어판 제목): <https://raw.githubusercontent.com/krahets/hello-algo/main/ko/mkdocs.yml>
- Grokking Algorithms, Second Edition: <https://www.manning.com/books/grokking-algorithms-second-edition>
- Problem Solving with Algorithms and Data Structures using Python (pythonds): <https://raw.githubusercontent.com/RunestoneInteractive/pythonds/master/_sources/index.rst>
- A Common-Sense Guide to Data Structures and Algorithms in Python, Volume 1: <https://pragprog.com/titles/jwpython/a-common-sense-guide-to-data-structures-and-algorithms-in-python-volume-1/>
- 알고리즘 도감 증보개정판(アルゴリズム図鑑, 쇼에이샤): <https://www.shoeisha.co.jp/book/detail/9784798172439>
- Brilliant: Computer Science Algorithms: <https://brilliant.org/courses/computer-science-algorithms/>
- MIT 6.006 Spring 2020 강의 노트: <https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/resources/lecture-notes/>
- Algorithms Illuminated (Parts 1~4): <https://www.algorithmsilluminated.org/>
- CS50x 2026: <https://cs50.harvard.edu/x/weeks/3/>
- Data Structures and Information Retrieval in Python (Downey): <https://allendowney.github.io/DSIRP/>
- Open Data Structures (pseudocode/Python판): <https://opendatastructures.org/ods-python/>
- Tech Interview Handbook: Algorithms study cheatsheets: <https://www.techinterviewhandbook.org/algorithms/study-cheatsheet/>
- Educative: Grokking the Coding Interview Patterns: <https://www.educative.io/courses/grokking-coding-interview>
- Interview Cake 용어집 내비게이션: <https://www.interviewcake.com/concept/python/binary-search>
- TheAlgorithms/Python DIRECTORY.md: <https://raw.githubusercontent.com/TheAlgorithms/Python/master/DIRECTORY.md>

## 5. 학습과학 문헌

- AV는 수동 시청으로는 거의 효과가 없고, 학습자의 활동(예측, 질문 응답, 입력 구성)이 효과를 결정한다. <https://www.cc.gatech.edu/~stasko/papers/jvlc02.pdf>
- Naps 등(2002)의 참여 분류(engagement taxonomy)는 6단계이고, 이 사이트가 노릴 구간은 Responding과 Changing이다. <https://typeset.io/pdf/exploring-the-role-of-visualization-and-engagement-in-bhelf2687d.pdf> · <https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6302837/>
- AV 효과 요인 중 가장 큰 것은 사용자가 속도를 직접 제어하는 것이었고, 의사코드를 옆에 띄우는 것만으로는 이해가 늘지 않았다. <https://people.cs.vt.edu/~shaffer/Papers/ShafferTOCE11.pdf>
- 부드러운 연속 애니메이션은 정적 그림보다 낫다는 근거가 약하다. 사람은 과정을 이산 단계로 이해한다. <https://hci.stanford.edu/courses/cs448b/papers/Tversky_AnimationFacilitate_IJHCS02.pdf>
- 다시 읽기보다 인출(시험)이 장기 기억에 훨씬 유리하다. 그런데 다시 읽은 사람이 더 자신만만하다. <https://gwern.net/doc/psychology/spaced-repetition/2006-roediger.pdf>
- 소리 내지 않는 은밀한 인출도 효과가 있다. 다만 복잡한 자료에서는 불완전하게 끝나 효과가 줄 수 있다. <https://pcllab.github.io/downloads/2013/2013_Smith_Roediger_Karpicke_JEPLMC.pdf> · <https://profiles.wustl.edu/en/publications/does-covert-retrieval-benefit-learning-of-key-term-definitions/>
- 작업기억은 약 3~5 청크다. 머릿속 트레이스의 크기 상한을 여기에 맞춰야 한다. <https://pmc.ncbi.nlm.nih.gov/articles/PMC2864034> · <https://gvu.gatech.edu/sites/default/files/related_project_files/p164-cunningham.pdf>
- 종이에 추적을 적으면 정답률이 크게 오른다. 종이 없는 머릿속 추적은 본질적으로 불리한 조건이다. <https://gvu.gatech.edu/sites/default/files/related_project_files/p164-cunningham.pdf> · <https://faculty.washington.edu/ajko/papers/Xie2018TracingStrategies.pdf>
- 추적 → 설명 → 작성의 기술 위계가 있다. 추적만 잘한다고 코드를 쓸 수 있는 것은 아니다. <https://opus.lib.uts.edu.au/bitstream/10453/10806/1/2008001530.pdf> · <https://opus.lib.uts.edu.au/handle/10453/10806>
- 난이도의 실체는 '동시에 처리해야 하는 상호작용 요소 수'이며, 학습자의 스키마가 생기면 같은 내용도 쉬워진다. <https://link.springer.com/doi/10.1007/s10648-010-9128-5> · <https://link.springer.com/article/10.1007/s10648-023-09782-w>
- 초보자에게는 풀이 예제 → 뒤에서부터 지워 가는 페이딩 → 독립 풀이 순서가 유리하고, 숙련되면 풀이 예제가 오히려 방해가 된다. <https://link.springer.com/doi/10.1007/s11251-009-9107-8> · <https://en.wikipedia.org/wiki/Expertise_reversal_effect>
- Mayer의 멀티미디어 원리 중 분절, 사전 훈련, 신호, 공간 근접, 군더더기 제거는 효과 크기가 크고 모바일 스테퍼 설계와 직접 대응된다. <https://www.unh.edu/teaching-learning-resource-hub/sites/default/files/media/2023-06/itow-research-based-principles-for-designing-multimedia-instruction-mayer.pdf>
- 복습 간격은 기억하고 싶은 기간에 비례해 넓혀야 한다. 개인용으로는 단순 스케줄러면 충분하다. <https://pubmed.ncbi.nlm.nih.gov/19076480/> · <https://escholarship.org/uc/item/0kp5q19x>
- 10가지 학습 기법 중 연습 시험과 분산 연습만 '높음'이고, 다시 읽기·하이라이트·요약은 '낮음'이다. <https://www.psychologicalscience.org/news/releases/which-study-strategies-make-the-grade.html> · <https://www.psychologicalscience.org/journals/pspi/1529100612453266/>
- 인터리빙은 연습 중 성적을 떨어뜨리지만 지연 시험 성적을 크게 올린다. 핵심 이득은 '어떤 방법을 쓸지 고르는 능력'이다. <https://link.springer.com/article/10.3758/s13423-014-0588-3> · <https://bjorklab.psych.ucla.edu/wp-content/uploads/sites/13/2016/04/EBjork_RBjork_2011.pdf>
- 예측을 먼저 하고 답을 보는 것은 예측이 틀려도 학습에 도움이 되지만, 예측 기능만 붙인다고 효과가 나지는 않는다. <https://pubmed.ncbi.nlm.nih.gov/19751074/> · <https://www.cc.gatech.edu/~stasko/papers/jvlc02.pdf>
- 심상 연습(mental practice)은 수행을 실제로 높이지만 효과는 작고, 인지적 과제일수록, 직후일수록 크다. <https://pure.ul.ie/en/publications/does-mental-practice-still-enhance-performance-a-24-year-follow-u/> · <https://academicnewsletter.sufe.edu.cn/info/372964>
- 하위 목표 라벨과 Parsons 문제는 타이핑 없이 절차를 익히는 근거 기반 형식이다. <https://scholarworks.gsu.edu/ltd_facpub/34> · <https://strathprints.strath.ac.uk/86100/>
- CS의 문턱 개념과 DP의 구체적 난점이 난이도 급등 지점이다. <https://www.csc.kth.se/~emmaen/FIE13.pdf> · <https://informahealthcare.com/doi/abs/10.1080/08993408.2022.2079865>
- 숙달 학습은 '통과해야 다음으로' 방식이며, 효과는 중간 크기다. <https://gwern.net/doc/psychology/1984-bloom.pdf> · <https://en.wikipedia.org/wiki/Bloom%27s_2_sigma_problem>
- 단조로운 작업에서는 마음이 원래 자주 떠돌고, 그때 외부 신호 처리가 떨어진다. 계산과 기억을 동시에 하는 과제는 인지 분산이 최고 수준이다. <https://www.frontiersin.org/journals/neuroscience/articles/10.3389/fnins.2017.00541/full> · <https://aaafoundation.org/measuring-cognitive-distraction-automobile/>
- 커뮤니티의 '암기 대 이해' 논쟁은 '이유와 함께 외운 불변식·템플릿 + 변형 질문'으로 수렴한다. <https://news.ycombinator.com/item?id=40173237> · <https://news.ycombinator.com/item?id=38506900>
- 학습과학 원리를 Agent Skill로 옮긴 공개 라이브러리가 있으며, 구조를 그대로 참고할 수 있다. <https://github.com/GarethManning/education-agent-skills> · <https://raw.githubusercontent.com/GarethManning/education-agent-skills/main/README.md>

1차 조사의 문장이다. 2절에서 따로 검증한 항목은 2절의 문장이 우선한다.

## 6. 읽지 못한 곳

- runestone.academy pythonds 본문 (Cloudflare 차단) : GitHub raw의 toctree.rst로 대체
- mitpress.mit.edu CLRS 4판 페이지 (403), penguinrandomhouse.com 페이지에는 목차 없음 : 전체 목차는 기억 + 전환 가이드 PDF로 부분 확인
- wiley.com 및 oreilly.com의 Goodrich 목차 (403) : zyBooks 목차로 대체
- link.springer.com Skiena 3판 페이지 (차단) : 2차 출처와 2판 목차 PDF로 대체
- khanacademy.org (봇 차단 페이지), web.archive.org (연결 실패) : Khan 단원 순서는 기억 기반
- leetcode.com/explore (403) : Explore 카드 순서는 검색 스니펫의 커뮤니티 제안뿐
- neetcode.io/roadmap의 렌더링된 선수 관계 DAG (JS 렌더링) : 카테고리 배열만 JS 번들에서 확인
- roadmap.sh 인터랙티브 페이지 (JS 렌더링), github.com 트리 페이지 (403), jsdelivr 파일 목록 (50MB 초과) : 공식 PDF로 대체
- algoexpert.io (Unsupported browser 페이지)
- acmicpc.net/step 백준 단계별로 풀어보기 (HTML에 단계 목록 없음)
- educative.io DSA 경로 (가져오지 않음)
- wiki.python.org TimeComplexity (리다이렉트 페이지만 반환, 본문 추출 실패) : docs.python.org로 대체
- hello-algo.com (지시에 따라 직접 접근하지 않고 GitHub raw 사용)
- link.springer.com 요소 상호작용성 논문 본문 (내용 추출 실패) : 검색 스니펫만
- freeCodeCamp 블록 내부의 챌린지 순서 (superblock 구조 파일만 확인)
- https://news.hada.io (GeekNews: 자동 접속 차단 403, 재시도하지 않음. Show GN과 스킬 관련 글의 본문·댓글 미확인)
- https://solved.ac/class (403: CLASS 구성 미확인, 기억 기반 서술만 포함)
- https://wikidocs.net/book/13314, https://wikidocs.net/232031 (Cloudflare/403: 코딩 테스트 합격자 되기 무료 공개본과 공부법 절 본문 미확인, 목차는 Yes24로 대체)
- https://yozm.wishket.com/magazine/detail/2612 (405: 요즘IT '코딩 테스트를 준비하는 모두를 위한 조언' 미확인)
- https://coddy.tech/visualize/ko (403: 한국어 시각화 사이트 기능은 검색 요약으로만 확인)
- https://mygithub05253.github.io/Claude-Code-Study/skills/learn (404)
- OKKY, disquiet: 한국어 검색에서 관련 글이 나오지 않아 확인한 내용 없음
- velog·tistory의 개별 '그리디 증명이 어렵다', '출퇴근 공부법' 글: 검색 요약만 확인하고 본문은 읽지 않음
- virgiliojr94/book-to-skill의 SKILL.md: 저장소 파일 목록에서 위치를 찾지 못해 본문 미확인(PyTorch KR 소개 글만 읽음)
- cote-analysis 스킬의 원 GitHub 저장소와 작성자: 레지스트리 페이지에 출처 링크가 없어 미확인
- pubmed.ncbi.nlm.nih.gov: 쿠키 요구로 초록 본문을 직접 읽지 못함 (Cepeda 2008, Richland 2009, Cummings 2016은 검색 요약으로만 확인)
- link.springer.com: 인증 리다이렉트(303)로 Sweller 2010/2023, Rohrer 2014 본문을 읽지 못함
- core.ac.uk/download/519840252.pdf (Morrison, Margulieux & Guzdial 2015): PDF 대신 HTML이 반환됨
- appliedcognition.psych.utah.edu/publications/aaa_phase_i.pdf (Strayer 2013 원 보고서): 다운로드 실패. aaafoundation.org 요약 페이지로 대체
- psychology.ecu.edu의 Roediger & Karpicke PDF: HTML이 반환됨. gwern.net 미러로 원문 확인
- Driskell, Copper & Moran 1994 원문: 유료라 검색 요약과 2020년 추적 연구 초록으로 대체
- Kalyuga 2007, Renkl & Atkinson 2003, Lopez et al. 2008, Shindler et al. 2022, Boustedt et al. 2007, Kulik et al. 1990 원문: 가져오지 않았거나 접근하지 못해 검색 요약에 의존
- reddit.com: 지침에 따라 직접 접근을 시도하지 않음
- raw.githubusercontent.com/wiki/open-spaced-repetition/fsrs4anki/ABC-of-FSRS.md: 이전 안내만 반환됨. awesome-fsrs 위키에서 원문 확인
- Google Play 스토어 상세 페이지(Codecademy Go, Sololearn): JS 렌더링으로 본문이 잘려 App Store 페이지로 대체
- developer.apple.com HIG 접근성 HTML 페이지: 본문 미수신, 같은 문서의 데이터 JSON으로 대체
- m3.material.io 접근성 페이지: 본문 미수신, Android Accessibility Help로 대체
- pubmed.ncbi.nlm.nih.gov/16507066 (Roediger & Karpicke 초록): 쿠키 벽, 워싱턴대 보도자료로 대체
- web.dev/articles/page-lifecycle-api: 404, developer.chrome.com 판으로 대체
- ghacks.net의 Py 앱 리뷰: 403. Py 앱 App Store 페이지는 빈 응답이라 Py 앱의 현재 상태와 레슨 구조는 확인하지 못함

모두 110건 가운데 40건만 실었다. 전체는 [data/sweep/](data/sweep/) 각 파일의 `unreachable` 항목에 있다.
