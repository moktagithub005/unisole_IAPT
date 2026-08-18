import streamlit as st

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
        ("Modules", "3"),
        ("Live Labs", "3"),
        ("Pedagogy", "Experiment First"),
        ("Bridge", "Prompting on Day 2"),
    ]
)

with st.sidebar:
    st.markdown("### Session Controls")
    model_name = st.text_input("Groq model", value=get_default_model())
    temperature = st.slider("Creativity", min_value=0.0, max_value=1.0, value=0.3, step=0.1)
    if get_groq_api_key():
        st.success("Groq key detected")
    else:
        st.error("Groq key not found in .env")

st.subheader("Day 1 Design Goals")
left, right = st.columns([1.1, 0.9], gap="large")
with left:
    st.write(
        "This day is designed for a national-level audience that wants depth without losing clarity. "
        "The experience moves from curiosity, to evidence, to experimentation, to reflective caution."
    )
    st.markdown("**Participants should leave with:**")
    for objective in DAY_ONE_OBJECTIVES:
        st.write(f"- {objective}")
with right:
    render_section_card(
        "Emotional outcome",
        "Participants should feel two things at the same time: AI is powerful enough to matter, "
        "and imperfect enough that good prompting and verification become essential.",
    )
    render_section_card(
        "Why they come back on Day 2",
        "By the end of Day 1, the audience should naturally ask: if prompting changes outcomes so much, "
        "how do we do it well and responsibly?",
    )

st.subheader("Session Flow")
for module in DAY_ONE_MODULES:
    with st.expander(f"{module['title']} • {module['duration']}", expanded=True):
        st.write(module["focus"])
        for item in module["outcomes"]:
            st.write(f"- {item}")

st.subheader("Facilitator Script Spine")
script_col1, script_col2 = st.columns(2, gap="large")
with script_col1:
    render_section_card(
        "Opening hook",
        "Ask one question: Can ChatGPT solve physics? Let the room split. Then reveal that both believers "
        "and skeptics are partly right.",
    )
    render_section_card(
        "Mystery frame",
        "Show the paradox: research-level help on one problem, surprising failure on another. This keeps the audience leaning in.",
    )
with script_col2:
    render_section_card(
        "Research connection",
        "Use evidence and case studies to show that the model is not random. It has recognizable strengths and weaknesses.",
    )
    render_section_card(
        "Bridge to Day 2",
        "End with a practical question rather than a conclusion: if interaction quality matters, how should we prompt better?",
    )

st.subheader("Live Experiment Studio")
st.write(
    "Use these live activities during the session. They are designed to move the workshop from lecture mode "
    "into evidence-based experimentation."
)

tab1, tab2, tab3 = st.tabs(["Concept Builder", "Trust but Verify", "Day 2 Teaser"])

with tab1:
    topic = st.text_input(
        "Physics or mathematics topic",
        value="Why ChatGPT can solve some calculus steps but fail at logical reasoning",
        key="concept_topic",
    )
    if st.button("Generate teaching explanation", key="concept_button", use_container_width=True):
        prompt = f"""
        Mode: {EXPERIMENT_MODES["Concept Builder"]}

        Topic: {topic}

        Output format:
        1. A short workshop explanation in easy English
        2. One classroom analogy
        3. One common misconception
        4. One question to ask the audience
        """
        with st.spinner("Building an explanation from Groq..."):
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
    question = st.text_area(
        "Enter a question to test the model",
        value="A student says: 'If ChatGPT scores high on AP Physics, does that mean it really understands physics?' Explain carefully.",
        height=140,
        key="verify_question",
    )
    if st.button("Run answer + verification checklist", key="verify_button", use_container_width=True):
        prompt = f"""
        Mode: {EXPERIMENT_MODES["Trust but Verify"]}

        Question:
        {question}

        Output format:
        1. Best possible answer
        2. Where the answer may still be weak
        3. What a human expert should verify
        4. A confidence label: High, Medium, or Low
        """
        with st.spinner("Testing the model with a verification-first workflow..."):
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
    weak_prompt = st.text_area(
        "Weak prompt",
        value="Explain prompt engineering.",
        height=100,
        key="weak_prompt",
    )
    better_prompt = st.text_area(
        "Structured prompt",
        value=(
            "You are teaching physics professors in a national workshop. Explain prompt engineering in easy English. "
            "Use one physics example, one bad prompt, one improved prompt, and a short reason why the second works better."
        ),
        height=120,
        key="better_prompt",
    )
    if st.button("Compare prompt quality", key="teaser_button", use_container_width=True):
        prompt = f"""
        Mode: {EXPERIMENT_MODES["Day 2 Teaser"]}

        Weak prompt:
        {weak_prompt}

        Better prompt:
        {better_prompt}

        Output format:
        1. What answer quality the weak prompt is likely to produce
        2. What answer quality the structured prompt is likely to produce
        3. Why this makes Day 2 necessary
        """
        with st.spinner("Comparing prompt structures..."):
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

st.subheader("Audience Reflection")
for index, item in enumerate(REFLECTION_QUESTIONS, start=1):
    st.write(f"{index}. {item}")

st.info(
    "Facilitator close: 'Tomorrow we learn how to guide the model so it becomes more useful, more reliable, "
    "and easier to evaluate in teaching and research contexts.'"
)
