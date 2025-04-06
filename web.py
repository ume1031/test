import streamlit as st

# 20問分のクイズデータ
quiz_data = [
    {"question": "「俺の年収2000万」これマジかな？",  "options": ["本当", "ちょっと盛ってる", "結構盛ってる", "ちょっと考えた嘘", "結構考えた嘘", "見栄張ろうとしてついた嘘"], "answer": "見栄張ろうとしてついた嘘"},
    {"question": "普通の人間の染色体が√2本としたとき人間を―2乗した生き物がいたとしたら染色体は何本？",  "options": ["2本", "4本", "√2分1本", "2分の1本", "√2本", "4分の1本"], "answer": "2分の1本"},
    {"question": "双極性障害+PTSD+ADHD+染色体半分+虚言癖こんな人間は実在するか",  "options": ["いるはずない", "ありえない", "いる", "いそうではある", "いなさそう", "わからん"], "answer": "いる"},
    {"question": "？に入るものは？", "image": "images/Q1.png", "options": ["3分の1", "33%", "3分の2", "66%", "3分の3", "100%"], "answer": "3分の3"},
    {"question": "嘘つき精神病通い親の財布金盗み童貞包茎野郎は実在するか",  "options": ["セフレすぎる", "英検すぎる", "クラスの中心すぎる", "いる", "仲間すぎる", "イきりmacすぎる"], "answer": "いる"},
    {"question": "ファンタでうまいのはオレンジ味である", "options": ["そうだよ", "そうだよ", "そうだよ", "そうだよ", "そうだよ", "そうだよ"], "answer": "そうだよ"},
    {"question": "webサイトにおけるCookieはどんな役割か", "options": ["サイトの最新情報をサイトに反映するためのファイル", "デバイスの情報をサイトのサーバーに送信するファイル", "サイトの設定や変更、ログインなどを保存しておくファイル", "リンクをクリックした際ほかのサイトに飛んでもいいという同意", "通信速度をあげるためのもの", "HikakinClipTV"], "answer": "サイトの設定や変更、ログインなどを保存しておくファイル"},
    {"question": "IPv6はなぜ設計されたか",  "options": ["IPv4のセキュリティが強固すぎてIotデバイスと接続しずらいから", "IPv4のアドレス形式に限りがあってIPアドレスが足りなくなりそうだったから", "生成AIの発達に伴いインターネットが見直されたから", "darkmasuoTV", "実験", "Iotデバイスと接続しやすいようにバージョンアップされた"], "answer": "IPv4のアドレス形式に限りがあってIPアドレスが足りなくなりそうだったから"},
    {"question": "AIがデータ予測する際に一般的に使われる手法はなにか",  "options": ["ランダムフォレスト", "重回帰分析", "ニューラルネットワーク", "勘", "単回帰分析", "口コミ"], "answer": "重回帰分析"},
    {"question": "Windowsキー+Rを押して「cmd」と入力してエンターを押してそのあと「cd /」「del *」を入力してエンターを教えてみてほしい", "options": ["なんもおきない", "なんもおきない", "なんもおきない", "なんもおきない", "なんもおきない", "なんもおきない"], "answer": "なんもおきない"},
]

st.title("クイズ！")

user_answers = []

# クイズ表示
for i, quiz in enumerate(quiz_data):
    st.subheader(f"Q{i+1}. {quiz['question']}")
    
    # 画像を表示
    if "image" in quiz and quiz["image"]:
        st.image(quiz["image"], caption=f"問題{i+1}の画像", use_container_width=True)

    answer = st.radio("選択肢を選んでください", quiz['options'], key=f"q{i}")
    user_answers.append(answer)

# 採点
if st.button("採点する"):
    score = sum([1 for i, quiz in enumerate(quiz_data) if user_answers[i] == quiz["answer"]])

    st.markdown(f"### 🎯 あなたのスコア: {score} / {len(quiz_data)}")

    # フィードバックコメント
    if score == len(quiz_data):
        st.success("サブスク半年分おごります")
    elif score >= 8:
        st.info("南すぎる")
    elif score >= 5:
        st.warning("通知表オール3だろ")
    else:
        st.error("義務教育の敗北")
