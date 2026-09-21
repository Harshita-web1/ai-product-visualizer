"""Project overview."""

import streamlit as st

from components import media, theme

CAPABILITIES = [
    ("Image understanding", "Reads a single product photo as the only input."),
    ("Product classification", "Places the item in a category and product type."),
    ("Visual attribute extraction", "Pulls out colors, material, shape, style and features."),
    ("AI-generated descriptions", "Turns those attributes into readable copy."),
    ("Product Q&A", "Answers follow-up questions about the same image."),
]


def render_about() -> None:
    st.markdown(
        """
        <div class="pv-hero" style="padding:2.2rem 2.4rem">
          <h2 style="font-size:1.7rem">About AI Product Visualizer</h2>
          <p>AI Product Visualizer uses multimodal AI to analyze product images and
          generate structured visual insights: what the product is, what it is made
          of, how it looks, and how it can be described.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    theme.section("Technology", "What the project is built on.")
    c1, c2, c3 = st.columns(3, gap="medium")
    with c1:
        theme.card("Frontend", "Streamlit, with a custom dark interface layer.", media.ICON_LAYERS)
    with c2:
        theme.card("AI platform", "Microsoft Foundry hosts the model endpoint.", media.ICON_SCAN)
    with c3:
        theme.card("Model", "GPT-4.1-mini for multimodal image analysis.", media.ICON_TEXT)

    theme.spacer(2.0)
    theme.section("Capabilities", "Planned scope of the analysis pipeline.")
    theme.rows([(name, detail) for name, detail in CAPABILITIES])

    theme.spacer(2.0)
    left, right = st.columns([1.4, 1], gap="large")
    with left:
        st.markdown(
            """
            <div class="pv-card">
              <div class="pv-eyebrow">Current status</div>
              <p style="font-size:.88rem;line-height:1.7">
                This build is the interface only. Every result on the analysis and
                history screens is placeholder content used to preview layout and
                interaction. No model is called, and nothing is stored between
                sessions.
              </p>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with right:
        st.markdown(
            """
            <div class="pv-card">
              <div class="pv-eyebrow">Project</div>
              <p style="font-size:.88rem;line-height:1.7">
                Built as an academic / hackathon project.
              </p>
            </div>
            """,
            unsafe_allow_html=True,
        )
