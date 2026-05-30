import streamlit as st
import streamlit.components.v1 as components
import json

st.set_page_config(page_title='함창중 문법 부르마블(음운)', layout='wide', initial_sidebar_state='collapsed')

# 여백 제거 (한 화면 꽉 차게)
st.markdown('''<style>
#MainMenu,header,footer{visibility:hidden;}
.block-container{padding:0!important;max-width:100%!important;}
section.main>div{padding:0!important;}
iframe{display:block;}
</style>''', unsafe_allow_html=True)

QUESTIONS = [{"q": "'ㄱ'의 조음 위치와 조음 방법은?", "a": "연구개, 파열음"}, {"q": "'ㄲ'의 조음 위치와 조음 방법은?", "a": "연구개, 파열음"}, {"q": "'ㅋ'의 조음 위치와 조음 방법은?", "a": "연구개, 파열음"}, {"q": "'ㄷ'의 조음 위치와 조음 방법은?", "a": "치조(잇몸), 파열음"}, {"q": "'ㄸ'의 조음 위치와 조음 방법은?", "a": "치조(잇몸), 파열음"}, {"q": "'ㅌ'의 조음 위치와 조음 방법은?", "a": "치조(잇몸), 파열음"}, {"q": "'ㅂ'의 조음 위치와 조음 방법은?", "a": "양순(입술), 파열음"}, {"q": "'ㅃ'의 조음 위치와 조음 방법은?", "a": "양순(입술), 파열음"}, {"q": "'ㅍ'의 조음 위치와 조음 방법은?", "a": "양순(입술), 파열음"}, {"q": "'ㅈ'의 조음 위치와 조음 방법은?", "a": "경구개, 파찰음"}, {"q": "'ㅉ'의 조음 위치와 조음 방법은?", "a": "경구개, 파찰음"}, {"q": "'ㅊ'의 조음 위치와 조음 방법은?", "a": "경구개, 파찰음"}, {"q": "'ㅅ'의 조음 위치와 조음 방법은?", "a": "치조(잇몸), 마찰음"}, {"q": "'ㅆ'의 조음 위치와 조음 방법은?", "a": "치조(잇몸), 마찰음"}, {"q": "'ㅎ'의 조음 위치와 조음 방법은?", "a": "목청(후두), 마찰음"}, {"q": "'ㅁ'의 조음 위치와 조음 방법은?", "a": "양순(입술), 비음"}, {"q": "'ㄴ'의 조음 위치와 조음 방법은?", "a": "치조(잇몸), 비음"}, {"q": "'ㅇ'의 조음 위치와 조음 방법은?", "a": "연구개, 비음"}, {"q": "'ㄹ'의 조음 위치와 조음 방법은?", "a": "치조(잇몸), 유음"}, {"q": "양순음(입술소리)을 모두 쓰시오.", "a": "ㅂ,ㅃ,ㅍ,ㅁ"}, {"q": "치조음(잇몸소리)을 모두 쓰시오.", "a": "ㄷ,ㄸ,ㅌ,ㅅ,ㅆ,ㄴ,ㄹ"}, {"q": "경구개음을 모두 쓰시오.", "a": "ㅈ,ㅉ,ㅊ"}, {"q": "연구개음을 모두 쓰시오.", "a": "ㄱ,ㄲ,ㅋ,ㅇ"}, {"q": "목청소리(후음)는 무엇인가?", "a": "ㅎ"}, {"q": "파열음을 모두 쓰시오.", "a": "ㄱ,ㄲ,ㅋ,ㄷ,ㄸ,ㅌ,ㅂ,ㅃ,ㅍ"}, {"q": "파찰음을 모두 쓰시오.", "a": "ㅈ,ㅉ,ㅊ"}, {"q": "마찰음을 모두 쓰시오.", "a": "ㅅ,ㅆ,ㅎ"}, {"q": "비음을 모두 쓰시오.", "a": "ㄴ,ㅁ,ㅇ"}, {"q": "유음은 무엇인가?", "a": "ㄹ"}, {"q": "유성음(울림소리) 자음을 모두 쓰시오.", "a": "ㄴ,ㄹ,ㅁ,ㅇ"}, {"q": "비음과 유음을 합쳐 무엇이라 부르는가?", "a": "울림소리(유성음)"}, {"q": "'ㄱ'의 된소리는?", "a": "ㄲ"}, {"q": "'ㄱ'의 거센소리는?", "a": "ㅋ"}, {"q": "'ㄷ'의 된소리는?", "a": "ㄸ"}, {"q": "'ㄷ'의 거센소리는?", "a": "ㅌ"}, {"q": "'ㅂ'의 된소리는?", "a": "ㅃ"}, {"q": "'ㅂ'의 거센소리는?", "a": "ㅍ"}, {"q": "'ㅈ'의 된소리는?", "a": "ㅉ"}, {"q": "'ㅈ'의 거센소리는?", "a": "ㅊ"}, {"q": "'ㅅ'의 된소리는?", "a": "ㅆ"}, {"q": "된소리(경음)를 모두 쓰시오.", "a": "ㄲ,ㄸ,ㅃ,ㅆ,ㅉ"}, {"q": "거센소리(격음)를 모두 쓰시오.", "a": "ㅋ,ㅌ,ㅍ,ㅊ"}, {"q": "예사소리(평음)를 모두 쓰시오.", "a": "ㄱ,ㄷ,ㅂ,ㅅ,ㅈ"}, {"q": "안울림소리(무성음)는 어떤 소리들인가?", "a": "파열음·파찰음·마찰음"}, {"q": "국어의 자음은 모두 몇 개인가?", "a": "19개"}, {"q": "단모음 'ㅏ'의 혀의 위치/높이/입술 모양은?", "a": "후설, 저모음, 평순"}, {"q": "단모음 'ㅓ'의 혀의 위치/높이/입술 모양은?", "a": "후설, 중모음, 평순"}, {"q": "단모음 'ㅗ'의 혀의 위치/높이/입술 모양은?", "a": "후설, 중모음, 원순"}, {"q": "단모음 'ㅜ'의 혀의 위치/높이/입술 모양은?", "a": "후설, 고모음, 원순"}, {"q": "단모음 'ㅡ'의 혀의 위치/높이/입술 모양은?", "a": "후설, 고모음, 평순"}, {"q": "단모음 'ㅣ'의 혀의 위치/높이/입술 모양은?", "a": "전설, 고모음, 평순"}, {"q": "단모음 'ㅔ'의 혀의 위치/높이/입술 모양은?", "a": "전설, 중모음, 평순"}, {"q": "단모음 'ㅐ'의 혀의 위치/높이/입술 모양은?", "a": "전설, 저모음, 평순"}, {"q": "단모음 'ㅚ'의 혀의 위치/높이/입술 모양은?", "a": "전설, 중모음, 원순"}, {"q": "단모음 'ㅟ'의 혀의 위치/높이/입술 모양은?", "a": "전설, 고모음, 원순"}, {"q": "단모음을 모두 쓰시오.", "a": "ㅏ,ㅐ,ㅓ,ㅔ,ㅗ,ㅚ,ㅜ,ㅟ,ㅡ,ㅣ"}, {"q": "국어의 단모음은 모두 몇 개인가?", "a": "10개"}, {"q": "전설 모음을 모두 쓰시오.", "a": "ㅣ,ㅔ,ㅐ,ㅟ,ㅚ"}, {"q": "후설 모음을 모두 쓰시오.", "a": "ㅡ,ㅓ,ㅏ,ㅜ,ㅗ"}, {"q": "고모음(폐모음)을 모두 쓰시오.", "a": "ㅣ,ㅟ,ㅡ,ㅜ"}, {"q": "중모음을 모두 쓰시오.", "a": "ㅔ,ㅚ,ㅓ,ㅗ"}, {"q": "저모음(개모음)을 모두 쓰시오.", "a": "ㅐ,ㅏ"}, {"q": "원순 모음을 모두 쓰시오.", "a": "ㅗ,ㅜ,ㅚ,ㅟ"}, {"q": "평순 모음을 모두 쓰시오.", "a": "ㅏ,ㅐ,ㅓ,ㅔ,ㅡ,ㅣ"}, {"q": "발음할 때 입술 모양이나 혀가 움직이는 모음을 무엇이라 하는가?", "a": "이중 모음"}, {"q": "이중 모음을 만드는 반모음 두 가지는?", "a": "반모음 ㅣ(j), 반모음 ㅗ/ㅜ(w)"}, {"q": "'ㅑ, ㅕ, ㅛ, ㅠ'처럼 반모음 ㅣ로 시작하는 이중모음의 종류는?", "a": "상향 이중 모음"}, {"q": "국어의 모음은 모두 몇 개인가?", "a": "21개"}, {"q": "단모음 중 발음 위치가 변할 수 있어 이중모음으로도 발음되는 것은?", "a": "ㅚ, ㅟ"}, {"q": "혀의 최고점이 앞쪽에 있는 모음을 무엇이라 하는가?", "a": "전설 모음"}, {"q": "혀의 높이가 낮고 입을 크게 벌리는 모음을 무엇이라 하는가?", "a": "저모음(개모음)"}, {"q": "입술을 둥글게 오므려 소리내는 모음을 무엇이라 하는가?", "a": "원순 모음"}, {"q": "말의 뜻을 구별해 주는 소리의 가장 작은 단위는?", "a": "음운"}, {"q": "자음과 모음처럼 나눌 수 있는 음운을 무엇이라 하는가?", "a": "분절 음운(음소)"}, {"q": "소리의 길이(장단)처럼 경계를 나눌 수 없는 음운을 무엇이라 하는가?", "a": "비분절 음운(운소)"}, {"q": "공기가 막힘 없이 나오는 소리는 자음인가 모음인가?", "a": "모음"}, {"q": "발음 기관의 장애를 받아 나는 소리는 자음인가 모음인가?", "a": "자음"}, {"q": "홀로 음절을 이룰 수 있는 음운은?", "a": "모음"}, {"q": "국어의 음운 중 자음과 모음을 합치면 모두 몇 개인가?", "a": "40개"}, {"q": "'ㄴ'과 'ㄷ'의 공통점은? (조음 위치 기준)", "a": "둘 다 치조음(잇몸소리)"}, {"q": "'ㅁ'과 'ㅂ'의 공통점은? (조음 위치 기준)", "a": "둘 다 양순음(입술소리)"}, {"q": "'ㅇ'과 'ㄱ'의 공통점은? (조음 위치 기준)", "a": "둘 다 연구개음"}, {"q": "'ㅈ'과 'ㅅ'은 조음 방법이 어떻게 다른가?", "a": "ㅈ은 파찰음, ㅅ은 마찰음"}, {"q": "'ㄱ'과 'ㅇ'은 조음 방법이 어떻게 다른가?", "a": "ㄱ은 파열음, ㅇ은 비음"}, {"q": "코로 공기를 내보내며 내는 자음을 무엇이라 하는가?", "a": "비음(ㄴ,ㅁ,ㅇ)"}, {"q": "혀를 굴리거나 떨어 내는 자음을 무엇이라 하는가?", "a": "유음(ㄹ)"}, {"q": "공기를 막았다가 터뜨려 내는 소리는?", "a": "파열음"}, {"q": "공기를 막았다가 좁은 틈으로 마찰시키며 터뜨리는 소리는?", "a": "파찰음"}, {"q": "좁은 틈으로 공기를 내보내 마찰시키는 소리는?", "a": "마찰음"}, {"q": "'ㅏ'와 'ㅗ'의 차이는? (입술 모양 기준)", "a": "ㅏ는 평순, ㅗ는 원순"}, {"q": "'ㅣ'와 'ㅡ'의 차이는? (혀의 앞뒤 기준)", "a": "ㅣ는 전설, ㅡ는 후설"}, {"q": "'ㅐ'와 'ㅔ'는 혀의 높이가 어떻게 다른가?", "a": "ㅐ는 저모음, ㅔ는 중모음"}, {"q": "'ㅜ'와 'ㅗ'는 혀의 높이가 어떻게 다른가?", "a": "ㅜ는 고모음, ㅗ는 중모음"}, {"q": "전설 원순 모음 두 가지는?", "a": "ㅟ, ㅚ"}, {"q": "후설 원순 모음 두 가지는?", "a": "ㅜ, ㅗ"}, {"q": "전설 평순 고모음은?", "a": "ㅣ"}, {"q": "후설 평순 저모음은?", "a": "ㅏ"}, {"q": "소리의 세기에 따라 자음을 셋으로 나눈 갈래는?", "a": "예사소리·된소리·거센소리"}, {"q": "목청의 울림 여부에 따라 소리를 둘로 나눈 갈래는?", "a": "울림소리·안울림소리"}, {"q": "'ㅅ'의 된소리는 무엇이며 거센소리는 없는가?", "a": "된소리는 ㅆ, 거센소리는 없음"}]

HTML = r'''
<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Jua&family=Gaegu:wght@700&display=swap" rel="stylesheet">
<style>
*{margin:0;padding:0;box-sizing:border-box;font-family:'Jua','Gaegu',sans-serif;}
html,body{width:100%;height:100%;overflow:hidden;}
#wrap{position:fixed;inset:0;background:
   radial-gradient(circle at 20% 15%,#bff0ff 0%,transparent 40%),
   radial-gradient(circle at 80% 10%,#ffe3a3 0%,transparent 35%),
   linear-gradient(180deg,#8fd8ff 0%,#a8e6ff 35%,#cdf3c4 100%);}
.cloud{position:absolute;background:#fff;border-radius:50%;opacity:.85;filter:blur(1px);animation:float 22s linear infinite;}
@keyframes float{from{transform:translateX(-15vw)}to{transform:translateX(115vw)}}
#stage{position:absolute;left:50%;top:50%;width:1280px;height:720px;transform-origin:center center;}

/* ===== 시작 타이틀 ===== */
#setup{position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:flex-start;padding-top:18px;}
.bigtitle{font-size:62px;color:#fff;text-align:center;line-height:1.05;
  text-shadow:0 4px 0 #ff8fc7,0 8px 0 #e85fae,0 12px 14px rgba(0,0,0,.25);
  animation:bounce 1.6s ease-in-out infinite;}
.bigtitle .o{color:#fff36b;text-shadow:0 4px 0 #f2b705,0 8px 0 #d99e00,0 12px 14px rgba(0,0,0,.25);}
@keyframes bounce{0%,100%{transform:translateY(0)}50%{transform:translateY(-10px)}}
.subt{margin-top:6px;font-size:21px;color:#3a5a8c;background:#ffffffbb;padding:4px 16px;border-radius:14px;}
.panel{margin-top:14px;background:#fffdf7;border:5px solid #ffd36b;border-radius:22px;
  padding:14px 20px;box-shadow:0 10px 0 #e9b94a,0 16px 24px rgba(0,0,0,.18);width:880px;}
.row{display:flex;gap:8px;align-items:center;margin-bottom:8px;flex-wrap:wrap;}
.row label{font-size:17px;color:#7a5a18;width:74px;}
input[type=text]{font-size:17px;padding:7px 10px;border:3px solid #ffd36b;border-radius:12px;outline:none;background:#fff;}
.charpick{display:flex;gap:5px;flex-wrap:wrap;}
.charbtn{font-size:26px;width:44px;height:44px;border:3px solid #eee;border-radius:12px;background:#fff;cursor:pointer;transition:.12s;}
.charbtn.sel{border-color:#ff5fa2;background:#ffe9f3;transform:scale(1.12);}
.teamcard{border:3px dashed #ffcf5f;border-radius:16px;padding:8px 12px;margin-bottom:8px;background:#fffef9;}
.btn{font-size:19px;padding:9px 22px;border:none;border-radius:16px;cursor:pointer;color:#fff;
  background:#ff5fa2;box-shadow:0 5px 0 #d63d83;transition:.1s;}
.btn:active{transform:translateY(3px);box-shadow:0 2px 0 #d63d83;}
.btn.g{background:#34c759;box-shadow:0 5px 0 #239b43;}
.btn.b{background:#3a8bff;box-shadow:0 5px 0 #2667c9;}
.btn.y{background:#ffb800;box-shadow:0 5px 0 #cc9300;color:#5a3d00;}
.btn.sm{font-size:15px;padding:6px 14px;border-radius:12px;}
.hint{font-size:14px;color:#9a7b3a;margin-top:4px;}

/* ===== 게임 보드 ===== */
#game{position:absolute;inset:0;display:none;}
#boardArea{position:absolute;left:336px;top:40px;width:640px;height:640px;perspective:1400px;}
#board{position:relative;width:100%;height:100%;transform:rotateX(20deg);transform-style:preserve-3d;}
.cell{position:absolute;border-radius:12px;display:flex;flex-direction:column;align-items:center;justify-content:center;
  text-align:center;color:#3a2a10;border:3px solid rgba(255,255,255,.7);
  box-shadow:0 7px 0 rgba(0,0,0,.22), inset 0 2px 6px rgba(255,255,255,.6);overflow:hidden;}
.cell .ic{font-size:22px;line-height:1;}
.cell .lb{font-size:12px;margin-top:2px;font-weight:bold;}
.cell.q{background:#fff7d6;}
.cell.gold{background:#ffe08a;}
.cell.island{background:#9fd3ff;}
.cell.start{background:#ffc1dd;}
.cell.pop{animation:pop .4s ease;}
@keyframes pop{0%{transform:scale(1)}40%{transform:scale(1.18)}100%{transform:scale(1)}}
.piece{position:absolute;width:34px;height:34px;border-radius:50%;display:flex;align-items:center;justify-content:center;
  font-size:22px;background:#fff;border:3px solid #ff5fa2;box-shadow:0 5px 8px rgba(0,0,0,.3);
  transition:left .28s cubic-bezier(.34,1.56,.64,1),top .28s cubic-bezier(.34,1.56,.64,1);z-index:30;}
.piece.hop{animation:hop .28s ease;}
@keyframes hop{0%{transform:translateY(0)}50%{transform:translateY(-26px) scale(1.12)}100%{transform:translateY(0)}}

/* 점수판 */
#score{position:absolute;left:14px;top:40px;width:300px;background:#fffdf7ee;border:4px solid #ffd36b;
  border-radius:18px;padding:10px 12px;box-shadow:0 8px 0 #e9b94a;}
#score h3{font-size:18px;color:#c0392b;text-align:center;margin-bottom:6px;}
.srow{border-radius:12px;padding:6px 8px;margin-bottom:6px;border:2px solid #f0e2bf;background:#fff;}
.srow .top{display:flex;justify-content:space-between;align-items:center;font-size:16px;}
.srow .sc{font-weight:bold;font-size:18px;color:#1f7a3d;}
.srow .mem{font-size:12px;color:#777;margin-top:2px;line-height:1.3;}
.srow.cur{border-color:#ff5fa2;background:#fff0f7;box-shadow:0 0 0 3px #ffd0e6;}
.srow.bust{opacity:.45;filter:grayscale(.6);}

/* 주사위/조작 */
#ctrl{position:absolute;left:992px;top:40px;width:274px;display:flex;flex-direction:column;align-items:center;gap:10px;}
#dice{width:120px;height:120px;border-radius:24px;background:#fff;border:5px solid #ff5fa2;
  display:flex;align-items:center;justify-content:center;font-size:74px;color:#ff3d8b;
  box-shadow:0 10px 0 #d63d83;}
#dice.shake{animation:shake .5s ease;}
@keyframes shake{0%,100%{transform:rotate(0)}20%{transform:rotate(-16deg) scale(1.05)}40%{transform:rotate(14deg)}60%{transform:rotate(-10deg)}80%{transform:rotate(8deg)}}
#turnInfo{font-size:18px;color:#3a5a8c;text-align:center;background:#ffffffcc;border-radius:12px;padding:6px 10px;width:100%;}
#msg{font-size:15px;color:#8a5a00;text-align:center;min-height:20px;}

/* 오버레이 퀴즈 (칸 위 덮기) */
#overlay{position:absolute;left:336px;top:40px;width:640px;height:640px;display:none;
  align-items:center;justify-content:center;z-index:60;}
#qcard{width:560px;background:#fffdf7;border:6px solid #ff5fa2;border-radius:26px;padding:20px 24px;
  box-shadow:0 14px 0 #d63d83,0 22px 40px rgba(0,0,0,.3);text-align:center;animation:pop .35s ease;}
#qcard .who{font-size:18px;color:#3a8bff;margin-bottom:6px;}
#qcard .qt{font-size:26px;color:#3a2a10;line-height:1.35;margin:8px 0 12px;}
#timer{font-size:60px;color:#e74c3c;font-weight:bold;}
#answerBox{display:none;font-size:24px;color:#1f7a3d;background:#e9ffe9;border:3px dashed #34c759;
  border-radius:14px;padding:10px;margin:10px 0;}
.gold-evt{font-size:22px;color:#a05a00;margin:10px 0;line-height:1.4;}

/* 결과 */
#result{position:absolute;inset:0;display:none;align-items:center;justify-content:center;z-index:80;background:#0008;}
#resultCard{background:#fffdf7;border:8px solid #ffd36b;border-radius:30px;padding:40px 60px;text-align:center;
  box-shadow:0 20px 50px rgba(0,0,0,.4);}
#resultCard h1{font-size:52px;color:#ff3d8b;margin-bottom:10px;}
#resultCard p{font-size:24px;color:#555;margin-bottom:18px;}

/* 하단 제작자 — 우측 끝, 작게 */
#credit{position:fixed;right:10px;bottom:6px;font-size:12px;color:#5a6b86;opacity:.8;z-index:200;}
#soundBtn{position:fixed;left:10px;bottom:8px;z-index:200;font-size:13px;}
.confetti{position:fixed;width:10px;height:14px;z-index:300;animation:fall 2.6s linear forwards;}
@keyframes fall{to{transform:translateY(110vh) rotate(540deg);opacity:.2}}
</style>
</head>
<body>
<div id="wrap">
  <div class="cloud" style="width:120px;height:46px;top:8%;animation-duration:26s"></div>
  <div class="cloud" style="width:90px;height:36px;top:24%;animation-duration:34s;animation-delay:-8s"></div>
  <div class="cloud" style="width:140px;height:52px;top:5%;animation-duration:40s;animation-delay:-20s"></div>

  <div id="stage">
    <!-- ===== 시작 화면 ===== -->
    <div id="setup">
      <div class="bigtitle">함창중 문법 부르마블<span class="o">(음운)</span></div>
      <div class="subt">중3 국어 · 음운의 종류와 특징 (자음·모음 체계표)</div>
      <div class="panel">
        <div id="teamList"></div>
        <button class="btn y sm" onclick="addTeam()">＋ 모둠 추가</button>
        <div class="hint">모둠을 2~4개 만들고, 구성원(최대 4명)과 캐릭터를 골라 주세요.</div>
        <div style="text-align:center;margin-top:12px;">
          <button class="btn g" onclick="goOrder()">순서 정하러 가기 ▶</button>
        </div>
      </div>
    </div>

    <!-- ===== 게임 화면 ===== -->
    <div id="game">
      <div id="score"></div>
      <div id="boardArea"><div id="board"></div></div>
      <div id="overlay"><div id="qcard"></div></div>
      <div id="ctrl">
        <div id="turnInfo"></div>
        <div id="dice">🎲</div>
        <button class="btn" id="rollBtn" onclick="rollDice()">주사위 던지기 🎲</button>
        <div id="msg"></div>
      </div>
    </div>

    <!-- 결과 -->
    <div id="result"><div id="resultCard"></div></div>
  </div>
</div>
<div id="credit">제작 : 함창고 교사 박호종</div>
<button class="btn b sm" id="soundBtn" onclick="toggleMusic()">🔊 배경음악 ON</button>

<script>
const QUESTIONS = __QUESTIONS__;
const CHARS = ["🐰","🐱","🐶","🐼","🦊","🐯","🐸","🐧","🐥","🦁","🐹","🐨"];
const COLORS = ["#ff5fa2","#3a8bff","#34c759","#ff9f1c","#9b59b6","#16a085"];

/* ---------- 무대 스케일 (스크롤 없이 한 화면) ---------- */
function fit(){
  const s=Math.min(window.innerWidth/1300, window.innerHeight/760);
  document.getElementById('stage').style.transform='translate(-50%,-50%) scale('+s+')';
}
window.addEventListener('resize',fit); fit();

/* ---------- 시작화면: 모둠/캐릭터 ---------- */
let setupTeams=[];
function addTeam(){
  if(setupTeams.length>=4){alert('모둠은 최대 4개까지!');return;}
  setupTeams.push({name:'모둠'+(setupTeams.length+1),members:['','','',''],char:CHARS[setupTeams.length]});
  renderSetup();
}
function renderSetup(){
  let h='';
  setupTeams.forEach((t,i)=>{
    h+='<div class="teamcard">';
    h+='<div class="row"><label>모둠명</label><input type="text" value="'+t.name+'" oninput="setupTeams['+i+'].name=this.value"> ';
    h+='<button class="btn sm" style="background:#e74c3c;box-shadow:0 4px 0 #b03228" onclick="delTeam('+i+')">삭제</button></div>';
    h+='<div class="row"><label>구성원</label>';
    for(let m=0;m<4;m++) h+='<input type="text" style="width:110px" placeholder="학생'+(m+1)+'" value="'+t.members[m]+'" oninput="setupTeams['+i+'].members['+m+']=this.value">';
    h+='</div>';
    h+='<div class="row"><label>캐릭터</label><div class="charpick">';
    CHARS.forEach(c=>{h+='<button class="charbtn '+(t.char===c?'sel':'')+'" onclick="setupTeams['+i+'].char=\''+c+'\';renderSetup()">'+c+'</button>';});
    h+='</div></div></div>';
  });
  document.getElementById('teamList').innerHTML=h;
}
function delTeam(i){setupTeams.splice(i,1);renderSetup();}
addTeam();addTeam();

/* ---------- 보드 구성 (10x10 둘레 = 36칸) ---------- */
const N=10, PER=(N-1)*4; // 36
function buildLayout(){
  // 둘레 좌표 (격자 index 0~9). 시계방향: 하단변→우변→상단변→좌변
  let coords=[];
  for(let x=0;x<N;x++) coords.push([x,N-1]);      // 하단 (왼→오) 0..9
  for(let y=N-2;y>=0;y--) coords.push([N-1,y]);    // 우변 (아래→위)
  for(let x=N-2;x>=0;x--) coords.push([x,0]);       // 상단 (오→왼)
  for(let y=1;y<N-1;y++) coords.push([0,y]);        // 좌변 (위→아래)
  // 타입 지정
  let cells=coords.map((c,i)=>({x:c[0],y:c[1],type:'q'}));
  cells[0].type='start';                 // 좌하단 출발
  cells[N-1].type='gold';                // 우하단
  cells[2*(N-1)].type='island';          // 우상단
  cells[3*(N-1)].type='gold';            // 좌상단
  // 변 중간에 황금열쇠/무인도 추가
  [5,14,23,32].forEach(i=>cells[i].type='gold');
  [9].forEach(()=>{}); // 코너 외
  cells[18].type='island';
  return cells;
}
const LAYOUT=buildLayout();
const GOLD_EVENTS=[
 {t:"🎁 생일 축하금!",d:"이번 달 생일인 친구가 있으면 +15점! 없으면 +5점.",pt:15},
 {t:"💸 벌금!",d:"숙제 안 한 친구가 있으면 -10점! (단합으로 막아보세요)",pt:-10},
 {t:"🤝 단합력 테스트!",d:"모둠 전원이 구호를 외치면 +10점!",pt:10},
 {t:"🎤 개인기 찬스!",d:"한 명이 개인기를 선보이면 +12점!",pt:12},
 {t:"🍀 행운의 황금열쇠!",d:"공짜로 +8점 획득!",pt:8},
 {t:"📚 복습 보너스!",d:"방금 배운 음운 개념 하나를 외치면 +10점!",pt:10},
];

/* ---------- 게임 상태 ---------- */
let G=null;
function goOrder(){
  let ts=setupTeams.filter(t=>t.name.trim());
  if(ts.length<2){alert('모둠을 2개 이상 만들어 주세요!');return;}
  // 순서 랜덤
  let order=ts.map((_,i)=>i);
  for(let i=order.length-1;i>0;i--){let j=Math.floor(Math.random()*(i+1));[order[i],order[j]]=[order[j],order[i]];}
  G={teams:ts.map(t=>({
        name:t.name.trim(),char:t.char,
        members:t.members.map(m=>m.trim()).filter(m=>m),
        score:100,pos:0,skip:0,bust:false,
        ind:{}
     })),
     order, ptr:0, qIdx:0, phase:'roll', curStudent:'', wrongTeams:[]};
  G.teams.forEach(t=>{ if(t.members.length===0)t.members=['전체']; t.members.forEach(m=>t.ind[m]=0); });
  document.getElementById('setup').style.display='none';
  document.getElementById('game').style.display='block';
  buildBoard();
  let names=G.order.map(i=>G.teams[i].name).join(' → ');
  setMsg('🎲 순서: '+names);
  render();
  startMusic();
}

function buildBoard(){
  const board=document.getElementById('board');
  board.innerHTML='';
  const size=640, gap=6, cs=(size-gap)/N - gap; // 셀 한 변
  // 칸을 크게: 둘레 칸을 격자에 꽉 차게 배치
  LAYOUT.forEach((c,i)=>{
    const el=document.createElement('div');
    el.className='cell '+c.type; el.id='cell'+i;
    const w=(size-gap*2)/N;
    el.style.width=(w-gap)+'px'; el.style.height=(w-gap)+'px';
    el.style.left=(c.x*w+gap)+'px'; el.style.top=(c.y*w+gap)+'px';
    let ic='📝',lb='문제';
    if(c.type==='start'){ic='🏁';lb='출발 +5';}
    else if(c.type==='gold'){ic='🗝️';lb='황금열쇠';}
    else if(c.type==='island'){ic='🏝️';lb='무인도';}
    el.innerHTML='<div class="ic">'+ic+'</div><div class="lb">'+lb+'</div>';
    board.appendChild(el);
  });
  // 말 생성
  G.teams.forEach((t,ti)=>{
    const p=document.createElement('div');
    p.className='piece'; p.id='piece'+ti; p.textContent=t.char;
    p.style.borderColor=COLORS[ti%COLORS.length];
    document.getElementById('board').appendChild(p);
    placePiece(ti,0);
  });
}
function cellCenter(idx){
  const size=640,gap=6,w=(size-gap*2)/N;
  const c=LAYOUT[idx];
  return {x:c.x*w+gap+(w-gap)/2, y:c.y*w+gap+(w-gap)/2};
}
function placePiece(ti,idx){
  const teamsOnCell=G.teams.filter((t,k)=>t.pos===idx).length;
  const order=G.teams.filter((t,k)=>t.pos===idx);
  const ctr=cellCenter(idx);
  // 같은 칸 여러 말 살짝 분산
  let myRank=0,cnt=0;
  for(let k=0;k<G.teams.length;k++){if(G.teams[k].pos===idx){if(k===ti)myRank=cnt;cnt++;}}
  const off=(myRank-(cnt-1)/2)*16;
  const p=document.getElementById('piece'+ti);
  p.style.left=(ctr.x-17+off)+'px';
  p.style.top=(ctr.y-17-(myRank*3))+'px';
}

/* ---------- 점수판 ---------- */
function render(){
  let h='<h3>🏆 점수 현황판</h3>';
  G.teams.forEach((t,ti)=>{
    const isCur=(G.order[G.ptr]===ti && G.phase!=='end');
    h+='<div class="srow'+(isCur?' cur':'')+(t.bust?' bust':'')+'">';
    h+='<div class="top"><span>'+t.char+' '+t.name+(t.bust?' 💥파산':'')+'</span><span class="sc">'+t.score+'점</span></div>';
    h+='<div class="mem">'+t.members.map(m=>m+' '+(t.ind[m]>=0?'+':'')+t.ind[m]).join(' · ')+'</div>';
    h+='</div>';
  });
  document.getElementById('score').innerHTML=h;
  const cur=G.teams[G.order[G.ptr]];
  document.getElementById('turnInfo').innerHTML=(G.phase==='end')?'게임 종료':('지금 차례<br><b style="font-size:22px;color:#ff3d8b">'+cur.char+' '+cur.name+'</b>');
}
function setMsg(m){document.getElementById('msg').innerHTML=m;}

/* ---------- 주사위 & 이동 ---------- */
let busy=false;
function rollDice(){
  if(busy||G.phase==='end')return; if(G.phase!=='roll')return;
  const cur=G.teams[G.order[G.ptr]];
  if(cur.skip>0){cur.skip--;sfx('skip');setMsg('🏝️ '+cur.name+' 무인도에서 1턴 쉽니다!');nextTeam();render();return;}
  busy=true;
  const dice=document.getElementById('dice'); dice.classList.add('shake'); sfx('dice');
  let ticks=0;const iv=setInterval(()=>{dice.textContent=1+Math.floor(Math.random()*6);ticks++;
    if(ticks>10){clearInterval(iv);const n=1+Math.floor(Math.random()*6);dice.textContent=n;dice.classList.remove('shake');
      setMsg('🎲 '+n+' 칸 이동!');movePiece(G.order[G.ptr],n);}},60);
}
function movePiece(ti,steps){
  const t=G.teams[ti];let done=0;
  const step=()=>{
    if(done>=steps){afterMove(ti);return;}
    let prev=t.pos; t.pos=(t.pos+1)%PER;
    if(t.pos===0){ t.score+=5; sfx('coin'); setMsg('🏁 출발 통과! +5점 보너스!'); }
    const p=document.getElementById('piece'+ti); p.classList.add('hop');
    placePiece(ti,t.pos);
    setTimeout(()=>p.classList.remove('hop'),280);
    done++; render(); setTimeout(step,300);
  };
  step();
}
function afterMove(ti){
  const t=G.teams[ti];
  const cell=LAYOUT[t.pos];
  const el=document.getElementById('cell'+t.pos); el.classList.add('pop');setTimeout(()=>el.classList.remove('pop'),400);
  if(cell.type==='island'){ t.skip=1; sfx('skip'); setMsg('🏝️ 무인도! 다음 턴 1번 쉽니다.'); busy=false; G.phase='roll'; nextTeam(); render(); return; }
  if(cell.type==='gold'){ goldEvent(ti); return; }
  // 문제칸 / 출발칸도 문제 → 학생 무작위 지정 후 퀴즈
  askQuiz(ti);
}

/* ---------- 황금열쇠 ---------- */
function goldEvent(ti){
  const t=G.teams[ti];
  const ev=GOLD_EVENTS[Math.floor(Math.random()*GOLD_EVENTS.length)];
  sfx('gold');
  showOverlay('<div class="who">'+t.char+' '+t.name+' · 황금열쇠</div>'
    +'<div style="font-size:34px;margin:6px">🗝️</div>'
    +'<div class="qt">'+ev.t+'</div><div class="gold-evt">'+ev.d+'</div>'
    +'<button class="btn '+(ev.pt>=0?'g':'')+'" onclick="applyGold('+ti+','+ev.pt+')">확인 ('+(ev.pt>=0?'+':'')+ev.pt+'점)</button>');
}
function applyGold(ti,pt){
  const t=G.teams[ti]; t.score+=pt;
  const m=t.members[Math.floor(Math.random()*t.members.length)]; t.ind[m]+=pt;
  sfx(pt>=0?'correct':'wrong'); hideOverlay(); render();
  if(checkEnd())return;
  G.phase='roll'; busy=false; nextTeam(); render();
}

/* ---------- 퀴즈 ---------- */
let timerIV=null;
function askQuiz(ti,forced){
  const t=G.teams[ti];
  const student=t.members[Math.floor(Math.random()*t.members.length)];
  G.curStudent=student;
  const q=QUESTIONS[G.qIdx%QUESTIONS.length]; G.qIdx++;
  G.curQ=q;
  let cd=10;
  showOverlay(
    '<div class="who">'+t.char+' '+t.name+' · 답변자: <b>'+student+'</b></div>'
    +'<div class="qt">'+q.q+'</div>'
    +'<div id="timer">'+cd+'</div>'
    +'<div id="answerBox">정답: '+q.a+'</div>'
    +'<div id="qbtns"></div>');
  document.getElementById('qbtns').innerHTML='<button class="btn b" onclick="revealAnswer('+ti+')">정답 공개 👀</button>';
  clearInterval(timerIV);
  timerIV=setInterval(()=>{cd--;const tm=document.getElementById('timer');if(tm)tm.textContent=cd;if(cd<=3)sfx('tick');
    if(cd<=0){clearInterval(timerIV);if(document.getElementById('timer'))document.getElementById('timer').textContent='⏰';sfx('timeup');}},1000);
}
function revealAnswer(ti){
  clearInterval(timerIV);
  document.getElementById('answerBox').style.display='block';
  document.getElementById('qbtns').innerHTML=
     '<button class="btn g" onclick="judge('+ti+',true)">⭕ 정답 (+10)</button> '
    +'<button class="btn" style="background:#e74c3c;box-shadow:0 5px 0 #b03228" onclick="judge('+ti+',false)">❌ 오답 (-10)</button>';
}
function judge(ti,correct){
  const t=G.teams[ti]; const m=G.curStudent;
  if(correct){
    t.score+=10; t.ind[m]+=10; sfx('correct'); hideOverlay(); render();
    if(checkEnd())return;
    G.phase='roll'; busy=false; G.wrongTeams=[]; nextTeam(); render(); setMsg('⭕ 정답! 다음 모둠 차례!');
  }else{
    t.score-=10; t.ind[m]-=10; sfx('wrong'); render();
    if(checkEnd()){hideOverlay();return;}
    // 오답 → 다른 모둠 무작위 찬스
    G.wrongTeams.push(ti);
    let cand=G.teams.map((x,k)=>k).filter(k=>!G.teams[k].bust && !G.wrongTeams.includes(k));
    if(cand.length===0){G.wrongTeams=[];hideOverlay();G.phase='roll';busy=false;nextTeam();render();setMsg('❌ 아무도 못 맞혔어요! 다음 모둠 차례!');return;}
    const nx=cand[Math.floor(Math.random()*cand.length)];
    setMsg('❌ 오답! 찬스가 '+G.teams[nx].char+' '+G.teams[nx].name+' 에게 넘어갑니다!');
    setTimeout(()=>askQuiz(nx,true),700);
  }
}

/* ---------- 턴/종료 ---------- */
function nextTeam(){
  let n=G.order.length,c=0;
  do{G.ptr=(G.ptr+1)%n;c++;}while(G.teams[G.order[G.ptr]].bust && c<=n);
}
function checkEnd(){
  // 파산
  G.teams.forEach(t=>{if(!t.bust && t.score<=-100){t.bust=true;sfx('bust');setMsg('💥 '+t.name+' 파산!');}});
  const alive=G.teams.filter(t=>!t.bust);
  // 승리
  let winner=G.teams.find(t=>!t.bust && t.score>=500);
  if(!winner && alive.length===1) winner=alive[0];
  if(winner){endGame(winner);return true;}
  return false;
}
function endGame(w){
  G.phase='end'; busy=false; clearInterval(timerIV); sfx('win'); confetti();
  document.getElementById('result').style.display='flex';
  document.getElementById('resultCard').innerHTML=
    '<h1>🎉 '+w.char+' '+w.name+' 승리! 🎉</h1>'
    +'<p>최종 점수 <b>'+w.score+'점</b><br>축하합니다! 음운 마스터 모둠!</p>'
    +'<button class="btn g" onclick="location.reload()">다시 시작하기 🔄</button>';
}

/* ---------- 오버레이 ---------- */
function showOverlay(html){const o=document.getElementById('overlay');o.style.display='flex';document.getElementById('qcard').innerHTML=html;}
function hideOverlay(){document.getElementById('overlay').style.display='none';}

/* ---------- 효과음 (WebAudio 합성) ---------- */
let AC=null,musicOn=true,musicNodes=[],musicTimer=null;
function ac(){if(!AC){try{AC=new (window.AudioContext||window.webkitAudioContext)();}catch(e){}}return AC;}
function tone(f,d,type,vol,when){const a=ac();if(!a)return;const t=(when||a.currentTime);
  const o=a.createOscillator(),g=a.createGain();o.type=type||'sine';o.frequency.value=f;
  g.gain.setValueAtTime(0,t);g.gain.linearRampToValueAtTime(vol||0.2,t+0.02);
  g.gain.exponentialRampToValueAtTime(0.001,t+d);o.connect(g);g.connect(a.destination);o.start(t);o.stop(t+d);}
function sfx(k){const a=ac();if(!a)return;const n=a.currentTime;
  if(k==='dice'){for(let i=0;i<4;i++)tone(300+i*60,0.06,'square',0.12,n+i*0.05);}
  else if(k==='coin'){tone(880,0.08,'square',0.15,n);tone(1320,0.12,'square',0.15,n+0.08);}
  else if(k==='correct'){[523,659,784,1047].forEach((f,i)=>tone(f,0.2,'triangle',0.2,n+i*0.08));}
  else if(k==='wrong'){tone(300,0.25,'sawtooth',0.2,n);tone(200,0.35,'sawtooth',0.2,n+0.12);}
  else if(k==='gold'){[784,988,1175,1568].forEach((f,i)=>tone(f,0.18,'sine',0.18,n+i*0.07));}
  else if(k==='tick'){tone(880,0.05,'square',0.12,n);}
  else if(k==='timeup'){tone(180,0.5,'sawtooth',0.22,n);}
  else if(k==='skip'){tone(400,0.15,'sine',0.15,n);tone(300,0.2,'sine',0.15,n+0.1);}
  else if(k==='bust'){[400,300,200,120].forEach((f,i)=>tone(f,0.3,'sawtooth',0.22,n+i*0.12));}
  else if(k==='win'){[523,659,784,1047,1319,1047,1319,1568].forEach((f,i)=>tone(f,0.28,'triangle',0.22,n+i*0.13));}
}
/* 배경음악: 밝은 루프 멜로디 */
const MEL=[523,587,659,784,659,587,523,659,784,880,784,659,587,523,587,659];
let melStep=0;
function startMusic(){const a=ac();if(!a||!musicOn)return;if(musicTimer)return;
  const beat=0.34;
  musicTimer=setInterval(()=>{if(!musicOn)return;const f=MEL[melStep%MEL.length];
    tone(f,0.3,'triangle',0.07);tone(f/2,0.3,'sine',0.05);melStep++;},beat*1000);
}
function stopMusic(){if(musicTimer){clearInterval(musicTimer);musicTimer=null;}}
function toggleMusic(){musicOn=!musicOn;const b=document.getElementById('soundBtn');
  if(musicOn){b.textContent='🔊 배경음악 ON';startMusic();}else{b.textContent='🔇 배경음악 OFF';stopMusic();}}
document.body.addEventListener('click',()=>{const a=ac();if(a&&a.state==='suspended')a.resume();},{once:false});

function confetti(){for(let i=0;i<80;i++){const c=document.createElement('div');c.className='confetti';
  c.style.left=Math.random()*100+'vw';c.style.top='-20px';c.style.background=COLORS[i%COLORS.length];
  c.style.animationDelay=(Math.random()*0.8)+'s';document.body.appendChild(c);setTimeout(()=>c.remove(),3200);}}

renderSetup();
</script>
</body>
</html>
'''

html = HTML.replace('__QUESTIONS__', json.dumps(QUESTIONS, ensure_ascii=False))
components.html(html, height=760, scrolling=False)
