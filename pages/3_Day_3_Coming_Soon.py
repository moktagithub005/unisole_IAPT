import sys
from pathlib import Path

import streamlit as st


ROOT_DIR = Path(__file__).resolve().parents[1]
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

from utils.ui_helpers import render_hero, render_metric_strip, render_section_card, render_sidebar_note


st.set_page_config(page_title="Day 3: Coming Soon", page_icon="🧭", layout="wide")
render_sidebar_note()
render_hero(
    "Day 3: Coming Soon",
    "This page is intentionally empty and contains no Day 2 content.",
)

render_metric_strip(
    [
        ("Status", "Reserved"),
        ("Workshop Stage", "Future Design"),
        ("Current Use", "No activity yet"),
        ("Priority", "After Day 2"),
    ]
)

st.subheader("Current Status")
render_section_card(
    "No workshop content here",
    "All Day 2 material stays only in the Day 2 main page and its Day 2 subpages.",
)
render_section_card(
    "Reserved for future design",
    "Day 3 will be planned separately when the workshop reaches that stage.",
)
