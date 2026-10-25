# 본문 프레임(02~08) 그림: 「클로드 회의록 정리법」 예시 편
#
# 엔진이 이 파일을 읽어 HTML 로 조립한다. 여기서는 그림 내용만 쓴다.
#   (제목 줄은 없다. 말은 자막이 하고, 화면은 그림만으로 설명한다)
#   ART[f]     SVG 도형 (viewBox 1080 x CH)
#   JS[f]      등장 시점. 전부 cue(프레임, 단어번호) 로 쓴다. 초를 박지 않는다
#   DOTS[f]    스텝 진행 도트 · PROMPT[f] 그림 아래 다크 띠 · ALT[f] 그림 설명
#   움직임     pop(튀어나옴) · land(떨어져 납작) · rise(바닥에서 솟음) · slide(강조 상자가 옮겨 감)
#              tap(커서가 눌러 물결) · focus(카메라가 밀고 들어감): references/look.md §4
#
# 캔버스 높이 CH 는 배치에 따라 다르다: 아래 캐릭터 있음 700 · 없음 1000(화면을 거의 다 쓴다).
# 이 예시는 700 기준으로 잡은 좌표를 Y() 로 늘려 두 배치에서 다 쓴다. 새 편은 그 편 배치에 맞춰 바로 그려도 된다.
# 안전 영역: x 40~1040 · y 30~CH-40.
# 비유는 편 전체에 하나: 「세 칸」. 03 에서 빈 칸 셋을 세우고 04~08 이 그 칸을 채운다.

K = CH / 700            # 세로 늘림 배율 (700 → 1, 1000 → 1.43)


def Y(v):
    """700 기준 세로 좌표 · 높이를 이 배치의 캔버스에 맞춘다."""
    return int(round(v * K))


def F(s):
    """글자 크기. 화면을 다 쓰는 배치에서는 조금 키운다."""
    return int(round(s * (1.15 if FULL else 1)))


def memo(x, y, w, h, title, gid):
    """줄이 빼곡한 메모 한 장. 줄 수는 높이에 맞춘다."""
    n = int((h - 110) / 34)
    bars = "".join(card(x + 30, y + 86 + k * 34, int((w - 60) * (0.55 + 0.45 * ((k * 37) % 10) / 10)), 10,
                        stroke="none", fill=FAINT, r=5, sw=0) for k in range(n))
    return masked(gid, x, y, w, h, card(x, y, w, h, stroke=INK, sw=4) + T(x + 30, y + 56, title, GRAY, F(30), "800", a="start") + bars)


def slots(x, y, w, h, gap, labels, gid, filled=False):
    """세 칸. 줄마다 <g class="row"> 라서 land("#gid .row") 로 하나씩 떨어뜨린다. filled 면 강조색 테두리 + 체크."""
    out = ""
    for i, lab in enumerate(labels):
        yy = y + i * (h + gap)
        out += ('<g class="row">' + card(x, yy, w, h, stroke=ACC if filled else FAINT, sw=5 if filled else 4, dash=not filled)
                + T(x + 36, yy + h // 2 + 13, lab, INK if filled else GRAY, F(38), "800", a="start")
                + (check(x + w - 56, yy + h // 2, 0.9, ACC, 8) if filled else "") + "</g>")
    return '<g id="%s">%s</g>' % (gid, out)


# ── 02 · 메모를 통째로 넣고 요약만 시켰다 ───────────────────────────────────
ART[2] = (memo(100, Y(70), 330, Y(470), "회의 메모", "c2memo")
          + '<g id="c2arrow">' + arrow(462, Y(300), 590, Y(300)) + "</g>"
          + memo(630, Y(40), 350, Y(530), "긴 요약", "c2sum")
          + '<g id="c2tag">' + pill(805, Y(622), "또 읽어야 해요", fill=INK, s=F(34)) + "</g>")
JS[2] = f'''
  wipeY("c2memo", {cue(2, 2)}, {Y(70)}, {Y(470)}, 0.55);
  fade("#c2arrow", {cue(2, 4)});
  wipeY("c2sum", {cue(2, 5)}, {Y(40)}, {Y(530)}, 0.7);
  focus({cue(2, 5, 0.2)}, 760, {Y(330)}, 1.12);
  pop("#c2tag", {cue(2, 6, 0.1)}, 16);
'''
ALT[2] = "줄이 빼곡한 회의 메모가 화살표를 지나 더 긴 요약이 되고, 또 읽어야 한다는 표시가 붙는다"

# ── 03 · 용어는 버리고, 뽑을 칸부터 정한다 ──────────────────────────────────
ART[3] = ('<g id="c3t1">' + card(130, Y(44), 360, 84, r=18) + T(310, Y(44) + 56, "프롬프트 공식", GRAY, F(34), "700") + "</g>"
          + '<g id="c3t2">' + card(590, Y(44), 360, 84, r=18) + T(770, Y(44) + 56, "역할 부여", GRAY, F(34), "700") + "</g>"
          + '<g id="c3cut">' + '<line x1="160" y1="%d" x2="460" y2="%d" stroke="%s" stroke-width="6" stroke-linecap="round"/>' % (Y(44) + 42, Y(44) + 42, FAINT)
          + '<line x1="620" y1="%d" x2="920" y2="%d" stroke="%s" stroke-width="6" stroke-linecap="round"/></g>' % (Y(44) + 42, Y(44) + 42, FAINT)
          + slots(250, Y(180), 580, Y(110), Y(26), ["?", "?", "?"], "c3slots")
          + '<g id="c3lbl">' + T(540, Y(636), "뽑을 칸부터", ACC, F(54), "800") + "</g>")
JS[3] = f'''
  pop("#c3t1", {cue(3, 0)}, 14);
  pop("#c3t2", {cue(3, 1)}, 14);
  draw("#c3cut line", {cue(3, 2)}, 0.4);
  tl.to(q("#c3t1"), {{opacity:0.3, duration:0.4, ease:"power2.out"}}, {cue(3, 3)});
  tl.to(q("#c3t2"), {{opacity:0.3, duration:0.4, ease:"power2.out"}}, {cue(3, 3)});
  land("#c3slots .row", {cue(3, 5)});
  pop("#c3lbl", {cue(3, 7)}, 16);
'''
ALT[3] = "프롬프트 공식과 역할 부여라는 말이 지워지고, 물음표가 든 빈 칸 세 개가 선다"

# ── 04 · 정할 건 셋: 결정, 할 일, 질문 ─────────────────────────────────────
NAMES = [("결정", "정해진 것"), ("할 일", "누가 · 언제"), ("질문", "안 끝난 것")]
c4y, c4h = Y(120), Y(360)
cards4 = "".join(
    '<g id="c4n%d">' % i + card(92 + i * 306, c4y, 266, c4h, stroke=INK, sw=5)
    + T(225 + i * 306, c4y + Y(92), "0%d" % (i + 1), ACC, F(44), "800", fam="IBM Plex Mono")
    + T(225 + i * 306, c4y + c4h // 2 + 30, n, INK, F(64), "800")
    + T(225 + i * 306, c4y + c4h - Y(66), d, GRAY, F(32), "600") + "</g>"
    for i, (n, d) in enumerate(NAMES))
ART[4] = (hilite("c4hl", 76, c4y - 16, 298, c4h + 32, 30) + cards4
          + '<g id="c4tail">' + T(540, Y(600), "이 세 칸만 채우면 끝", GRAY, F(40), "700") + "</g>")
JS[4] = f'''
  land("#c4n0, #c4n1, #c4n2", {at(4, "세")});
  pop("#c4hl", {at(4, "결정")});
  slide("c4hl", {at(4, "할")}, 382, {c4y - 16}, 298, {c4h + 32});
  slide("c4hl", {at(4, "질문")}, 688, {c4y - 16}, 298, {c4h + 32});
  fade("#c4tail", {at(4, "질문", 0.3)});
'''
ALT[4] = "결정 · 할 일 · 질문 세 장의 카드가 떨어져 놓이고, 강조 상자가 말하는 카드로 옮겨 간다"

# ── 05 · ① 결정: 정해진 것만 한 줄씩 ───────────────────────────────────────
DOTS[5] = dots(3, 0)
PROMPT[5] = prompt("이렇게 시켰습니다", "회의에서 *정해진 것만* 한 줄씩 뽑아 줘")
DECIDED = ["출시일은 금요일", "디자인은 B안", "예산은 그대로"]
r5y, r5h, r5s = (190, 180, 235) if FULL else (140, 104, 128)   # 화면 전체 배치에선 줄을 크게
rows5 = "".join(
    '<g class="r5">' + card(150, r5y + i * r5s, 780, r5h, stroke=INK, sw=4, r=18)
    + T(270, r5y + i * r5s + r5h // 2 + 16, t, INK, F(42), "700", a="start") + "</g>"
    + '<g id="k5%d">' % i + check(214, r5y + i * r5s + r5h // 2, 0.8, ACC, 8) + "</g>"
    for i, t in enumerate(DECIDED))
ART[5] = (T(150, Y(100), "결정 · 예시", GRAY, F(30), "800", a="start") + rows5
          + '<g id="c5n">' + T(930, Y(100), "3줄", ACC, F(40), "800", a="end", fam="IBM Plex Mono") + "</g>")
JS[5] = f'''
  rise(".r5", {at(5, "정해진")});
  [0,1,2].forEach(function(i){{ pop("#k5"+i, {at(5, "정해진")}+i*0.12+0.34); }});
  pop("#c5n", {at(5, "줄씩")}, 14);
'''
ALT[5] = "체크 표시가 붙은 결정 세 줄이 차례로 놓인다. 예시 내용이다"

# ── 06 · ② 할 일: 누가, 언제까지, 무엇을 ───────────────────────────────────
DOTS[6] = dots(3, 1)
PROMPT[6] = prompt("이렇게 시켰습니다", "누가 · 언제까지 · 무엇을 *표로* 정리해 줘")
COLS = [("누가", 150), ("언제까지", 400), ("무엇을", 650)]
TODO = [("민지", "금요일", "시안 정리"), ("준호", "다음 주", "견적 받기"), ("나", "내일", "공지 쓰기")]
h6 = Y(120)                                   # 머리 글자 baseline
HW = [130, 192, 156]                          # 머리마다 강조 상자 폭
head6 = "".join('<g id="c6h%d">' % i + T(x + 20, h6, h, ACC, F(36), "800", a="start") + "</g>" for i, (h, x) in enumerate(COLS))
r6y, r6h, r6s = (214, 170, 225) if FULL else (150, 116, 136)
rows6 = '<g id="c6rows">' + "".join(
    '<g class="r6">' + card(130, r6y + i * r6s, 820, r6h, stroke=INK if i == 0 else FAINT, sw=4, r=18)
    + "".join(T(x + 20, r6y + i * r6s + r6h // 2 + 14, v, INK, F(38), "700", a="start") for (h, x), v in zip(COLS, row)) + "</g>"
    for i, row in enumerate(TODO)) + "</g>"
ART[6] = hilite("c6hl", COLS[0][1] - 4, h6 - 48, HW[0], 66, 33) + head6 + rows6
JS[6] = f'''
  pop("#c6h0, #c6h1, #c6h2", {at(6, "할")});
  tap("#c6h0", {at(6, "누가")}, {COLS[0][1] + 60}, {h6 - 8});
  pop("#c6hl", {at(6, "누가")});
  tap("#c6h1", {at(6, "언제까지")}, {COLS[1][1] + 80}, {h6 - 8});
  slide("c6hl", {at(6, "언제까지")}, {COLS[1][1] - 4}, {h6 - 48}, {HW[1]}, 66);
  tap("#c6h2", {at(6, "무엇을")}, {COLS[2][1] + 70}, {h6 - 8});
  slide("c6hl", {at(6, "무엇을")}, {COLS[2][1] - 4}, {h6 - 48}, {HW[2]}, 66);
  rise(".r6", {at(6, "표로")});
'''
ALT[6] = "누가 · 언제까지 · 무엇을 세 칸 머리 아래로 할 일 세 줄이 표로 채워진다. 예시 내용이다"

# ── 07 · ③ 질문: 결론 안 난 것만 따로 ──────────────────────────────────────
DOTS[7] = dots(3, 2)
PROMPT[7] = prompt("이렇게 시켰습니다", "결론 *안 난 것만* 따로 모아 줘")
QS = ["로고 색은?", "외주 줄까?", "일정 당길까?"]
q7y = Y(60)
bx, by, bw, bh = 150, Y(290), 780, Y(320)
qcards = "".join('<g id="c7q%d">' % i + card(110 + i * 300, q7y, 260, 120, stroke=INK, sw=4, r=60)
                 + T(240 + i * 300, q7y + 74, q, INK, F(36), "800") + "</g>" for i, q in enumerate(QS))
ART[7] = (masked("c7box", bx, by, bw, bh,
                 card(bx, by, bw, bh, stroke=ACC, sw=6) + T(540, by + 82, "다음 회의에서 이어 갈 것", ACC, F(44), "800"))
          + '<g id="c7down">' + arrow(540, q7y + 136, 540, by - 20) + "</g>"
          + qcards)
drop7 = (by + bh * 0.66) - (q7y + 60)          # 카드 가운데를 상자 아래쪽 2/3 지점으로
JS[7] = f'''
  pop("#c7q0", {at(7, "결론이")}, 16);
  pop("#c7q1", {at(7, "결론이", 0.2)}, 16);
  pop("#c7q2", {at(7, "결론이", 0.4)}, 16);
  wipeY("c7box", {at(7, "따로")}, {by}, {bh}, 0.5);
  fade("#c7down", {at(7, "따로")});
  [0,1,2].forEach(function(i){{
    tl.to(q("#c7q"+i), {{x:(1-i)*90, y:{drop7:.0f}, scale:0.78, transformOrigin:"50% 50%", duration:0.7, ease:sp(12,7,0.7)}}, {at(7, "모읍니다")}+i*0.08);
  }});
'''
ALT[7] = "결론이 안 난 질문 카드 셋이 아래 '다음 회의' 상자로 모인다. 예시 내용이다"

# ── 08 · 긴 요약 대신 세 칸 ─────────────────────────────────────────────────
ART[8] = (memo(90, Y(50), 330, Y(520), "긴 요약", "c8sum")
          + '<g id="c8x">' + cross(255, Y(310), 70, RED, 12) + "</g>"
          + '<g id="c8arrow">' + arrow(450, Y(310), 560, Y(310)) + "</g>"
          + slots(590, Y(80), 400, Y(130), Y(30), ["결정", "할 일", "질문"], "c8slots", filled=True)
          + '<g id="c8lbl">' + T(790, Y(636), "다음 회의에 바로", INK, F(40), "800") + "</g>")
JS[8] = f'''
  wipeY("c8sum", {at(8, "긴")}, {Y(50)}, {Y(520)}, 0.5);
  pop("#c8x", {at(8, "대신")}, 12);
  fade("#c8arrow", {at(8, "다음")});
  land("#c8slots .row", {at(8, "세")});
  pop("#c8lbl", {at(8, "칸이")}, 12);
'''
ALT[8] = "긴 요약에 가위표가 그어지고, 결정 · 할 일 · 질문 세 칸이 체크와 함께 채워진다"
