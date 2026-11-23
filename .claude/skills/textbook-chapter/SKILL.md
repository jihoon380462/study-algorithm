---
name: textbook-chapter
description: Python 알고리즘·자료구조 교과서의 장 하나를 만든다. 폰으로 읽는 교과서 형태(버튼 없이 위에서 아래로 읽는 글, 그림, 코드)로 쓴다. 새 장을 쓰거나 기존 장을 고칠 때 사용한다.
---

# 교과서 장 만들기

괄호 안은 그 항목을 가져온 스킬이다. 수집한 36개 중 교과서 형태에 맞는 것만 골랐다.

## 고정 조건(사용자 지정)

- Python 코드가 중심인 알고리즘·자료구조 **교과서**. 버튼·애니메이션·입력 칸 없이 읽기만 한다.
- 읽는 사람은 한 명, Android 폰.
- 장 사이 난이도가 급하게 오르지 않는다.

## 장의 구성

모든 장이 같은 순서를 따른다. (teach-me, cote-analysis, book-chapter-generator)

1. **질문**: 이 장이 답할 질문 한 줄로 시작한다. (talk-to-me-in-html, cote-analysis)
2. **비유와 큰 그림**: 일상의 비유로 먼저 설명하고, 정식 용어는 그 뒤에 붙인다. 비유가 어디서 안 맞는지도 한 줄 적는다. (talk-to-me-in-html, pdf-to-interactive-web, codebase-to-course)
3. **코드**: Python 함수 하나.
4. **실행 과정**: 그림을 번호 붙여 펼친다. 그림마다 세 가지를 적는다: 지금 상태, 방금 한 일, 눈여겨볼 점 한 문장. (worked-example-walkthrough, visual-explainer)
5. **함정**: 흔한 착각이나 경계 사례 하나. (talk-to-me-in-html, learn-with-claude, tutor)
6. **정리 카드**: 외울 문장 하나와 복잡도 한 줄. 본문을 다시 읽지 않고 이것만 봐도 되게 쓴다. (teach, teach-me, algo-sensei)
7. **확인 문제**: 두 개. 하나는 이 장, 하나는 앞 장에서 낸다. 문제 문장만 읽고는 답할 수 없어야 한다. (teach-me, retrieval-practice-generator)

## 규칙

1. **한 장에 개념 하나.** 개념이 둘이면 장도 둘이다. 앞 장에서 소개하지 않은 개념이 나오면 실패다. (teach-me, codebase-to-course, explainer-book, book-chapter-generator)
2. **가장 작은 예제로, 중간 상태를 빼지 않는다.** 그림이 7장을 넘으면 입력을 줄이거나 장을 나눈다. (worked-example-walkthrough, worked-example-fading-designer, algo-sensei)
3. **실제로 실행한 결과만 싣는다.** 그럴듯하게 틀린 그림은 밋밋하게 맞는 글보다 나쁘다. 확신이 없으면 돌려 보고 쓴다. (talk-to-me-in-html, teach-me, pypeep)
4. **"짧게" 대신 숫자로 정한다.** 문단은 세 문장 이하, 코드는 15줄·한 줄 36자 이하. (pdf-to-interactive-web, drill-me, talk-to-me-in-html)
5. **폰 폭 380px이 기준이다.** 가로 스크롤 없음, 본문 17px 이상, 그림과 글을 두 열로 놓지 않고 세로로 쌓는다. (talk-to-me-in-html, pdf-to-interactive-web, explainer-book)
6. **한 개념에 이름 하나.** 용어집에 올린 이름을 모든 장에서 그대로 쓴다. 색으로만 구분하지 않고 모양이나 글자를 함께 쓴다. (teach, teach-me, visual-explainer)
7. **목차를 먼저 보여 주고 승인받는다. 한 번에 한 장만 만들고 확인한 뒤 다음으로 간다.** (book-chapter-generator, learn-with-claude, codebase-to-course)

## 끝내기 전에

(pdf-to-interactive-web, talk-to-me-in-html, codebase-to-course의 점검 방식)

- 코드를 실행해 그림의 값, 정리 카드의 숫자, 확인 문제의 정답과 맞췄는가.
- 380px 화면에서 가로로 넘치는 곳이 없는가.
- 이 장에서 처음 나온 개념이 하나뿐이고, 용어가 용어집과 같은가.
