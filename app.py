# app.py  -- 부루마블 형식 중3 국어 문법 퀴즈 게임 (Streamlit)
import streamlit as st
import random, time

st.set_page_config(page_title="국어 문법 부루마블", page_icon="🎲", layout="wide")

# ===================== 문제은행 (100문항) =====================
CONS = {
 'ㄱ':('여린입천장소리(연구개음)','파열음'),'ㄲ':('여린입천장소리(연구개음)','파열음'),'ㅋ':('여린입천장소리(연구개음)','파열음'),
 'ㄷ':('잇몸소리(치조음)','파열음'),'ㄸ':('잇몸소리(치조음)','파열음'),'ㅌ':('잇몸소리(치조음)','파열음'),
 'ㅂ':('입술소리(양순음)','파열음'),'ㅃ':('입술소리(양순음)','파열음'),'ㅍ':('입술소리(양순음)','파열음'),
 'ㅈ':('센입천장소리(경구개음)','파찰음'),'ㅉ':('센입천장소리(경구개음)','파찰음'),'ㅊ':('센입천장소리(경구개음)','파찰음'),
 'ㅅ':('잇몸소리(치조음)','마찰음'),'ㅆ':('잇몸소리(치조음)','마찰음'),'ㅎ':('목청소리(후음)','마찰음'),
 'ㄴ':('잇몸소리(치조음)','비음'),'ㅁ':('입술소리(양순음)','비음'),'ㅇ':('여린입천장소리(연구개음)','비음'),
 'ㄹ':('잇몸소리(치조음)','유음'),
}
def build_questions():
    Q=[]
    for c,(pos,man) in CONS.items():
        Q.append({"q":f"자음 '{c}'의 조음 위치와 조음 방법을 모두 말하시오.","a":f"{pos} / {man}"})
        Q.append({"q":f"자음 '{c}'의 조음 위치는?","a":pos})
        Q.append({"q":f"자음 '{c}'의 조음 방법은?","a":man})
    extra=[
     ("국어의 유성음(울림소리) 자음을 모두 말하시오.","ㄴ, ㄹ, ㅁ, ㅇ"),
     ("비음에 속하는 자음을 모두 말하시오.","ㄴ, ㅁ, ㅇ"),
     ("유음에 속하는 자음을 말하시오.","ㄹ"),
     ("파열음을 모두 말하시오.","ㄱ,ㄲ,ㅋ, ㄷ,ㄸ,ㅌ, ㅂ,ㅃ,ㅍ"),
     ("파찰음을 모두 말하시오.","ㅈ, ㅉ, ㅊ"),
     ("마찰음을 모두 말하시오.","ㅅ, ㅆ, ㅎ"),
     ("예사소리(평음)를 모두 말하시오.","ㄱ, ㄷ, ㅂ, ㅅ, ㅈ"),
     ("된소리(경음)를 모두 말하시오.","ㄲ, ㄸ, ㅃ, ㅆ, ㅉ"),
     ("거센소리(격음)를 모두 말하시오.","ㅋ, ㅌ, ㅍ, ㅊ"),
     ("양순음(입술소리)을 모두 말하시오.","ㅂ, ㅃ, ㅍ, ㅁ"),
     ("연구개음(여린입천장소리)을 모두 말하시오.","ㄱ, ㄲ, ㅋ, ㅇ"),
     ("경구개음(센입천장소리)을 모두 말하시오.","ㅈ, ㅉ, ㅊ"),
     ("치조음(잇몸소리)을 모두 말하시오.","ㄷ,ㄸ,ㅌ,ㅅ,ㅆ,ㄴ,ㄹ"),
     ("후음(목청소리)에 해당하는 자음은?","ㅎ"),
     ("우리말 단모음은 모두 몇 개인가?","10개"),
     ("단모음 10개를 모두 쓰시오.","ㅏ,ㅐ,ㅓ,ㅔ,ㅗ,ㅚ,ㅜ,ㅟ,ㅡ,ㅣ"),
     ("전설 모음을 모두 말하시오.","ㅣ, ㅔ, ㅐ, ㅟ, ㅚ"),
     ("후설 모음을 모두 말하시오.","ㅡ, ㅓ, ㅏ, ㅜ, ㅗ"),
     ("고모음을 모두 말하시오.","ㅣ, ㅟ, ㅡ, ㅜ"),
     ("중모음을 모두 말하시오.","ㅔ, ㅚ, ㅓ, ㅗ"),
     ("저모음을 모두 말하시오.","ㅐ, ㅏ"),
     ("원순 모음을 모두 말하시오.","ㅟ, ㅚ, ㅜ, ㅗ"),
     ("평순 모음을 모두 말하시오.","ㅣ, ㅔ, ㅐ, ㅡ, ㅓ, ㅏ"),
     ("'ㅟ'의 혀의 높이/혀의 위치/입술 모양을 말하시오.","고모음 / 전설 / 원순"),
     ("'ㅏ'의 혀의 높이/혀의 위치/입술 모양을 말하시오.","저모음 / 후설 / 평순"),
     ("'ㅗ'의 혀의 높이/혀의 위치/입술 모양을 말하시오.","중모음 / 후설 / 원순"),
     ("'ㅣ'의 혀의 높이/혀의 위치/입술 모양을 말하시오.","고모음 / 전설 / 평순"),
     ("'ㅐ'의 혀의 높이/혀의 위치/입술 모양을 말하시오.","저모음 / 전설 / 평순"),
     ("발음할 때 입술 모양이나 혀의 위치가 변하는 모음을 무엇이라 하는가?","이중 모음"),
     ("이중 모음의 예를 3개 이상 말하시오.","ㅑ,ㅕ,ㅛ,ㅠ,ㅘ,ㅝ,ㅢ 등"),
     ("반모음 'ㅣ[j]'가 결합한 이중모음을 2개 이상 말하시오.","ㅑ, ㅕ, ㅛ, ㅠ, ㅒ, ㅖ 등"),
     ("반모음 'ㅗ/ㅜ[w]'가 결합한 이중모음을 2개 이상 말하시오.","ㅘ, ㅙ, ㅝ, ㅞ, ㅟ 등"),
     ("자음을 소리내는 방법(조음 방법)의 종류 5가지를 말하시오.","파열음, 파찰음, 마찰음, 비음, 유음"),
     ("자음의 조음 위치 5가지를 말하시오.","양순음, 치조음, 경구개음, 연구개음, 후음"),
     ("소리의 세기에 따른 자음 분류 3가지는?","예사소리, 된소리, 거센소리"),
     ("콧속을 울려서 내는 소리를 무엇이라 하는가?","비음(콧소리)"),
     ("혀끝을 잇몸에 가볍게 대었다 떼거나 굴려 내는 소리는?","유음"),
     ("공기를 막았다가 터뜨리며 내는 소리는?","파열음"),
     ("'ㅊ'과 'ㅈ'의 공통된 조음 방법은?","파찰음"),
     ("'ㅁ'과 'ㅂ'의 공통된 조음 위치는?","입술소리(양순음)"),
     ("뜻을 구별해 주는 소리의 가장 작은 단위는?","음운"),
     ("'불'과 '풀'의 뜻을 구별해 주는 음운은?","ㅂ / ㅍ (자음)"),
     ("'살'과 '술'의 뜻을 구별해 주는 음운은?","ㅏ / ㅜ (모음)"),
    ]
    for q,a in extra: Q.append({"q":q,"a":a})
    return Q[:100]

QUESTIONS = build_questions()

GOLDEN = [
 ("🎂 생일 축하금","오늘의 주인공! 생일 축하금을 받습니다.", 20),
 ("🎤 개인기 찬스","지정 학생이 개인기 성공 시 보너스! (교사 판정)", 15),
 ("🤝 단합력 테스트","모둠 전원이 구호를 외치면 단합 보너스!", 10),
 ("🎁 보너스 카드","행운의 보너스 점수를 획득합니다.", 15),
 ("💸 통행료 납부","길을 잘못 들어 통행료를 냈습니다.", -10),
 ("🚓 과속 벌금","너무 신났네요! 벌금을 냅니다.", -10),
 ("🧹 청소 당번","청소 당번에 걸려 점수가 차감됩니다.", -5),
 ("⭐ 럭키 찬스","아무 일도 일어나지 않았어요. 럭키!", 5),
]
EMOJIS = ["🐶","🐱","🐰","🐼","🦊","🐯","🐸","🐵"]
COLORS = ["#ff6b6b","#4dabf7","#51cf66","#ffd43b","#cc5de8","#ff922b","#20c997","#f06595"]

def board_layout():
    coords=[]
    for c in range(10): coords.append((0,c))
    for r in range(1,10): coords.append((r,9))
    for c in range(8,-1,-1): coords.append((9,c))
    for r in range(8,0,-1): coords.append((r,0))
    cells=[]
    for i,(r,c) in enumerate(coords):
        if i==0: t,label=("start","출발\n🏁")
        elif i==9: t,label=("island","무인도\n🏝️")
        elif i in (18,27): t,label=("golden","황금열쇠\n🗝️")
        else: t,label=("quiz","문법\n📖")
        cells.append({"idx":i,"r":r,"c":c,"type":t,"label":label})
    return cells
BOARD = board_layout()
NCELL = len(BOARD)

def init():
    s=st.session_state
    s.setdefault("phase","setup"); s.setdefault("teams",[]); s.setdefault("order",[])
    s.setdefault("turn_ptr",0); s.setdefault("step","roll"); s.setdefault("dice",None)
    s.setdefault("cur_q",None); s.setdefault("cur_student",None); s.setdefault("active_team",None)
    s.setdefault("msg",""); s.setdefault("winner",None)
init()
ss=st.session_state

st.markdown('''<style>
@keyframes pop{0%{transform:scale(.3)}60%{transform:scale(1.2)}100%{transform:scale(1)}}
@keyframes bounce{0%,100%{transform:translateY(0)}50%{transform:translateY(-10px)}}
.dice{font-size:90px;text-align:center;animation:pop .6s;background:#fff3bf;border-radius:20px;padding:10px;border:4px solid #ffd43b}
.bigq{font-size:30px;font-weight:800;color:#1864ab;background:#e7f5ff;padding:20px;border-radius:16px;border:3px dashed #4dabf7}
.cnt{font-size:80px;text-align:center;color:#e8590c;font-weight:900;animation:bounce .5s infinite}
.cell{border:2px solid #ced4da;border-radius:8px;padding:2px;font-size:11px;text-align:center;
      display:flex;flex-direction:column;justify-content:center;align-items:center;min-height:52px;white-space:pre-line}
.q{background:#f8f9fa}.golden{background:#fff3bf}.island{background:#d0ebff}.start{background:#d3f9d8;font-weight:800}
.center{grid-area:2/2/10/10;background:#fff9db;border-radius:16px;display:flex;
      flex-direction:column;justify-content:center;align-items:center;border:3px solid #ffe066}
.pieces{font-size:18px;line-height:1}
.board{display:grid;grid-template-columns:repeat(10,1fr);grid-template-rows:repeat(10,1fr);
      gap:3px;aspect-ratio:1/1;max-width:760px}
.title{font-weight:900;background:linear-gradient(90deg,#ff6b6b,#4dabf7,#51cf66);
      -webkit-background-clip:text;-webkit-text-fill-color:transparent;font-size:34px}
</style>''',unsafe_allow_html=True)

def render_board():
    pos_map={}
    for t in ss.teams:
        pos_map.setdefault(t["pos"],[]).append(t["emoji"])
    html='<div class="board">'
    for cell in BOARD:
        pieces="".join(pos_map.get(cell["idx"],[]))
        html+=f'<div class="cell {cell["type"]}" style="grid-row:{cell["r"]+1};grid-column:{cell["c"]+1}">{cell["label"]}<span class="pieces">{pieces}</span></div>'
    turn_txt=""
    if ss.phase=="play" and ss.winner is None:
        at=ss.active_team if ss.active_team is not None else ss.order[ss.turn_ptr]
        turn_txt=f'<div style="font-size:20px;font-weight:800">▶ {ss.teams[at]["emoji"]} {ss.teams[at]["name"]} 차례</div>'
    dice_txt=f'<div class="dice">🎲 {ss.dice}</div>' if ss.dice else '<div style="font-size:50px">🎲</div>'
    html+=f'<div class="center">{dice_txt}{turn_txt}</div></div>'
    st.markdown(html,unsafe_allow_html=True)

def render_scores():
    st.markdown("### 🏆 점수 현황판")
    for t in ss.teams:
        flag=" 💀파산" if t["bankrupt"] else (" 👑우승" if ss.winner==t["name"] else "")
        st.markdown(f"**{t['emoji']} {t['name']} : {t['score']}점**{flag}")
        st.caption("　".join([f"{m}:{t['mscore'][m]}" for m in t['members']]))
        st.progress(max(0.0,min(1.0,(t["score"]+100)/600)))

def alive_teams():
    return [i for i,t in enumerate(ss.teams) if not t["bankrupt"]]

def check_end():
    alive=alive_teams()
    for t in ss.teams:
        if not t["bankrupt"] and t["score"]>=500:
            ss.winner=t["name"]; ss.step="over"; return True
    if len(alive)==1 and len(ss.teams)>1:
        ss.winner=ss.teams[alive[0]]["name"]; ss.step="over"; return True
    return False

def apply_score(ti,delta,student=None):
    t=ss.teams[ti]; t["score"]+=delta
    if student: t["mscore"][student]=t["mscore"].get(student,0)+delta
    if t["score"]<=-100 and not t["bankrupt"]:
        t["bankrupt"]=True; ss.msg=f"💀 {t['name']} 모둠이 파산했습니다!"

def next_turn():
    if check_end(): return
    n=len(ss.order)
    for _ in range(n):
        ss.turn_ptr=(ss.turn_ptr+1)%n
        t=ss.teams[ss.order[ss.turn_ptr]]
        if t["bankrupt"]: continue
        if t.get("skip"):
            t["skip"]=False; ss.msg=f"🏝️ {t['name']} 모둠은 무인도에서 1턴 쉽니다!"; continue
        break
    ss.active_team=None; ss.dice=None; ss.step="roll"; ss.cur_q=None

def new_question(ti):
    ss.cur_q=random.choice(QUESTIONS)
    ss.cur_student=random.choice(ss.teams[ti]["members"])
    ss.active_team=ti

st.markdown('<div class="title">🎲 국어 문법 부루마블 🎲</div>',unsafe_allow_html=True)
st.caption("중3 국어 · 음운(자음체계표·모음체계표) 퀴즈 보드게임")

if ss.phase=="setup":
    st.subheader("1️⃣ 모둠 만들기")
    n=st.number_input("모둠 수",2,8,4)
    teams=[]; cols=st.columns(2)
    for i in range(int(n)):
        with cols[i%2]:
            st.markdown(f"**{EMOJIS[i]} {i+1}모둠**")
            name=st.text_input(f"모둠명 {i+1}",value=f"{i+1}모둠",key=f"nm{i}")
            mem=st.text_input(f"구성원(쉼표, 최대 4명) {i+1}",value="학생1,학생2",key=f"mem{i}")
            members=[m.strip() for m in mem.split(",") if m.strip()][:4]
            teams.append({"name":name,"members":members,"emoji":EMOJIS[i],"color":COLORS[i],
                          "pos":0,"score":100,"mscore":{m:0 for m in members},
                          "bankrupt":False,"skip":False})
    if st.button("✅ 게임 만들기",type="primary"):
        if all(t["members"] for t in teams):
            ss.teams=teams; ss.phase="order"; st.rerun()
        else: st.error("모든 모둠에 구성원을 입력하세요.")

elif ss.phase=="order":
    st.subheader("2️⃣ 진행 순서 정하기")
    if not ss.order: ss.order=list(range(len(ss.teams)))
    st.write("현재 순서:", " → ".join(ss.teams[i]["name"] for i in ss.order))
    c1,c2=st.columns(2)
    if c1.button("🎲 랜덤으로 순서 섞기"):
        random.shuffle(ss.order); st.rerun()
    if c2.button("▶ 이 순서로 시작",type="primary"):
        ss.turn_ptr=0; ss.phase="play"; ss.step="roll"; st.rerun()

elif ss.phase=="play":
    left,right=st.columns([1,2])
    with left: render_scores()
    with right: render_board()
    if ss.msg: st.info(ss.msg)
    st.divider()

    if ss.step=="over":
        st.balloons()
        st.success(f"🎉🎉 우승: {ss.winner} 모둠! 축하합니다! 🎉🎉")
        if st.button("🔄 새 게임"):
            for k in list(ss.keys()): del ss[k]
            st.rerun()
        st.stop()

    cur=ss.order[ss.turn_ptr]; t=ss.teams[cur]

    if ss.step=="roll":
        st.subheader(f"🎯 {t['emoji']} {t['name']} 모둠 차례")
        if st.button("🎲 주사위 던지기!",type="primary",use_container_width=True):
            ss.msg=""; ss.dice=random.randint(1,6)
            old=t["pos"]; new=old+ss.dice
            if new>=NCELL: apply_score(cur,20); ss.msg="💰 출발선 통과! 월급 +20점"
            t["pos"]=new%NCELL
            ctype=BOARD[t["pos"]]["type"]
            if ctype in ("quiz","start"): new_question(cur); ss.step="quiz"
            elif ctype=="golden": ss.step="golden"
            elif ctype=="island": t["skip"]=True; ss.msg="🏝️ 무인도 도착! 다음 턴 쉽니다."; ss.step="island"
            st.rerun()

    elif ss.step=="golden":
        title,desc,delta=random.choice(GOLDEN)
        st.subheader("🗝️ 황금열쇠!"); st.markdown(f"### {title}"); st.write(desc)
        st.markdown(f"## {'➕' if delta>=0 else '➖'} {abs(delta)}점")
        if st.button("확인 ▶",type="primary"):
            apply_score(cur,delta); next_turn(); st.rerun()

    elif ss.step=="island":
        st.subheader("🏝️ 무인도"); st.write("다음 차례를 쉽니다.")
        if st.button("확인 ▶",type="primary"): next_turn(); st.rerun()

    elif ss.step in ("quiz","rebound"):
        at=ss.active_team; team=ss.teams[at]
        head="❓ 문제!" if ss.step=="quiz" else "🔁 기회 이동! 다른 모둠 도전"
        st.subheader(head)
        st.markdown(f"#### 🙋 {team['emoji']} {team['name']} — **{ss.cur_student}** 학생 답변!")
        st.markdown(f'<div class="bigq">{ss.cur_q["q"]}</div>',unsafe_allow_html=True)
        c1,c2=st.columns(2)
        if c1.button("⏱️ 10초 카운트다운 시작"):
            ph=st.empty()
            for s in range(10,0,-1):
                ph.markdown(f'<div class="cnt">{s}</div>',unsafe_allow_html=True); time.sleep(1)
            ph.markdown('<div class="cnt">⏰ 시간 종료!</div>',unsafe_allow_html=True)
        with c2.expander("👀 교사용 정답 보기"): st.success(ss.cur_q["a"])
        st.divider(); st.write("교사 확인 후 채점:")
        j1,j2=st.columns(2)
        if j1.button("⭕ 정답 (+10)",type="primary",use_container_width=True):
            apply_score(at,10,ss.cur_student); st.toast("정답! +10점 🎉"); next_turn(); st.rerun()
        if j2.button("❌ 오답 (-10)",use_container_width=True):
            apply_score(at,-10,ss.cur_student); st.toast("오답! -10점")
            if check_end(): st.rerun()
            others=[i for i in alive_teams() if i!=at]
            if ss.step=="quiz" and others:
                ro=random.choice(others); new_question(ro); ss.step="rebound"
                ss.msg=f"🔁 오답! 기회가 {ss.teams[ro]['name']} 모둠으로 넘어갑니다!"
            else: next_turn()
            st.rerun()
