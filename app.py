import streamlit as st

from utils.constants import (
    DAY_ONE_MODULES,
    DAY_TWO_MODULES,
    WORKSHOP_SUBTITLE,
    WORKSHOP_TITLE,
)
from utils.ui_helpers import (
    apply_page_header,
    render_hero,
    render_metric_strip,
    render_section_card,
    render_sidebar_note,
)


st.set_page_config(
    page_title="UNISOLE IAPT Workshop",
    page_icon="🧠",
    layout="wide",
)

render_sidebar_note()
apply_page_header(WORKSHOP_TITLE, WORKSHOP_SUBTITLE)
render_hero(
    "AI for Physics Educators",
    "A workshop app built for live teaching, participant experimentation, and research-oriented follow-through.",
)

render_metric_strip(
    [
        ("Format", "7-Day Workshop"),
        ("Audience", "Physics Educators"),
        ("Mode", "Live + Interactive"),
        ("Focus Today", "Day 2 Research Shift"),
    ]
)

st.subheader("Workshop Snapshot")
st.write(
    "This space is meant to support a national-level workshop where participants do not just hear "
    "about AI, but actively question it, test it, and learn how to guide it responsibly."
)

st.subheader("Why Day 2 Matters")
render_section_card(
    "This is where AI becomes research-relevant",
    "Day 2 is the turning point of the workshop. Participants move beyond prompt curiosity and start "
    "seeing AI as a careful instrument for literature discovery, mathematical understanding, and scientific workflow design.",
)
render_section_card(
    "Participants should leave feeling more capable",
    "The design goal is that every participant leaves with something reusable: a better reading strategy, "
    "a safer derivation workflow, or a simulation-analysis prompt they can adapt in their own research after the workshop.",
)

col1, col2 = st.columns(2, gap="large")
with col1:
    st.subheader("Day 1 Foundation")
    for module in DAY_ONE_MODULES:
        with st.container(border=True):
            left, right = st.columns([3, 1])
            left.markdown(f"#### {module['title']}")
            left.write(module["focus"])
            right.metric("Duration", module["duration"])
            st.markdown("**Key takeaways**")
            for item in module["outcomes"]:
                st.write(f"- {item}")
with col2:
    st.subheader("Day 2 Agenda")
    for module in DAY_TWO_MODULES:
        with st.container(border=True):
            left, right = st.columns([3, 1])
            left.markdown(f"#### {module['title']}")
            left.write(module["focus"])
            right.metric("Duration", module["duration"])
            st.markdown("**Key takeaways**")
            for item in module["outcomes"]:
                st.write(f"- {item}")

st.success(
    "Open the Day 2 pages from the sidebar to run the live participant activities for literature review, mathematical reasoning, and research workflows."
)
