# 목소리 고르기

`brand/brand.json` 의 `voice.provider` 하나만 바꾸면 된다. 처음 쓰는 사람에게는 **무료 목소리**를 권한다.

| 고르는 값 | 돈 | 단어 타이밍 | 준비 | 이럴 때 |
|---|---|---|---|---|
| `none` | 없음 | 어림 | 없음 | 소리 없이 화면부터 볼 때 |
| `edge` **무료 목소리** | 없음 | **정확** | `python3 -m pip install -U edge-tts` | 처음 · 연습 · 개인 채널 |
| `elevenlabs` | 유료 | **정확** | `.env` 의 `ELEVENLABS_API_KEY` + 목소리 ID | 목소리 품질이 가장 중요할 때 |
| `minimax` | 유료 | 어림(소리 구간 안에서) | `.env` 의 `MINIMAX_API_KEY` + 목소리 ID | 한국어 억양 · 복제 목소리 |
| `files` | 없음 | 어림 | 편 폴더 `voice-in/01.wav` … | 내 목소리로 녹음할 때 |

"어림"이면 화면 등장이 말보다 조금 이르거나 늦을 수 있다. 대시보드에서 들어 보고 거슬리면 정확한 쪽으로 바꾼다.

## 무료 목소리 (edge)

- 한국어: `ko-KR-SunHiNeural`(여) · `ko-KR-InJoonNeural`(남) · `ko-KR-HyunsuMultilingualNeural`(남). `voice.edge.voice` 에 넣는다
- 빠르기: `voice.edge.rate` 에 `"+10%"` · `"-5%"` 처럼
- **마이크로소프트의 온라인 읽기 서비스를 쓴다.** 상업적으로 써도 된다는 공식 문구는 찾지 못했다(2026-10 기준). 수익을 내는 채널이면 유료 목소리를 쓰는 편이 안전하다. 판단은 쓰는 사람 몫이다
- 오류 없이 멈추거나 `403` 이 나면 edge-tts 가 옛 판이다: `python3 -m pip install -U edge-tts`
- 같은 문장은 저장해 둔 소리를 다시 쓴다

## 키 넣기 (처음 쓰는 사람)

**대시보드 1단계 → 4. 소리**에서 ElevenLabs · MiniMax 를 고르면 키 칸이 나온다. 받는 곳 링크와 3단계 안내가 있고, 붙여 넣은 키는 키트 폴더 `.env` 에만 저장된다(화면 · 응답에 값이 다시 나오지 않는다). 저장하면 「목소리 불러오기」로 목소리 목록을 들어 보고 고른다(ElevenLabs 는 이번 달 남은 글자 수도 보인다). 고른 목소리 ID 는 `brand.json` 의 `voice.<서비스>.voice_id` 에 들어간다.
- ElevenLabs 키: https://elevenlabs.io/app/api/api-keys
- MiniMax 가입: https://platform.minimax.io/login · 키: https://platform.minimax.io/user-center/basic-information/interface-key
- **사용자에게 키를 채팅에 붙여 넣게 하지 않는다.** 붙여 넣었으면 쓰지 말고 대시보드 칸에 넣으라고 안내하고, 그 키는 새로 만드는 게 안전하다고 알린다

## ElevenLabs

- 키: `.env` 에 `ELEVENLABS_API_KEY=…`. 목소리 ID: ElevenLabs 목소리 화면에서 복사해 `voice.elevenlabs.voice_id`
- 줄마다 크레딧이 든다. **뽑기 전에 사용자에게 확인받는다.** 같은 문장은 다시 안 부른다

## MiniMax

- 키: `.env` 에 `MINIMAX_API_KEY=…`. 목소리 ID: MiniMax 목소리 목록(또는 내가 복제한 목소리 ID)을 `voice.minimax.voice_id`
- 모델 기본 `speech-2.8-hd`, 빠르기 `voice.minimax.speed`
- 중국 쪽 계정이면 `voice.minimax.endpoint` 에 그 계정의 주소를 넣는다
- 줄마다 크레딧이 든다. **뽑기 전에 확인받는다**

## 바꾼 뒤

`python3 engine/reel.py voice <편>` (전체) → `build` → `snapshot` · `board`. 공급처가 바뀌면 한 줄만 다시 뽑기는 안 된다(전체를 다시).
