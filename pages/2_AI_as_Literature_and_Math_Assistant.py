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


st.set_page_config(page_title="Day 2: Literature Discovery", page_icon="📚", layout="wide")
render_sidebar_note()
render_hero(DAY_TWO_TITLE, DAY_TWO_TAGLINE)

render_metric_strip(
    [
        ("Session Role", "Research Companion"),
        ("Best Use", "Live + After Workshop"),
        ("Core Habit", "Select Before You Read"),
        ("Takeaway", "Reusable Literature Workflow"),
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
    st.markdown("### How to use this page")
    st.write("1. Start from the research question.")
    st.write("2. Identify a seed paper strategy.")
    st.write("3. Build a reading sequence.")
    st.write("4. Verify paper quality yourself.")

st.subheader("Why This Page Matters")
col1, col2 = st.columns([1.1, 0.9], gap="large")
with col1:
    st.write(
        "This Day 2 page helps participants move from random searching to intentional literature discovery. "
        "It is designed to work during your live teaching and later when participants start a real topic for "
        "their own classroom practice, PhD work, or research planning."
    )
    st.markdown("**Participants should leave able to:**")
    for objective in DAY_TWO_OBJECTIVES:
        st.write(f"- {objective}")
with col2:
    render_section_card(
        "Core message",
        "Researchers do not search for papers. Researchers search for understanding, sequence, and evidence.",
    )
    render_section_card(
        "Most useful Day 2 shift",
        "AI should help reduce time spent searching and sorting, not time spent thinking and verifying.",
    )

with st.expander("Day 2 module flow", expanded=False):
    for module in DAY_TWO_MODULES:
        st.write(f"**{module['title']}** ({module['duration']})")
        st.write(module["focus"])

st.subheader("Live Literature Workspace")
tab1, tab2, tab3, tab4 = st.tabs(
    ["Instrument Mindset", "Seed Paper Builder", "Reading Sequence", "Research Gap Scanner"]
)

with tab1:
    st.markdown("### Use This When You Introduce AI as a Research Instrument")
    research_task = st.text_input(
        "Research task or challenge",
        value="I want to understand a new topic without drowning in too many papers.",
    )
    if st.button("Generate Day 2 framing", key="instrument_framing", use_container_width=True):
        prompt = f"""
        Mode: {RESEARCH_EXPERIMENT_MODES["Instrument Mindset"]}

        Research challenge:
        {research_task}

        Output format:
        1. A short explanation for workshop participants
        2. Why this is different from normal chatbot use
        3. One research example from physics
        4. One caution about overtrusting the model
        """
        with st.spinner("Building a research-instrument explanation..."):
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
    st.markdown("### Build a Strong Starting Point")
    topic = st.text_area(
        "Research topic or theme",
        value="Physics-informed neural networks for solving differential equations in fluid dynamics",
        height=90,
    )
    stage = st.selectbox(
        "Current stage",
        ["I am totally new to this topic", "I know the basics", "I already read a few papers"],
        index=0,
    )
    goal = st.selectbox(
        "What do you need most?",
        ["Find a seed paper", "Find a review paper", "Map the field", "Prepare a reading list"],
        index=0,
    )
    if st.button("Build my seed paper strategy", key="seed_paper", use_container_width=True):
        prompt = f"""
        Mode: {RESEARCH_EXPERIMENT_MODES["Literature Mapper"]}

        Topic:
        {topic}

        Participant stage:
        {stage}

        Immediate goal:
        {goal}

        Output format:
        1. What kind of seed paper to search for first
        2. Which paper categories matter next: foundational, method, application, review, frontier
        3. A reading order for the first 5-8 papers
        4. A shortlist of questions to ask while reading
        """
        with st.spinner("Designing a seed paper strategy..."):
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
    st.markdown("### Turn a Topic into a Reading Sequence")
    seed_paper = st.text_input(
        "Seed paper, review, or starting point",
        value="A recent review paper on quantum error correction",
    )
    reading_goal = st.selectbox(
        "What should the reading path optimize for?",
        ["Fast orientation", "Thesis preparation", "Classroom understanding", "Finding a research gap"],
        index=0,
        key="reading_goal",
    )
    if st.button("Plan my reading sequence", key="reading_sequence", use_container_width=True):
        prompt = f"""
        Mode: {RESEARCH_EXPERIMENT_MODES["Literature Mapper"]}

        Seed paper:
        {seed_paper}

        Reading goal:
        {reading_goal}

        Output format:
        1. What to extract from the seed paper first
        2. What kinds of cited papers to follow backward
        3. What kinds of newer papers to follow forward
        4. How to decide reading priority
        5. A simple note-taking template for the participant
        """
        with st.spinner("Planning a literature pathway..."):
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
    st.markdown("### Ask Better Research Questions")
    paper_notes = st.text_area(
        "Notes from 2-3 papers, or what you think the field is saying",
        value=(
            "Most papers show strong results on benchmark problems, but many assume clean boundary conditions "
            "and only limited real-world noise."
        ),
        height=130,
    )
    if st.button("Scan for possible research gaps", key="gap_scan", use_container_width=True):
        prompt = f"""
        Mode: {RESEARCH_EXPERIMENT_MODES["Literature Mapper"]}

        Current field notes:
        {paper_notes}

        Output format:
        1. Recurring assumptions or patterns
        2. Possible disagreements or limitations
        3. 3 plausible research-gap directions
        4. What evidence a human researcher should verify before trusting those gap ideas
        """
        with st.spinner("Looking for research-gap directions..."):
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

st.subheader("Reusable Prompt Patterns")
for pattern in RESEARCH_PROMPT_PATTERNS:
    render_section_card(pattern["title"], pattern["body"])

st.subheader("Participant Reflection")
st.write("Before moving on, ask yourself:")
st.write("- Did I define my research question clearly enough?")
st.write("- Do I know what kind of paper I need first, rather than just wanting more papers?")
st.write("- What will I verify manually before trusting an AI-made reading plan?")
