# 멈췄을 때

`reel.py` 는 멈출 때 `[멈춤]` 으로 시작하는 한 줄을 남긴다. 그 줄을 아래에서 찾는다.

| 메시지 | 원인 | 할 일 |
|---|---|---|
| `'ffmpeg' 이(가) 설치돼 있지 않습니다` | 준비물이 없다 | 맥: `brew install ffmpeg` (윈도 · 리눅스는 확인하지 않음) |
| `playwright 가 없습니다` | 키트 폴더에서 설치를 안 했다 | `npm install` 뒤 `npx playwright install chromium` |
| `playwright 브라우저가 없습니다` | 브라우저만 빠졌다 | `npx playwright install chromium` |
| `대본은 9줄이나 10줄입니다` | `episode.json` 의 `lines` 개수 | 줄을 맞춘다 |
| `JSON 형식이 틀렸습니다 (N번째 줄)` | 쉼표 · 따옴표 빠짐 | 그 줄 근처를 본다. 마지막 항목 뒤 쉼표가 가장 흔하다 |
| `무료 목소리를 쓰려면 edge-tts 를 설치하세요` | edge-tts 가 없다 | `python3 -m pip install -U edge-tts` |
| `무료 목소리 … 실패 · 403` 또는 오래 멈춤 | edge-tts 가 옛 판이라 서버가 막았다 | `python3 -m pip install -U edge-tts` |
| `MINIMAX_API_KEY 가 없습니다` · `voice.minimax.voice_id 가 비었습니다` | MiniMax 준비가 덜 됐다 | `.env` 와 `brand.json` (`references/voices.md`) |
| `ELEVENLABS_API_KEY 가 없습니다` | `.env` 가 없거나 비었다 | `env.example` 을 `.env` 로 복사해 키를 넣거나, `voice.provider` 를 `none` 으로 |
| `voice_id 가 비었습니다` | 목소리 ID 를 안 넣었다 | ElevenLabs 목소리 화면에서 ID 를 복사해 `brand.json` 에 |
| `ElevenLabs … HTTP 401` | 키가 틀렸다 | 키를 다시 복사한다 |
| `ElevenLabs … HTTP 402 · 429` | 크레딧이 없거나 너무 빨리 불렀다 | 크레딧 확인 · 잠시 뒤 다시. 같은 문장은 저장해 둔 걸 다시 써서 크레딧이 안 든다 |
| `녹음 파일이 없습니다: voice-in/01.wav` | `files` 모드인데 파일이 없다 | 편 폴더 안 `voice-in/` 에 `01.wav`(mp3 · m4a 도 됨) … 줄 수만큼 |
| `audio_meta.json 이 없습니다` | 음성을 안 뽑았다 | `voice` 를 먼저 |
| `대본은 N줄인데 음성은 M줄` | 대본 줄 수를 바꾼 뒤 음성을 안 뽑았다 | `voice` 를 다시(전체) |
| `frames.py 에 N번 프레임(HEAD[N])이 없습니다` | 그 프레임 그림을 안 썼다 | `HEAD[N]` · `ART[N]` · `JS[N]` 을 채운다 |
| `frames.py 실행 중 오류` | 파이썬 문법 · 이름 오타 | 메시지의 이름을 본다. f-문자열 안 JS 중괄호는 `{{ }}` 로 겹친다 |
| `N번 프레임 음성에 '단어' 이(가) 없습니다` | `at()` 에 준 단어가 그 줄에 없다 | 단어를 고치거나 `cue(N, 번호)` 로 |
| `그림이 안전 영역을 넘습니다` | 좌표가 가장자리에 닿았다 | `check` 가 찍은 숫자대로 그 프레임 좌표를 안쪽으로 |
| `HyperFrames 검사에서 에러` | 화면 규칙 위반 | 위에 찍힌 `✗` 줄을 본다. 아래 표 |
| `배경이 한 색이 아닙니다` | 마스코트 그림 배경에 무늬 · 그림자가 있다. 대시보드에서 올렸다면 캐릭터는 안 바뀌고 이전 그림이 그대로다 | 투명 배경이나 초록 단색 배경으로 다시 뽑는다 (`references/mascot.md` §2). 배경을 지워 달라는 부탁은 §8 의 순서(설치 전에 먼저 묻기)로 |
| 마스코트 가장자리에 초록 · 흰 테가 남는다 | 배경을 지운 자리가 번졌다 | `brand/mascot/*-check.png` 의 어두운 쪽을 본다. 흰 배경이면 초록 배경으로 다시 뽑는다 |
| `BGM 파일이 없습니다` | `bgm.provider` 가 `file` 인데 경로가 틀렸다 | `brand.json` 의 `bgm.file` |

## HyperFrames 검사에서 자주 나오는 것

| 줄 | 뜻 | 고침 |
|---|---|---|
| `content_overlap` | 글자 상자가 겹친다(눈에는 안 겹쳐 보여도) | 실수면 글자 크기의 위 1.03배 · 아래 0.27배로 간격을 다시 잡는다. 일부러 겹친 거면 그 글자마다 `T(…, extra="data-layout-allow-overlap")` (부모 `<g>` 에는 안 먹는다) |
| `container_overflow` | 그림이 칸 밖으로 나간다 | 크기를 줄이거나, 일부러 넘치는 거면 그 태그에 `data-layout-allow-overflow` |
| `overlapping_gsap_tweens` | 앞 움직임이 끝나기 전에 같은 속성을 또 움직였다 | 뒤 움직임을 앞 것이 끝난 뒤로 민다 |
| 대비(Contrast) 경고 | 글자색이 바탕과 비슷하다 | 강조색이 너무 밝으면 `brand.json` 의 `accent` 를 조금 진하게 |

## 화면이 이상할 때

| 증상 | 할 일 |
|---|---|
| 어두운 배경에서 글자 · 카드가 안 보인다 | frames.py 에 색 코드(`#FFFFFF` · `#1B1B1F`)나 `WHITE` 카드를 직접 썼다. `CARD` · `INK` 같은 이름으로 바꾸고 `build` |
| 훅 첫 줄 글자가 작다 | 첫 줄 말이 길다. 줄을 줄이면 커진다 |
| 마지막 화면 알약이 늦게 뜬다 | 마지막 줄에서 키워드를 늦게 말한다. 앞으로 당긴다 |
| 마감 문구가 말과 따로 논다 | `cta.tagline` 과 마지막 줄 끝을 같은 말로 |
| 영상이 무음처럼 시작한다 | BGM 이 없으면 정상이다(앞 1.4초는 말이 없다). 음악을 켜면 채워진다 |
| 소리가 겹친다 | 손으로 `index.html` 을 고쳤다. `build` 를 다시 돌린다 |

## 다시 돌리는 순서

| 바꾼 것 | 다시 돌릴 것 |
|---|---|
| `brand.json` | `build` 부터 (목소리를 바꿨으면 `voice` 부터) |
| 대본 한 줄 | `voice --line NN` → `build` → `check` |
| 대본 여러 줄 · 줄 수 | `voice` → `build` → `check` |
| `kit.html` | `materials` → `build` |
| `frames.py` | `build` → `check` |
| `episode.json` 의 `hook` · `kit` | `build` |
