"""Session state setup and navigation."""

import streamlit as st

PAGES = ["Dashboard", "Analyze Product", "History", "About"]

_DEFAULTS = {
    "page": "Dashboard",
    "upload": None,          # UploadedFile from the uploader
    "analysis": None,        # dict matching the contract in data/mock_data.py
    "analysis_source": None, # label describing what produced the current result
    "qa": [],                # [{"role": "user"|"ai", "text": str}]
    "history": None,         # list of history records
    "pending_question": None,
    "toast": None,
}


def init_state() -> None:
    for key, value in _DEFAULTS.items():
        if key not in st.session_state:
            st.session_state[key] = value
    if st.session_state.history is None:
        from data.mock_data import SAMPLE_HISTORY
        st.session_state.history = list(SAMPLE_HISTORY)


def go(page: str, toast: str | None = None) -> None:
    st.session_state.page = page
    if toast:
        st.session_state.toast = toast
    st.rerun()


def reset_analysis() -> None:
    st.session_state.analysis = None
    st.session_state.analysis_source = None
    st.session_state.qa = []
