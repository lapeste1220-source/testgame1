import json
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="함창중 문법 부르마블(음운)", layout="wide", initial_sidebar_state="collapsed")

# 여백 제거(전체화면 느낌)
st.markdown("""
<style>
#MainMenu{visibility:hidden;} footer{visibility:hidden;} header{visibility:hidden;}
.block-container{padding:0 !important;max-width:100% !important;}
[data-testid="stAppViewContainer"]>.main{padding:0 !important;}
iframe{border:none;}
</style>
""", unsafe_allow_html=True)

QUESTIONS = json.loads(r'''[{"q": "'ㄱ'의 조음 위치와 조음 방법은?", "a": "여린입천장소리(연구개음) · 파열음"}, {"q": "'ㄲ'의 조음 위치와 조음 방법은?", "a": "여린입천장소리(연구개음) · 파열음"}, {"q": "'ㅋ'의 조음 위치와 조음 방법은?", "a": "여린입천장소리(연구개음) · 파열음"}, {"q": "'ㄷ'의 조음 위치와 조음 방법은?", "a": "잇몸소리(치조음) · 파열음"}, {"q": "'ㄸ'의 조음 위치와 조음 방법은?", "a": "잇몸소리(치조음) · 파열음"}, {"q": "'ㅌ'의 조음 위치와 조음 방법은?", "a": "잇몸소리(치조음) · 파열음"}, {"q": "'ㅂ'의 조음 위치와 조음 방법은?", "a": "입술소리(양순음) · 파열음"}, {"q": "'ㅃ'의 조음 위치와 조음 방법은?", "a": "입술소리(양순음) · 파열음"}, {"q": "'ㅍ'의 조음 위치와 조음 방법은?", "a": "입술소리(양순음) · 파열음"}, {"q": "'ㅈ'의 조음 위치와 조음 방법은?", "a": "센입천장소리(경구개음) · 파찰음"}, {"q": "'ㅉ'의 조음 위치와 조음 방법은?", "a": "센입천장소리(경구개음) · 파찰음"}, {"q": "'ㅊ'의 조음 위치와 조음 방법은?", "a": "센입천장소리(경구개음) · 파찰음"}, {"q": "'ㅅ'의 조음 위치와 조음 방법은?", "a": "잇몸소리(치조음) · 마찰음"}, {"q": "'ㅆ'의 조음 위치와 조음 방법은?", "a": "잇몸소리(치조음) · 마찰음"}, {"q": "'ㅎ'의 조음 위치와 조음 방법은?", "a": "목청소리(후음) · 마찰음"}, {"q": "'ㅁ'의 조음 위치와 조음 방법은?", "a": "입술소리(양순음) · 비음"}, {"q": "'ㄴ'의 조음 위치와 조음 방법은?", "a": "잇몸소리(치조음) · 비음"}, {"q": "'ㅇ'의 조음 위치와 조음 방법은?", "a": "여린입천장소리(연구개음) · 비음"}, {"q": "'ㄹ'의 조음 위치와 조음 방법은?", "a": "잇몸소리(치조음) · 유음"}, {"q": "'ㅂ'의 조음 위치(소리 나는 자리)는?", "a": "입술소리(양순음)"}, {"q": "'ㅁ'의 조음 위치(소리 나는 자리)는?", "a": "입술소리(양순음)"}, {"q": "'ㅍ'의 조음 위치(소리 나는 자리)는?", "a": "입술소리(양순음)"}, {"q": "'ㄷ'의 조음 위치(소리 나는 자리)는?", "a": "잇몸소리(치조음)"}, {"q": "'ㅌ'의 조음 위치(소리 나는 자리)는?", "a": "잇몸소리(치조음)"}, {"q": "'ㅅ'의 조음 위치(소리 나는 자리)는?", "a": "잇몸소리(치조음)"}, {"q": "'ㄴ'의 조음 위치(소리 나는 자리)는?", "a": "잇몸소리(치조음)"}, {"q": "'ㄹ'의 조음 위치(소리 나는 자리)는?", "a": "잇몸소리(치조음)"}, {"q": "'ㅈ'의 조음 위치(소리 나는 자리)는?", "a": "센입천장소리(경구개음)"}, {"q": "'ㅊ'의 조음 위치(소리 나는 자리)는?", "a": "센입천장소리(경구개음)"}, {"q": "'ㄱ'의 조음 위치(소리 나는 자리)는?", "a": "여린입천장소리(연구개음)"}, {"q": "'ㅋ'의 조음 위치(소리 나는 자리)는?", "a": "여린입천장소리(연구개음)"}, {"q": "'ㅇ'의 조음 위치(소리 나는 자리)는?", "a": "여린입천장소리(연구개음)"}, {"q": "'ㅎ'의 조음 위치(소리 나는 자리)는?", "a": "목청소리(후음)"}, {"q": "'ㅂ'의 조음 방법(소리 내는 방법)은?", "a": "파열음"}, {"q": "'ㄷ'의 조음 방법(소리 내는 방법)은?", "a": "파열음"}, {"q": "'ㄱ'의 조음 방법(소리 내는 방법)은?", "a": "파열음"}, {"q": "'ㅈ'의 조음 방법(소리 내는 방법)은?", "a": "파찰음"}, {"q": "'ㅊ'의 조음 방법(소리 내는 방법)은?", "a": "파찰음"}, {"q": "'ㅅ'의 조음 방법(소리 내는 방법)은?", "a": "마찰음"}, {"q": "'ㅆ'의 조음 방법(소리 내는 방법)은?", "a": "마찰음"}, {"q": "'ㅎ'의 조음 방법(소리 내는 방법)은?", "a": "마찰음"}, {"q": "'ㅁ'의 조음 방법(소리 내는 방법)은?", "a": "비음"}, {"q": "'ㄴ'의 조음 방법(소리 내는 방법)은?", "a": "비음"}, {"q": "'ㅇ'의 조음 방법(소리 내는 방법)은?", "a": "비음"}, {"q": "'ㄹ'의 조음 방법(소리 내는 방법)은?", "a": "유음"}, {"q": "'ㅋ'의 조음 방법(소리 내는 방법)은?", "a": "파열음"}, {"q": "'ㅌ'의 조음 방법(소리 내는 방법)은?", "a": "파열음"}, {"q": "입술소리(양순음)에 해당하는 자음을 모두 쓰시오.", "a": "ㅂ, ㅃ, ㅍ, ㅁ"}, {"q": "잇몸소리(치조음)에 해당하는 자음을 모두 쓰시오.", "a": "ㄷ, ㄸ, ㅌ, ㅅ, ㅆ, ㄴ, ㄹ"}, {"q": "센입천장소리(경구개음)에 해당하는 자음을 모두 쓰시오.", "a": "ㅈ, ㅉ, ㅊ"}, {"q": "여린입천장소리(연구개음)에 해당하는 자음을 모두 쓰시오.", "a": "ㄱ, ㄲ, ㅋ, ㅇ"}, {"q": "목청소리(후음)에 해당하는 자음을 쓰시오.", "a": "ㅎ"}, {"q": "파열음에 해당하는 자음을 모두 쓰시오.", "a": "ㅂ,ㅃ,ㅍ, ㄷ,ㄸ,ㅌ, ㄱ,ㄲ,ㅋ"}, {"q": "파찰음에 해당하는 자음을 모두 쓰시오.", "a": "ㅈ, ㅉ, ㅊ"}, {"q": "마찰음에 해당하는 자음을 모두 쓰시오.", "a": "ㅅ, ㅆ, ㅎ"}, {"q": "비음에 해당하는 자음을 모두 쓰시오.", "a": "ㅁ, ㄴ, ㅇ"}, {"q": "유음에 해당하는 자음을 쓰시오.", "a": "ㄹ"}, {"q": "울림소리(유성음)에 해당하는 자음을 모두 쓰시오.", "a": "ㄴ, ㄹ, ㅁ, ㅇ"}, {"q": "비음 3개를 모두 쓰시오.", "a": "ㅁ, ㄴ, ㅇ"}, {"q": "코로 공기를 내보내며 소리 내는 자음(비음)을 모두 쓰시오.", "a": "ㅁ, ㄴ, ㅇ"}, {"q": "혀끝을 잇몸에 댔다 떼거나 굴려 내는 소리(유음)는?", "a": "ㄹ"}, {"q": "예사소리 'ㄱ'의 된소리와 거센소리를 차례로 쓰시오.", "a": "된소리 ㄲ, 거센소리 ㅋ"}, {"q": "예사소리 'ㄷ'의 된소리와 거센소리를 차례로 쓰시오.", "a": "된소리 ㄸ, 거센소리 ㅌ"}, {"q": "예사소리 'ㅂ'의 된소리와 거센소리를 차례로 쓰시오.", "a": "된소리 ㅃ, 거센소리 ㅍ"}, {"q": "예사소리 'ㅈ'의 된소리와 거센소리를 차례로 쓰시오.", "a": "된소리 ㅉ, 거센소리 ㅊ"}, {"q": "예사소리 'ㅅ'의 된소리를 쓰시오. (거센소리는 없음)", "a": "된소리 ㅆ"}, {"q": "예사소리·된소리·거센소리 중 'ㄲ, ㄸ, ㅃ, ㅆ, ㅉ'은 무엇인가?", "a": "된소리"}, {"q": "예사소리·된소리·거센소리 중 'ㅋ, ㅌ, ㅍ, ㅊ'은 무엇인가?", "a": "거센소리"}, {"q": "예사소리(평음)에 해당하는 파열음·파찰음을 모두 쓰시오.", "a": "ㄱ, ㄷ, ㅂ, ㅈ"}, {"q": "국어의 단모음은 모두 몇 개이며 무엇인가?", "a": "10개: ㅏ,ㅐ,ㅓ,ㅔ,ㅗ,ㅚ,ㅜ,ㅟ,ㅡ,ㅣ"}, {"q": "전설모음을 모두 쓰시오.", "a": "ㅣ, ㅔ, ㅐ, ㅟ, ㅚ"}, {"q": "후설모음을 모두 쓰시오.", "a": "ㅡ, ㅓ, ㅏ, ㅜ, ㅗ"}, {"q": "고모음(혀의 높이가 높은 모음)을 모두 쓰시오.", "a": "ㅣ, ㅟ, ㅡ, ㅜ"}, {"q": "중모음을 모두 쓰시오.", "a": "ㅔ, ㅚ, ㅓ, ㅗ"}, {"q": "저모음을 모두 쓰시오.", "a": "ㅐ, ㅏ"}, {"q": "원순모음(입술을 둥글게 하는 모음)을 모두 쓰시오.", "a": "ㅟ, ㅚ, ㅜ, ㅗ"}, {"q": "평순모음을 모두 쓰시오.", "a": "ㅣ, ㅔ, ㅐ, ㅡ, ㅓ, ㅏ"}, {"q": "단모음 'ㅣ'의 분류를 '혀의 앞뒤/혀의 높이/입술 모양' 순으로 쓰시오.", "a": "전설모음 · 고모음 · 평순모음"}, {"q": "단모음 'ㅔ'의 분류를 '혀의 앞뒤/혀의 높이/입술 모양' 순으로 쓰시오.", "a": "전설모음 · 중모음 · 평순모음"}, {"q": "단모음 'ㅐ'의 분류를 '혀의 앞뒤/혀의 높이/입술 모양' 순으로 쓰시오.", "a": "전설모음 · 저모음 · 평순모음"}, {"q": "단모음 'ㅟ'의 분류를 '혀의 앞뒤/혀의 높이/입술 모양' 순으로 쓰시오.", "a": "전설모음 · 고모음 · 원순모음"}, {"q": "단모음 'ㅚ'의 분류를 '혀의 앞뒤/혀의 높이/입술 모양' 순으로 쓰시오.", "a": "전설모음 · 중모음 · 원순모음"}, {"q": "단모음 'ㅡ'의 분류를 '혀의 앞뒤/혀의 높이/입술 모양' 순으로 쓰시오.", "a": "후설모음 · 고모음 · 평순모음"}, {"q": "단모음 'ㅓ'의 분류를 '혀의 앞뒤/혀의 높이/입술 모양' 순으로 쓰시오.", "a": "후설모음 · 중모음 · 평순모음"}, {"q": "단모음 'ㅏ'의 분류를 '혀의 앞뒤/혀의 높이/입술 모양' 순으로 쓰시오.", "a": "후설모음 · 저모음 · 평순모음"}, {"q": "단모음 'ㅜ'의 분류를 '혀의 앞뒤/혀의 높이/입술 모양' 순으로 쓰시오.", "a": "후설모음 · 고모음 · 원순모음"}, {"q": "단모음 'ㅗ'의 분류를 '혀의 앞뒤/혀의 높이/입술 모양' 순으로 쓰시오.", "a": "후설모음 · 중모음 · 원순모음"}, {"q": "'ㅣ'는 혀의 높이가 높은가 낮은가? (고/중/저)", "a": "고모음"}, {"q": "'ㅜ'는 혀의 높이가 높은가 낮은가? (고/중/저)", "a": "고모음"}, {"q": "'ㅡ'는 혀의 높이가 높은가 낮은가? (고/중/저)", "a": "고모음"}, {"q": "'ㅟ'는 혀의 높이가 높은가 낮은가? (고/중/저)", "a": "고모음"}, {"q": "'ㅏ'는 혀의 높이로 보면 어떤 모음인가? (고/중/저)", "a": "저모음"}, {"q": "'ㅗ'는 입술 모양으로 보면 어떤 모음인가? (평순/원순)", "a": "원순모음"}, {"q": "'ㅓ'는 혀의 앞뒤 위치로 보면 어떤 모음인가? (전설/후설)", "a": "후설모음"}, {"q": "'ㅔ'와 'ㅐ'의 공통점은? (혀 위치/입술 모양 기준)", "a": "둘 다 전설모음이며 평순모음"}, {"q": "'ㅚ'와 'ㅟ'의 공통점은? (혀 위치/입술 모양 기준)", "a": "둘 다 전설모음이며 원순모음"}, {"q": "발음할 때 입술 모양이나 혀의 위치가 변하지 않는 모음을 무엇이라 하는가?", "a": "단모음"}, {"q": "발음 도중 입술 모양이나 혀의 위치가 변하는 모음을 무엇이라 하는가?", "a": "이중모음"}, {"q": "이중모음을 만들 때 쓰이는 반모음 2가지는?", "a": "ㅣ계(j), ㅗ/ㅜ계(w)"}, {"q": "자음과 모음을 합쳐 국어의 음운(분절 음운)은 모두 몇 개인가?", "a": "자음 19개 + 모음 21개 = 40개"}]''')

GAME_HTML = r'''<!DOCTYPE html>
<html lang="ko"><head><meta charset="utf-8">
<style>
@import url('https://fonts.googleapis.com/css2?family=Jua&family=Gaegu:wght@700&display=swap');
*{margin:0;padding:0;box-sizing:border-box;font-family:'Jua','Gaegu',sans-serif;-webkit-user-select:none;user-select:none;}
html,body{width:100%;height:100%;overflow:hidden;background:#0b1020;}
#wrap{position:fixed;inset:0;display:flex;align-items:center;justify-content:center;
  background:linear-gradient(180deg,#aee3ff 0%,#d6f0ff 40%,#ffe6b8 78%,#bdf0c6 100%);}
#stage{position:relative;width:1520px;height:856px;transform-origin:center center;}
.cloud{position:absolute;background:#fff;border-radius:50%;opacity:.85;filter:blur(1px);}
/* ===== 공통 버튼 ===== */
.btn{cursor:pointer;border:none;border-radius:16px;font-family:'Jua',sans-serif;color:#fff;
  box-shadow:0 5px 0 rgba(0,0,0,.18);transition:transform .08s,box-shadow .08s;}
.btn:active{transform:translateY(4px);box-shadow:0 1px 0 rgba(0,0,0,.18);}
.btn.pink{background:#ff7eb3;}.btn.blue{background:#5aa9ff;}.btn.green{background:#46c98b;}
.btn.orange{background:#ffa53b;}.btn.red{background:#ff6b6b;}.btn.purple{background:#b08bff;}.btn.gray{background:#9aa6b2;}
/* ===== 타이틀 ===== */
#title{text-align:center;}
#title h1{font-size:64px;letter-spacing:1px;line-height:1;
  color:#fff;text-shadow:0 5px 0 #ff7eb3,0 9px 14px rgba(0,0,0,.18);animation:bob 2.4s ease-in-out infinite;}
#title h1 .y{color:#ffd23f;text-shadow:0 5px 0 #ff9f1c,0 9px 14px rgba(0,0,0,.18);}
@keyframes bob{0%,100%{transform:translateY(0)}50%{transform:translateY(-9px)}}
#title .sub{display:inline-block;margin-top:12px;background:#fff;color:#ff5fa2;
  font-size:20px;padding:7px 22px;border-radius:30px;box-shadow:0 4px 0 #ffd0e3;}
/* ===== 시작 설정 ===== */
#setup{position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;padding-top:14px;}
#panel{margin-top:10px;width:980px;background:rgba(255,255,255,.78);border:4px dashed #ffc36b;border-radius:26px;padding:16px 22px;}
#teamList{max-height:330px;overflow-y:auto;padding-right:8px;}
#teamList::-webkit-scrollbar{width:12px;}#teamList::-webkit-scrollbar-thumb{background:#ffd27d;border-radius:10px;}
.teamCard{background:#fff;border:3px solid #ffe1a8;border-radius:20px;padding:12px 16px;margin-bottom:12px;}
.row{display:flex;align-items:center;gap:10px;margin-bottom:8px;}
.row .lab{width:74px;font-size:19px;color:#ff7eb3;}
.inp{flex:0 0 auto;border:2px solid #ffd9a3;border-radius:12px;padding:8px 12px;font-size:18px;font-family:'Jua';outline:none;}
.inp.team{width:230px;}.inp.mem{width:120px;}
.charPick{display:flex;gap:6px;flex-wrap:wrap;}
.charBtn{width:46px;height:46px;font-size:28px;line-height:46px;text-align:center;border-radius:12px;
  background:#f4f6fa;border:3px solid transparent;cursor:pointer;}
.charBtn.sel{border-color:#ff5fa2;background:#fff0f6;transform:scale(1.08);}
#setBar{display:flex;gap:14px;align-items:center;margin-top:6px;}
.winset{display:flex;align-items:center;gap:8px;background:#fff;border:3px solid #ffd27d;border-radius:16px;padding:6px 12px;font-size:18px;color:#ff7e3b;}
.winset .v{font-size:22px;color:#e8590c;min-width:78px;text-align:center;}
.miniBtn{width:38px;height:38px;font-size:22px;border-radius:12px;}
/* ===== 순서 정하기 ===== */
#order{position:absolute;inset:0;display:none;flex-direction:column;align-items:center;justify-content:center;gap:18px;}
#orderBox{background:rgba(255,255,255,.85);border:4px dashed #8fd0ff;border-radius:26px;padding:26px 40px;text-align:center;}
.ord{display:inline-flex;align-items:center;gap:10px;background:#fff;border:3px solid #cdeafe;border-radius:18px;
  padding:10px 18px;margin:7px;font-size:22px;color:#3a7bd5;}
.ord .n{background:#5aa9ff;color:#fff;border-radius:50%;width:34px;height:34px;line-height:34px;text-align:center;}
/* ===== 플레이 화면 ===== */
#play{position:absolute;inset:0;display:none;}
#board{position:absolute;left:392px;top:48px;width:736px;height:736px;
  display:grid;grid-template-columns:repeat(10,1fr);grid-template-rows:repeat(10,1fr);gap:6px;
  transform:perspective(1500px) rotateX(16deg);transform-style:preserve-3d;}
.cell{position:relative;border-radius:13px;display:flex;flex-direction:column;align-items:center;justify-content:center;
  font-size:14px;color:#5b4636;box-shadow:0 6px 0 rgba(0,0,0,.16);border:2px solid rgba(255,255,255,.7);}
.cell .ico{font-size:22px;line-height:1;}
.cell .nm{font-size:13px;margin-top:2px;}
.cell.quiz{background:#fff7e8;}
.cell.golden{background:#ffe08a;color:#8a5a00;}
.cell.island{background:#9fd8ff;color:#0b5a87;}
.cell.start{background:#ffc6e0;color:#c2185b;}
.cell.lit{animation:pop .5s ease;}
@keyframes pop{0%{transform:scale(1)}40%{transform:scale(1.16)}100%{transform:scale(1)}}
.pawn{position:absolute;font-size:26px;z-index:6;transition:left .28s cubic-bezier(.34,1.56,.64,1),top .28s cubic-bezier(.34,1.56,.64,1);
  filter:drop-shadow(0 3px 2px rgba(0,0,0,.35));pointer-events:none;}
.pawn.hop{animation:hop .28s ease;}
@keyframes hop{0%,100%{transform:translateY(0)}50%{transform:translateY(-16px) scale(1.12)}}
/* 가운데 승리조건 패널 */
#centerPanel{position:absolute;left:610px;top:322px;width:300px;
  background:rgba(255,255,255,.94);border:4px solid #ffd27d;border-radius:24px;padding:16px 18px;text-align:center;
  box-shadow:0 8px 0 rgba(0,0,0,.10);z-index:4;}
#centerPanel .ttl{font-size:23px;color:#ff5fa2;}
#centerPanel .winrow{display:flex;align-items:center;justify-content:center;gap:10px;margin:10px 0 6px;}
#centerPanel .wv{font-size:34px;color:#e8590c;min-width:120px;}
#centerPanel .small{font-size:16px;color:#7a6a58;}
#centerPanel .bk{font-size:18px;color:#e03131;margin-top:7px;}
/* 점수판 */
#score{position:absolute;left:14px;top:48px;width:368px;background:rgba(255,255,255,.92);
  border:4px solid #ffd27d;border-radius:22px;padding:12px 14px;z-index:5;}
#score h3{text-align:center;font-size:22px;color:#ff7e3b;margin-bottom:8px;}
.sc{border-radius:15px;padding:8px 12px;margin-bottom:8px;border:3px solid #eee;}
.sc .top{display:flex;justify-content:space-between;align-items:center;font-size:21px;}
.sc .nm{color:#3a3a3a;}.sc .pt{color:#2f9e44;font-size:24px;}
.sc .mem{font-size:14px;color:#8a7a68;margin-top:3px;line-height:1.35;}
.sc.cur{border-color:#ff7eb3;background:#fff2f8;box-shadow:0 0 0 3px #ffd9ea inset;}
.sc.bust{opacity:.45;filter:grayscale(.6);}
/* 우측 조작부 */
#right{position:absolute;right:14px;top:48px;width:368px;text-align:center;}
#turnBox{background:rgba(255,255,255,.92);border:3px solid #ffe1a8;border-radius:20px;padding:10px;margin-bottom:14px;}
#turnBox .l{font-size:20px;color:#9aa6b2;}#turnBox .t{font-size:30px;color:#ff5fa2;margin-top:2px;}
#dice{width:150px;height:150px;margin:0 auto;background:#fff;border:5px solid #ff9ec7;border-radius:28px;
  display:flex;align-items:center;justify-content:center;font-size:96px;color:#ff5fa2;
  box-shadow:0 10px 0 rgba(255,126,179,.35);}
#dice.shake{animation:shake .5s linear;}
@keyframes shake{0%,100%{transform:rotate(0)}20%{transform:rotate(-12deg) scale(1.05)}40%{transform:rotate(10deg)}60%{transform:rotate(-7deg)}80%{transform:rotate(5deg)}}
#rollBtn{margin-top:16px;font-size:26px;padding:14px 30px;}
#msg{margin-top:14px;font-size:21px;min-height:30px;color:#444;}
/* 오버레이(퀴즈/황금열쇠) - 보드 위를 덮음 */
#overlay{position:absolute;left:392px;top:48px;width:736px;height:736px;display:none;
  align-items:center;justify-content:center;z-index:20;}
#ovcard{width:600px;background:#fff;border:6px solid #ffd27d;border-radius:30px;padding:26px 30px;text-align:center;
  box-shadow:0 16px 40px rgba(0,0,0,.3);animation:popin .3s ease;}
@keyframes popin{0%{transform:scale(.7);opacity:0}100%{transform:scale(1);opacity:1}}
#ovcard.golden{border-color:#ffc107;background:#fffaf0;}
.ovtag{display:inline-block;background:#ff7eb3;color:#fff;font-size:19px;padding:5px 18px;border-radius:20px;}
.ovtag.g{background:#ffb300;}
#ovWho{font-size:22px;color:#ff5fa2;margin:12px 0 4px;}
#ovQ{font-size:28px;color:#333;line-height:1.4;margin:10px 0;min-height:74px;}
#ovTimer{font-size:60px;color:#ff6b6b;margin:6px 0;}
#ovA{display:none;font-size:26px;color:#2b8a3e;background:#eafff0;border-radius:16px;padding:12px;margin:10px 0;}
.ovBtns{display:flex;gap:12px;justify-content:center;flex-wrap:wrap;margin-top:12px;}
.ovBtns .btn{font-size:21px;padding:12px 22px;}
/* 황금열쇠 점수 조절 */
#gAdj{display:none;align-items:center;justify-content:center;gap:12px;margin:14px 0 4px;}
#gAdj .gv{font-size:34px;color:#e8590c;min-width:88px;}
#gDesc{font-size:21px;color:#7a6a58;margin:8px 0;line-height:1.4;}
/* 종료 화면 */
#endscreen{position:absolute;inset:0;display:none;flex-direction:column;align-items:center;justify-content:center;
  background:rgba(10,16,32,.45);z-index:40;}
#endcard{background:#fff;border-radius:32px;padding:40px 56px;text-align:center;box-shadow:0 20px 60px rgba(0,0,0,.4);animation:popin .4s ease;}
#endcard .big{font-size:52px;color:#ff5fa2;}#endcard .em{font-size:80px;}
#endcard .d{font-size:24px;color:#555;margin:10px 0 22px;}
/* 하단/배경음악 */
#credit{position:absolute;right:14px;bottom:8px;font-size:12px;color:rgba(90,70,60,.6);}
#bgmBtn{position:absolute;left:12px;bottom:10px;font-size:16px;padding:8px 14px;z-index:50;}
.confetti{position:absolute;width:12px;height:18px;top:-30px;z-index:45;animation:fall linear forwards;}
@keyframes fall{to{transform:translateY(820px) rotate(720deg);opacity:.9}}
</style></head>
<body><div id="wrap"><div id="stage">
  <div class="cloud" style="left:80px;top:60px;width:130px;height:54px"></div>
  <div class="cloud" style="left:1080px;top:120px;width:160px;height:60px"></div>
  <div class="cloud" style="left:600px;top:40px;width:120px;height:48px"></div>

  <!-- 설정 -->
  <div id="setup">
    <div id="title"><h1>함창중 문법 부르마블<span class="y">(음운)</span></h1>
      <span class="sub">중3 국어 · 음운의 종류와 특징 (자음·모음 체계표)</span></div>
    <div id="panel">
      <div id="teamList"></div>
      <div id="setBar">
        <button class="btn orange" style="font-size:20px;padding:10px 20px" onclick="addTeam()">＋ 모둠 추가</button>
        <div class="winset">🎯 승리 점수
          <button class="btn blue miniBtn" onclick="setWin(-50)">－</button>
          <span class="v" id="winV">200점</span>
          <button class="btn blue miniBtn" onclick="setWin(50)">＋</button>
        </div>
        <button class="btn green" style="font-size:22px;padding:11px 26px;margin-left:auto" onclick="goOrder()">순서 정하러 가기 ▶</button>
      </div>
    </div>
  </div>

  <!-- 순서 -->
  <div id="order">
    <div id="orderBox">
      <div style="font-size:30px;color:#3a7bd5;margin-bottom:10px">🎲 주사위 던질 순서</div>
      <div id="ordList"></div>
      <div style="margin-top:18px;display:flex;gap:14px;justify-content:center">
        <button class="btn purple" style="font-size:22px;padding:12px 26px" onclick="shuffleOrder()">🔀 랜덤으로 순서 섞기</button>
        <button class="btn green" style="font-size:22px;padding:12px 26px" onclick="startGame()">이 순서로 시작 ▶</button>
      </div>
    </div>
  </div>

  <!-- 플레이 -->
  <div id="play">
    <div id="score"><h3>🏆 점수 현황판</h3><div id="scoreList"></div></div>
    <div id="board"></div>
    <div id="centerPanel">
      <div class="ttl">🎯 승리 · 파산 조건</div>
      <div class="winrow">
        <button class="btn blue miniBtn" onclick="setWinLive(-50)">－</button>
        <span class="wv" id="winLive">200점</span>
        <button class="btn blue miniBtn" onclick="setWinLive(50)">＋</button>
      </div>
      <div class="small">먼저 도달하면 🏆 승리!</div>
      <div class="bk">💥 －100점 이하 → 파산</div>
    </div>
    <div id="right">
      <div id="turnBox"><div class="l">지금 차례</div><div class="t" id="turnName">-</div></div>
      <div id="dice">🎲</div>
      <button class="btn pink" id="rollBtn" onclick="rollDice()">주사위 던지기 🎲</button>
      <div id="msg"></div>
    </div>
    <!-- 오버레이 -->
    <div id="overlay"><div id="ovcard">
      <span class="ovtag" id="ovTag">문제</span>
      <div id="ovWho"></div>
      <div id="ovQ"></div>
      <div id="gDesc"></div>
      <div id="ovTimer"></div>
      <div id="gAdj"><button class="btn blue miniBtn" onclick="gAdjust(-5)">－</button>
        <span class="gv" id="gVal">+10</span>
        <button class="btn blue miniBtn" onclick="gAdjust(5)">＋</button></div>
      <div id="ovA"></div>
      <div class="ovBtns" id="ovBtns"></div>
    </div></div>
  </div>

  <!-- 종료 -->
  <div id="endscreen"><div id="endcard">
    <div class="em" id="endEm">🏆</div><div class="big" id="endTitle"></div>
    <div class="d" id="endDesc"></div>
    <button class="btn pink" style="font-size:24px;padding:14px 34px" onclick="location.reload()">🔄 다시 시작</button>
  </div></div>

  <button class="btn gray" id="bgmBtn" onclick="toggleBgm()">🔊 배경음악 ON</button>
  <div id="credit">제작 : 함창고 교사 박호종</div>
</div></div>
<script>
const QUESTIONS = __QUESTIONS__;
const CHARS = ['🐰','🐱','🐶','🐼','🦊','🐯','🐸','🐧','🐥','🦁','🐭','🐨'];

/* ===================== 상태 ===================== */
let teams=[];            // {name,members:[name], char, score, mem:[pt], bust, skip}
let winScore=200, bustScore=-100;
let order=[];            // 팀 인덱스 진행 순서
let turnPtr=0;           // order 내 위치
let curTeam=0;           // 현재 팀 index(teams 기준)
let pos=[];              // 팀별 보드 위치
let busy=false;
let qIdx=0;              // 문제 포인터(셔플)
let qOrder=[];
let curQuestion=null, curStudent='', chanceMode=false, originTeam=0;
let curGolden=null, gPoints=10;
let timerId=null;

/* ===================== 보드 ===================== */
function cellType(i){
  if(i===0) return 'start';
  if(i===18) return 'island';
  if(i===9||i===27) return 'golden';
  if(i%5===0) return 'golden';
  return 'quiz';
}
function cellPos(i){ // grid row/col 1..10
  if(i<=9) return {r:10,c:i+1};
  if(i<=18) return {r:10-(i-9),c:10};
  if(i<=27) return {r:1,c:10-(i-18)};
  return {r:1+(i-27),c:1};
}
const TOTAL=36;
function buildBoard(){
  const b=document.getElementById('board'); b.innerHTML='';
  for(let i=0;i<TOTAL;i++){
    const t=cellType(i), p=cellPos(i);
    const d=document.createElement('div');
    d.className='cell '+t; d.id='cell'+i;
    d.style.gridRow=p.r; d.style.gridColumn=p.c;
    let ico='📝',nm='문제';
    if(t==='start'){ico='🏁';nm='출발 +5';}
    if(t==='golden'){ico='🗝️';nm='황금열쇠';}
    if(t==='island'){ico='🏝️';nm='무인도';}
    d.innerHTML='<div class="ico">'+ico+'</div><div class="nm">'+nm+'</div>';
    b.appendChild(d);
  }
}
function pawnXY(cellIdx,slot){
  const p=cellPos(cellIdx);
  const cw=(736-6*9)/10; // cell width approx
  const gx=(p.c-1)*(cw+6), gy=(p.r-1)*(cw+6);
  const ox=[ -8, 10, -8, 10 ][slot]+cw/2-13;
  const oy=[ -8, -8, 12, 12 ][slot]+cw/2-13;
  return {x:gx+ox, y:gy+oy};
}
function placePawns(){
  document.querySelectorAll('.pawn').forEach(e=>e.remove());
  const b=document.getElementById('board');
  teams.forEach((t,ti)=>{
    if(t.bust) return;
    const xy=pawnXY(pos[ti], ti);
    const s=document.createElement('div');
    s.className='pawn'; s.id='pawn'+ti; s.textContent=t.char;
    s.style.left=xy.x+'px'; s.style.top=xy.y+'px';
    b.appendChild(s);
  });
}

/* ===================== 설정 화면 ===================== */
let setupTeams=[
  {name:'모둠1',members:['','','',''],char:'🐰'},
  {name:'모둠2',members:['','','',''],char:'🐱'},
];
function renderSetup(){
  const L=document.getElementById('teamList'); L.innerHTML='';
  setupTeams.forEach((t,i)=>{
    let mem=t.members.map((m,j)=>`<input class="inp mem" placeholder="${j+1}번" value="${m}" oninput="setMem(${i},${j},this.value)">`).join('');
    let chars=CHARS.map(c=>`<div class="charBtn ${t.char===c?'sel':''}" onclick="setChar(${i},'${c}')">${c}</div>`).join('');
    const card=document.createElement('div'); card.className='teamCard';
    card.innerHTML=`
      <div class="row"><span class="lab">모둠명</span>
        <input class="inp team" value="${t.name}" oninput="setName(${i},this.value)">
        ${setupTeams.length>2?`<button class="btn red" style="font-size:16px;padding:7px 14px" onclick="delTeam(${i})">삭제</button>`:''}</div>
      <div class="row"><span class="lab">구성원</span>${mem}</div>
      <div class="row"><span class="lab">캐릭터</span><div class="charPick">${chars}</div></div>`;
    L.appendChild(card);
  });
  document.getElementById('winV').textContent=winScore+'점';
}
function setName(i,v){setupTeams[i].name=v;}
function setMem(i,j,v){setupTeams[i].members[j]=v;}
function setChar(i,c){setupTeams[i].char=c;renderSetup();}
function addTeam(){
  if(setupTeams.length>=6){alert('최대 6모둠까지 가능해요!');return;}
  const used=setupTeams.map(t=>t.char);
  const free=CHARS.find(c=>!used.includes(c))||'🐰';
  setupTeams.push({name:'모둠'+(setupTeams.length+1),members:['','','',''],char:free});
  renderSetup();
}
function delTeam(i){setupTeams.splice(i,1);renderSetup();}
function setWin(d){winScore=Math.max(100,Math.min(2000,winScore+d));renderSetup();}

/* ===================== 순서 화면 ===================== */
function goOrder(){
  teams=setupTeams.map(t=>({
    name:t.name.trim()||'모둠',
    members:t.members.map(m=>m.trim()).filter(m=>m),
    char:t.char, score:100, mem:[], bust:false, skip:false
  }));
  teams.forEach(t=>{ if(t.members.length===0)t.members=['1','2','3','4']; t.mem=t.members.map(_=>0); });
  order=teams.map((_,i)=>i);
  document.getElementById('setup').style.display='none';
  document.getElementById('order').style.display='flex';
  renderOrder();
}
function renderOrder(){
  document.getElementById('ordList').innerHTML=order.map((ti,k)=>
    `<span class="ord"><span class="n">${k+1}</span>${teams[ti].char} ${teams[ti].name}</span>`).join('');
}
function shuffleOrder(){ for(let i=order.length-1;i>0;i--){const j=Math.floor(Math.random()*(i+1));[order[i],order[j]]=[order[j],order[i]];} renderOrder(); playSound('dice'); }

/* ===================== 게임 시작 ===================== */
function startGame(){
  document.getElementById('order').style.display='none';
  document.getElementById('play').style.display='block';
  pos=teams.map(_=>0);
  turnPtr=0; curTeam=order[0];
  qOrder=QUESTIONS.map((_,i)=>i); for(let i=qOrder.length-1;i>0;i--){const j=Math.floor(Math.random()*(i+1));[qOrder[i],qOrder[j]]=[qOrder[j],qOrder[i]];}
  qIdx=0;
  buildBoard(); placePawns(); renderScore(); updateTurn();
  document.getElementById('winLive').textContent=winScore+'점';
  startBgm();
}
function nextQuestion(){ const q=QUESTIONS[qOrder[qIdx%qOrder.length]]; qIdx++; return q; }
function renderScore(){
  document.getElementById('scoreList').innerHTML=teams.map((t,i)=>{
    const mem=t.members.map((m,j)=>`${m} ${t.mem[j]>=0?'+':''}${t.mem[j]}`).join(' · ');
    return `<div class="sc ${i===curTeam?'cur':''} ${t.bust?'bust':''}">
      <div class="top"><span class="nm">${t.char} ${t.name}</span><span class="pt">${t.score}점</span></div>
      <div class="mem">${mem}</div></div>`;
  }).join('');
}
function updateTurn(){ document.getElementById('turnName').textContent=teams[curTeam].char+' '+teams[curTeam].name; renderScore(); }
function setMsg(s){ document.getElementById('msg').innerHTML=s; }
function setWinLive(d){ winScore=Math.max(100,Math.min(2000,winScore+d)); document.getElementById('winLive').textContent=winScore+'점'; checkWinAll(); }

/* ===================== 주사위 & 이동 ===================== */
function rollDice(){
  if(busy) return; busy=true;
  // 무인도 쉬기 체크
  if(teams[curTeam].skip){ teams[curTeam].skip=false; setMsg('🏝️ '+teams[curTeam].name+'은(는) 무인도에서 한 턴 쉬어요!'); playSound('island'); busy=false; nextTurn(); return; }
  setMsg(''); document.getElementById('ovA').style.display='none';
  const dice=document.getElementById('dice'); dice.classList.add('shake'); playSound('dice');
  let cnt=0; const iv=setInterval(()=>{ dice.textContent=1+Math.floor(Math.random()*6); cnt++; if(cnt>10){ clearInterval(iv); finalizeRoll(); } },60);
}
function finalizeRoll(){
  const n=1+Math.floor(Math.random()*6);
  const dice=document.getElementById('dice'); dice.textContent=n; dice.classList.remove('shake');
  setMsg('🎲 '+n+' 칸 이동!');
  moveStep(n);
}
function moveStep(steps){
  if(steps<=0){ landed(); return; }
  pos[curTeam]=(pos[curTeam]+1)%TOTAL;
  if(pos[curTeam]===0){ teams[curTeam].score+=5; playSound('coin'); setMsg('🏁 출발 통과! +5점'); }
  const pw=document.getElementById('pawn'+curTeam);
  const xy=pawnXY(pos[curTeam],curTeam);
  pw.classList.add('hop'); pw.style.left=xy.x+'px'; pw.style.top=xy.y+'px';
  setTimeout(()=>{ pw.classList.remove('hop'); moveStep(steps-1); },280);
}
function landed(){
  renderScore();
  const c=document.getElementById('cell'+pos[curTeam]); c.classList.add('lit'); setTimeout(()=>c.classList.remove('lit'),500);
  const t=cellType(pos[curTeam]);
  if(t==='island'){ teams[curTeam].skip=true; setMsg('🏝️ 무인도 도착! 다음 차례 한 번 쉬어요.'); playSound('island'); busy=false; setTimeout(nextTurn,1200); return; }
  if(t==='golden'){ showGolden(); return; }
  if(t==='start'){ teams[curTeam].score+=5; renderScore(); playSound('coin'); setMsg('🏁 출발칸 도착! +5점'); busy=false; setTimeout(nextTurn,1200); checkWinAll(); return; }
  // 퀴즈
  askQuestion(curTeam, false);
}

/* ===================== 퀴즈 ===================== */
function pickStudent(ti){ const m=teams[ti].members; return Math.floor(Math.random()*m.length); }
function askQuestion(ti, isChance){
  chanceMode=isChance; const sIdx=pickStudent(ti); curStudent=sIdx;
  if(!isChance){ curQuestion=nextQuestion(); originTeam=curTeam; }
  curTeam=ti; updateTurn();
  const ov=document.getElementById('overlay'), card=document.getElementById('ovcard');
  card.className=''; document.getElementById('ovTag').className='ovtag'; document.getElementById('ovTag').textContent= isChance?'🔥 찬스 문제':'문제';
  document.getElementById('ovWho').textContent=(isChance?'🔥 찬스! ':'')+teams[ti].char+' '+teams[ti].name+' — '+teams[ti].members[sIdx]+' 학생';
  document.getElementById('ovQ').textContent=curQuestion.q;
  document.getElementById('gDesc').style.display='none';
  document.getElementById('gAdj').style.display='none';
  document.getElementById('ovA').style.display='none';
  document.getElementById('ovBtns').innerHTML=`<button class="btn orange" onclick="revealAnswer()">바로 정답 확인 ⏩</button>`;
  ov.style.display='flex';
  startCountdown(10, ()=>{ showAnswerBtns(); });
}
function startCountdown(sec, onEnd){
  const el=document.getElementById('ovTimer'); let t=sec; el.style.color='#ff6b6b'; el.textContent='⏰ '+t;
  clearInterval(timerId);
  timerId=setInterval(()=>{ t--; if(t<=3)el.style.color='#e03131'; if(t<=0){ clearInterval(timerId); el.textContent='⏰ 시간 종료!'; playSound('buzz'); onEnd&&onEnd(); } else { el.textContent='⏰ '+t; playSound('tick'); } },1000);
}
function showAnswerBtns(){
  document.getElementById('ovBtns').innerHTML=
    `<button class="btn blue" onclick="revealAnswer()">정답 공개 👀</button>`;
}
function revealAnswer(){
  clearInterval(timerId);
  const a=document.getElementById('ovA'); a.style.display='block'; a.textContent='정답 : '+curQuestion.a;
  document.getElementById('ovTimer').textContent='';
  document.getElementById('ovBtns').innerHTML=
    `<button class="btn green" onclick="mark(true)">⭕ 정답 (+10)</button>
     <button class="btn red" onclick="mark(false)">❌ 오답 (−10)</button>`;
}
function mark(correct){
  const ti=curTeam, sIdx=curStudent;
  if(correct){ teams[ti].score+=10; teams[ti].mem[sIdx]+=10; playSound('correct'); }
  else{ teams[ti].score-=10; teams[ti].mem[sIdx]-=10; playSound('wrong'); }
  renderScore();
  closeOverlay();
  if(checkWinAll()) return;
  if(correct){
    setMsg('⭕ 정답! 다음 모둠 차례예요.');
    setTimeout(nextTurn,1100);
  } else {
    if(!chanceMode){
      // 다른 모둠에게 찬스
      const others=order.map(x=>x).filter(x=>x!==originTeam && !teams[x].bust);
      if(others.length>0){
        const pick=others[Math.floor(Math.random()*others.length)];
        setMsg('❌ 오답! 🔥 '+teams[pick].name+'에게 찬스가 넘어가요!');
        setTimeout(()=>{ busy=true; askQuestion(pick, true); },1300);
        return;
      }
    }
    setMsg('❌ 아쉬워요! 다음 모둠 차례예요.');
    setTimeout(nextTurn,1200);
  }
}
function closeOverlay(){ document.getElementById('overlay').style.display='none'; clearInterval(timerId); }

/* ===================== 황금열쇠 (조건부 인터랙티브) ===================== */
const GOLDEN=[
 {tag:'🎂 생일 축하금', desc:'이 모둠에 <b>오늘(또는 이번 달) 생일</b>인 친구가 있나요?<br>있으면 축하금을 주고, 없으면 변동 없음!', base:20,
  outs:[{label:'생일 친구 있음 → 축하금 주기',sign:1},{label:'생일 친구 없음 → 변동 없음',sign:0}]},
 {tag:'🎤 개인기 한마당', desc:'지정된 학생이 <b>개인기에 도전</b>합니다!<br>성공하면 점수 획득, 실패하면 변동 없음.', base:15,
  outs:[{label:'개인기 성공 → 점수 주기',sign:1},{label:'아쉽게 실패 → 변동 없음',sign:0}]},
 {tag:'🤝 단합력 테스트', desc:'모둠원 <b>전체가 함께 미션</b>에 도전!<br>성공하면 보너스, 실패하면 감점.', base:20,
  outs:[{label:'미션 성공 → 점수 주기',sign:1},{label:'미션 실패 → 점수 빼기',sign:-1}]},
 {tag:'🧾 벌금 고지서', desc:'이런! <b>벌금</b>을 내야 해요.<br>금액을 정해 점수를 빼 주세요.', base:15,
  outs:[{label:'벌금 납부 → 점수 빼기',sign:-1},{label:'봐주기 → 변동 없음',sign:0}]},
 {tag:'🍀 행운의 보너스', desc:'행운이 찾아왔어요!<br>보너스 점수를 받습니다.', base:15,
  outs:[{label:'보너스 받기 → 점수 주기',sign:1}]},
 {tag:'📚 깜짝 상식', desc:'지정된 학생에게 <b>깜짝 질문</b>! (선생님이 즉석 출제)<br>맞히면 점수, 틀리면 변동 없음.', base:10,
  outs:[{label:'정답 → 점수 주기',sign:1},{label:'오답 → 변동 없음',sign:0}]},
];
function showGolden(){
  curGolden=GOLDEN[Math.floor(Math.random()*GOLDEN.length)];
  gPoints=curGolden.base;
  playSound('golden');
  const ov=document.getElementById('overlay'), card=document.getElementById('ovcard');
  card.className='golden';
  const tag=document.getElementById('ovTag'); tag.className='ovtag g'; tag.textContent='🗝️ 황금열쇠';
  document.getElementById('ovWho').textContent=teams[curTeam].char+' '+teams[curTeam].name;
  document.getElementById('ovQ').textContent=curGolden.tag;
  const desc=document.getElementById('gDesc'); desc.style.display='block'; desc.innerHTML=curGolden.desc;
  document.getElementById('ovTimer').textContent='';
  document.getElementById('gAdj').style.display='flex'; updateGVal();
  document.getElementById('ovA').style.display='none';
  // 결과 버튼들
  const btns=curGolden.outs.map((o,k)=>{
    const cls=o.sign>0?'green':(o.sign<0?'red':'gray');
    return `<button class="btn ${cls}" onclick="goldenApply(${o.sign})">${o.label}</button>`;
  }).join('');
  document.getElementById('ovBtns').innerHTML=btns;
  ov.style.display='flex';
}
function updateGVal(){ document.getElementById('gVal').textContent=(gPoints>=0?'+':'')+gPoints; }
function gAdjust(d){ gPoints=Math.max(0,Math.min(100,gPoints+d)); updateGVal(); }
function goldenApply(sign){
  const delta=sign*gPoints;
  teams[curTeam].score+=delta;
  if(delta>0)playSound('coin'); else if(delta<0)playSound('wrong'); else playSound('tick');
  renderScore(); closeOverlay();
  if(delta>0) setMsg('🗝️ '+curGolden.tag+' → +'+gPoints+'점!');
  else if(delta<0) setMsg('🗝️ '+curGolden.tag+' → '+delta+'점!');
  else setMsg('🗝️ '+curGolden.tag+' → 점수 변동 없음!');
  if(checkWinAll()) return;
  setTimeout(nextTurn,1200);
}

/* ===================== 턴 넘기기 & 승패 ===================== */
function nextTurn(){
  busy=false;
  do{ turnPtr=(turnPtr+1)%order.length; curTeam=order[turnPtr]; }while(teams[curTeam].bust);
  updateTurn();
}
function checkWinAll(){
  // 파산
  let changed=false;
  teams.forEach((t,i)=>{ if(!t.bust && t.score<=bustScore){ t.bust=true; changed=true; setMsg('💥 '+t.name+' 파산!'); playSound('bust'); } });
  if(changed){ placePawns(); renderScore(); }
  const alive=teams.filter(t=>!t.bust);
  // 승리: 목표 도달
  const reached=teams.find(t=>!t.bust && t.score>=winScore);
  if(reached){ endGame(reached,'goal'); return true; }
  if(alive.length===1 && teams.length>1){ endGame(alive[0],'last'); return true; }
  if(alive.length===0){ endGame(null,'none'); return true; }
  return false;
}
function endGame(team,reason){
  busy=true; clearInterval(timerId); closeOverlay();
  const es=document.getElementById('endscreen'); es.style.display='flex';
  document.getElementById('endEm').textContent='🏆';
  if(team){
    document.getElementById('endTitle').textContent=team.char+' '+team.name+' 우승! 🎉';
    document.getElementById('endDesc').textContent=(reason==='goal'?('목표 '+winScore+'점 달성! 최종 '+team.score+'점'):'다른 모둠이 모두 파산했어요! 최종 '+team.score+'점');
    playSound('win'); confetti();
  } else {
    document.getElementById('endTitle').textContent='모두 파산… 😵';
    document.getElementById('endDesc').textContent='아무도 살아남지 못했어요!';
    playSound('bust');
  }
}
function confetti(){
  const cols=['#ff7eb3','#ffd23f','#5aa9ff','#46c98b','#b08bff','#ffa53b'];
  for(let i=0;i<80;i++){ const c=document.createElement('div'); c.className='confetti';
    c.style.left=Math.random()*1360+'px'; c.style.background=cols[i%cols.length];
    c.style.animationDuration=(2+Math.random()*2)+'s'; c.style.animationDelay=(Math.random()*0.6)+'s';
    document.getElementById('stage').appendChild(c); setTimeout(()=>c.remove(),4500); }
}

/* ===================== 사운드(WebAudio 합성) ===================== */
let AC=null, bgmOn=true, bgmTimer=null, bgmStep=0;
function ac(){ if(!AC){ try{AC=new (window.AudioContext||window.webkitAudioContext)();}catch(e){} } if(AC&&AC.state==='suspended')AC.resume(); return AC; }
function tone(freq,dur,type,vol,when){ const a=ac(); if(!a)return; const t=a.currentTime+(when||0);
  const o=a.createOscillator(),g=a.createGain(); o.type=type||'sine'; o.frequency.value=freq;
  g.gain.setValueAtTime(0,t); g.gain.linearRampToValueAtTime(vol||0.18,t+0.02); g.gain.exponentialRampToValueAtTime(0.0001,t+dur);
  o.connect(g); g.connect(a.destination); o.start(t); o.stop(t+dur); }
function playSound(k){
  switch(k){
    case 'dice': tone(220,0.08,'square',0.12);tone(330,0.08,'square',0.12,0.08);tone(440,0.1,'square',0.12,0.16);break;
    case 'correct': tone(660,0.12,'sine',0.2);tone(880,0.16,'sine',0.2,0.12);tone(1100,0.22,'sine',0.2,0.26);break;
    case 'wrong': tone(300,0.18,'sawtooth',0.16);tone(200,0.28,'sawtooth',0.16,0.16);break;
    case 'coin': tone(988,0.07,'square',0.16);tone(1319,0.16,'square',0.16,0.07);break;
    case 'golden': tone(784,0.1,'triangle',0.18);tone(1047,0.1,'triangle',0.18,0.1);tone(1319,0.2,'triangle',0.18,0.2);break;
    case 'island': tone(392,0.16,'sine',0.16);tone(294,0.26,'sine',0.16,0.14);break;
    case 'tick': tone(700,0.05,'square',0.07);break;
    case 'buzz': tone(160,0.4,'sawtooth',0.18);break;
    case 'win': [523,659,784,1047,784,1047,1319].forEach((f,i)=>tone(f,0.3,'triangle',0.2,i*0.18));break;
    case 'bust': [400,330,260,200].forEach((f,i)=>tone(f,0.3,'sawtooth',0.18,i*0.16));break;
  }
}
const MELODY=[523,659,784,659,587,784,659,523, 587,659,698,659,587,523,494,523];
function startBgm(){ if(bgmTimer)return; bgmStep=0;
  bgmTimer=setInterval(()=>{ if(!bgmOn)return; const a=ac(); if(!a)return;
    const f=MELODY[bgmStep%MELODY.length]; tone(f,0.32,'triangle',0.05);
    if(bgmStep%2===0) tone(f/2,0.3,'sine',0.04); bgmStep++; },340); }
function toggleBgm(){ bgmOn=!bgmOn; ac(); document.getElementById('bgmBtn').textContent=bgmOn?'🔊 배경음악 ON':'🔈 배경음악 OFF'; if(bgmOn)startBgm(); }

/* ===================== 스케일(한 화면 고정) ===================== */
function fit(){ const s=Math.min(window.innerWidth/1520, window.innerHeight/856);
  document.getElementById('stage').style.transform='scale('+s+')'; }
window.addEventListener('resize',fit);
window.addEventListener('click',()=>{ ac(); },{once:false});

/* ===================== 초기화 ===================== */
renderSetup(); fit();
</script></body></html>
'''

html = GAME_HTML.replace("__QUESTIONS__", json.dumps(QUESTIONS, ensure_ascii=False))
components.html(html, height=860, scrolling=False)
