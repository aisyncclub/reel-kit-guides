# 표에 없는 움직임: Motion Prompt 카탈로그에서 찾아 옮기기

`look.md` 「장면에 맞는 움직임 고르기」 표로 안 되는 장면만 여기로 온다.
Motion Prompt(https://showheyohtaki.github.io/motion-prompt/)는 움직임 144가지에 번호(#001~)를 붙인 공개 목록이다. MIT 라이선스라 값을 옮겨 써도 된다. **설치는 필요 없다.** 아래 주소를 `curl` 로 읽는다.

## 1. 찾기

```bash
curl -s https://showheyohtaki.github.io/motion-prompt/api/v1/en/catalog.tsv | grep -i "flip\|card"
```

- 한 줄이 움직임 하나: `번호 · 묶음 · 분류 · 이름 · 태그 · 한 줄 설명`. 영어로 찾는다(flip · typewriter · morph · reveal · count …)
- 영상에 쓸 것은 묶음이 `motion`(그림 · 글자 움직임) · `ui`(버튼 · 탭 · 목록 같은 화면 부품)인 것. `photo` 는 사진 느낌이라 쓰지 않는다
- 장면 하나에 후보 두세 개를 보고, 설명이 **대사가 하는 말**과 가장 가까운 것 하나를 고른다

## 2. 읽기

```bash
curl -s https://showheyohtaki.github.io/motion-prompt/api/v1/en/e/021.txt
```

맨 위 `Motion spec:` 에 길이 · 늦춤 · 이징 · 넘침 · 거리 · 각도가 숫자로 있다. 아래 코드는 캔버스용이라 그대로 붙이지 않는다.

## 3. 옮기기 (frames.py 의 JS[f])

- **숫자는 그대로 둔다.** 길이 · 이징 · 넘침이 그 움직임의 맛이다. 바꾸는 것은 글 · 색 · 위치뿐이다
- 스프링 `1 − e^(−d·t)·cos(w·t)` 는 `ease:sp(w, d, 길이)` 로 그대로 쓴다. `backOut(s)` 는 `"back.out(s)"`, `easeInOutCubic` 은 `"power3.inOut"`
- 시점은 초가 아니라 `at(f, "단어")` 다. 카탈로그의 0.28초 같은 시작 늦춤은 `at(f, "단어", 0.28)` 처럼 더한다
- 반복(`cycle`)은 한 번만 쓴다. 영상 안에서 되풀이하지 않는다
- 옮긴 줄 바로 위에 출처 주석을 단다. 대시보드가 이 주석으로 번호를 보여 준다:

예: #024 쿵 떨어지기(Impact shake): 숫자가 위에서 떨어지고 닿는 순간 그림 전체가 1.1초 흔들린다.

```python
JS[5] = f'''
  // Motion Prompt #024 · MIT License (c) 2026 Shohei Ohtaki · https://showheyohtaki.github.io/motion-prompt/#024
  tl.fromTo(q("#c5n"), {{y:-700, scaleY:1.12, transformOrigin:"50% 100%"}}, {{y:0, scaleY:1, duration:0.32, ease:"power3.in"}}, {at(5, "줄씩")});
  var sk={{t:0}};
  tl.fromTo(sk, {{t:0}}, {{t:1.1, duration:1.1, ease:"none", onUpdate:function(){{
    var e=Math.exp(-5*sk.t), w=2*Math.PI*sk.t;
    q(".art svg").style.transform = sk.t<=0 ? "" : "translate("+(15*e*Math.sin(5*w))+"px,"+(11*e*Math.cos(6.5*w))+"px) rotate("+(0.02*e*Math.sin(5*w+0.6))+"rad)";
  }}}}, {at(5, "줄씩", 0.32)});
'''
```

- `build` → `check` 를 돌리고 스틸에서 그 순간을 눈으로 본다
- **같은 동작을 두 편 넘게 쓰면** 엔진 함수로 올릴 만하다. 사용자에게 알린다(엔진은 사용자가 고치는 곳이 아니다)

## 4. 사용자가 직접 고르고 싶다고 하면

갤러리 주소를 준다: https://showheyohtaki.github.io/motion-prompt/
마음에 드는 것에서 「選ぶ / Pick」을 누르고 「選んだ物をコピー / Copy picks」로 복사해 대화에 붙여 넣으면 된다고 알린다.
붙여 넣은 번호는 **그대로** 쓴다(빼거나 바꾸지 않는다). 장면에 안 맞으면 그렇다고 말하고 묻는다.

## 5. 못 읽을 때

인터넷이 안 되면 카탈로그를 쓰지 않고 `look.md` 표 안에서 가장 가까운 것으로 만든다. 번호나 값을 기억으로 지어내지 않는다.
