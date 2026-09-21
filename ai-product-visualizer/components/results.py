"""Analysis results dashboard."""

import streamlit as st

from components import media, theme
from components.qa import render_qa
from components.state import reset_analysis


def _attribute_card(title: str, body_html: str) -> str:
    return (
        f'<div class="pv-card"><div class="pv-eyebrow">{title}</div>'
        f'<div style="margin-top:.2rem">{body_html}</div></div>'
    )


def render_results() -> None:
    analysis = st.session_state.analysis
    overview = analysis["overview"]
    attrs = analysis["attributes"]
    conf = analysis["confidence"]

    head, action = st.columns([3, 1])
    with head:
        theme.section(
            "Product analysis",
            f"Source image: {st.session_state.analysis_source or 'sample product'}",
        )
    with action:
        if st.button("New analysis", **theme.STRETCH):
            reset_analysis()
            st.rerun()

    left, right = st.columns([1.15, 1.35], gap="large")

    with left:
        image = st.session_state.upload
        if image is not None:
            st.image(image, **theme.STRETCH)
        else:
            st.image(media.placeholder_image("#8A93A3"), **theme.STRETCH)

    with right:
        theme.section("Product overview", eyebrow="Summary")
        theme.rows(overview.items())
        theme.spacer(0.7)

        st.markdown(
            f"""
            <div class="pv-card">
              <div class="pv-eyebrow">AI confidence</div>
              <div style="display:flex;align-items:baseline;justify-content:space-between">
                <span style="font-size:.9rem;font-weight:600">{conf['label']}</span>
                <span style="font-size:1.35rem;font-weight:700">{conf['score']}%</span>
              </div>
              <div class="pv-meter"><span style="width:{conf['score']}%"></span></div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    theme.spacer(2.0)
    theme.section("Visual attributes", "What the image shows, grouped by attribute.")

    swatches = {c["name"]: c["hex"] for c in attrs["Colors"]}
    color_html = theme.chips([c["name"] for c in attrs["Colors"]], swatches)

    row1 = st.columns(3, gap="medium")
    with row1[0]:
        st.markdown(_attribute_card("Colors", color_html), unsafe_allow_html=True)
    with row1[1]:
        st.markdown(
            _attribute_card("Material", theme.chips(attrs["Material"])),
            unsafe_allow_html=True,
        )
    with row1[2]:
        st.markdown(
            _attribute_card("Shape", theme.chips(attrs["Shape"])),
            unsafe_allow_html=True,
        )

    theme.spacer(0.9)
    row2 = st.columns([1, 2], gap="medium")
    with row2[0]:
        st.markdown(
            _attribute_card("Style", theme.chips(attrs["Style"])),
            unsafe_allow_html=True,
        )
    with row2[1]:
        st.markdown(
            _attribute_card("Features", theme.chips(attrs["Features"])),
            unsafe_allow_html=True,
        )

    theme.spacer(2.0)
    theme.section("AI product description", "A written summary of the same image.")
    st.markdown(
        f"""
        <div class="pv-card" style="padding:1.5rem 1.7rem">
          <p style="font-size:.95rem;line-height:1.75;color:#DCE2EA;max-width:74ch">
            {analysis['description']}
          </p>
          <div style="margin-top:1.1rem;padding-top:.9rem;border-top:1px solid var(--border)">
            <span class="pv-pill">Placeholder text &mdash; model not connected</span>
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    theme.spacer(2.0)
    render_qa()
