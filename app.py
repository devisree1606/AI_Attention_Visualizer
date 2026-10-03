import streamlit as st
from PIL import Image
import re
import numpy as np
import matplotlib.pyplot as plt

from ocr import extract_text
from embedding import create_embeddings
from attention import calculate_attention


st.set_page_config(
    page_title="AI Text Insight Visualizer",
    layout="wide"
)

st.title("AI Text Insight Visualizer")

st.write(
    "Convert image text into words and visualize word-level attention "
    "using an attention mechanism."
)

st.divider()


uploaded_file = st.file_uploader(
    "Upload an Image",
    type=["png", "jpg", "jpeg"]
)


if uploaded_file is not None:

    image = Image.open(uploaded_file)

    st.subheader("Uploaded Image")

    st.image(
        image,
        width=700
    )

    st.divider()

    st.subheader("Extracted Text")

    text = extract_text(image)

    if text.startswith("OCR Error:"):

        st.error(text)

    elif not text:

        st.warning(
            "No text could be detected in the image."
        )

    else:

        st.text_area(
            "OCR Result",
            text,
            height=180
        )

        words = re.findall(
            r"\b[a-zA-Z0-9]+\b",
            text.lower()
        )

        if len(words) > 0:

            st.divider()

            st.subheader("Word-Level Attention")

            embeddings = create_embeddings(words)

            attention_scores = calculate_attention(
                embeddings
            )

            attention_scores = np.asarray(
                attention_scores
            )

            max_score = np.max(attention_scores)

            if max_score > 0:

                display_scores = (
                    attention_scores / max_score
                )

            else:

                display_scores = attention_scores


            for word, score in zip(
                words,
                display_scores
            ):

                st.progress(
                    float(score),
                    text=f"{word} - {score:.4f}"
                )


            st.divider()

            st.subheader("Attention Visualization")

            fig, ax = plt.subplots(
                figsize=(14, 6)
            )

            positions = np.arange(
                len(words)
            )

            bars = ax.bar(
                positions,
                display_scores
            )

            ax.set_xticks(
                positions
            )

            ax.set_xticklabels(
                words,
                rotation=60,
                ha="right"
            )

            ax.set_xlabel(
                "Words"
            )

            ax.set_ylabel(
                "Attention Score"
            )

            ax.set_title(
                "Word-Level Attention"
            )

            for bar, score in zip(
                bars,
                display_scores
            ):

                ax.text(
                    bar.get_x() + bar.get_width() / 2,
                    bar.get_height(),
                    f"{score:.2f}",
                    ha="center",
                    va="bottom",
                    fontsize=8
                )

            plt.tight_layout()

            st.pyplot(fig)


            st.divider()

            st.subheader("Most Important Words")

            word_scores = list(
                zip(words, display_scores)
            )

            word_scores.sort(
                key=lambda x: x[1],
                reverse=True
            )

            top_words = word_scores[:5]

            for word, score in top_words:

                st.write(
                    f"{word} : {score:.4f}"
                )