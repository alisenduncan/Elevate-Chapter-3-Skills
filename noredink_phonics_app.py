import streamlit as st
import pandas as pd
import random

# Set Streamlit Page Config
st.set_page_config(
    page_title="Elevate Phonics Master - NoRedInk Style",
    page_icon="✏️",
    layout="wide"
)

# Custom CSS for Dyslexia-Friendly Fonts & NoRedInk Aesthetic Styling
def apply_custom_css(font_choice):
    font_family_map = {
        "Lexend (Clean & Dyslexia-Friendly)": "'Lexend', sans-serif",
        "OpenDyslexic (Dyslexia-Focused)": "'OpenDyslexic', sans-serif",
        "Atkinson Hyperlegible": "'Atkinson Hyperlegible', sans-serif",
        "Comic Neue / Child Friendly": "'Comic Neue', sans-serif",
        "Arial / Standard Sans": "Arial, sans-serif"
    }
    selected_font = font_family_map.get(font_choice, "'Lexend', sans-serif")
    
    css = f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Lexend:wght@300;400;600;700&family=Atkinson+Hyperlegible:ital,wght@0,400;0,700;1,400&family=Comic+Neue:wght@400;700&display=swap');
    
    html, body, [class*="css"] {{
        font-family: {selected_font} !important;
        background-color: #F8F9FA;
        color: #2D3748;
    }}
    
    .stButton>button {{
        font-family: {selected_font} !important;
        border-radius: 12px;
        background-color: #4C6EF5;
        color: white;
        font-weight: 600;
        padding: 0.5rem 1.5rem;
        border: none;
        transition: all 0.2s ease;
    }}
    .stButton>button:hover {{
        background-color: #3B5BDB;
        transform: translateY(-1px);
        box-shadow: 0 4px 12px rgba(76, 110, 245, 0.25);
    }}
    
    .card {{
        background: white;
        border-radius: 16px;
        padding: 1.5rem;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.05);
        border: 1px solid #E9ECEF;
        margin-bottom: 1.5rem;
    }}
    
    .badge-mastered {{
        background-color: #D3F9D8;
        color: #2B8A3E;
        padding: 0.25rem 0.75rem;
        border-radius: 20px;
        font-weight: 700;
        font-size: 0.85rem;
    }}
    
    .badge-practicing {{
        background-color: #FFF3BF;
        color: #F08C00;
        padding: 0.25rem 0.75rem;
        border-radius: 20px;
        font-weight: 700;
        font-size: 0.85rem;
    }}
    
    .badge-notstarted {{
        background-color: #F1F3F5;
        color: #868E96;
        padding: 0.25rem 0.75rem;
        border-radius: 20px;
        font-weight: 700;
        font-size: 0.85rem;
    }}
    
    .proving-box {{
        background-color: #E7F5FF;
        border-left: 5px solid #1C7ED6;
        padding: 1rem;
        border-radius: 8px;
        font-size: 1.1rem;
        margin: 1rem 0;
    }}
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)

# ---------------------------------------------------------
# INITIALIZE SESSION STATE
# ---------------------------------------------------------
if "classes" not in st.session_state:
    st.session_state.classes = {
        "Period 1 - Reading Stars": ["Alex M.", "Bella C.", "Chris P.", "David K."],
        "Period 3 - Phonics Champions": ["Emma R.", "Frankie L.", "Grace T.", "Hannah W."]
    }

if "student_progress" not in st.session_state:
    st.session_state.student_progress = {
        "Alex M.": {"class": "Period 1 - Reading Stars", "skills": {}},
        "Bella C.": {"class": "Period 1 - Reading Stars", "skills": {}},
        "Chris P.": {"class": "Period 1 - Reading Stars", "skills": {}},
        "David K.": {"class": "Period 1 - Reading Stars", "skills": {}},
        "Emma R.": {"class": "Period 3 - Phonics Champions", "skills": {}},
        "Frankie L.": {"class": "Period 3 - Phonics Champions", "skills": {}},
        "Grace T.": {"class": "Period 3 - Phonics Champions", "skills": {}},
        "Hannah W.": {"class": "Period 3 - Phonics Champions", "skills": {}},
    }

skills_list = [
    "Phonetic Skill 1", "Phonetic Skill 2", "Phonetic Skill 3",
    "Phonetic Skill 4", "Phonetic Skill 5", "Adding Suffixes to Phonetic Skills 1 and 2",
    "Three Sounds of -ED", "Vowel Families O+I", "Another Sound for C and G",
    "Adding Suffixes to Phonetic Skills 3 and 4", "GH IGH and IGHT", "Adding Suffixes to Phonetic Skill 5"
]

for student in st.session_state.student_progress:
    for sk in skills_list:
        if sk not in st.session_state.student_progress[student]["skills"]:
            st.session_state.student_progress[student]["skills"][sk] = {
                "attempts": random.randint(0, 15),
                "correct": random.randint(0, 12),
                "status": random.choice(["Mastered", "Practicing", "Not Started"]),
                "reflection_score": random.choice([1, 2, 3, 4, 5])
            }

# ---------------------------------------------------------
# CURRICULUM DATA & QUESTION GENERATOR
# Grounded strictly in Elevate Chapter 3 Practice Book
# ---------------------------------------------------------

CURRICULUM = {
    "Phonetic Skill 1": {
        "rule": "When a vowel is followed by one guardian consonant, the vowel sound is short.",
        "marking": "Place an x under the vowel. Mark guardian consonant with 1 guardian star (*). Mark vowel short with breve (˘). Digraphs count as 1 guardian consonant.",
        "words": ["stop", "man", "path", "hat", "dog", "rug", "wish", "such", "box", "big", "step", "run", "quit", "plan", "cash", "frog", "swim", "flag", "cut"]
    },
    "Phonetic Skill 2": {
        "rule": "When a vowel is followed by two guardian consonants, the vowel sound is short.",
        "marking": "Place an x under the vowel. Mark each guardian consonant with a guardian star (*) [Blends get 2 stars (**); Digraphs follow another consonant get 1 star]. Mark vowel short with breve (˘).",
        "words": ["last", "help", "soft", "must", "match", "list", "mess", "next", "stand", "ask", "pitch", "dust", "lift", "bench", "fizz", "camp", "plant", "desk"]
    },
    "Phonetic Skill 3": {
        "rule": "When the vowel stands alone (has no guardian consonant), the vowel sound is long.",
        "marking": "Place an x under the vowel. No guardian consonants. Mark vowel long with macron (¯). Exceptions: to, the, do, who, two.",
        "words": ["go", "hi", "we", "me", "so", "be", "I", "no", "she", "flu"]
    },
    "Phonetic Skill 4": {
        "rule": "When silent e comes at the end of a word, it makes the first vowel sound long.",
        "marking": "Place an x under first vowel and silent e. Draw a straight line down through e and its x. Mark first vowel long with macron (¯).",
        "words": ["bone", "lake", "state", "bathe", "side", "same", "vote", "life", "cute", "safe", "make", "time", "drive", "clothe", "home", "name", "smile", "stove"]
    },
    "Phonetic Skill 5": {
        "rule": "When two vowels stand next to each other (adjacent), the second vowel is silent, and the first vowel sound is long.",
        "marking": "Adjacent vowels: ai, ay, ea, ee, oa, oe, ui, ue, ie. Place x under each vowel. Draw line through 2nd vowel and its x. Mark 1st vowel long with macron (¯).",
        "words": ["see", "wait", "feel", "true", "paint", "keep", "road", "read", "need", "heat", "rain", "say", "pie", "blue", "boat", "toe", "lie", "fruit"]
    },
    "Adding Suffixes to Phonetic Skills 1 and 2": {
        "rule": "To add -ing, -ed, -er, -est to Skill 1 words: double the final consonant. For Skill 2, words ending in x, or Digraphs: just add suffix.",
        "marking": "1. Prove base word. 2. Rewrite word with suffix (check for 2 consonants before suffix). 3. Underline the suffix.",
        "examples": [("hop", "-ing", "hopping"), ("test", "-ed", "tested"), ("slip", "-ing", "slipping"), ("plant", "-er", "planter"), ("big", "-est", "biggest"), ("fix", "-ing", "fixing")]
    },
    "Three Sounds of -ED": {
        "rule": "The suffix -ed has 3 sounds: /t/ after voiceless letters (f, k, p, s, x); /d/ after voiced letters (n, m, b, g, v, l, z, vowels); /id/ after t or d.",
        "marking": "Prove base word, rewrite with suffix -ed, underline suffix, identify sound (/t/, /d/, or /id/).",
        "examples": [("drop", "/t/"), ("call", "/d/"), ("land", "/id/"), ("stop", "/t/"), ("rub", "/d/"), ("test", "/id/"), ("fix", "/t/"), ("buzz", "/d/"), ("plant", "/id/")]
    },
    "Vowel Families O+I": {
        "rule": "When two consonants follow o or i, the vowel sound will often be long. Vowel Families: -old, -olt, -ost, -ind, -ild.",
        "marking": "Place an x under vowel. Underline Vowel Family. Mark vowel long with macron (¯).",
        "words": ["hold", "jolt", "most", "grind", "mild", "scold", "volt", "host", "mind", "wild", "find", "bolt", "gold", "child", "post"]
    },
    "Another Sound for C and G": {
        "rule": "C before e/i = /s/ (soft C). G before e/i = /j/ (soft G). Endings: long vowel ends -ge (cage); short vowel ends -dge (judge).",
        "marking": "Draw arc above ci/ce with 's' ('Bridge S'). Draw arc above gi/ge with 'j' ('Bridge J'). Two consonants act as guardians (dance, prince).",
        "words": ["nice", "dance", "page", "bridge", "wage", "place", "gel", "prince", "age", "cell", "stage", "since", "ice", "gem", "face", "judge", "huge", "lodge"]
    },
    "Adding Suffixes to Phonetic Skills 3 and 4": {
        "rule": "Skill 3: just add suffix (go -> going). Skill 4 + vowel suffix (-ing, -ed, -er, -est): drop silent e. Skill 4 + consonant suffix (-ful, -less, -ness, -able): keep silent e.",
        "marking": "Prove base word. Rewrite with suffix. Underline suffix.",
        "examples": [("go", "-ing", "going"), ("hope", "-ing", "hoping"), ("late", "-est", "latest"), ("grace", "-ful", "graceful"), ("hope", "-less", "hopeless"), ("size", "-able", "sizeable")]
    },
    "GH IGH and IGHT": {
        "rule": "1) gh at start = /g/ (ghost) with silent h. 2) gh at end = /f/ (laugh) with small f. 3) igh/ight = silent gh, cross out g & h, mark i long.",
        "marking": "Start gh: mark h silent. End gh: small f above gh. igh/ight: cross out g and h, mark i long with macron (¯).",
        "words": ["bright", "high", "night", "tight", "sigh", "fight", "light", "flight", "ghost", "laugh", "rough", "might", "right"]
    },
    "Adding Suffixes to Phonetic Skill 5": {
        "rule": "To add suffixes -ing, -ed, -er, -est to Phonetic Skill 5 words: just add the suffix without doubling or dropping.",
        "marking": "1. Prove base word. 2. Rewrite word with suffix. 3. Underline the suffix.",
        "examples": [("need", "-ed", "needed"), ("wait", "-ing", "waiting"), ("clean", "-er", "cleaner"), ("deep", "-est", "deepest"), ("roast", "-ed", "roasted"), ("rain", "-ing", "raining")]
    }
}

def generate_question(skill_name):
    data = CURRICULUM[skill_name]
    
    if skill_name in ["Phonetic Skill 1", "Phonetic Skill 2", "Phonetic Skill 3", "Phonetic Skill 4", "Phonetic Skill 5"]:
        word = random.choice(data["words"])
        qtype = random.choice(["proving", "rule"])
        
        if qtype == "proving":
            if skill_name == "Phonetic Skill 1":
                correct = f"x under vowel, 1 guardian star (*) on consonant, breve (˘) on vowel"
                wrongs = [
                    "x under vowel, 2 guardian stars (**) on consonant, macron (¯) on vowel",
                    "x under vowel, line through consonant, no vowel mark",
                    "x under vowel, arc on consonant, macron (¯) on vowel"
                ]
            elif skill_name == "Phonetic Skill 2":
                correct = f"x under vowel, guardian stars (*) on both consonants, breve (˘) on vowel"
                wrongs = [
                    "x under vowel, 1 guardian star (*), macron (¯) on vowel",
                    "x under vowel, arc over consonants, no star",
                    "line through both consonants, macron (¯) on vowel"
                ]
            elif skill_name == "Phonetic Skill 3":
                correct = "x under vowel, no guardian consonants, mark vowel long with macron (¯)"
                wrongs = [
                    "x under vowel, 1 guardian star (*), mark vowel short with breve (˘)",
                    "x under vowel, draw line through vowel",
                    "arc over vowel, mark vowel short"
                ]
            elif skill_name == "Phonetic Skill 4":
                correct = "x under 1st vowel & silent e, line through e and its x, mark 1st vowel long with macron (¯)"
                wrongs = [
                    "x under 1st vowel, guardian star on ending e, mark 1st vowel short",
                    "x under silent e only, arc over consonant",
                    "double the ending e and mark both vowels long"
                ]
            else: # Skill 5
                correct = "x under each vowel, line through 2nd vowel and its x, mark 1st vowel long with macron (¯)"
                wrongs = [
                    "x under 1st vowel only, guardian star on 2nd vowel",
                    "arc over both vowels, mark both short with breve (˘)",
                    "x under 2nd vowel, line through 1st vowel"
                ]
            
            opts = wrongs + [correct]
            random.shuffle(opts)
            return {
                "question": f"How do you correctly prove the word **'{word}'** according to {skill_name} in Elevate Phonics?",
                "options": opts,
                "answer": correct,
                "explanation": f"Rule: {data['rule']} Markings: {data['marking']}"
            }
        else:
            if skill_name in ["Phonetic Skill 1", "Phonetic Skill 2"]:
                correct = "Short, because it is followed by guardian consonant(s)."
                wrongs = ["Long, because the vowel stands alone.", "Silent, because of ending e.", "Long, because of adjacent vowels."]
            elif skill_name == "Phonetic Skill 3":
                correct = "Long, because the vowel stands alone (no guardian consonant)."
                wrongs = ["Short, because of guardian consonants.", "Silent, because it comes first.", "Short, because of adjacent vowels."]
            elif skill_name == "Phonetic Skill 4":
                correct = "Long, because silent e at the end makes the first vowel long."
                wrongs = ["Short, because the middle consonant acts as a guardian.", "Silent, because it stands alone.", "Short, because of Vowel Families."]
            else:
                correct = "Long, because when two vowels are adjacent, the 2nd is silent and 1st is long."
                wrongs = ["Short, because both vowels make a short sound.", "Long, because of guardian consonants.", "Silent, because of ending -ed."]
            
            opts = wrongs + [correct]
            random.shuffle(opts)
            return {
                "question": f"Why is the vowel sound in **'{word}'** pronounced the way it is?",
                "options": opts,
                "answer": correct,
                "explanation": f"Rule: {data['rule']}"
            }
            
    elif "Suffixes" in skill_name:
        if "1 and 2" in skill_name or "Skill 5" in skill_name:
            example = random.choice(data["examples"])
            base, suf, res = example
            qtext = f"What is the correct form when you add **'{suf}'** to the base word **'{base}'**?"
            correct = res
            wrongs = [base + suf, base + base[-1] + suf if "2" in skill_name else base[:-1] + suf, base + "e" + suf]
            opts = list(set([w for w in wrongs if w != correct]))[:3] + [correct]
            random.shuffle(opts)
            return {
                "question": qtext,
                "options": opts,
                "answer": correct,
                "explanation": f"Elevate Suffix Rule: {data['rule']}"
            }
        else: # Skills 3 and 4
            example = random.choice(data["examples"])
            base, suf, res = example
            qtext = f"When adding the suffix **'{suf}'** to the Phonetic Skill word **'{base}'**, what is the correct new word?"
            correct = res
            wrongs = [base + suf, base[:-1] + suf if res == base + suf else base + base[-1] + suf, base + "ing"]
            opts = list(set([w for w in wrongs if w != correct]))[:3] + [correct]
            random.shuffle(opts)
            return {
                "question": qtext,
                "options": opts,
                "answer": correct,
                "explanation": f"Rule for Skills 3 & 4 Suffixes: {data['rule']}"
            }
            
    elif skill_name == "Three Sounds of -ED":
        example = random.choice(data["examples"])
        word, snd = example
        qtext = f"In Elevate Phonics, what sound does the suffix **-ed** make in the word **'{word}'**?"
        correct = snd
        opts = ["/t/", "/d/", "/id/"]
        return {
            "question": qtext,
            "options": opts,
            "answer": correct,
            "explanation": f"Rule: {data['rule']}"
        }
        
    elif skill_name == "Vowel Families O+I":
        word = random.choice(data["words"])
        qtext = f"How is the vowel in the Vowel Family word **'{word}'** proved and pronounced?"
        correct = "The vowel is marked long (¯) because it is followed by a Vowel Family pattern (-old, -olt, -ost, -ind, -ild)."
        wrongs = [
            "The vowel is short because it has two guardian consonants.",
            "The vowel is silent because of an adjacent vowel.",
            "The vowel is short because it ends in a blend."
        ]
        opts = wrongs + [correct]
        random.shuffle(opts)
        return {
            "question": qtext,
            "options": opts,
            "answer": correct,
            "explanation": f"Vowel Families Rule: {data['rule']}"
        }
        
    elif skill_name == "Another Sound for C and G":
        word = random.choice(data["words"])
        qtext = f"How do you mark and prove the soft C or soft G sound in **'{word}'**?"
        correct = "Draw an arc above ci/ce with 's' ('Bridge S') or above gi/ge with 'j' ('Bridge J')."
        wrongs = [
            "Mark with a guardian star (*) on C or G.",
            "Draw a line straight down through C or G.",
            "Place a breve (˘) above C or G."
        ]
        opts = wrongs + [correct]
        random.shuffle(opts)
        return {
            "question": qtext,
            "options": opts,
            "answer": correct,
            "explanation": f"Bridge Marking Rule: {data['rule']}"
        }
        
    else: # GH IGH and IGHT
        word = random.choice(data["words"])
        qtext = f"What is the correct Elevate proving rule for **'{word}'**?"
        correct = "If igh/ight: gh is silent, cross out g and h, and mark i long (¯). If gh at start: sound /g/. If end gh: small f above gh."
        wrongs = [
            "Mark gh with two guardian stars (**).",
            "Mark gh as an adjacent vowel combination.",
            "Underline gh and mark the vowel short."
        ]
        opts = wrongs + [correct]
        random.shuffle(opts)
        return {
            "question": qtext,
            "options": opts,
            "answer": correct,
            "explanation": f"GH Rules: {data['rule']}"
        }

# ---------------------------------------------------------
# UI APP LAYOUT
# ---------------------------------------------------------

st.sidebar.title("Elevate Phonics Engine")
st.sidebar.markdown("*NoRedInk-Style Practice & Mastery Platform*")

font_choice = st.sidebar.selectbox(
    "🔤 Dyslexia & Accessibility Font",
    ["Lexend (Clean & Dyslexia-Friendly)", "OpenDyslexic (Dyslexia-Focused)", "Atkinson Hyperlegible", "Comic Neue / Child Friendly", "Arial / Standard Sans"]
)
apply_custom_css(font_choice)

user_role = st.sidebar.radio("👤 Switch Platform View", ["🎓 Student Practice Platform", "👩‍🏫 Teacher Dashboard"])

st.sidebar.divider()
st.sidebar.info("💡 **Grounded in Elevate Chapter 3 Curriculum**\nIncludes exact Proving Steps, Guardian Consonants, Breves, Macrons, Bridge S/J, and Suffix Rules.")

# ---------------------------------------------------------
# TEACHER DASHBOARD PLATFORM
# ---------------------------------------------------------
if user_role == "👩‍🏫 Teacher Dashboard":
    st.title("👩‍🏫 Teacher Dashboard & Progress Monitor")
    st.markdown("Manage class periods, assign students, and monitor real-time skill mastery & self-reflection data.")
    
    tab1, tab2, tab3 = st.tabs(["📊 Live Class Analytics", "➕ Create & Assign Class Period", "📋 Class Skill Matrix"])
    
    with tab1:
        st.subheader("Class Progress Overview")
        selected_class = st.selectbox("Select Class Period", list(st.session_state.classes.keys()))
        
        class_students = st.session_state.classes[selected_class]
        
        records = []
        for student in class_students:
            sdata = st.session_state.student_progress[student]
            mastered_cnt = sum(1 for sk, v in sdata["skills"].items() if v["status"] == "Mastered")
            practicing_cnt = sum(1 for sk, v in sdata["skills"].items() if v["status"] == "Practicing")
            total_attempts = sum(v["attempts"] for sk, v in sdata["skills"].items())
            total_correct = sum(v["correct"] for sk, v in sdata["skills"].items())
            accuracy = round((total_correct / total_attempts * 100), 1) if total_attempts > 0 else 0.0
            avg_reflection = round(sum(v["reflection_score"] for sk, v in sdata["skills"].items()) / len(skills_list), 1)
            
            records.append({
                "Student Name": student,
                "Skills Mastered": f"{mastered_cnt} / 12",
                "Practicing": practicing_cnt,
                "Total Questions": total_attempts,
                "Accuracy (%)": f"{accuracy}%",
                "Avg Self-Reflection (1-5)": avg_reflection
            })
            
        df_class = pd.DataFrame(records)
        st.dataframe(df_class, use_container_width=True)
        
        st.divider()
        st.subheader("Student Deep Dive")
        st_select = st.selectbox("Choose Student to Inspect", class_students)
        s_detail = st.session_state.student_progress[st_select]["skills"]
        
        detail_rows = []
        for sk, v in s_detail.items():
            detail_rows.append({
                "Phonics Skill Module": sk,
                "Status": v["status"],
                "Attempts": v["attempts"],
                "Accuracy": f"{round(v['correct']/v['attempts']*100, 1) if v['attempts']>0 else 0}%",
                "Student Self-Reflection": f"⭐ {v['reflection_score']} / 5"
            })
        st.table(pd.DataFrame(detail_rows))

    with tab2:
        st.subheader("➕ Create a New Class Period & Enroll Students")
        col_c1, col_c2 = st.columns(2)
        
        with col_c1:
            new_class_name = st.text_input("New Class Period Name (e.g., Period 4 - Phonics Stars)")
            if st.button("Create Class Period"):
                if new_class_name and new_class_name not in st.session_state.classes:
                    st.session_state.classes[new_class_name] = []
                    st.success(f"Class '{new_class_name}' created successfully!")
                    st.rerun()
                elif new_class_name in st.session_state.classes:
                    st.warning("Class already exists.")
                    
        with col_c2:
            target_class = st.selectbox("Add Student To Class Period", list(st.session_state.classes.keys()))
            new_student_name = st.text_input("Student Full Name")
            if st.button("Assign Student to Class"):
                if new_student_name and new_student_name not in st.session_state.student_progress:
                    st.session_state.classes[target_class].append(new_student_name)
                    st.session_state.student_progress[new_student_name] = {
                        "class": target_class,
                        "skills": {
                            sk: {"attempts": 0, "correct": 0, "status": "Not Started", "reflection_score": 3}
                            for sk in skills_list
                        }
                    }
                    st.success(f"Assigned {new_student_name} to {target_class}!")
                    st.rerun()

    with tab3:
        st.subheader("📋 Class-Wide Skill Mastery Heatmap")
        selected_class_m = st.selectbox("View Skill Matrix for Class", list(st.session_state.classes.keys()), key="matrix_class")
        
        matrix_data = []
        for sk in skills_list:
            row = {"Phonics Skill": sk}
            for stud in st.session_state.classes[selected_class_m]:
                st_sk = st.session_state.student_progress[stud]["skills"][sk]
                row[stud] = st_sk["status"]
            matrix_data.append(row)
            
        st.dataframe(pd.DataFrame(matrix_data), use_container_width=True)

# ---------------------------------------------------------
# STUDENT PRACTICE PLATFORM
# ---------------------------------------------------------
else:
    st.title("🎓 Student Phonics Mastery Platform")
    st.markdown("Practice your Elevate Phonics skills, prove words, and build your mastery streak!")
    
    col_s1, col_s2 = st.columns(2)
    with col_s1:
        current_class = st.selectbox("Select Your Class Period", list(st.session_state.classes.keys()))
    with col_s2:
        current_student = st.selectbox("Select Your Name", st.session_state.classes[current_class])
        
    st.divider()
    
    selected_skill = st.selectbox("🎯 Choose Phonics Skill Module to Practice", skills_list)
    skill_info = CURRICULUM[selected_skill]
    
    with st.expander(f"📘 Rule & Proving Guide: {selected_skill}", expanded=True):
        st.markdown(f"**Core Rule:** {skill_info['rule']}")
        st.markdown(f"**Elevate Proving Steps:** {skill_info['marking']}")
        
    st.divider()
    
    st.subheader("💭 Formative Self-Reflection Check-In")
    student_skill_data = st.session_state.student_progress[current_student]["skills"][selected_skill]
    
    col_r1, col_r2 = st.columns([2, 3])
    with col_r1:
        current_ref = st.slider(
            "How confident do you feel applying this rule right now?",
            min_value=1, max_value=5,
            value=int(student_skill_data.get("reflection_score", 3)),
            format="%d ⭐"
        )
        if st.button("Save Self-Reflection"):
            st.session_state.student_progress[current_student]["skills"][selected_skill]["reflection_score"] = current_ref
            st.toast("Self-reflection saved! Great metacognitive check-in. 🌟")
            
    with col_r2:
        st.write("**Metacognitive Reflection Prompt:**")
        ref_notes = st.text_area(
            "What step or marking (e.g., guardian stars, breves, macrons, bridge S/J) do you need to pay closest attention to?",
            placeholder="E.g., I need to remember that blends get 2 guardian stars while digraphs count as 1 star..."
        )
        
    st.divider()
    
    st.subheader(f"✏️ Practice Bank: {selected_skill}")
    
    q_key = f"current_q_{selected_skill}"
    if q_key not in st.session_state:
        st.session_state[q_key] = generate_question(selected_skill)
        
    qdata = st.session_state[q_key]
    
    st.markdown(f"### {qdata['question']}")
    
    user_choice = st.radio("Choose your answer:", qdata["options"], key=f"radio_{selected_skill}")
    
    if st.button("Check Answer"):
        st.session_state.student_progress[current_student]["skills"][selected_skill]["attempts"] += 1
        
        if user_choice == qdata["answer"]:
            st.balloons()
            st.success("🎉 **Correct! Spot on!**")
            st.markdown(f"<div class='proving-box'><b>Elevate Rule Explanation:</b><br>{qdata['explanation']}</div>", unsafe_allow_html=True)
            st.session_state.student_progress[current_student]["skills"][selected_skill]["correct"] += 1
            
            cor = st.session_state.student_progress[current_student]["skills"][selected_skill]["correct"]
            if cor >= 5:
                st.session_state.student_progress[current_student]["skills"][selected_skill]["status"] = "Mastered"
            else:
                st.session_state.student_progress[current_student]["skills"][selected_skill]["status"] = "Practicing"
                
        else:
            st.error("❌ **Not quite. Let me explain the rule for you!**")
            st.markdown(f"<div class='proving-box'><b>Elevate Proving & Rule Explanation:</b><br>{qdata['explanation']}<br><br><b>Correct Answer:</b> {qdata['answer']}</div>", unsafe_allow_html=True)
            st.session_state.student_progress[current_student]["skills"][selected_skill]["status"] = "Practicing"
            
    if st.button("Next Question ➡️"):
        st.session_state[q_key] = generate_question(selected_skill)
        st.rerun()
