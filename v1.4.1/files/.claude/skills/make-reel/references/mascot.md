# 마스코트 만들기: 내 캐릭터 그림을 뽑아서 키트에 넣기

릴스 첫 화면과 마지막 화면에 서는 캐릭터 그림을 만드는 지침이다. 다 해 본 예시는 `examples/mascot-syncbear/`(싱크곰).
**그림은 사용자가 쓰는 이미지 생성 도구로 뽑는다.** Claude 는 사용자의 설명으로 문장(프롬프트)을 써 주고, 받은 그림을 확인해서 키트에 넣는다.

```
캐릭터 정하기 → 기준 그림 1장 → 포즈 2장(첫 화면 · 마지막 화면) → 확인 · 고치기 → reel.py mascot → build · snapshot
```

---

## 1. 필요한 그림은 두 장이다 (아래 캐릭터를 켜면 세 장)

| 자리 | 화면에서 | 포즈 | 싱크곰 예시 |
|---|---|---|---|
| `hook` 첫 화면 | 훅 카드 아래에 크게 선다. 화면 아래쪽 선(y 1594)에서 잘려 **머리부터 가슴까지** 보인다 | 놀람 · 반응 (두 손으로 볼을 감싼다, 입을 동그랗게) | `2-hook.webp` |
| `cta` 마지막 화면 | "댓글에 ○○" 알약 아래, 마감 문구 옆에 선다. **위쪽 60%만** 보인다 | 위를 가리킨다 (한 손 검지를 위로, 알약을 가리키는 손짓) | `3-cta.webp` |
| `body` 본문 아래 (`mascot.bottom: true` 일 때) | 본문 화면마다 자막 아래(y 1250)에서 시작해 화면 아래 끝까지 선다. 자막을 가리지 않는다. 다리 쪽은 잘리고 말하는 단어마다 살짝 들썩인다 | 정면 · 손 흔들기나 설명하는 손짓, 입은 다물거나 살짝 웃기 | `1-reference.webp` |

전신 그림을 넣어도 된다. 엔진이 위쪽만 보이게 자른다. 대신 **얼굴과 손짓이 그림 위쪽 절반 안에** 있어야 한다.

## 2. 규격

| 항목 | 값 |
|---|---|
| 모양 | 세로로 긴 그림(대략 2:3), 캐릭터 하나, 정면이나 살짝 비스듬히 |
| 크기 | 가로 1000px 이상 |
| 배경 | **투명 PNG 가 가장 좋다.** 안 되면 **초록 단색(#00FF00)**. 엔진이 지운다 |
| 하지 않는 것 | 흰 배경(눈 흰자 · 흰 옷이 같이 빠진다, `4-green-vs-white.webp`), 그림자 · 바닥 · 배경 소품, 글자(캐릭터 옷의 로고는 괜찮다) |

- 캐릭터 몸에 초록색이 있으면 초록 배경 대신 **파란 단색(#0000FF)** 배경을 쓴다. 배경색과 같은 색은 같이 빠진다
- 투명 배경 옵션이 있는 도구면 그걸 켜고, 아래 문장의 배경 지시는 뺀다

---

## 3. 캐릭터 고정 문장: 모든 문장 맨 앞에 그대로 넣는다

캐릭터가 그림마다 달라지지 않게 하는 핵심이다. 사용자에게 아래 다섯 칸을 묻고 영어로 채운다(이미지 도구는 영어 문장을 더 잘 따른다).

```
The character from the reference image, kept exactly the same:
[생김새] a chubby brown bear with a big round head and small round ears, small solid black dot eyes,
[옷 · 소품] a navy baseball cap with "ABC" written on the front, round gold wire glasses, an oversized navy hoodie,
[그림 결] flat 2D illustration with clean dark outlines and soft cel shading,
[얼굴 규칙] a small symmetrical smile centered under the nose, no blush on the cheeks.
```

| 칸 | 묻는 것 | 쓰는 법 |
|---|---|---|
| 생김새 | 무슨 동물 · 사람 · 사물? 몸 비율(2등신 등) · 색 · **눈 모양** | 색은 이름으로 정확히(navy · cream · mint). 눈은 꼭 적는다(`small solid black dot eyes` 처럼). 안 적으면 포즈마다 흰자가 생기거나 눈 모양이 바뀐다 |
| 옷 · 소품 | 늘 하고 있는 것 2~4개 | 글자가 있으면 철자를 따옴표로 |
| 그림 결 | 2D 선화 · 3D 클레이 · 수채화 · 픽셀 중 무엇 | 한 결로 고정. 편마다 바꾸지 않는다 |
| 얼굴 규칙 | 꼭 지킬 표정 규칙 | 찡그림은 넣지 않는다(작은 화면에서 화난 얼굴로 보인다) |
| 금지 | 빼고 싶은 것 | 맨 끝에 `no …` 로 |

**표정이 바뀌는 포즈(놀람 등)에서는 [얼굴 규칙] 줄을 빼고** 포즈 문장의 표정을 따른다. 나머지 줄은 그대로 둔다.

첫 그림(기준 그림)을 뽑을 때는 아직 참조할 그림이 없으니 첫 줄 `The character from the reference image, kept exactly the same:` 을 빼고 설명만 넣는다.

## 4. 기준 그림 1장

```
{고정 문장}
Full-body front view, standing, arms relaxed at the sides, friendly neutral expression.
Single character only, centered, filling the frame from head to feet with a small margin.
Plain solid pure green background (#00FF00), no shadow, no floor, no other objects.
No text anywhere except the logo on the clothes.
```

**마음에 들 때까지 여기서 고른다.** 이 한 장이 앞으로 모든 그림의 기준이다. 얼굴 · 옷 · 결이 전부 이 그림에서 나온다. 고른 그림은 `brand/mascot/reference.png` 로 저장해 둔다.

## 5. 포즈 두 장: 기준 그림을 참조 이미지로 같이 넣는다

참조 이미지 칸이 있는 도구면 거기에, 없으면 대화창에 기준 그림을 첨부하고 아래 문장을 보낸다.

**첫 화면 (`hook`)**
```
{고정 문장}
Same character, surprised reaction: eyes wide open, mouth open in a small round "o", both hands pressed against the cheeks.
Front view. Face and hands in the upper half of the image.
Single character only, centered, filling the frame from head to feet with a small margin.
Plain solid pure green background (#00FF00), no shadow, no floor, no other objects.
No text anywhere except the logo on the clothes.
```

**마지막 화면 (`cta`)**
```
{고정 문장}
Same character, cheerful: one hand raised with the index finger pointing straight up, the other hand in the hoodie pocket, a friendly closed-mouth smile.
Front view. Face and hands in the upper half of the image.
Single character only, centered, filling the frame from head to feet with a small margin.
Plain solid pure green background (#00FF00), no shadow, no floor, no other objects.
No text anywhere except the logo on the clothes.
```

포즈만 바꿔서 더 뽑아 두면(손 흔들기 · 엄지 척 · 생각하기) 나중에 카드뉴스 · 썸네일에도 쓴다. 이름은 `brand/mascot/pose-<이름>.png`.

## 6. 받은 뒤 확인: 직접 열어 본다

- [ ] 얼굴 · 옷 · 색이 기준 그림과 같은가 (**눈 모양** · 소품 위치까지. 눈에 흰자가 새로 생기거나 커지면 다시)
- [ ] 옷의 글자 철자가 맞는가
- [ ] 손가락 개수가 맞는가 (손이 크게 나오는 `cta` 에서 가장 자주 틀린다)
- [ ] 다른 회사 로고가 없나
- [ ] 배경이 한 색인가, 캐릭터 몸에 배경색이 없나
- [ ] 유명 캐릭터를 닮지 않았나

## 7. 고치는 문장: 다시 뽑지 말고 편집한다

받은 그림을 참조로 넣고:

```
Edit this exact image. Keep everything identical: the character, pose, colors and background.
Change only <고칠 것>.
```

| 고칠 것 | 넣는 말 |
|---|---|
| 입이 한쪽으로 쏠림 | `make the mouth a small, perfectly symmetrical smile centered exactly under the nose` |
| 볼터치 | `remove the pink blush on the cheeks completely` |
| 글자 철자 | `the text on the cap must read exactly "ABC"` |
| 손가락 | `each hand has exactly four fingers and one thumb` (캐릭터 손 모양에 맞춰) |
| 배경이 섞였다 | `replace the background with plain solid pure green (#00FF00), no shadow` |

---

## 8. 키트에 넣기

```bash
python3 engine/reel.py mascot hook ~/Downloads/내캐릭터-놀람.png
python3 engine/reel.py mascot cta  ~/Downloads/내캐릭터-가리킴.png
python3 engine/reel.py mascot body ~/Downloads/내캐릭터-정면.png   # 아래 캐릭터를 켤 때 (brand.json 의 mascot.bottom: true)
```

엔진이 하는 일: 배경이 투명이면 그대로, 한 색이면 그 색을 지운다(초록 번짐도 걷어 낸다) → 빈 여백을 자른다 → `brand/mascot/hook.png` · `cta.png` 로 저장 → **`hook-check.png` · `cta-check.png`** 를 만든다.

확인 그림은 밝은 바탕과 어두운 바탕에 나란히 얹은 것이다. **어두운 쪽에서 가장자리에 색 테가 보이거나 눈 · 흰 옷이 비면** 배경을 바꿔 다시 뽑는다.

그다음 실제 화면에서 본다:

```bash
python3 engine/reel.py build <편>
python3 engine/reel.py snapshot <편> 0.9        # 첫 화면 (훅 카드)
```

마지막 화면은 `snapshot` 기본값(프레임마다 끝 0.25초 앞)의 마지막 장에 있다. 결과 예시: `examples/mascot-syncbear/5-in-kit.webp`.

### 대시보드에서 올린 그림이 안 바뀌었다고 할 때

대시보드 1단계 「캐릭터」에 그림을 올리면 `brand/mascot/_내그림.(png|jpg|webp)` 로 저장하고 위 `mascot body` 를 돌린다. 네 귀퉁이 색이 다른 그림(배경에 그림자 · 무늬 · 그라데이션)은 `배경이 한 색이 아닙니다` 로 멈추고 **지금 들어간 `body.png` 는 그대로**다. 대시보드는 이때 「배경이 여러 색이라 못 지웠어요」와 「채팅에 부탁할 말 복사」 단추를 보여 준다.

사용자가 「brand/mascot 의 _내그림 파일 배경을 지워서 캐릭터로 넣어 줘」라고 하면 이 순서로 한다.

1. `brand/mascot/_내그림.*` 를 열어 보고 무슨 그림인지 · 배경이 어떤지 한 줄로 알린다
2. **쓸 방법을 먼저 말하고 사용자 허락을 받는다.** 배경이 단순하면 새로 깔 것 없이 이미지 편집(ffmpeg 의 색 지우기, 이미 설치돼 있다)으로 되는지 먼저 본다. 사람 · 동물처럼 배경이 복잡하면 배경 지우기 패키지(예: Python `rembg`)가 필요할 수 있다. **새 패키지를 까는 일이면 이름 · 크기 · 무엇을 하는지를 말하고 「설치해도 될까요?」를 먼저 묻는다.** 몰래 설치하지 않는다. 허락하지 않으면 사용자가 투명 PNG 나 초록 단색 배경 그림으로 다시 뽑아 올리게 안내한다
3. 지운 결과를 `brand/mascot/_내그림-투명.png` 처럼 **다른 이름으로** 저장하고(원본은 두고), `python3 engine/reel.py mascot body brand/mascot/_내그림-투명.png` 로 넣는다
4. `brand/mascot/body-check.png`(밝은 · 어두운 바탕)를 열어 가장자리에 색 테가 없는지 · 눈 · 흰 옷이 비지 않았는지 보여 주고, 사용자가 괜찮다고 하면 끝낸다. 이미 만든 편에도 넣으려면 `build` → `snapshot` 으로 다시 만든다(음성은 다시 뽑지 않는다)

## 9. 도구와 비용 · 권리

- **참조 이미지를 넣을 수 있는 도구**를 쓴다. 그래야 포즈를 바꿔도 같은 캐릭터가 나온다(ChatGPT 이미지 · Gemini · Midjourney · Higgsfield 등, 어느 것이든)
- 도구 비용은 사용자 몫이다. **Claude 가 연결된 이미지 도구로 직접 뽑을 때는 뽑기 전에 도구 이름 · 장 수 · 예상 비용을 말하고 확인받는다**
- 쓰는 도구의 이용약관에서 **상업적 이용**이 되는지 확인한다
- 남의 캐릭터 이름을 문장에 쓰지 않는다. 이름을 빼고 특징만 나열해 유명 캐릭터를 다시 만드는 것도 하지 않는다

## 10. 예시: 싱크곰 (`examples/mascot-syncbear/`)

| 파일 | 무엇 |
|---|---|
| `1-reference.webp` | 기준 그림 (손 흔드는 전신, 점 눈) |
| `2-hook.webp` | 첫 화면용: 두 손으로 볼을 감싼 놀람 |
| `3-cta.webp` | 마지막 화면용: 한 손 검지를 위로 |
| `4-green-vs-white.webp` | 같은 그림을 초록 배경(왼쪽) · 흰 배경(오른쪽)에서 지운 결과. 흰 배경은 「샘플」 도장의 흰 바탕 · 신발 밑창까지 빠지고 흰 테가 남는다 |
| `5-in-kit.webp` | 키트에 넣고 뽑은 첫 화면 · 마지막 화면 |

싱크곰 고정 문장:

```
The bear character from the reference image, kept exactly the same:
a chubby brown bear with a big round head and small round ears, small solid black dot eyes behind the glasses,
a navy baseball cap with "AISyncClub" written on the front, round gold wire glasses,
an oversized navy hoodie with drawstrings, dark brown pants, navy sneakers with cream soles,
flat 2D illustration with clean dark outlines and soft cel shading,
a small symmetrical smile centered under the nose, no blush on the cheeks.
```

**싱크곰은 AI싱크클럽의 캐릭터다.** 지침을 보여 주려고 넣은 예시라 그림마다 「샘플」 도장이 찍혀 있고, 내 영상 · 자료에 쓰지 않는다. 내 캐릭터는 위 순서로 새로 만든다.
