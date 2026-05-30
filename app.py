import json
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title='함창중 문법 부르마블(음운)', layout='wide', initial_sidebar_state='collapsed')

st.markdown("""<style>
#MainMenu{visibility:hidden;} header{visibility:hidden;} footer{visibility:hidden;}
.block-container{padding:0 !important; max-width:100% !important;}
.stApp{background:#0b1020;}
iframe{border:none !important;}
</style>""", unsafe_allow_html=True)

QUESTIONS = [{'q': "'ㄱ'의 조음 위치와 조음 방법을 말하시오.", 'a': '연구개음 · 파열음', 'cat': '자음'}, {'q': "'ㄲ'의 조음 위치와 조음 방법을 말하시오.", 'a': '연구개음 · 파열음', 'cat': '자음'}, {'q': "'ㄴ'의 조음 위치와 조음 방법을 말하시오.", 'a': '치조음 · 비음', 'cat': '자음'}, {'q': "'ㄷ'의 조음 위치와 조음 방법을 말하시오.", 'a': '치조음 · 파열음', 'cat': '자음'}, {'q': "'ㄸ'의 조음 위치와 조음 방법을 말하시오.", 'a': '치조음 · 파열음', 'cat': '자음'}, {'q': "'ㄹ'의 조음 위치와 조음 방법을 말하시오.", 'a': '치조음 · 유음', 'cat': '자음'}, {'q': "'ㅁ'의 조음 위치와 조음 방법을 말하시오.", 'a': '양순음 · 비음', 'cat': '자음'}, {'q': "'ㅂ'의 조음 위치와 조음 방법을 말하시오.", 'a': '양순음 · 파열음', 'cat': '자음'}, {'q': "'ㅃ'의 조음 위치와 조음 방법을 말하시오.", 'a': '양순음 · 파열음', 'cat': '자음'}, {'q': "'ㅅ'의 조음 위치와 조음 방법을 말하시오.", 'a': '치조음 · 마찰음', 'cat': '자음'}, {'q': "'ㅆ'의 조음 위치와 조음 방법을 말하시오.", 'a': '치조음 · 마찰음', 'cat': '자음'}, {'q': "'ㅇ'의 조음 위치와 조음 방법을 말하시오.", 'a': '연구개음 · 비음', 'cat': '자음'}, {'q': "'ㅈ'의 조음 위치와 조음 방법을 말하시오.", 'a': '경구개음 · 파찰음', 'cat': '자음'}, {'q': "'ㅉ'의 조음 위치와 조음 방법을 말하시오.", 'a': '경구개음 · 파찰음', 'cat': '자음'}, {'q': "'ㅊ'의 조음 위치와 조음 방법을 말하시오.", 'a': '경구개음 · 파찰음', 'cat': '자음'}, {'q': "'ㅋ'의 조음 위치와 조음 방법을 말하시오.", 'a': '연구개음 · 파열음', 'cat': '자음'}, {'q': "'ㅌ'의 조음 위치와 조음 방법을 말하시오.", 'a': '치조음 · 파열음', 'cat': '자음'}, {'q': "'ㅍ'의 조음 위치와 조음 방법을 말하시오.", 'a': '양순음 · 파열음', 'cat': '자음'}, {'q': "'ㅎ'의 조음 위치와 조음 방법을 말하시오.", 'a': '후음음 · 마찰음', 'cat': '자음'}, {'q': "'ㄱ'은(는) 예사소리·된소리·거센소리 중 무엇인가?", 'a': '예사소리', 'cat': '자음'}, {'q': "'ㄷ'은(는) 예사소리·된소리·거센소리 중 무엇인가?", 'a': '예사소리', 'cat': '자음'}, {'q': "'ㅂ'은(는) 예사소리·된소리·거센소리 중 무엇인가?", 'a': '예사소리', 'cat': '자음'}, {'q': "'ㅅ'은(는) 예사소리·된소리·거센소리 중 무엇인가?", 'a': '예사소리', 'cat': '자음'}, {'q': "'ㅈ'은(는) 예사소리·된소리·거센소리 중 무엇인가?", 'a': '예사소리', 'cat': '자음'}, {'q': "'ㄲ'은(는) 예사소리·된소리·거센소리 중 무엇인가?", 'a': '된소리', 'cat': '자음'}, {'q': "'ㄸ'은(는) 예사소리·된소리·거센소리 중 무엇인가?", 'a': '된소리', 'cat': '자음'}, {'q': "'ㅃ'은(는) 예사소리·된소리·거센소리 중 무엇인가?", 'a': '된소리', 'cat': '자음'}, {'q': "'ㅆ'은(는) 예사소리·된소리·거센소리 중 무엇인가?", 'a': '된소리', 'cat': '자음'}, {'q': "'ㅉ'은(는) 예사소리·된소리·거센소리 중 무엇인가?", 'a': '된소리', 'cat': '자음'}, {'q': "'ㅋ'은(는) 예사소리·된소리·거센소리 중 무엇인가?", 'a': '거센소리', 'cat': '자음'}, {'q': "'ㅌ'은(는) 예사소리·된소리·거센소리 중 무엇인가?", 'a': '거센소리', 'cat': '자음'}, {'q': "'ㅍ'은(는) 예사소리·된소리·거센소리 중 무엇인가?", 'a': '거센소리', 'cat': '자음'}, {'q': "'ㅊ'은(는) 예사소리·된소리·거센소리 중 무엇인가?", 'a': '거센소리', 'cat': '자음'}, {'q': '유성음(울림소리)인 자음을 모두 말하시오.', 'a': 'ㄴ, ㄹ, ㅁ, ㅇ', 'cat': '자음'}, {'q': '양순음(입술소리)을 모두 말하시오.', 'a': 'ㅂ, ㅃ, ㅍ, ㅁ', 'cat': '자음'}, {'q': '연구개음을 모두 말하시오.', 'a': 'ㄱ, ㄲ, ㅋ, ㅇ', 'cat': '자음'}, {'q': '경구개음을 모두 말하시오.', 'a': 'ㅈ, ㅉ, ㅊ', 'cat': '자음'}, {'q': '치조음(잇몸소리)을 모두 말하시오.', 'a': 'ㄷ,ㄸ,ㅌ,ㄴ,ㅅ,ㅆ,ㄹ', 'cat': '자음'}, {'q': '파열음을 모두 말하시오.', 'a': 'ㅂㅃㅍ, ㄷㄸㅌ, ㄱㄲㅋ', 'cat': '자음'}, {'q': '파찰음을 모두 말하시오.', 'a': 'ㅈ, ㅉ, ㅊ', 'cat': '자음'}, {'q': '마찰음을 모두 말하시오.', 'a': 'ㅅ, ㅆ, ㅎ', 'cat': '자음'}, {'q': '비음을 모두 말하시오.', 'a': 'ㅁ, ㄴ, ㅇ', 'cat': '자음'}, {'q': '유음을 말하시오.', 'a': 'ㄹ', 'cat': '자음'}, {'q': '후음(목청소리)을 말하시오.', 'a': 'ㅎ', 'cat': '자음'}, {'q': '예사소리(평음)를 모두 말하시오.', 'a': 'ㄱ, ㄷ, ㅂ, ㅅ, ㅈ', 'cat': '자음'}, {'q': '된소리(경음)를 모두 말하시오.', 'a': 'ㄲ, ㄸ, ㅃ, ㅆ, ㅉ', 'cat': '자음'}, {'q': '거센소리(격음)를 모두 말하시오.', 'a': 'ㅋ, ㅌ, ㅍ, ㅊ', 'cat': '자음'}, {'q': '국어의 자음은 모두 몇 개인가?', 'a': '19개', 'cat': '자음'}, {'q': "단모음 'ㅏ'의 혀의 최고점 위치(전설/후설), 혀의 높이(고/중/저), 입술 모양(평순/원순)을 말하시오.", 'a': '후설모음 · 저모음 · 평순모음', 'cat': '모음'}, {'q': "단모음 'ㅐ'의 혀의 최고점 위치(전설/후설), 혀의 높이(고/중/저), 입술 모양(평순/원순)을 말하시오.", 'a': '전설모음 · 저모음 · 평순모음', 'cat': '모음'}, {'q': "단모음 'ㅓ'의 혀의 최고점 위치(전설/후설), 혀의 높이(고/중/저), 입술 모양(평순/원순)을 말하시오.", 'a': '후설모음 · 중모음 · 평순모음', 'cat': '모음'}, {'q': "단모음 'ㅔ'의 혀의 최고점 위치(전설/후설), 혀의 높이(고/중/저), 입술 모양(평순/원순)을 말하시오.", 'a': '전설모음 · 중모음 · 평순모음', 'cat': '모음'}, {'q': "단모음 'ㅗ'의 혀의 최고점 위치(전설/후설), 혀의 높이(고/중/저), 입술 모양(평순/원순)을 말하시오.", 'a': '후설모음 · 중모음 · 원순모음', 'cat': '모음'}, {'q': "단모음 'ㅚ'의 혀의 최고점 위치(전설/후설), 혀의 높이(고/중/저), 입술 모양(평순/원순)을 말하시오.", 'a': '전설모음 · 중모음 · 원순모음', 'cat': '모음'}, {'q': "단모음 'ㅜ'의 혀의 최고점 위치(전설/후설), 혀의 높이(고/중/저), 입술 모양(평순/원순)을 말하시오.", 'a': '후설모음 · 고모음 · 원순모음', 'cat': '모음'}, {'q': "단모음 'ㅟ'의 혀의 최고점 위치(전설/후설), 혀의 높이(고/중/저), 입술 모양(평순/원순)을 말하시오.", 'a': '전설모음 · 고모음 · 원순모음', 'cat': '모음'}, {'q': "단모음 'ㅡ'의 혀의 최고점 위치(전설/후설), 혀의 높이(고/중/저), 입술 모양(평순/원순)을 말하시오.", 'a': '후설모음 · 고모음 · 평순모음', 'cat': '모음'}, {'q': "단모음 'ㅣ'의 혀의 최고점 위치(전설/후설), 혀의 높이(고/중/저), 입술 모양(평순/원순)을 말하시오.", 'a': '전설모음 · 고모음 · 평순모음', 'cat': '모음'}, {'q': '단모음을 모두 말하시오.', 'a': 'ㅏㅐㅓㅔㅗㅚㅜㅟㅡㅣ (10개)', 'cat': '모음'}, {'q': '전설 모음을 모두 말하시오.', 'a': 'ㅣ, ㅔ, ㅐ, ㅟ, ㅚ', 'cat': '모음'}, {'q': '후설 모음을 모두 말하시오.', 'a': 'ㅡ, ㅓ, ㅏ, ㅜ, ㅗ', 'cat': '모음'}, {'q': '고모음을 모두 말하시오.', 'a': 'ㅣ, ㅟ, ㅡ, ㅜ', 'cat': '모음'}, {'q': '중모음을 모두 말하시오.', 'a': 'ㅔ, ㅚ, ㅓ, ㅗ', 'cat': '모음'}, {'q': '저모음을 모두 말하시오.', 'a': 'ㅐ, ㅏ', 'cat': '모음'}, {'q': '원순 모음을 모두 말하시오.', 'a': 'ㅟ, ㅚ, ㅜ, ㅗ', 'cat': '모음'}, {'q': '평순 모음을 모두 말하시오.', 'a': 'ㅣ,ㅔ,ㅐ,ㅡ,ㅓ,ㅏ', 'cat': '모음'}, {'q': '국어의 단모음은 모두 몇 개인가?', 'a': '10개', 'cat': '모음'}, {'q': '이중 모음은 모두 몇 개인가?', 'a': '11개', 'cat': '모음'}, {'q': '발음할 때 입술·혀가 움직이는 모음을 무엇이라 하는가?', 'a': '이중 모음', 'cat': '모음'}, {'q': "반모음 'ㅣ[j]'와 결합한 이중모음을 3개만 말하시오.", 'a': '예) ㅑ, ㅕ, ㅛ, ㅠ 등', 'cat': '모음'}, {'q': "단모음 'ㅚ, ㅟ'의 공통점을 입술 모양으로 설명하시오.", 'a': '둘 다 전설·원순 모음', 'cat': '모음'}, {'q': '음운의 정의를 간단히 말하시오.', 'a': '말의 뜻을 구별해 주는 소리의 가장 작은 단위', 'cat': '공통'}, {'q': '분절 음운 두 가지를 말하시오.', 'a': '자음, 모음', 'cat': '공통'}, {'q': '비분절 음운(운소) 예를 한 가지 말하시오.', 'a': '소리의 길이(장단) 등', 'cat': '공통'}, {'q': "'ㄱ'과 'ㅋ'의 공통점과 차이점을 말하시오.", 'a': '공통: 연구개·파열음 / 차이: 세기(예사·거센)', 'cat': '자음'}, {'q': "'ㄷ, ㄸ, ㅌ'의 공통된 조음 위치와 방법은?", 'a': '치조음 · 파열음', 'cat': '자음'}, {'q': "'ㅈ, ㅉ, ㅊ'의 공통된 조음 방법은?", 'a': '파찰음', 'cat': '자음'}, {'q': "'ㅁ'의 조음 위치와 방법은?", 'a': '양순음 · 비음', 'cat': '자음'}, {'q': "'ㅇ'의 조음 위치와 방법은?", 'a': '연구개음 · 비음', 'cat': '자음'}, {'q': "'ㄴ'의 조음 위치와 방법은?", 'a': '치조음 · 비음', 'cat': '자음'}, {'q': "'ㄹ'의 조음 위치와 방법은?", 'a': '치조음 · 유음', 'cat': '자음'}, {'q': "'ㅎ'의 조음 위치와 방법은?", 'a': '후음 · 마찰음', 'cat': '자음'}, {'q': '파열음을 조음 위치에 따라 세 무리로 나누시오.', 'a': '양순(ㅂㅃㅍ)·치조(ㄷㄸㅌ)·연구개(ㄱㄲㅋ)', 'cat': '자음'}, {'q': '안울림소리(무성음)이면서 마찰음인 것을 모두 말하시오.', 'a': 'ㅅ, ㅆ, ㅎ', 'cat': '자음'}, {'q': '콧소리(비음)는 모두 울림소리인가?', 'a': '예 (ㅁ,ㄴ,ㅇ 모두 울림소리)', 'cat': '자음'}, {'q': "'ㅂ'을 거센소리로 바꾸면?", 'a': 'ㅍ', 'cat': '자음'}, {'q': "'ㅅ'을 된소리로 바꾸면?", 'a': 'ㅆ', 'cat': '자음'}, {'q': "'ㄷ'을 거센소리로 바꾸면?", 'a': 'ㅌ', 'cat': '자음'}, {'q': "'ㅈ'을 된소리로 바꾸면?", 'a': 'ㅉ', 'cat': '자음'}, {'q': "조음 방법이 '파찰음'인 자음의 조음 위치는?", 'a': '경구개', 'cat': '자음'}, {'q': '입술을 둥글게 오므려 발음하는 단모음을 무엇이라 하는가?', 'a': '원순 모음', 'cat': '모음'}, {'q': '혀의 최고점이 입 앞쪽에 있는 모음을 무엇이라 하는가?', 'a': '전설 모음', 'cat': '모음'}, {'q': '입을 가장 크게 벌려(혀를 낮춰) 발음하는 모음 무리는?', 'a': '저모음 (ㅐ, ㅏ)', 'cat': '모음'}, {'q': "'ㅣ'와 'ㅡ'의 공통점과 차이점을 말하시오.", 'a': '공통: 고·평순 / 차이: ㅣ전설, ㅡ후설', 'cat': '모음'}, {'q': "'ㅗ'와 'ㅜ'의 공통점과 차이점을 말하시오.", 'a': '공통: 후설·원순 / 차이: ㅗ중, ㅜ고', 'cat': '모음'}, {'q': "'ㅏ'의 혀 높이·혀 위치·입술 모양을 말하시오.", 'a': '저모음·후설·평순', 'cat': '모음'}, {'q': "'ㅟ'의 혀 높이·혀 위치·입술 모양을 말하시오.", 'a': '고모음·전설·원순', 'cat': '모음'}, {'q': "'ㅐ'와 'ㅔ'의 차이를 혀 높이로 설명하시오.", 'a': 'ㅐ는 저모음, ㅔ는 중모음', 'cat': '모음'}, {'q': '전설 모음 중 원순 모음 두 개를 말하시오.', 'a': 'ㅟ, ㅚ', 'cat': '모음'}, {'q': '후설 모음 중 평순 모음을 모두 말하시오.', 'a': 'ㅡ, ㅓ, ㅏ', 'cat': '모음'}]

GAME_HTML = r'''<!doctype html><html lang='ko'><head><meta charset='utf-8'>
<meta name='viewport' content='width=device-width, initial-scale=1'>
<style>
*{box-sizing:border-box; margin:0; padding:0; font-family:'Pretendard','Segoe UI',system-ui,sans-serif;}
html,body{height:100%; overflow:hidden;
  background:radial-gradient(1200px 600px at 50% -10%, #bdeaff 0%, #7ec8f0 38%, #4aa8e8 70%, #2b7fd6 100%);}
#stage{position:absolute; left:50%; top:50%; width:1280px; height:720px;
  transform:translate(-50%,-50%); transform-origin:center center;}
.screen{position:absolute; inset:0; display:none; align-items:center; justify-content:center; flex-direction:column;}
.screen.show{display:flex;}

/* ---------- 3D 타이틀 ---------- */
.title-3d{font-weight:900; font-size:96px; letter-spacing:2px; color:#fff; text-align:center; line-height:1.05;
  text-shadow:0 2px 0 #ffd23f,0 4px 0 #ffb703,0 6px 0 #fb8500,0 8px 0 #e85d04,0 10px 0 #d00000,0 18px 22px rgba(0,0,0,.35);
  transform:rotate(-2deg); animation:bob 2.4s ease-in-out infinite;}
.title-3d span{display:block; font-size:60px; color:#caf0f8;
  text-shadow:0 2px 0 #48cae4,0 4px 0 #00b4d8,0 6px 0 #0096c7,0 10px 14px rgba(0,0,0,.3);}
@keyframes bob{0%,100%{transform:translateY(0) rotate(-2deg);}50%{transform:translateY(-14px) rotate(-2deg);}}
.sub-note{margin-top:18px; color:#fff; font-size:20px; font-weight:700; background:rgba(0,0,0,.25); padding:8px 18px; border-radius:14px;}

/* ---------- 버튼 ---------- */
.big-btn{margin-top:34px; font-size:30px; font-weight:900; color:#fff; cursor:pointer; border:none;
  padding:18px 46px; border-radius:20px; background:linear-gradient(#ffba08,#fb8500);
  box-shadow:0 7px 0 #c05600,0 12px 18px rgba(0,0,0,.3); transition:.08s;}
.big-btn:active{transform:translateY(5px); box-shadow:0 2px 0 #c05600;}
.btn{font-size:18px; font-weight:800; color:#fff; cursor:pointer; border:none; padding:12px 22px; border-radius:14px;
  background:linear-gradient(#4cc9f0,#4361ee); box-shadow:0 5px 0 #2f3fa0; transition:.08s; margin:6px;}
.btn:active{transform:translateY(4px); box-shadow:0 1px 0 #2f3fa0;}
.btn.green{background:linear-gradient(#80ed99,#38b000); box-shadow:0 5px 0 #2d6a4f;}
.btn.red{background:linear-gradient(#ff8fa3,#e5383b); box-shadow:0 5px 0 #9d0208;}
.btn.gray{background:linear-gradient(#adb5bd,#6c757d); box-shadow:0 5px 0 #343a40;}

/* ---------- 설정 화면 ---------- */
.panel{background:rgba(255,255,255,.92); border-radius:22px; padding:24px 28px; box-shadow:0 14px 30px rgba(0,0,0,.25);}
.h{font-size:34px; font-weight:900; color:#03396c; margin-bottom:14px; text-shadow:0 2px 0 #cde;}
.setup-grid{display:flex; gap:24px; align-items:flex-start;}
.inp{display:block; width:280px; font-size:18px; padding:11px 14px; margin:7px 0; border:2px solid #cdd; border-radius:12px;}
#teamList,#orderList{min-width:380px; max-height:360px; overflow:auto;}
.tcard{display:flex; align-items:center; gap:12px; background:#fff; border-radius:14px; padding:10px 14px; margin:8px 0;
  box-shadow:0 4px 0 rgba(0,0,0,.12); font-size:17px; font-weight:700; color:#222;}
.tcard .emo{font-size:30px;} .tcard .mem{font-size:14px; color:#667; font-weight:600;}
.dot{width:16px; height:16px; border-radius:50%;}

/* ---------- 게임 화면 ---------- */
#scoreboard{position:absolute; left:14px; top:14px; width:268px; z-index:30;
  background:rgba(255,255,255,.93); border-radius:18px; padding:12px; box-shadow:0 10px 24px rgba(0,0,0,.3);}
#scoreboard h3{font-size:18px; color:#03396c; margin-bottom:8px; text-align:center;}
.sb{display:flex; align-items:center; gap:8px; padding:7px 9px; border-radius:12px; margin:5px 0; background:#f3f7fb;}
.sb.turn{background:#fff3bf; box-shadow:0 0 0 3px #ffd43b;}
.sb .nm{font-weight:800; font-size:15px; flex:1; color:#222;}
.sb .sc{font-weight:900; font-size:22px; color:#1864ab;}
.sb .mm{font-size:11px; color:#556; width:100%; margin-top:2px;}
.sb.dead{opacity:.45; filter:grayscale(1);}

#boardWrap{position:absolute; left:50%; top:50%; transform:translate(-50%,-50%); width:560px; height:560px;
  perspective:1100px; z-index:10;}
#board{position:absolute; inset:0; transform:rotateX(20deg); transform-style:preserve-3d;}
.cell{position:absolute; width:54px; height:54px; border-radius:10px; display:flex; align-items:center; justify-content:center;
  flex-direction:column; font-size:11px; font-weight:800; color:#1b2a3a; text-align:center; line-height:1.05;
  box-shadow:0 7px 0 rgba(0,0,0,.32),0 10px 14px rgba(0,0,0,.25); border:2px solid rgba(255,255,255,.6);}
.cell .ico{font-size:20px;}
.c-quiz{background:linear-gradient(#e8f7ff,#bfe6ff);}
.c-golden{background:linear-gradient(#fff3b0,#ffd43b);}
.c-island{background:linear-gradient(#ffd6a5,#ff924c);}
.c-start{background:linear-gradient(#caffbf,#52b788); color:#fff; font-size:13px;}
.cell.hot{animation:pop .5s ease;}
@keyframes pop{0%{transform:scale(1);}50%{transform:scale(1.18);}100%{transform:scale(1);}}
#boardCenter{position:absolute; left:50%; top:50%; width:330px; height:200px; transform:translate(-50%,-50%);
  display:flex; align-items:center; justify-content:center; flex-direction:column; pointer-events:none;}
#boardCenter .bt{font-size:30px; font-weight:900; color:#03396c; text-shadow:0 2px 0 #fff;}
#boardCenter .bs{font-size:15px; font-weight:800; color:#1864ab; background:rgba(255,255,255,.7); padding:4px 12px; border-radius:10px; margin-top:6px;}

#pieces{position:absolute; inset:0; transform:rotateX(20deg); pointer-events:none;}
.piece{position:absolute; width:34px; height:34px; border-radius:10px; display:flex; align-items:center; justify-content:center;
  font-size:20px; transition:left .2s cubic-bezier(.34,1.56,.64,1), top .2s cubic-bezier(.34,1.56,.64,1);
  box-shadow:0 6px 0 rgba(0,0,0,.4),0 8px 10px rgba(0,0,0,.3); border:2px solid #fff; z-index:5;}
.piece.hop{animation:hop .22s ease;}
@keyframes hop{0%{transform:translateY(0);}50%{transform:translateY(-22px) scale(1.1);}100%{transform:translateY(0);}}

#sidePanel{position:absolute; right:16px; top:50%; transform:translateY(-50%); width:280px; z-index:20;
  display:flex; flex-direction:column; align-items:center; gap:12px;}
#turnInfo{background:rgba(255,255,255,.93); border-radius:16px; padding:12px 14px; text-align:center; width:100%;
  box-shadow:0 8px 20px rgba(0,0,0,.28);}
#turnInfo .who{font-size:22px; font-weight:900; color:#03396c;}
#turnInfo .sub{font-size:14px; color:#556; margin-top:3px;}
#dice{width:120px; height:120px; border-radius:24px; background:#fff; display:flex; align-items:center; justify-content:center;
  font-size:74px; font-weight:900; color:#e5383b; box-shadow:0 10px 0 #adb5bd,0 16px 22px rgba(0,0,0,.3);}
#dice.roll{animation:shake .5s ease;}
@keyframes shake{0%,100%{transform:rotate(0);}20%{transform:rotate(-18deg) scale(1.05);}40%{transform:rotate(16deg);}60%{transform:rotate(-10deg);}80%{transform:rotate(8deg);}}
#log{font-size:13px; color:#fff; background:rgba(0,0,0,.32); border-radius:12px; padding:8px 10px; width:100%; min-height:54px; text-align:center; font-weight:700;}

/* ---------- 오버레이(칸 위 퀴즈/이벤트) ---------- */
#overlay{position:absolute; left:50%; top:50%; transform:translate(-50%,-50%); width:600px; height:600px;
  display:none; align-items:center; justify-content:center; z-index:40;}
#overlay.show{display:flex;}
#overlay .back{position:absolute; inset:-200px; background:rgba(8,16,40,.55);}
.ocard{position:relative; width:560px; background:#fff; border-radius:24px; padding:22px 26px; text-align:center;
  box-shadow:0 20px 50px rgba(0,0,0,.5); animation:drop .35s cubic-bezier(.34,1.56,.64,1); border:5px solid #ffd23f;}
@keyframes drop{0%{transform:translateY(-60px) scale(.85); opacity:0;}100%{transform:none; opacity:1;}}
.badge{display:inline-block; font-size:14px; font-weight:900; color:#fff; padding:5px 14px; border-radius:20px; background:#4361ee;}
.badge.g{background:#f08c00;} .badge.i{background:#e8590c;}
.qwho{margin-top:10px; font-size:19px; font-weight:900; color:#e5383b;}
.qtext{margin:16px 6px; font-size:26px; font-weight:900; color:#1b2a3a; line-height:1.35;}
.timer{font-size:60px; font-weight:900; color:#1864ab;}
.timer.warn{color:#e5383b; animation:tk .5s infinite;}
@keyframes tk{50%{transform:scale(1.18);}}
.tbar{height:14px; background:#e9ecef; border-radius:8px; overflow:hidden; margin:10px 40px;}
.tbar>i{display:block; height:100%; width:100%; background:linear-gradient(#80ed99,#38b000); transition:width 1s linear;}
.answer{margin:14px; font-size:24px; font-weight:900; color:#2d6a4f; background:#e7f7ec; padding:12px; border-radius:14px; display:none;}
.answer.show{display:block;}

/* ---------- 결과 ---------- */
#result{position:absolute; inset:0; display:none; align-items:center; justify-content:center; z-index:60; background:rgba(8,16,40,.6);}
#result.show{display:flex;}
.rcard{background:#fff; border-radius:28px; padding:40px 56px; text-align:center; box-shadow:0 24px 60px rgba(0,0,0,.5); animation:drop .4s;}
.rcard .big{font-size:60px; font-weight:900; margin-bottom:10px;}
.conf{position:absolute; top:-20px; width:12px; height:18px; border-radius:3px; animation:fall linear forwards;}
@keyframes fall{0%{transform:translateY(-40px) rotate(0);}100%{transform:translateY(760px) rotate(720deg);}}

#credit{position:absolute; left:0; right:0; bottom:8px; text-align:center; color:#fff; font-weight:800; font-size:16px;
  text-shadow:0 1px 3px rgba(0,0,0,.5); z-index:50;}
</style></head><body>
<div id='stage'>

  <section id='s-start' class='screen show'>
    <div class='title-3d'>함창중 문법 부르마블<span>( 음 운 )</span></div>
    <div class='sub-note'>중3 국어 · 자음 / 모음 체계표 마스터 게임</div>
    <button class='big-btn' onclick='go("setup")'>게임 시작 ▶</button>
  </section>

  <section id='s-setup' class='screen'>
    <div class='panel'>
      <div class='h'>① 모둠 만들기 <span style='font-size:16px;color:#667'>(2~6모둠 · 모둠원 4명 이내)</span></div>
      <div class='setup-grid'>
        <div>
          <input class='inp' id='teamName' placeholder='모둠 이름 (예: 번개팀)'>
          <input class='inp' id='m1' placeholder='구성원 1'>
          <input class='inp' id='m2' placeholder='구성원 2'>
          <input class='inp' id='m3' placeholder='구성원 3 (선택)'>
          <input class='inp' id='m4' placeholder='구성원 4 (선택)'>
          <button class='btn' onclick='addTeam()'>+ 이 모둠 추가</button>
        </div>
        <div id='teamList'></div>
      </div>
      <div style='text-align:center;margin-top:10px'>
        <button class='big-btn' onclick='toOrder()'>② 순서 정하기 ▶</button>
      </div>
    </div>
  </section>

  <section id='s-order' class='screen'>
    <div class='panel' style='text-align:center'>
      <div class='h'>② 주사위 던질 순서 정하기</div>
      <div id='orderList'></div>
      <button class='btn' onclick='shuffleOrder()'>🎲 랜덤으로 순서 섞기</button>
      <button class='big-btn' onclick='startGame()'>이 순서로 시작 ▶</button>
    </div>
  </section>

  <section id='s-game' class='screen'>
    <div id='scoreboard'></div>
    <div id='boardWrap'>
      <div id='board'></div>
      <div id='boardCenter'><div class='bt'>음운 부르마블</div><div class='bs'>먼저 500점! 또는 상대 파산 시 승리</div></div>
      <div id='pieces'></div>
    </div>
    <div id='overlay'></div>
    <div id='sidePanel'>
      <div id='turnInfo'></div>
      <div id='dice'>🎲</div>
      <button class='big-btn' id='rollBtn' onclick='rollDice()'>🎲 주사위 굴리기</button>
      <div id='log'>게임을 시작합니다!</div>
    </div>
    <div id='result'></div>
  </section>

  <div id='credit'>제작 : 함창고 교사 박호종</div>
</div>

<script>
var Q = /*QJSON*/;
var EMO=["🦊","🐯","🐼","🐸","🐵","🐰","🦁","🐨"];
var COL=["#ff6b6b","#4dabf7","#51cf66","#ffd43b","#cc5de8","#22b8cf","#ff922b","#94d82d"];

var teams=[], order=[], turnPtr=0, originPtr=0, stealMode=false, busy=false;
var curTeam=null, curMember=-1, curQ=null, timer=null, recent=[];

// 보드 정의
var N=36;
var TYPE=new Array(N).fill("quiz");
TYPE[0]="start"; [9,27,4,14,23,32].forEach(function(i){TYPE[i]="golden";});
[18,13].forEach(function(i){TYPE[i]="island";});
var CS=54, GAP=2, STEP=56, OFF=8;  // 셀 배치
function rc(i){
  if(i<=9) return [0,i];
  if(i<=18) return [i-9,9];
  if(i<=27) return [9,9-(i-18)];
  return [9-(i-27),0];
}
function cx(i){return rc(i)[1]*STEP+OFF;}
function cy(i){return rc(i)[0]*STEP+OFF;}

function go(name){
  document.querySelectorAll(".screen").forEach(function(s){s.classList.remove("show");});
  document.getElementById("s-"+name).classList.add("show");
}
function sleep(ms){return new Promise(function(r){setTimeout(r,ms);});}

/* ---------- 효과음 (WebAudio, 외부파일 불필요) ---------- */
var AC=null;
function ac(){ if(!AC){AC=new (window.AudioContext||window.webkitAudioContext)();} return AC; }
function tone(f,t0,dur,type){
  var c=ac(); var o=c.createOscillator(), g=c.createGain();
  o.type=type||"square"; o.frequency.value=f; o.connect(g); g.connect(c.destination);
  var t=c.currentTime+t0; g.gain.setValueAtTime(0.0001,t); g.gain.exponentialRampToValueAtTime(0.25,t+0.02);
  g.gain.exponentialRampToValueAtTime(0.0001,t+dur); o.start(t); o.stop(t+dur+0.02);
}
function sfx(k){
  try{
    if(k=="correct"){tone(660,0,0.12);tone(880,0.1,0.16);tone(1180,0.22,0.22);}
    else if(k=="wrong"){tone(200,0,0.25,"sawtooth");tone(150,0.18,0.3,"sawtooth");}
    else if(k=="dice"){tone(500,0,0.05);tone(700,0.07,0.05);tone(900,0.14,0.06);}
    else if(k=="win"){[523,659,784,1046,1318].forEach(function(f,i){tone(f,i*0.12,0.3);});}
    else if(k=="bust"){tone(330,0,0.2,"sawtooth");tone(220,0.2,0.25,"sawtooth");tone(110,0.45,0.4,"sawtooth");}
    else if(k=="gold"){tone(880,0,0.1);tone(1320,0.1,0.18);}
  }catch(e){}
}

/* ---------- 설정 ---------- */
function addTeam(){
  if(teams.length>=6){alert("최대 6모둠까지 가능합니다.");return;}
  var nm=document.getElementById("teamName").value.trim();
  if(!nm){alert("모둠 이름을 입력하세요.");return;}
  var mem=[];
  ["m1","m2","m3","m4"].forEach(function(id){
    var v=document.getElementById(id).value.trim();
    if(v) mem.push({name:v,score:0});
  });
  if(mem.length===0){alert("구성원을 최소 1명 입력하세요.");return;}
  var k=teams.length;
  teams.push({name:nm, members:mem, score:100, pos:0, skip:false, alive:true, emo:EMO[k], col:COL[k]});
  ["teamName","m1","m2","m3","m4"].forEach(function(id){document.getElementById(id).value="";});
  renderTeamList();
}
function renderTeamList(){
  var h="";
  teams.forEach(function(t){
    h+="<div class='tcard'><span class='dot' style='background:"+t.col+"'></span><span class='emo'>"+t.emo+
       "</span><div><div>"+t.name+"</div><div class='mem'>"+t.members.map(function(m){return m.name;}).join(", ")+"</div></div></div>";
  });
  document.getElementById("teamList").innerHTML=h||"<div class='mem'>아직 추가된 모둠이 없습니다.</div>";
}
function toOrder(){
  if(teams.length<2){alert("최소 2모둠이 필요합니다.");return;}
  order=teams.map(function(_,i){return i;});
  renderOrder(); go("order");
}
function renderOrder(){
  var h="";
  order.forEach(function(ti,idx){
    var t=teams[ti];
    h+="<div class='tcard'><b style='font-size:22px;color:#e5383b'>"+(idx+1)+"</b><span class='emo'>"+t.emo+
       "</span><span class='nm'>"+t.name+"</span></div>";
  });
  document.getElementById("orderList").innerHTML=h;
}
function shuffleOrder(){
  for(var i=order.length-1;i>0;i--){var j=Math.floor(Math.random()*(i+1));var x=order[i];order[i]=order[j];order[j]=x;}
  renderOrder(); sfx("dice");
}

/* ---------- 게임 시작 ---------- */
function startGame(){
  go("game"); buildBoard(); buildPieces(); turnPtr=0; updateAll();
  log("첫 번째 모둠부터 주사위를 굴려 주세요!");
}
function buildBoard(){
  var b=document.getElementById("board"); var h="";
  var label={quiz:["문법 문제","❓"],golden:["황금열쇠","🔑"],island:["무인도","🏝️"],start:["출발","🚩"]};
  for(var i=0;i<N;i++){
    var lb=label[TYPE[i]];
    h+="<div class='cell c-"+TYPE[i]+"' id='cell"+i+"' style='left:"+cx(i)+"px;top:"+cy(i)+"px'>"+
       "<div class='ico'>"+lb[1]+"</div>"+lb[0]+"</div>";
  }
  b.innerHTML=h;
}
function buildPieces(){
  var p=document.getElementById("pieces"); var h="";
  teams.forEach(function(t,k){
    h+="<div class='piece' id='pc"+k+"' style='background:"+t.col+"'>"+t.emo+"</div>";
  });
  p.innerHTML=h;
  teams.forEach(function(_,k){placePiece(k);});
}
function placePiece(k){
  var t=teams[k]; var el=document.getElementById("pc"+k);
  var n=teams.length; var ang=(2*Math.PI/n)*k;
  var ox=Math.cos(ang)*11, oy=Math.sin(ang)*11;
  el.style.left=(cx(t.pos)+CS/2-17+ox)+"px";
  el.style.top=(cy(t.pos)+CS/2-17+oy)+"px";
}

/* ---------- 점수판 / 턴 ---------- */
function updateAll(){updateScore(); updateTurn();}
function updateScore(){
  var h="<h3>🏆 점수 현황판</h3>";
  teams.forEach(function(t,k){
    var isTurn=(order[turnPtr]===k);
    h+="<div class='sb"+(isTurn?" turn":"")+(t.alive?"":" dead")+"'>"+
       "<span class='dot' style='background:"+t.col+"'></span><span class='emo' style='font-size:20px'>"+t.emo+
       "</span><span class='nm'>"+t.name+"</span><span class='sc'>"+t.score+"</span>"+
       "<div class='mm'>"+t.members.map(function(m){return m.name+" "+(m.score>=0?"+":"")+m.score;}).join(" · ")+"</div></div>";
  });
  document.getElementById("scoreboard").innerHTML=h;
}
function updateTurn(){
  var t=teams[order[turnPtr]];
  var ti=document.getElementById("turnInfo");
  if(t.skip){
    ti.innerHTML="<div class='who' style='color:"+t.col+"'>"+t.emo+" "+t.name+"</div><div class='sub'>🏝️ 무인도에서 쉬는 중</div>";
    var b=document.getElementById("rollBtn"); b.textContent="⏭ 한 턴 건너뛰기";
  }else{
    ti.innerHTML="<div class='who' style='color:"+t.col+"'>"+t.emo+" "+t.name+" 차례</div><div class='sub'>주사위를 굴리세요!</div>";
    document.getElementById("rollBtn").textContent="🎲 주사위 굴리기";
  }
}
function log(m){document.getElementById("log").innerHTML=m;}
function nextAlive(p){for(var k=1;k<=order.length;k++){var np=(p+k)%order.length; if(teams[order[np]].alive) return np;} return p;}
function aliveCount(){return teams.filter(function(t){return t.alive;}).length;}

/* ---------- 주사위 / 이동 ---------- */
async function rollDice(){
  if(busy) return; busy=true;
  var t=teams[order[turnPtr]];
  if(!t.alive){ turnPtr=nextAlive(turnPtr); busy=false; updateAll(); return; }
  if(t.skip){ t.skip=false; log(t.name+" 모둠은 무인도에서 한 턴 쉬었습니다."); turnPtr=nextAlive(turnPtr); updateAll(); busy=false; return; }
  var dice=document.getElementById("dice"); dice.classList.add("roll"); sfx("dice");
  var roll=1+Math.floor(Math.random()*6);
  for(var f=0;f<10;f++){dice.textContent=1+Math.floor(Math.random()*6); await sleep(45);}
  dice.textContent=roll; dice.classList.remove("roll");
  log(t.emo+" "+t.name+" → 주사위 <b style='font-size:20px;color:#ffd43b'>"+roll+"</b> 칸 이동!");
  await sleep(350);
  for(var s=0;s<roll;s++){
    t.pos=(t.pos+1)%N; var k=order[turnPtr];
    var pc=document.getElementById("pc"+k); pc.classList.add("hop"); placePiece(k);
    await sleep(220); pc.classList.remove("hop");
  }
  var cell=document.getElementById("cell"+t.pos); cell.classList.add("hot"); setTimeout(function(){cell.classList.remove("hot");},600);
  await sleep(250);
  handleLanding();
}
function handleLanding(){
  var t=teams[order[turnPtr]]; var ty=TYPE[t.pos];
  if(ty==="quiz"){ curTeam=order[turnPtr]; stealMode=false; presentQuiz(); }
  else if(ty==="golden"){ goldenEvent(); }
  else if(ty==="island"){ islandEvent(); }
  else if(ty==="start"){ apply(order[turnPtr],-1,10); log("🚩 출발 도착 보너스 +10점!"); sfx("gold"); afterResolve(false); }
}

/* ---------- 퀴즈 오버레이 ---------- */
function pickQ(){
  var idx;
  do{ idx=Math.floor(Math.random()*Q.length); }while(recent.indexOf(idx)>=0 && recent.length<Q.length);
  recent.push(idx); if(recent.length>30) recent.shift();
  return Q[idx];
}
function presentQuiz(){
  var t=teams[curTeam];
  curMember=Math.floor(Math.random()*t.members.length);
  curQ=pickQ();
  var who=t.emo+" "+t.name+" 모둠 · <u>"+t.members[curMember].name+"</u> 학생";
  var badge=curQ.cat==="모음"?"모음 체계":(curQ.cat==="자음"?"자음 체계":"음운 기초");
  var ov=document.getElementById("overlay");
  ov.innerHTML="<div class='back'></div><div class='ocard'>"+
    "<span class='badge'>"+badge+(stealMode?" · 찬스 문제!":"")+"</span>"+
    "<div class='qwho'>"+who+"</div>"+
    "<div class='qtext'>"+curQ.q+"</div>"+
    "<div class='timer' id='qtimer'>10</div>"+
    "<div class='tbar'><i id='tbar'></i></div>"+
    "<div class='answer' id='ans'>정답 : "+curQ.a+"</div>"+
    "<div id='qbtns'><button class='btn gray' onclick='reveal()'>👀 정답 공개</button></div>"+
    "</div>";
  ov.classList.add("show");
  startTimer(10);
}
function startTimer(sec){
  clearInterval(timer); var left=sec; var tm=document.getElementById("qtimer"); var bar=document.getElementById("tbar");
  tm.textContent=left; bar.style.width="100%";
  timer=setInterval(function(){
    left--; tm.textContent=Math.max(left,0); bar.style.width=(left/sec*100)+"%";
    if(left<=3) tm.classList.add("warn");
    if(left<=0){clearInterval(timer); tm.textContent="시간 종료!"; sfx("wrong");}
  },1000);
}
function reveal(){
  clearInterval(timer);
  document.getElementById("ans").classList.add("show");
  document.getElementById("qbtns").innerHTML=
    "<button class='btn green' onclick='mark(true)'>⭕ 정답 (+10)</button>"+
    "<button class='btn red' onclick='mark(false)'>❌ 오답 (-10)</button>";
}
function mark(ok){
  clearInterval(timer);
  apply(curTeam, curMember, ok?10:-10);
  if(ok){
    sfx("correct"); log("⭕ "+teams[curTeam].name+" 정답! +10점");
    closeOverlay(); afterResolve(false);
  }else{
    sfx("wrong"); log("❌ "+teams[curTeam].name+" 오답! -10점");
    if(checkEnd()) {closeOverlay(); return;}
    if(!stealMode){
      // 찬스: 무작위 다른 모둠 + 무작위 학생
      var others=[]; teams.forEach(function(t,i){if(t.alive && i!==curTeam) others.push(i);});
      if(others.length===0){closeOverlay(); afterResolve(false); return;}
      stealMode=true; originPtr=turnPtr;
      curTeam=others[Math.floor(Math.random()*others.length)];
      log("🔄 찬스! "+teams[curTeam].name+" 모둠으로 기회가 넘어갑니다.");
      closeOverlay();
      setTimeout(function(){presentQuiz();},700);
    }else{
      closeOverlay(); afterResolve(true);
    }
  }
}
function closeOverlay(){document.getElementById("overlay").classList.remove("show");}

/* ---------- 황금열쇠 / 무인도 ---------- */
var GOLD=[
 {t:"생일 축하금 🎂",d:"모둠 전원에게 생일 축하금이 도착했어요! <b>+20점</b>",p:20},
 {t:"벌금 고지서 💸",d:"이런! 지각 벌금이 부과되었습니다. <b>-20점</b>",p:-20},
 {t:"단합력 테스트 🤝",d:"모둠 구호를 우렁차게 외치면 성공!",p:0,r:10},
 {t:"개인기 찬스 🎤",d:"한 명이 개인기를 멋지게 성공하면!",p:0,r:10},
 {t:"행운의 룰렛 🍀",d:"행운이 굴러들어왔어요! <b>+15점</b>",p:15},
 {t:"방심은 금물 ⚠️",d:"한눈판 사이 점수가 새어나갔어요. <b>-10점</b>",p:-10}
];
function goldenEvent(){
  var g=GOLD[Math.floor(Math.random()*GOLD.length)]; var t=teams[order[turnPtr]]; sfx("gold");
  var ov=document.getElementById("overlay");
  var body;
  if(g.p!==0){
    apply(order[turnPtr],-1,g.p); updateAll();
    body="<button class='btn' onclick='closeGold(false)'>확인 ▶</button>";
  }else{
    body="<button class='btn green' onclick='applyGold("+g.r+")'>성공! (+"+g.r+")</button>"+
         "<button class='btn gray' onclick='closeGold(false)'>실패 (0점)</button>";
  }
  ov.innerHTML="<div class='back'></div><div class='ocard' style='border-color:#ffd43b'>"+
    "<span class='badge g'>황금열쇠</span><div class='qwho' style='color:"+t.col+"'>"+t.emo+" "+t.name+" 모둠</div>"+
    "<div class='qtext'>"+g.t+"</div><div style='font-size:20px;color:#444;margin:6px 14px 14px'>"+g.d+"</div>"+body+"</div>";
  ov.classList.add("show");
}
function applyGold(r){apply(order[turnPtr],-1,r); sfx("correct"); updateAll(); closeGold(false);}
function closeGold(){closeOverlay(); afterResolve(false);}
function islandEvent(){
  var t=teams[order[turnPtr]]; t.skip=true; sfx("wrong");
  var ov=document.getElementById("overlay");
  ov.innerHTML="<div class='back'></div><div class='ocard' style='border-color:#ff924c'>"+
    "<span class='badge i'>무인도</span><div class='qwho' style='color:"+t.col+"'>"+t.emo+" "+t.name+" 모둠</div>"+
    "<div class='qtext'>🏝️ 무인도에 표류!</div><div style='font-size:20px;color:#444;margin:6px 14px 14px'>다음 차례 한 번 <b>쉬어갑니다.</b></div>"+
    "<button class='btn' onclick='closeIsland()'>확인 ▶</button></div>";
  ov.classList.add("show");
}
function closeIsland(){closeOverlay(); afterResolve(false);}

/* ---------- 점수 적용 / 승패 ---------- */
function apply(ti,mi,delta){
  var t=teams[ti]; t.score+=delta;
  if(mi>=0 && t.members[mi]) t.members[mi].score+=delta;
  updateScore();
}
function checkEnd(){
  // 승리: 500점 이상
  for(var i=0;i<teams.length;i++){ if(teams[i].alive && teams[i].score>=500){ win(i); return true; } }
  // 파산: -100점 이하
  for(var j=0;j<teams.length;j++){
    if(teams[j].alive && teams[j].score<=-100){
      teams[j].alive=false; updateScore(); log("💥 "+teams[j].name+" 모둠 파산!");
      if(aliveCount()===1){ var w=teams.findIndex(function(t){return t.alive;}); win(w); return true; }
    }
  }
  return false;
}
function afterResolve(fromSteal){
  if(checkEnd()) return;
  var base = (stealMode||fromSteal) ? originPtr : turnPtr;
  stealMode=false;
  turnPtr=nextAlive(base);
  updateAll(); busy=false;
}
function win(i){
  busy=true; sfx("win"); var t=teams[i];
  var conf="";
  for(var c=0;c<60;c++){ conf+="<div class='conf' style='left:"+(Math.random()*1280)+"px;background:"+COL[c%COL.length]+
    ";animation-duration:"+(1.6+Math.random()*1.6)+"s;animation-delay:"+(Math.random()*0.6)+"s'></div>"; }
  var r=document.getElementById("result");
  r.innerHTML=conf+"<div class='rcard'><div class='big'>🎉 우승! 🎉</div>"+
    "<div style='font-size:40px;font-weight:900;color:"+t.col+"'>"+t.emo+" "+t.name+" 모둠</div>"+
    "<div style='font-size:24px;margin:14px;color:#333'>최종 점수 <b style='color:#1864ab'>"+t.score+"점</b></div>"+
    "<div style='font-size:16px;color:#667;margin-bottom:18px'>구성원: "+t.members.map(function(m){return m.name+"("+m.score+")";}).join(", ")+"</div>"+
    "<button class='big-btn' onclick='location.reload()'>다시 시작 ↻</button></div>";
  r.classList.add("show");
}

/* ---------- 화면 맞춤(스크롤 없이 한 화면) ---------- */
function fit(){
  var s=Math.min(window.innerWidth/1280, window.innerHeight/720);
  document.getElementById("stage").style.transform="translate(-50%,-50%) scale("+s+")";
}
window.addEventListener("resize",fit); fit();
renderTeamList();
</script>
</body></html>'''

GAME_HTML = GAME_HTML.replace('/*QJSON*/', json.dumps(QUESTIONS, ensure_ascii=False))

components.html(GAME_HTML, height=760, scrolling=False)
