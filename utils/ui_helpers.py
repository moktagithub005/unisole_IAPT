import streamlit as st

from utils.constants import WORKSHOP_SUBTITLE, WORKSHOP_TITLE


def apply_page_header(title: str, subtitle: str) -> None:
    st.title(title)
    st.caption(subtitle)


def render_hero(title: str, tagline: str) -> None:
    st.markdown(
        f"""
        <div style="padding: 1.4rem 1.2rem; border-radius: 18px; background:
        linear-gradient(135deg, rgba(198,93,0,0.12), rgba(22,32,41,0.08));
        border: 1px solid rgba(198,93,0,0.18); margin-bottom: 1rem;">
            <div style="font-size: 0.9rem; letter-spacing: 0.06em; text-transform: uppercase; color: #8A470B;">
                {WORKSHOP_SUBTITLE}
            </div>
            <div style="font-size: 2rem; font-weight: 700; color: #162029; margin-top: 0.3rem;">
                {title}
            </div>
            <div style="font-size: 1rem; color: #2F3D46; margin-top: 0.6rem; line-height: 1.6;">
                {tagline}
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_sidebar_note() -> None:
    with st.sidebar:
        st.markdown(f"### {WORKSHOP_TITLE}")
        st.info(
            "This app is designed for guided workshop use: explain, test, question, "
            "verify, and then improve the prompt."
        )


def render_metric_strip(items: list[tuple[str, str]]) -> None:
    columns = st.columns(len(items))
    for column, (label, value) in zip(columns, items):
        column.metric(label, value)


def render_section_card(title: str, body: str) -> None:
    st.markdown(
        f"""
        <div style="padding: 1rem; border-radius: 16px; background: white;
        border-left: 6px solid #C65D00; box-shadow: 0 8px 24px rgba(0,0,0,0.04); margin-bottom: 0.9rem;">
            <div style="font-weight: 700; color: #162029; margin-bottom: 0.35rem;">{title}</div>
            <div style="color: #31424A; line-height: 1.6;">{body}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )
