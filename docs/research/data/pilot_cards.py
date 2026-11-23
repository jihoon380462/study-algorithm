"""Pilot replay cards: card code is exec'd as-is; traces come from instrumented twins that are
asserted to agree with the card code. Nothing in the output is typed by hand."""
import json, sys, itertools

CODE_SEL = '''def selection_sort(a):
    n = len(a)
    for i in range(n - 1):
        m = i
        for j in range(i + 1, n):
            if a[j] < a[m]:
                m = j
        a[i], a[m] = a[m], a[i]
    return a
'''

CODE_BS = '''def bsearch(a, t):
    lo, hi = 0, len(a)
    while lo < hi:
        mid = (lo + hi) // 2
        if a[mid] == t:
            return mid
        if a[mid] < t:
            lo = mid + 1
        else:
            hi = mid
    return -1
'''

CODE_BR = '''PAIR = {")": "(", "]": "[", "}": "{"}

def balanced(s):
    st = []
    for ch in s:
        if ch in "([{":
            st.append(ch)
        elif not st:
            return False
        elif st.pop() != PAIR[ch]:
            return False
    return not st
'''

ns = {}
for src in (CODE_SEL, CODE_BS, CODE_BR):
    exec(src, ns)
selection_sort, bsearch, balanced = ns['selection_sort'], ns['bsearch'], ns['balanced']

def lint(src):
    lines = [l for l in src.split('\n') if l.strip()]
    return {'lines': len(lines), 'maxWidth': max(len(l) for l in src.split('\n')),
            'indentOk': all((len(l) - len(l.lstrip(' '))) % 4 == 0 for l in lines)}

# ---------- selection sort (instrumented twin) ----------
def sel_trace(a):
    a = a[:]; orig = sorted(a); n = len(a); rows = []; comps = swaps = 0
    for i in range(n - 1):
        m = i
        for j in range(i + 1, n):
            comps += 1
            lt = a[j] < a[m]
            rows.append({'kind': '비교', 'i': i, 'j': j, 'm': m, 'what': f'a[{j}]={a[j]} < a[{m}]={a[m]} ?',
                         'result': '예 → m=' + str(j) if lt else '아니오', 'a': a[:]})
            if lt:
                m = j
        a[i], a[m] = a[m], a[i]; swaps += 1
        rows.append({'kind': '교환', 'i': i, 'j': '', 'm': m, 'what': f'a[{i}] ↔ a[{m}]', 'result': '', 'a': a[:]})
        assert a[:i + 1] == orig[:i + 1], 'invariant broken'   # after round i+1 the first i+1 cells are final
    return a, rows, comps, swaps

# ---------- binary search (instrumented twin) ----------
def bs_trace(a, t):
    lo, hi = 0, len(a); rows = []
    while lo < hi:
        if t in a:
            assert lo <= a.index(t) < hi, 'invariant broken'
        mid = (lo + hi) // 2
        row = {'lo': lo, 'hi': hi, 'mid': mid, 'amid': a[mid]}
        if a[mid] == t:
            row['result'] = f'{a[mid]} == {t} → 찾음, {mid} 반환'; rows.append(row); return mid, rows
        if a[mid] < t:
            row['result'] = f'{a[mid]} < {t} → lo = {mid + 1}'; lo = mid + 1
        else:
            row['result'] = f'{a[mid]} > {t} → hi = {mid}'; hi = mid
        rows.append(row)
    return -1, rows

def bs_buggy(a, t):   # variation: hi = mid - 1 with a half-open interval
    lo, hi = 0, len(a)
    while lo < hi:
        mid = (lo + hi) // 2
        if a[mid] == t:
            return mid
        if a[mid] < t:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1

# ---------- brackets (instrumented twin) ----------
PAIR = ns['PAIR']
def br_trace(s):
    st = []; rows = []; depth = 0
    for k, ch in enumerate(s):
        if ch in '([{':
            st.append(ch); rows.append({'k': k, 'ch': ch, 'action': 'push', 'st': ''.join(st)})
        elif not st:
            rows.append({'k': k, 'ch': ch, 'action': '스택이 비어 있음 → False', 'st': ''}); return False, rows, depth
        else:
            top = st.pop()
            if top != PAIR[ch]:
                rows.append({'k': k, 'ch': ch, 'action': f'pop {top} ≠ {PAIR[ch]} → False', 'st': ''.join(st)}); return False, rows, depth
            rows.append({'k': k, 'ch': ch, 'action': f'pop {top} (짝 맞음)', 'st': ''.join(st)})
        depth = max(depth, len(st))
        assert all(c in '([{' for c in st)
    return (not st), rows, depth

out = {'python': sys.version.split()[0], 'lint': {'selection_sort': lint(CODE_SEL), 'bsearch': lint(CODE_BS), 'balanced': lint(CODE_BR)}}

# selection sort facts
A = [3, 1, 4, 2]
res, rows, comps, swaps = sel_trace(A)
assert res == selection_sort(A[:]) == sorted(A)
rounds = [r['a'] for r in rows if r['kind'] == '교환']
r2, rows2, c2, s2 = sel_trace([1, 2, 3, 4])
r5, rows5, c5, s5 = sel_trace([5, 2, 4, 1, 3])
out['sel'] = {'input': A, 'rows': rows, 'comparisons': comps, 'swaps': swaps, 'result': res, 'afterEachRound': rounds,
              'sortedInput': {'input': [1, 2, 3, 4], 'comparisons': c2, 'swaps': s2, 'result': r2},
              'n5': {'input': [5, 2, 4, 1, 3], 'comparisons': c5, 'swaps': s5, 'events': c5 + s5},
              'formula_n4': 4 * 3 // 2}
assert comps == 4 * 3 // 2

# binary search facts
B = [1, 3, 5, 7, 9]
idx, brow = bs_trace(B, 7); assert idx == bsearch(B, 7) == B.index(7)
idx4, brow4 = bs_trace(B, 4); assert idx4 == bsearch(B, 4) == -1
worst = 0
for t in range(0, 11):
    i_, r_ = bs_trace(B, t); assert i_ == bsearch(B, t) == (B.index(t) if t in B else -1)
    worst = max(worst, len(r_))
out['bs'] = {'input': B, 't7': {'rows': brow, 'returns': idx, 'mids': [r['mid'] for r in brow]},
             't4': {'rows': brow4, 'returns': idx4, 'mids': [r['mid'] for r in brow4]},
             'worstLooks_n5': worst,
             'buggy_t3': bs_buggy(B, 3), 'correct_t3': bsearch(B, 3)}

# bracket facts
S = '([]{})'
ok, srow, depth = br_trace(S); assert ok == balanced(S) is True
ok2, srow2, d2 = br_trace('([)]'); assert ok2 == balanced('([)]') is False
ok3, srow3, d3 = br_trace('(()'); assert ok3 == balanced('(()') is False
ok4, srow4, d4 = br_trace('{[()]}'); assert ok4 == balanced('{[()]}') is True
ok5, srow5, d5 = br_trace('())'); assert ok5 == balanced('())') is False
for n in range(0, 7):   # exhaustive agreement check on short strings
    for tup in itertools.product('()[]', repeat=n):
        s = ''.join(tup); assert br_trace(s)[0] == balanced(s)
out['br'] = {'input': S, 'rows': srow, 'result': ok, 'maxDepth': depth,
             'crossed': {'input': '([)]', 'rows': srow2, 'result': ok2},
             'unclosed': {'input': '(()', 'result': ok3, 'leftOnStack': srow3[-1]['st']},
             'nested': {'input': '{[()]}', 'result': ok4, 'maxDepth': d4},
             'extraClose': {'input': '())', 'rows': srow5, 'result': ok5}}
out['code'] = {'selection_sort': CODE_SEL, 'bsearch': CODE_BS, 'balanced': CODE_BR}
json.dump(out, open('cards.json', 'w'), ensure_ascii=False, indent=1)
print(json.dumps({k: out[k] for k in ('python', 'lint')}, ensure_ascii=False))
print('SEL', comps, swaps, res, rounds, '| sorted input:', c2, s2, '| n5 events:', c5 + s5)
for r in rows: print('  ', r['kind'], r['i'], r['j'], r['m'], r['what'], r['result'], r['a'])
print('BS t=7', idx, [(r['lo'], r['hi'], r['mid'], r['amid'], r['result']) for r in brow])
print('BS t=4', idx4, [(r['lo'], r['hi'], r['mid'], r['amid'], r['result']) for r in brow4], 'worst', worst, 'buggy t=3 →', bs_buggy(B, 3))
print('BR', ok, depth, [(r['k'], r['ch'], r['action'], r['st']) for r in srow])
print('BR ([)]', ok2, [(r['k'], r['ch'], r['action'], r['st']) for r in srow2], '| (() left:', srow3[-1]['st'], '| {[()]} depth', d4, '| ()) ', [(r['k'], r['action']) for r in srow5])
