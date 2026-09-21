"""Chat-style question panel attached to the current analysis."""

import html

import streamlit as st

from components import theme
from data.mock_data import DEFAULT_ANSWER, SAMPLE_ANSWERS, SUGGESTED_QUESTIONS


def _answer_for(question: str) -> str:
    """Stands in for the request that will later be sent with the image."""
    return SAMPLE_ANSWERS.get(question.strip(), DEFAULT_ANSWER)


def _submit(question: str) -> None:
    question = question.strip()
    if not question:
        return
    st.session_state.qa.append({"role": "user", "text": question})
    st.session_state.qa.append({"role": "ai", "text": _answer_for(question)})


def render_qa() -> None:
    theme.section(
        "Ask about this product",
        "Questions stay tied to the image you analysed.",
    )

    if not st.session_state.qa:
        st.markdown(
            '<div class="pv-card"><p>No questions yet. Pick a suggestion below or '
            "write your own.</p></div>",
            unsafe_allow_html=True,
        )
    else:
        bubbles = []
        for msg in st.session_state.qa:
            role = "user" if msg["role"] == "user" else "ai"
            who = "You" if role == "user" else "Assistant &middot; preview"
            bubbles.append(
                f'<div class="pv-msg {role}"><div class="who">{who}</div>'
                f'{html.escape(msg["text"])}</div>'
            )
        st.markdown("".join(bubbles), unsafe_allow_html=True)

    theme.spacer(0.6)

    field, action = st.columns([4, 1])
    with field:
        question = st.text_input(
            "Question",
            key="qa_input",
            placeholder="Ask a question about this product...",
            label_visibility="collapsed",
        )
    with action:
        asked = st.button(
            "Ask AI",
            type="primary",
            **theme.STRETCH,
            disabled=not question.strip(),
        )

    if asked:
        _submit(question)
        st.rerun()

    st.markdown(
        '<div class="pv-eyebrow" style="margin-top:1rem">Try one of these</div>',
        unsafe_allow_html=True,
    )
    cols = st.columns(len(SUGGESTED_QUESTIONS), gap="small")
    for col, suggestion in zip(cols, SUGGESTED_QUESTIONS):
        with col:
            if st.button(suggestion, key=f"sq_{suggestion[:18]}", **theme.STRETCH):
                _submit(suggestion)
                st.rerun()
