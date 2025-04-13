# pdf_combiner
📎 PDF & Image Merger with Drag-and-Drop Reordering

An intuitive and user-friendly Streamlit web app that allows you to merge PDF and image files (PNG, JPG, JPEG) into a single PDF—with drag-and-drop reordering support! No installation of Adobe or third-party tools needed.

🚀 Features

    📤 Upload multiple PDFs and images

    🔀 Reorder files via drag-and-drop interface

    🖼️ Image to PDF conversion with proper formatting

    📄 Combine everything into one downloadable PDF

    ✅ Clean, modern, and minimal UI powered by Streamlit

🧩 Supported File Types

    .pdf

    .png

    .jpg

    .jpeg

🛠️ Installation & Running Locally

Clone the repository

git clone https://github.com/PRONGS-CHIRAG/pdf_combiner
cd pdf-combiner

Create a virtual environment (optional but recommended)

python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

Install dependencies

pip install -r requirements.txt

Run the app

    streamlit run app.py

📝 Requirements

    Python 3.7+

    Libraries:

        streamlit

        streamlit-sortables

        PyPDF2

        Pillow

📦 Example requirements.txt

streamlit
streamlit-sortables
PyPDF2
Pillow

💡 Use Cases

    Merge scanned documents and image attachments into one PDF

    Reorder and combine reports and reference materials

    Simplify document workflows without leaving the browser

📄 License

MIT
