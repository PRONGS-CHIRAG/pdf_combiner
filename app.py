"""
🚀 PDF & Image Merger
Created by: Chirag Natesh Vijay (https://chiragatgermany.wixsite.com/chirag-natesh-vijay | GitHub: @PRONGS-CHIRAG)
Version: 1.0
License: MIT

🛠️ Streamlit-based app for merging and reordering PDFs and images into a single PDF.
"""

import streamlit as st
from streamlit_sortables import sort_items
from PyPDF2 import PdfMerger
from PIL import Image
import tempfile
import os

st.set_page_config(page_title="PDF & Image Merger", layout="centered")
st.title("📎 PDF & Image Merger")

uploaded_files = st.file_uploader(
    "Upload PDF and/or Image files",
    type=["pdf", "png", "jpg", "jpeg"],
    accept_multiple_files=True
)

if uploaded_files:
    st.write("### 🗂️ Reorder Files by Drag-and-Drop")
    file_names = [file.name for file in uploaded_files]
    ordered_names = sort_items(file_names, direction="vertical")

    # Map file names to uploaded files
    name_to_file = {file.name: file for file in uploaded_files}
    ordered_files = [name_to_file[name] for name in ordered_names]

    if st.button("📄 Combine Files"):
        with st.spinner("Combining files..."):
            merger = PdfMerger()
            temp_files = []

            try:
                for file in ordered_files:
                    ext = os.path.splitext(file.name)[1].lower()
                    if ext == ".pdf":
                        merger.append(file)
                    elif ext in [".png", ".jpg", ".jpeg"]:
                        img = Image.open(file)
                        if img.mode in ("RGBA", "P"):
                            img = img.convert("RGB")
                        temp = tempfile.NamedTemporaryFile(delete=False, suffix=".pdf")
                        img.save(temp.name, "PDF", resolution=100.0)
                        temp_files.append(temp.name)
                        merger.append(temp.name)

                output = tempfile.NamedTemporaryFile(delete=False, suffix=".pdf")
                merger.write(output.name)
                merger.close()

                with open(output.name, "rb") as f:
                    st.success("✅ Files combined successfully!")
                    st.download_button(
                        label="📥 Download Combined PDF",
                        data=f,
                        file_name="combined_output.pdf",
                        mime="application/pdf"
                    )

            except Exception as e:
                st.error(f"An error occurred: {e}")
            finally:
                for temp_file in temp_files:
                    os.unlink(temp_file)
