"""Top header for every page."""

import streamlit as st


def render_header(title: str, subtitle: str) -> None:
    st.markdown(
        f"""
        <div class="pv-header">
          <div>
            <h1>{title}</h1>
            <p>{subtitle}</p>
          </div>
          <div class="pv-header-meta">
            <span class="pv-pill">Interface preview</span>
            <span class="pv-pill"><span class="pv-dot idle"></span> GPT-4.1-mini</span>
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
