import sys
from pathlib import Path

import streamlit as st


ROOT_DIR = Path(__file__).resolve().parents[1]
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

from utils.constants import (
    DAY_ONE_MODULES,
    DAY_ONE_OBJECTIVES,
    DAY_ONE_TAGLINE,
    DAY_ONE_TITLE,
    DEFAULT_SYSTEM_PROMPT,
    EXPERIMENT_MODES,
    REFLECTION_QUESTIONS,
)
from utils.groq_client import get_default_model, get_groq_api_key, groq_chat_completion
from utils.ui_helpers import render_hero, render_metric_strip, render_section_card, render_sidebar_note


st.set_page_config(page_title=DAY_ONE_TITLE, page_icon="🔬", layout="wide")
render_sidebar_note()
render_hero(DAY_ONE_TITLE, DAY_ONE_TAGLINE)

render_metric_strip(
    [
        ("Session Role", "Participant Companion"),
        ("Use Mode", "Alongside Lecture"),
        ("Practice Style", "Prompt + Verify"),
        ("Takeaway", "Reusable Prompt Habits"),
    ]
)

with st.sidebar:
    st.markdown("### Participant Controls")
    model_name = st.text_input("Groq model", value=get_default_model())
    temperature = st.slider("Creativity", min_value=0.0, max_value=1.0, value=0.3, step=0.1)
    if get_groq_api_key():
        st.success("Groq key detected")
    else:
        st.error("Groq key not found in .env")
    st.markdown("### How to use this page")
    st.write("1. Listen to the speaker.")
    st.write("2. Type the same question here.")
    st.write("3. Improve the prompt with the group.")
    st.write("4. Verify before trusting.")

st.subheader("How Participants Should Use This Page")
col1, col2 = st.columns([1.05, 0.95], gap="large")
with col1:
    st.write(
        "This page is not your lecture notes. It is your live working space during the session. "
        "As the speaker introduces examples, participants can enter the same problems here, compare answers, "
        "improve the wording, and notice how the output changes."
    )
    st.markdown("**Use it during the lecture to:**")
    for objective in DAY_ONE_OBJECTIVES:
        st.write(f"- {objective}")
with col2:
    render_section_card(
        "What the speaker does",
        "The speaker explains the ideas, gives the examples, and tells the room what to test together.",
    )
    render_section_card(
        "What participants do",
        "Participants use this page to frame questions, try prompts live, compare outputs, and build their own reusable style.",
    )

st.subheader("Today's Flow")
for module in DAY_ONE_MODULES:
    with st.expander(f"{module['title']} • {module['duration']}", expanded=True):
        st.write(module["focus"])
        for item in module["outcomes"]:
            st.write(f"- {item}")

st.subheader("Live Companion Workspace")
st.write(
    "When the speaker gives a concept, problem, or claim, use one of the spaces below. "
    "The goal is not to get a fast answer. The goal is to learn how to ask better and safer questions."
)

tab1, tab2, tab3, tab4 = st.tabs(
    ["Follow the Lecture", "Frame the Problem", "Improve the Prompt", "Verify the Answer"]
)

with tab1:
    st.markdown("### Use This With the Speaker")
    st.write(
        "If the speaker says, 'Try this question with me,' participants can paste the exact topic below and "
        "generate a clear workshop-friendly explanation."
    )
    lecture_topic = st.text_input(
        "Lecture concept or claim",
        value="Why can an AI system help with a hard derivation but still fail on a simple reasoning question?",
        key="lecture_topic",
    )
    if st.button("Generate a lecture companion explanation", key="lecture_button", use_container_width=True):
        prompt = f"""
        Mode: {EXPERIMENT_MODES["Concept Builder"]}

        Topic: {lecture_topic}

        Output format:
        1. A simple explanation for workshop participants
        2. One physics-friendly analogy
        3. One sentence on where the model may fail
        4. One follow-up question the participant should ask next
        """
        with st.spinner("Generating a lecture companion explanation..."):
            try:
                response = groq_chat_completion(
                    user_prompt=prompt,
                    system_prompt=DEFAULT_SYSTEM_PROMPT,
                    model=model_name,
                    temperature=temperature,
                )
                st.markdown(response)
            except Exception as exc:
                st.error(str(exc))

with tab2:
    st.markdown("### Turn a Vague Problem into a Better One")
    st.write(
        "Participants often ask the model badly the first time. Use this section to shape the problem before asking for an answer."
    )
    raw_problem = st.text_area(
        "My rough physics or mathematics question",
        value="Explain electric field between two charged plates.",
        height=100,
        key="raw_problem",
    )
    audience_type = st.selectbox(
        "Who is this for?",
        ["BSc students", "MSc students", "school students", "research scholars", "myself as a teacher"],
        index=0,
    )
    desired_output = st.selectbox(
        "What do you want from the model?",
        ["clear explanation", "step-by-step derivation", "analogy", "classroom activity", "summary with caution points"],
        index=0,
    )
    if st.button("Frame this into a better prompt", key="frame_button", use_container_width=True):
        prompt = f"""
        The participant's rough problem is:
        {raw_problem}

        Audience:
        {audience_type}

        Desired output:
        {desired_output}

        Rewrite this into:
        1. A weak prompt
        2. A stronger workshop-ready prompt
        3. A short note explaining why the stronger version is better
        """
        with st.spinner("Framing the problem more clearly..."):
            try:
                response = groq_chat_completion(
                    user_prompt=prompt,
                    system_prompt=DEFAULT_SYSTEM_PROMPT,
                    model=model_name,
                    temperature=temperature,
                )
                st.markdown(response)
            except Exception as exc:
                st.error(str(exc))

with tab3:
    st.markdown("### Improve the Prompt Live")
    st.write(
        "This is the section to use when the speaker says, 'Now let's improve the same prompt together.' "
        "Participants can compare a first draft against a better-framed version."
    )
    weak_prompt = st.text_area(
        "First attempt",
        value="Explain prompt engineering in physics.",
        height=100,
        key="weak_prompt_v2",
    )
    improved_prompt = st.text_area(
        "Improved attempt",
        value=(
            "You are helping a physics educator in a national workshop. Explain prompt engineering in easy English. "
            "Use one example from mechanics or electromagnetism, show one weak prompt and one improved prompt, "
            "and explain why the improved version is safer and more useful."
        ),
        height=140,
        key="improved_prompt_v2",
    )
    if st.button("Compare both prompts", key="compare_button", use_container_width=True):
        prompt = f"""
        Mode: {EXPERIMENT_MODES["Day 2 Teaser"]}

        Weak prompt:
        {weak_prompt}

        Improved prompt:
        {improved_prompt}

        Output format:
        1. What the weak prompt is likely to miss
        2. What the improved prompt adds
        3. A short participant takeaway
        4. One suggestion for making the prompt even better
        """
        with st.spinner("Comparing prompt quality..."):
            try:
                response = groq_chat_completion(
                    user_prompt=prompt,
                    system_prompt=DEFAULT_SYSTEM_PROMPT,
                    model=model_name,
                    temperature=temperature,
                )
                st.markdown(response)
            except Exception as exc:
                st.error(str(exc))

with tab4:
    st.markdown("### Trust but Verify")
    st.write(
        "This is where participants practice the most important habit of Day 1: never stop at the answer. "
        "Ask what should still be checked."
    )
    verification_question = st.text_area(
        "Question or answer to verify",
        value="If an AI gives a correct-looking derivation in electromagnetism, what should I still check before using it in class?",
        height=120,
        key="verification_question_v2",
    )
    if st.button("Generate verification checklist", key="verification_button_v2", use_container_width=True):
        prompt = f"""
        Mode: {EXPERIMENT_MODES["Trust but Verify"]}

        Question:
        {verification_question}

        Output format:
        1. Short answer
        2. What may still be unreliable
        3. A verification checklist for the participant
        4. A confidence label: High, Medium, or Low
        """
        with st.spinner("Building a verification checklist..."):
            try:
                response = groq_chat_completion(
                    user_prompt=prompt,
                    system_prompt=DEFAULT_SYSTEM_PROMPT,
                    model=model_name,
                    temperature=temperature,
                )
                st.markdown(response)
            except Exception as exc:
                st.error(str(exc))

st.subheader("Participant Prompt Patterns to Reuse Later")
reuse_col1, reuse_col2 = st.columns(2, gap="large")
with reuse_col1:
    render_section_card(
        "Pattern 1: Explain clearly",
        "You are helping me teach [topic] to [audience]. Explain it in simple but accurate language, "
        "use one analogy, and mention one common misconception.",
    )
    render_section_card(
        "Pattern 2: Derive carefully",
        "Solve or derive this step by step. State assumptions, define symbols, and mention where a human should verify the result.",
    )
with reuse_col2:
    render_section_card(
        "Pattern 3: Compare prompts",
        "Take my rough question and improve it for clarity, audience, scope, and safety. Then explain why the new version is better.",
    )
    render_section_card(
        "Pattern 4: Verify before use",
        "Answer the question, but then list possible weak points, likely mistakes, and what I must check manually or from a trusted source.",
    )

st.subheader("End-of-Session Reflection")
for index, item in enumerate(REFLECTION_QUESTIONS, start=1):
    st.write(f"{index}. {item}")

st.success(
    "Day 1 outcome: participants should leave with at least one better prompt, one safer verification habit, "
    "and a clear reason to return for Day 2."
)
