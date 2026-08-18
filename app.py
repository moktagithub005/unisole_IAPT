import streamlit as st

from utils.constants import DAY_ONE_MODULES, WORKSHOP_SUBTITLE, WORKSHOP_TITLE
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
    "A workshop app built for live teaching, audience experimentation, and reflective discussion.",
)

render_metric_strip(
    [
        ("Format", "7-Day Workshop"),
        ("Audience", "Physics Educators"),
        ("Mode", "Live + Interactive"),
        ("Engine", "Groq-Powered"),
    ]
)

st.subheader("Workshop Snapshot")
st.write(
    "This space is meant to support a national-level workshop where participants do not just hear "
    "about AI, but actively question it, test it, and learn how to guide it responsibly."
)

st.subheader("Why Day 1 Matters")
render_section_card(
    "Start with understanding, not hype",
    "Day 1 creates the mental model that everything else depends on: what an LLM really does, "
    "where it shines, where it breaks, and why better prompting matters.",
)
render_section_card(
    "Make the audience want Day 2",
    "The design goal is simple: participants should leave curious. They should feel that AI is useful, "
    "imperfect, worth experimenting with, and worth learning to steer more carefully tomorrow.",
)

st.subheader("Day 1 Agenda")
for module in DAY_ONE_MODULES:
    with st.container(border=True):
        left, right = st.columns([3, 1])
        left.markdown(f"#### {module['title']}")
        left.write(module["focus"])
        right.metric("Duration", module["duration"])
        st.markdown("**Key takeaways**")
        for item in module["outcomes"]:
            st.write(f"- {item}")

st.success("Open the Day 1 page from the sidebar to run the full interactive session.")
