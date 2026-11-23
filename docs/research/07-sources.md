# 07. 출처와 검증 상태

조사일 2026-11-23. 1차 조사에서 나온 주장 가운데 계획을 좌우하는 것을 골라, 1차 자료(공식 문서, 저장소 원문, 레지스트리, 논문)를 다시 받아 반증을 시도했다.

## 1. 검증 결과 요약

| 판정 | 건수 | 뜻 |
|---|---|---|
| 확인 | 10 | 1차 자료가 숫자·날짜·이름까지 뒷받침 |
| 부분 확인 | 4 | 핵심은 맞지만 고칠 부분이 있음 |
| 반증 | 0 | 1차 자료와 어긋남 |
| 확인 불가 | 0 | 1차 자료에 닿지 못함 |

표시가 "확인"이어도 그날 읽은 자료 기준이다. 버전과 서비스 상태는 바뀐다.

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
- arXiv 2203.16175 본문: 초록만 확인
- arXiv 2305.08346: 앞부분(초록과 서론)만 텍스트로 확인
- PMC11774797: 앞 10만 자만 확인(부록 일부 미확인)
- Brilliant의 레슨당 단계 수·소요 시간에 대한 공식 자료: 찾지 못함
- Duolingo 도움말의 레슨 길이·오프라인 정책: 찾지 못함
- Mimo의 레슨 설계 블로그: 찾지 못함
- LeetCode 모바일 경험: 검색 스니펫만 확보
- reddit.com: 지침에 따라 직접 접근하지 않음
- Brilliant 오프라인 도움말, Khan Academy 오프라인 도움말: 원문을 직접 열지 않고 검색 결과 요약으로 확인
- github.com 저장소 HTML 페이지 전반 (프록시 403: anthropics/skills, molechowski/claude-skills, molechowski/agent-skills에서 확인) : 파일 목록은 data.jsdelivr.com으로 대체
- api.github.com (과제 안내상 차단, 시도하지 않음) 및 GitHub MCP 도구(세션 허용 저장소 외 접근 거부)
- raw.githubusercontent.com/molechowski/claude-skills 및 molechowski/agent-skills 의 edu-visual-trace/SKILL.md (main/master/HEAD와 여러 경로 모두 404, jsdelivr 목록도 없음) : 본문은 skills.sh 페이지 payload에서 추출
- a5c-ai/babysitter 저장소의 algorithm-visualizer 원본 경로 (jsdelivr 목록 미제공, 추정 경로 404) : claudskills.com 미러본으로 대체
- sayed-moin-ahmed/DSA-CLAUDE-CODEX-GEMINI-SKILL (jsdelivr 목록 없음, tessl 등록 페이지는 검색 스니펫만 확인)
- raw.githubusercontent.com/dmccreary/claude-skills/main/skills/microsim-layout-reviewer/SKILL.md (jsdelivr 목록에는 있으나 raw 404)
- claudskills.com 의 edu-visual-trace, explorable-explanation, interactive-explainer, html-explainer, explanatory-playground, creating-explainers, visual-learner, microsim-p5, 3b1b-style-animation, dsa-pattern-practice, python-tutor, code-tracer, data-structures-
- petekp/claude-code-setup 의 explanatory-playground (저장소 목록에 없음), hoangnb24/skills 의 visual-learner (저장소 목록에 없음)
- reddit.com (과제 안내상 차단, 시도하지 않음)
- skillsmp.com : 직접 요청 시 403, 검색 스니펫으로만 확인
- claudepluginhub.com : 403
- smithery.ai/skills?q=... : 404 (skills.sh의 smithery 미러 스니펫으로만 확인: math-teacher, coding-tutor, memgrafter-socratic-teacher)
- claudskills.com 검색 : 가입 후에만 검색 가능, 홈 화면만 확인
- tessl.io/registry : 클라이언트 렌더링이라 검색어가 서버 응답에 반영되지 않음. 검색 스니펫으로만 확인(luongnv89 lesson-quiz, neomatrix369 learning-opportunity, tech-leads-club learning-opportunities)
- github.com HTML 트리 페이지와 api.github.com : 403 또는 빈 응답. jsDelivr 파일 목록과 raw.githubusercontent로 대체
- everyinc/compound-engineering-plugin의 coding-tutor : skills.sh에는 등재되어 있으나 현재 저장소 목록에 해당 경로 없음
- molechowski/agent-skills의 edu-visual-trace : jsDelivr 목록이 비어 있어 본문 미확인
- f-labs-io/html-skills의 html-interactive-playground : 목록 조회 실패
- szeyu/vibe-study-skills의 flashcard-creator, quiz-creator : 저장소 목록에 없음(obsidian-notes-creator만 확인)
- nityeshaga/claude-code-essentials coding-tutor, ingpoc/skills scroll-storyteller, lvtd-llc/skills technical-book-lab-design : raw 404
- mcpmarket.com의 Algorithm Visualizer 스킬 : 검색 스니펫만 확인, 본문 미확인
- hluaguo/learn-faster-kit, ljx-chase/research-field-onboarding, YujxZJCN/teaching-skills : SKILL.md 경로를 찾지 못함
- mattpocock/skills의 scaffold-exercises : 저장소가 재구성되어 skills/misc/scaffold-exercises에 있는 것만 목록으로 확인, 본문 미열람
- Reddit : 지시에 따라 직접 접근하지 않음
- api.github.com (지침상 차단, 시도하지 않음)
- https://data.jsdelivr.com/v1/packages/gh/krahets/hello-algo@main (403, 패키지 50MB 초과)
- https://github.com/krahets/hello-algo/tree/main/docs/utils (403). Hello Algo의 src 자리표시자를 펼치는 빌드 스크립트 위치를 확인하지 못함(추정 경로 3곳 404)
- https://github.com/micropython/micropython/tree/master/ports/webassembly/variants (403). 변형별 설정 파일을 읽지 못함
- VisuAlgo 내부 구현(상태 리스트, 애니메이션 컨트롤러)의 1차 자료를 찾지 못함
- 모바일 기기에서의 Pyodide·MicroPython 시작 시간과 메모리 실측 벤치마크를 찾지 못함
- Quarto(quarto-live), mdBook, SvelteKit/Next 정적 내보내기, Netlify/Vercel 한도는 이번 예산에서 1차 자료를 확인하지 못함
- Manim, manim-slides, Lottie의 사전 렌더 방식은 1차 자료를 확인하지 못함(일반 지식으로만 서술)
- reddit.com, hello-algo.com (지침상 직접 접근하지 않음)
- https://www.hello-algo.com (지침에 따라 직접 접근하지 않고 GitHub raw로 대체)
- https://runestone.academy/ns/books/published/pythonds3/index.html (Cloudflare 'Just a moment' 차단, GitHub RunestoneInteractive/pythonds RST 원본으로 대체)
- https://www.manning.com/books/grokking-algorithms-second-edition 의 목차 영역(정적 HTML에 없음, 2판 목차는 서점 목록 검색 요약에 의존)
- https://www.oreilly.com/library/view/grokking-algorithms/9781617292231/OEBPS/Text/kindle_split_002.html (290바이트만 반환)
- https://www.redblobgames.com/making-of/a-star/ (404, making-of/line-drawing 으로 대체)
- https://roadmap.sh/datastructures-and-algorithms 의 로드맵 노드 내용(JS 렌더링, GitHub 경로도 404)
- github.com 의 tree HTML 목록(378바이트만 반환되어 디렉터리 나열 불가)
- 알고리즘 도감 한국어판(제이펍) 목차(검색 결과 없음, 쇼에이샤 일본어 증보개정판 목차로 대체)
- Brilliant 수업 내부 화면(로그인 필요)
- Naps 2002, Hundhausen 2002 논문 원문(서지 정보와 초록 수준만 확인)
- CS50 shorts 영상 내용(목록만 확인)
- samwho.dev, ciechanow.ski, joshwcomeau.com, worrydream.com, ncase.me, brilliant.org, educative.io 는 원시 HTML이 아니라 WebFetch 요약 모델을 거쳐 읽음
- csacademy.com (lesson, graph_editor): JS로만 렌더링되어 제목만 반환. HN 댓글에서 존재만 확인
- neetcode.io/roadmap: SPA라 제목과 meta 설명만 확인
- algorithm-visualizer.org 본문: SPA라 제목만 반환(GitHub README와 저장소 파일 목록으로 대체)
- csvistool.com 본문: SPA라 제목만 반환(GitHub 저장소로 대체)
- opendsa-server.cs.vt.edu 개별 모듈 페이지(InsertionSort): 시도한 주소 404
- programiz.com/dsa/visualizer: 404
- animations.algomaster.io: 503
- support.leetcode.com (How to use Explore): 403
- mintlify.com/ds-visualizer: 페이지 삭제됨
- onenoughtone.com/visualizers: 목록이 로딩 상태로만 반환
- algo.monster/flowchart의 결정 노드 내용: JS 로딩이라 읽지 못함
- Byrne/Catrambone/Stasko 1999 논문 PDF(courses.cs.washington.edu): PDF 대신 HTML이 반환되어 원문 미확인
- Naps 외 2002 engagement taxonomy 원문: 서지 정보만 확인, 단계 목록은 원문으로 검증하지 못함
- hello-algo.com 웹판과 reddit.com: 지침에 따라 직접 접근하지 않음(Hello Algo는 GitHub 원본으로 확인, Reddit 의견은 수집하지 못함)
- TraceLit, NeurAL-Viz, DebugaBull: 검색 요약만 확인
- 모든 사이트의 실제 휴대폰 세로 화면 동작: 테스트 수단 없음
