import sys
from pathlib import Path

import streamlit as st


ROOT_DIR = Path(__file__).resolve().parents[1]
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

from utils.constants import DAY_TWO_TAGLINE, DEFAULT_SYSTEM_PROMPT, RESEARCH_EXPERIMENT_MODES
from utils.groq_client import get_default_model, get_groq_api_key, groq_chat_completion
from utils.ui_helpers import render_hero, render_metric_strip, render_section_card, render_sidebar_note


st.set_page_config(page_title="Day 2: Simulation and Data Analysis", page_icon="📈", layout="wide")
render_sidebar_note()
render_hero("Day 2: AI for Simulation and Data Analysis", DAY_TWO_TAGLINE)

render_metric_strip(
    [
        ("Session Role", "Workflow Builder"),
        ("Best Use", "Planning + Interpretation"),
        ("Core Habit", "Model, Plot, Check"),
        ("Takeaway", "Research-Ready Workflows"),
    ]
)

with st.sidebar:
    st.markdown("### Participant Controls")
    model_name = st.text_input("Groq model", value=get_default_model(), key="sim_model")
    temperature = st.slider("Creativity", min_value=0.0, max_value=1.0, value=0.2, step=0.1, key="sim_temp")
    if get_groq_api_key():
        st.success("Groq key detected")
    else:
        st.error("Groq key not found in .env")
    st.markdown("### Use this page to")
    st.write("1. Define the scientific problem.")
    st.write("2. Convert it into a computational workflow.")
    st.write("3. Decide what to plot and test.")
    st.write("4. Identify interpretation risks.")

st.subheader("Why This Matters After the Workshop")
col1, col2 = st.columns([1.05, 0.95], gap="large")
with col1:
    st.write(
        "Participants often leave an AI workshop inspired but unsure how to apply it to real scientific work. "
        "This page closes that gap by helping them turn a physics question into a practical simulation or "
        "data-analysis workflow they can adapt later in their teaching or research."
    )
with col2:
    render_section_card(
        "Right expectation",
        "AI can help design a workflow, suggest plots, and highlight useful checks.",
    )
    render_section_card(
        "Important limit",
        "AI cannot replace domain judgment about assumptions, numerical stability, or physical interpretation.",
    )

st.subheader("Simulation and Analysis Workspace")
tab1, tab2, tab3, tab4 = st.tabs(
    ["Plan the Workflow", "Variables and Plots", "Interpret the Output", "Research Extension Ideas"]
)

with tab1:
    problem = st.text_area(
        "Physics problem or dataset task",
        value="Simulate the damped harmonic oscillator and study how damping changes the motion over time.",
        height=110,
    )
    experience = st.selectbox(
        "Participant experience level",
        ["Beginner", "Comfortable with coding", "Research-level user"],
        index=0,
    )
    if st.button("Build the workflow", key="workflow_builder", use_container_width=True):
        prompt = f"""
        Mode: {RESEARCH_EXPERIMENT_MODES["Simulation Planner"]}

        Problem:
        {problem}

        Experience level:
        {experience}

        Output format:
        1. Goal of the simulation or analysis
        2. Inputs and parameters
        3. Step-by-step workflow
        4. Outputs or plots to generate
        5. What the participant should verify manually
        """
        with st.spinner("Designing the workflow..."):
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
    method_notes = st.text_area(
        "Describe the model, code idea, or dataset",
        value="I have time-series displacement data and want to compare underdamped, overdamped, and critically damped behavior.",
        height=110,
    )
    if st.button("Suggest variables and plots", key="plot_suggester", use_container_width=True):
        prompt = f"""
        Mode: {RESEARCH_EXPERIMENT_MODES["Simulation Planner"]}

        Method notes:
        {method_notes}

        Output format:
        1. Key variables or observables
        2. Best plots or visual comparisons
        3. What each plot may reveal physically
        4. Which plot could be misleading and why
        """
        with st.spinner("Planning variables and plots..."):
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
    output_summary = st.text_area(
        "Observed result or output summary",
        value=(
            "As damping increases, the oscillations decay more quickly, and the overdamped case shows no oscillation "
            "but a slow return to equilibrium."
        ),
        height=120,
    )
    if st.button("Interpret this output", key="interpret_output", use_container_width=True):
        prompt = f"""
        Mode: {RESEARCH_EXPERIMENT_MODES["Simulation Planner"]}

        Output summary:
        {output_summary}

        Output format:
        1. Physical interpretation
        2. What result seems expected
        3. What anomaly or artifact may still need checking
        4. One next experiment or analysis to run
        """
        with st.spinner("Interpreting the output..."):
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
    extension_prompt = st.text_area(
        "Current project, simulation, or class activity",
        value="A classroom or research mini-project on diffusion, random walk, or oscillator dynamics.",
        height=100,
    )
    if st.button("Suggest extension ideas", key="extension_ideas", use_container_width=True):
        prompt = f"""
        Mode: {RESEARCH_EXPERIMENT_MODES["Simulation Planner"]}

        Current project:
        {extension_prompt}

        Output format:
        1. 3 extension ideas
        2. Which one is easiest for participants to try after the workshop
        3. Which one has stronger research value
        4. Risks or cautions for each
        """
        with st.spinner("Generating extension ideas..."):
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

st.subheader("What Makes This Valuable")
render_section_card(
    "Immediate use in the workshop",
    "Participants can follow your examples live and instantly turn a concept into a workflow, plot plan, or interpretation checklist.",
)
render_section_card(
    "Long-term research value",
    "After the session, the same page becomes a starting point for exploring small simulations, analyzing datasets, and planning the next iteration of a research idea.",
)
