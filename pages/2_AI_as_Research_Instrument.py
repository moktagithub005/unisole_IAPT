import sys
from pathlib import Path

import streamlit as st


ROOT_DIR = Path(__file__).resolve().parents[1]
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

from utils.constants import (
    DAY_TWO_MODULES,
    DAY_TWO_OBJECTIVES,
    DAY_TWO_TAGLINE,
    DAY_TWO_TITLE,
    DEFAULT_SYSTEM_PROMPT,
    RESEARCH_EXPERIMENT_MODES,
    RESEARCH_PROMPT_PATTERNS,
)
from utils.groq_client import get_default_model, get_groq_api_key, groq_chat_completion
from utils.ui_helpers import render_hero, render_metric_strip, render_section_card, render_sidebar_note


st.set_page_config(page_title=DAY_TWO_TITLE, page_icon="🔬", layout="wide")
render_sidebar_note()
render_hero(DAY_TWO_TITLE, DAY_TWO_TAGLINE)

render_metric_strip(
    [
        ("Session Role", "Research Companion"),
        ("Best Use", "Live + After Workshop"),
        ("Day 2 Format", "Overview + Subpages"),
        ("Takeaway", "Reusable Research Workflows"),
    ]
)

with st.sidebar:
    st.markdown("### Participant Controls")
    model_name = st.text_input("Groq model", value=get_default_model())
    temperature = st.slider("Creativity", min_value=0.0, max_value=1.0, value=0.2, step=0.1)
    if get_groq_api_key():
        st.success("Groq key detected")
    else:
        st.error("Groq key not found in .env")
    st.markdown("### How to use Day 2")
    st.write("1. Start with this main Day 2 page.")
    st.write("2. Build the research mindset together.")
    st.write("3. Open the Day 2 subpages from the sidebar.")
    st.write("4. Use the subpages for deeper practice.")

st.subheader("Why Day 2 Is the Turning Point")
col1, col2 = st.columns([1.05, 0.95], gap="large")
with col1:
    st.write(
        "Day 2 is the most important shift in the workshop. Participants move beyond using AI as a chatbot and begin "
        "treating it as a scientific instrument for literature review, mathematical reasoning, and research workflow design."
    )
    st.markdown("**By the end of Day 2, participants should be able to:**")
    for objective in DAY_TWO_OBJECTIVES:
        st.write(f"- {objective}")
with col2:
    render_section_card(
        "Core message",
        "AI is not replacing the scientist. It is becoming the next scientific instrument.",
    )
    render_section_card(
        "Day 2 philosophy",
        "Science is not about producing answers quickly. It is about producing trustworthy answers.",
    )

st.subheader("Day 2 Structure")
for module in DAY_TWO_MODULES:
    with st.container(border=True):
        left, right = st.columns([3, 1])
        left.markdown(f"#### {module['title']}")
        left.write(module["focus"])
        right.metric("Duration", module["duration"])
        st.markdown("**What participants should gain**")
        for item in module["outcomes"]:
            st.write(f"- {item}")

st.subheader("Start the Session Here")
tab1, tab2, tab3 = st.tabs(
    ["Instrument Mindset", "Literature Discovery Starter", "Day 2 Reuse Prompts"]
)

with tab1:
    st.markdown("### Use This During Your Opening Day 2 Discussion")
    research_task = st.text_input(
        "Research task or challenge",
        value="I want to reduce the time spent searching, comparing, and interpreting scientific material.",
    )
    if st.button("Generate Day 2 opening explanation", key="day2_opening", use_container_width=True):
        prompt = f"""
        Mode: {RESEARCH_EXPERIMENT_MODES["Instrument Mindset"]}

        Research challenge:
        {research_task}

        Output format:
        1. A short explanation for workshop participants
        2. Why this is different from normal chatbot use
        3. One physics-research example
        4. One caution about overtrusting the model
        """
        with st.spinner("Building the Day 2 opening explanation..."):
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
    st.markdown("### Start Literature Discovery from the Main Day 2 Page")
    topic = st.text_area(
        "Research topic or theme",
        value="Quantum error correction, physics-informed neural networks, or any emerging topic you want to explore.",
        height=100,
    )
    if st.button("Build a Day 2 reading starter", key="day2_reading_starter", use_container_width=True):
        prompt = f"""
        Mode: {RESEARCH_EXPERIMENT_MODES["Literature Mapper"]}

        Topic:
        {topic}

        Output format:
        1. What kind of seed paper to find first
        2. Which paper categories matter next
        3. The first questions the participant should ask
        4. Which Day 2 subpage they should open next and why
        """
        with st.spinner("Designing a Day 2 reading starter..."):
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
    st.markdown("### Prompts Participants Can Reuse After the Workshop")
    for pattern in RESEARCH_PROMPT_PATTERNS:
        render_section_card(pattern["title"], pattern["body"])

st.subheader("Day 2 Subpages")
subpage_col1, subpage_col2 = st.columns(2, gap="large")
with subpage_col1:
    render_section_card(
        "Day 2.1: Math and Derivation Assistant",
        "Use this when participants want to unpack a derivation, surface assumptions, repair a weak step, or build a verification checklist.",
    )
with subpage_col2:
    render_section_card(
        "Day 2.2: Simulation and Data Analysis",
        "Use this when participants want to turn a physics idea into a workflow, choose plots, interpret outputs, or extend the work after the session.",
    )

st.info(
    "This is the Day 2 base page. All teaching content for Day 2 lives here and in the Day 2 subpages. Day 3 and Day 4 remain intentionally reserved and contain no Day 2 material."
)
