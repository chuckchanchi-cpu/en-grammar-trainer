import streamlit as st
import random

st.set_page_config(page_title="🔤 English Grammar Trainer", page_icon="🔤", layout="wide")

# ===== English Grammar Exercises Data =====

GRAMMAR_EXERCISES = {
    "Look and Write: 看圖寫作": {
        "date": "2026-10-06",
        "description": "觀看圖片並寫出完整句子，每句不少於5個字",
        "questions": [
            {
                "question": "Look at the classroom picture. Write a sentence using 'This is...'",
                "hint": "以 'This is' 開頭，描述圖片中的一件物品或一個人",
                "answer": "This is a teacher.",
                "explanation": "使用 'This is' 描述單數事物。例如：This is a teacher. (這是一位老師。)"
            },
            {
                "question": "Look at the classroom picture. Write a sentence using 'These are...'",
                "hint": "以 'These are' 開頭，描述圖片中的多件物品或多個人",
                "answer": "These are students.",
                "explanation": "使用 'These are' 描述複數事物。例如：These are students. (這些是學生。)"
            },
            {
                "question": "Write a sentence about yourself using 'I am...'",
                "hint": "使用 'I am' 介紹自己，可以寫年齡、名字或感受",
                "answer": "I am a student.",
                "explanation": "使用 'I am' 介紹自己。例如：I am a student. (我是一個學生。)"
            },
            {
                "question": "Write a sentence about something you like using 'I like...'",
                "hint": "使用 'I like' 表達喜歡的事物，可以是食物、活動或顏色",
                "answer": "I like pizza.",
                "explanation": "使用 'I like' 表達喜好。例如：I like pizza. (我喜歡吃 pizza。)"
            },
            {
                "question": "Look at the picture. Write 3 sentences about what you see.",
                "hint": "運用 'This is', 'These are', 'I am', 'I like' 等句型",
                "answer": "This is a classroom. These are desks. I am a student.",
                "explanation": "結合多個句型描述圖片。每句不少於5個字。"
            }
        ]
    },
    "Grammar 1: so (原因和結果)": {
        "date": "2026-09-20",
        "description": "使用 so 連接原因和結果句子",
        "questions": [
            {
                "question": "I want to help the homeless. I prepare meals for them sometimes.",
                "hint": "使用 so 連接兩個句子，前面加逗號",
                "answer": "I want to help the homeless, so I prepare meals for them sometimes.",
                "explanation": "原因：想幫助無家可歸者 → 結果：為他們準備食物"
            },
            {
                "question": "Chris likes helping blind people. He will sell flags next month.",
                "hint": "使用 so 連接，注意逗號位置",
                "answer": "Chris likes helping blind people, so he will sell flags next month.",
                "explanation": "原因：喜歡幫助盲人 → 結果：賣旗籌款"
            },
            {
                "question": "Karen is good at cooking. She helps her mother prepare food for the party.",
                "hint": "使用 so 連接因果關係",
                "answer": "Karen is good at cooking, so she helps her mother prepare food for the party.",
                "explanation": "原因：擅長烹飪 → 結果：幫助母親準備食物"
            },
            {
                "question": "The dog needs a home. We adopt it from the SPCA.",
                "hint": "使用 so 連接",
                "answer": "The dog needs a home, so we adopt it from the SPCA.",
                "explanation": "原因：狗隻需要家 → 結果：從 SPCA 領養"
            }
        ]
    },
    "Grammar 2: who / which (關係代詞)": {
        "date": "2026-09-20",
        "description": "使用 who 指人，使用 which 指物或動物",
        "questions": [
            {
                "question": "We can support a food charity. It prepares food for people in need.",
                "hint": "charity 是機構，使用 which",
                "answer": "We can support a food charity which prepares food for people in need.",
                "explanation": "charity = 機構 → 使用 which"
            },
            {
                "question": "We can visit sick children. They are in hospital.",
                "hint": "children 是人，使用 who",
                "answer": "We can visit sick children who are in hospital.",
                "explanation": "children = 人 → 使用 who"
            },
            {
                "question": "I know a boy. He collects money for blind people.",
                "hint": "boy 是人，使用 who",
                "answer": "I know a boy who collects money for blind people.",
                "explanation": "boy = 人 → 使用 who"
            },
            {
                "question": "I have a pet cat. It was adopted from the SPCA.",
                "hint": "cat 是動物，使用 which",
                "answer": "I have a pet cat which was adopted from the SPCA.",
                "explanation": "cat = 動物 → 使用 which"
            }
        ]
    },
    "Connectives: so / so that / because": {
        "date": "2026-09-20",
        "description": "分辨 so (結果), so that (目的), because (原因) 的用法",
        "questions": [
            {
                "question": "It was my birthday yesterday ___ we had a big meal.",
                "options": ["so", "so that", "because"],
                "answer": "so",
                "explanation": "生日是原因，吃大餐是結果 → 使用 so"
            },
            {
                "question": "I will help Mum ___ she will not be so busy.",
                "options": ["so", "so that", "because"],
                "answer": "so that",
                "explanation": "目的是讓母親不那麼忙碌 → 使用 so that (後有 will)"
            },
            {
                "question": "He did not play ___ he was sick.",
                "options": ["so", "so that", "because"],
                "answer": "because",
                "explanation": "生病是原因，沒有比賽是結果 → 使用 because"
            }
        ]
    },
    "Unit 3: Environmental Protection - Adverbs of Manner": {
        "date": "2026-10-08",
        "description": "Unit 3 環境保護 — 方式副詞 (Adverbs of Manner)",
        "questions": [
            {
                "question": "The students should listen to the teacher ______.",
                "hint": "將形容詞 careful 變成副詞 carefully",
                "answer": "carefully",
                "explanation": "形容詞 → 副詞：careful + ly = carefully (小心地)"
            },
            {
                "question": "Please ______ turn off the lights when you leave the room.",
                "hint": "將形容詞 careful 變成副詞 carefully",
                "answer": "carefully",
                "explanation": "修飾動詞 turn off 需要用副詞 carefully"
            },
            {
                "question": "The children played ______ in the playground.",
                "hint": "將形容詞 happy 變成副詞 happily",
                "answer": "happily",
                "explanation": "形容詞 → 副詞：happy → happily (快樂地)"
            },
            {
                "question": "We must throw the rubbish ______.",
                "hint": "將形容詞 proper 變成副詞 properly",
                "answer": "properly",
                "explanation": "形容詞 → 副詞：proper + ly = properly (正確地)"
            },
            {
                "question": "Please read the passage ______.",
                "hint": "將形容詞 careful 變成副詞 carefully",
                "answer": "carefully",
                "explanation": "修飾動詞 read 需要用副詞 carefully (仔細地)"
            },
            {
                "question": "The turtle walks ______.",
                "hint": "將形容詞 slow 變成副詞 slowly",
                "answer": "slowly",
                "explanation": "形容詞 → 副詞：slow + ly = slowly (慢地)"
            },
            {
                "question": "The students sit ______ in the library.",
                "hint": "將形容詞 quiet 變成副詞 quietly",
                "answer": "quietly",
                "explanation": "形容詞 → 副詞：quiet + ly = quietly (安靜地)"
            },
            {
                "question": "Do not speak ______ in the hospital.",
                "hint": "將形容詞 loud 變成副詞 loudly",
                "answer": "loudly",
                "explanation": "形容詞 → 副詞：loud + ly = loudly (大聲地)"
            }
        ]
    },
    "Adverbs: 副詞 (方式 + 頻率)": {
        "date": "2026-10-06",
        "description": "學習方式副詞 (how) 和頻率副詞 (how often)",
        "questions": [
            {
                "question": "She sings ___. (beautiful)",
                "hint": "將形容詞 beautiful 變成副詞 beautifully",
                "answer": "beautifully",
                "explanation": "形容詞 → 副詞：beautiful + ly = beautifully"
            },
            {
                "question": "He runs ___. (quick)",
                "hint": "將形容詞 quick 變成副詞 quickly",
                "answer": "quickly",
                "explanation": "形容詞 → 副詞：quick + ly = quickly"
            },
            {
                "question": "I ___ go to school by bus. (always)",
                "hint": "頻率副詞放在動詞前面",
                "answer": "always",
                "explanation": "頻率副詞 (always/usually/often/sometimes/never) 放在動詞前"
            },
            {
                "question": "She is ___ late for school. (never)",
                "hint": "頻率副詞放在 be 動詞後面",
                "answer": "never",
                "explanation": "頻率副詞放在 be 動詞 (is/am/are) 後面"
            }
        ]
    }
}

st.title("🔤 English Grammar Trainer")
st.markdown("### 分主題練習 — 選擇一個主題開始！")

# 選擇練習主題（顯示日期）
def format_topic(topic):
    data = GRAMMAR_EXERCISES[topic]
    return f"{topic} ({data['date']})"

selected_topic = st.selectbox(
    "選擇練習主題：",
    list(GRAMMAR_EXERCISES.keys()),
    format_func=format_topic
)

if selected_topic:
    topic_data = GRAMMAR_EXERCISES[selected_topic]
    st.subheader(f"📚 {selected_topic}")
    st.info(topic_data["description"])
    
    # 顯示題目
    for i, q in enumerate(topic_data["questions"]):
        with st.expander(f"Q{i+1}: {q['question']}", expanded=False):
            st.write("**提示：**")
            st.warning(q.get("hint", ""))
            
            if "options" in q:
                user_answer = st.radio("你的答案：", q["options"], key=f"q{i}")
                if st.button(f"檢查 Q{i+1}", key=f"check{i}"):
                    if user_answer == q["answer"]:
                        st.success("✅ 正確！")
                    else:
                        st.error(f"❌ 錯誤！正確答案：{q['answer']}")
            else:
                user_answer = st.text_area("你的答案：", key=f"q{i}")
                if st.button(f"檢查 Q{i+1}", key=f"check{i}"):
                    if user_answer.strip().lower() == q["answer"].strip().lower():
                        st.success("✅ 正確！")
                    else:
                        st.error(f"❌ 錯誤！正確答案：\n{q['answer']}")
            
            st.markdown("**解釋：**")
            st.info(q["explanation"])

st.markdown("---")
st.markdown("💡 **重點提示：**")
st.markdown("""
- **Look and Write**: 觀看圖片並寫句，每句不少於5個字，運用 'This is/These are/I am/I like' 等句型
- **so** = 所以（結果），前面加逗號
- **so that** = 以便（目的），後常有 can/will
- **because** = 因為（原因）
- **Adverbs**: 方式副詞 = 形容詞 + ly；頻率副詞放動詞前或 be 動詞後
""")