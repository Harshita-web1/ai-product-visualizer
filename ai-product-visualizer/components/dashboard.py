"""Dashboard / home page."""

import streamlit as st

from components import media, theme
from components.state import go


def render_dashboard() -> None:
    st.markdown(
        """
        <div class="pv-hero">
          <h2>Understand your product instantly.</h2>
          <p>Upload a product image and let AI identify its visual attributes,
          describe the product, and answer questions about it.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    left, right, _ = st.columns([1, 1, 3.4])
    with left:
        if st.button("Analyze product", type="primary", **theme.STRETCH):
            go("Analyze Product")
    with right:
        if st.button("View history", **theme.STRETCH):
            go("History")

    theme.spacer(2.2)
    theme.section(
        "What it does",
        "Three parts of the analysis, produced from a single image.",
    )

    c1, c2, c3 = st.columns(3, gap="medium")
    with c1:
        theme.card(
            "Product intelligence",
            "Identify category, materials, colors, shape and visual characteristics.",
            media.ICON_SCAN,
        )
    with c2:
        theme.card(
            "AI description",
            "Generate clear, structured product descriptions from a single image.",
            media.ICON_TEXT,
        )
    with c3:
        theme.card(
            "Product Q&A",
            "Ask questions about the uploaded product and get contextual answers.",
            media.ICON_CHAT,
        )

    theme.spacer(2.2)
    theme.section("Recent activity", "The last products opened in this workspace.")

    recent = st.session_state.history[:3]
    if not recent:
        st.markdown(
            '<div class="pv-empty"><h4>No product analyses yet</h4>'
            "<p>Upload your first product to get started.</p></div>",
            unsafe_allow_html=True,
        )
        return

    cols = st.columns(len(recent), gap="medium")
    for col, item in zip(cols, recent):
        with col:
            st.markdown(
                f"""
                <div class="pv-card">
                  <div style="display:flex;gap:.8rem;align-items:center">
                    <img class="pv-thumb" style="width:44px;height:44px;object-fit:cover"
                         src="{media.image_data_uri(media.placeholder_image(item['tint'], 120))}"/>
                    <div>
                      <h4 style="margin:0">{item['name']}</h4>
                      <p style="margin-top:.2rem">{item['category']} &middot; {item['date']}</p>
                    </div>
                  </div>
                </div>
                """,
                unsafe_allow_html=True,
            )
