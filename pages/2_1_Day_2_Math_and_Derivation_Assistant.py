import sys
from pathlib import Path

import streamlit as st


ROOT_DIR = Path(__file__).resolve().parents[1]
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

from utils.constants import (
    DAY_TWO_TAGLINE,
    DEFAULT_SYSTEM_PROMPT,
    RESEARCH_EXPERIMENT_MODES,
)
from utils.groq_client import get_default_model, get_groq_api_key, groq_chat_completion
from utils.ui_helpers import render_hero, render_metric_strip, render_section_card, render_sidebar_note


st.set_page_config(page_title="Day 2: Math and Derivation Assistant", page_icon="🧮", layout="wide")
render_sidebar_note()
render_hero("Day 2: AI for Mathematical Reasoning", DAY_TWO_TAGLINE)

render_metric_strip(
    [
        ("Session Role", "Derivation Companion"),
        ("Best Use", "Equation + Assumption Checks"),
        ("Core Habit", "Verify the Steps"),
        ("Takeaway", "Safer Math Prompts"),
    ]
)

with st.sidebar:
    st.markdown("### Participant Controls")
    model_name = st.text_input("Groq model", value=get_default_model(), key="math_model")
    temperature = st.slider("Creativity", min_value=0.0, max_value=1.0, value=0.1, step=0.1, key="math_temp")
    if get_groq_api_key():
        st.success("Groq key detected")
    else:
        st.error("Groq key not found in .env")
    st.markdown("### Use this page to")
    st.write("1. Break hard derivations into steps.")
    st.write("2. Surface assumptions.")
    st.write("3. Spot possible weak points.")
    st.write("4. Prepare what to verify manually.")

st.subheader("What Participants Gain Here")
col1, col2 = st.columns([1.05, 0.95], gap="large")
with col1:
    st.write(
        "This page supports one of the most practical Day 2 needs: using AI to make equations, derivations, "
        "and symbolic arguments more teachable and more readable without pretending the model is always correct."
    )
    st.write(
        "Participants can use it during the lecture to follow along, and later to unpack difficult mathematics "
        "from papers, class notes, or early research ideas."
    )
with col2:
    render_section_card(
        "Correct goal",
        "Use AI to reveal structure, assumptions, and checkpoints in a derivation.",
    )
    render_section_card(
        "Wrong goal",
        "Treat a polished-looking equation trail as proof that the derivation is trustworthy.",
    )

st.subheader("Derivation Workspace")
tab1, tab2, tab3, tab4 = st.tabs(
    ["Explain the Math", "Assumption Checker", "Step Repair", "Verification Checklist"]
)

with tab1:
    equation_topic = st.text_area(
        "Equation, derivation, or concept",
        value=r"Derive the electric field $E(r)$ for an infinite line charge using Gauss's law, $\nabla \cdot E = \frac{\rho}{\varepsilon_0}$.",
        height=110,
    )
    audience = st.selectbox(
        "Explain it for",
        ["BSc students", "MSc students", "research scholars", "my own preparation"],
        index=0,
    )
    if st.button("Explain this derivation", key="explain_math", use_container_width=True):
        prompt = f"""
        Mode: {RESEARCH_EXPERIMENT_MODES["Derivation Coach"]}

        Topic:
        {equation_topic}

        Audience:
        {audience}

        Output format:
        1. What the derivation is trying to show
        2. Step-by-step explanation
        3. Definitions of important symbols
        4. One common confusion point
        5. What should still be checked manually
        """
        with st.spinner("Explaining the derivation..."):
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
    derivation_text = st.text_area(
        "Paste the derivation or describe the method",
        value=(
            "We choose a cylindrical Gaussian surface and assume symmetry so that the electric field "
            r"$E(r)$ is constant in magnitude on the curved surface, giving $\Phi_E = E(2\pi r L)$."
        ),
        height=130,
    )
    if st.button("List the assumptions", key="assumption_check", use_container_width=True):
        prompt = f"""
        Mode: {RESEARCH_EXPERIMENT_MODES["Derivation Coach"]}

        Derivation description:
        {derivation_text}

        Output format:
        1. Explicit assumptions
        2. Hidden assumptions
        3. Where the logic may fail if assumptions are broken
        4. A short warning for a researcher or teacher
        """
        with st.spinner("Surfacing assumptions..."):
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
    stuck_step = st.text_area(
        "Which step feels unclear or incorrect?",
        value=r"I do not understand why the electric flux becomes $\Phi_E = E(2\pi r L)$ in this step.",
        height=110,
    )
    if st.button("Repair this step", key="repair_step", use_container_width=True):
        prompt = f"""
        Mode: {RESEARCH_EXPERIMENT_MODES["Derivation Coach"]}

        Unclear step:
        {stuck_step}

        Output format:
        1. What this step is assuming
        2. Why the step may be valid
        3. What would make the step invalid
        4. A slower explanation for a participant
        """
        with st.spinner("Clarifying the weak step..."):
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
    final_claim = st.text_area(
        "Equation or conclusion to verify",
        value=r"The resulting electric field satisfies $E(r) \propto \frac{1}{r}$ for an infinite line charge.",
        height=90,
    )
    if st.button("Build my verification checklist", key="verify_math", use_container_width=True):
        prompt = f"""
        Mode: {RESEARCH_EXPERIMENT_MODES["Derivation Coach"]}

        Final claim:
        {final_claim}

        Output format:
        1. Quick explanation
        2. A verification checklist
        3. Boundary cases or dimensional checks to perform
        4. Confidence label: High, Medium, or Low
        """
        with st.spinner("Creating a verification checklist..."):
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

st.subheader("Take This Beyond the Workshop")
render_section_card(
    "For teaching",
    "Paste a difficult derivation from your class notes and ask for assumptions, confusion points, and manual checks before using the explanation in class.",
)
render_section_card(
    "For research",
    "Use the model to unpack symbols, identify hidden assumptions, and propose sanity checks before trusting a symbolic result from a paper or draft idea.",
)
