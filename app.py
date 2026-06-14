import streamlit as st
import ollama
st.set_page_config(
    page_title="Solo Levelling Study Agent",
    page_icon="⚔️",
    layout="wide"
)
MODEL = "phi3:mini"

def ask_ai(prompt):
    try:
        response = ollama.chat(
            model=MODEL,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return response["message"]["content"]

    except Exception as e:
        return f"Error: {e}"
# Load CSS
try:
    with open("style.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
except:
    pass

def get_rank(xp):

    if xp >= 500:
        return "👑 Shadow Monarch"
    elif xp >= 400:
        return "🟣 S-Class Hunter"
    elif xp >= 300:
        return "🔴 A-Class Hunter"
    elif xp >= 200:
        return "🟠 B-Class Hunter"
    elif xp >= 100:
        return "🟡 C-Class Hunter"
    elif xp >= 50:
        return "🟢 D-Class Hunter"

    return "⚪ E-Class Hunter"


# XP System
if "xp" not in st.session_state:
    st.session_state.xp = 0

st.session_state.rank = get_rank(
    st.session_state.xp
)
# Sidebar
st.sidebar.markdown("## HUNTER PROFILE")

st.sidebar.markdown(
    f"""
**XP**

{st.session_state.xp}

**RANK**

{st.session_state.rank}
""")

st.sidebar.markdown("---")

st.sidebar.markdown("---")
if "page" not in st.session_state:
    st.session_state.page = "Monarch Gate"

if st.sidebar.button("Monarch Gate"):
    st.session_state.page = "Monarch Gate"

if st.sidebar.button("Hunter System"):
    st.session_state.page = "Hunter System"

if st.sidebar.button("Shadow Archive"):
    st.session_state.page = "Shadow Archive"

if st.sidebar.button("Quiz Dungeon"):
    st.session_state.page = "Quiz Dungeon"

if st.sidebar.button("Hunter Training"):
    st.session_state.page = "Hunter Training"

menu = st.session_state.page
# Dashboard
if menu == "Monarch Gate":
    st.markdown(
    """
    <div style='text-align:center'>
        <h1>SOLO LEVELLING</h1>
        <p>AI Hunter Training System</p>
    </div>
    """,
    unsafe_allow_html=True
)

    st.subheader("ARISE, HUNTER.")

    st.write(
        """
        Transform your study sessions into quests.
        Defeat Quiz Dungeons.
        Build your Shadow Archive.
        Rank up your knowledge.
        """
    )

    progress = min(st.session_state.xp, 100)

    st.progress(progress)

# Study Chat
elif menu == "Hunter System":

    st.title("Hunter System")

    question = st.text_area(
        "Ask your study question"
    )

    if st.button("Summon Knowledge"):

        st.session_state.xp += 10

        st.success(
            f"Question received.\n\nXP +10"
        )

        answer = ask_ai(question)

        st.write(answer)
# Notes Extraction
elif menu == "Shadow Archive":

    st.title("Shadow Archive")

    notes = st.text_area(
        "Paste your notes here"
    )

    if st.button("Extract Knowledge"):

        st.session_state.xp += 15

        st.success(
            "Knowledge Extracted.\n\nXP +15"
        )

        prompt = f"""
        Summarize these study notes.

        Provide:
        1. Summary
        2. Key Concepts
        3. Important Formulas
        4. Revision Tips

        Notes:
        {notes}
        """

        summary = ask_ai(prompt)

        st.write(summary)

# Quiz
elif menu == "Quiz Dungeon":

    st.title("Quiz Dungeon")

    topic = st.text_input(
        "Enter a topic"
    )

    if st.button("Enter Dungeon"):

        st.session_state.xp += 20

        st.success(
            "Dungeon Cleared.\n\nXP +20"
        )

        prompt = f"""
        Create a study quiz on {topic}.

        Generate:
        - 5 Multiple Choice Questions
        - 4 options each
        - Provide answers at the end

        Format clearly.
        """

        quiz = ask_ai(prompt)

        st.write(quiz)

# Planner
elif menu == "Hunter Training":

    st.title("Hunter Training")

    goal = st.text_input(
        "What are you studying?"
    )

    if st.button("Create Training Plan"):

        st.session_state.xp += 25

        st.success(
            "Training Plan Created.\n\nXP +25"
        )

        prompt = f"""
        Create a 7-day study plan for:

        {goal}

        Include:
        - Daily goals
        - Revision sessions
        - Practice questions
        - Time estimates

        Format it clearly day by day.
        """

        plan = ask_ai(prompt)

        st.write(plan)