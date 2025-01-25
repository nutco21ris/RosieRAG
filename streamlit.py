import streamlit as st
from PIL import Image

def main():
    st.set_page_config(page_title="Advertising in Your Pocket", layout="wide")

    st.markdown("""
        <style>
        .stApp {background-color: white; color: black;}
        .stButton button {
            background-color: black;
            color: white;
            border-radius: 4px;
            padding: 4px 16px;
        }
        .stTextInput input {
            border: none;
            border-radius: 0;
            border-bottom: 1px solid #ccc;
            padding: 10px 0;
            background: transparent;
        }
        .stTextInput input:focus {
            border-color: black;
            box-shadow: none;
        }
        .stUploadedFileMsg, .css-1qf60ue {display: none !important;}
        .css-1etr1iv {padding-top: 0 !important;}
        [data-testid="stFileUploader"] {
            width: 100%;
            padding: 0;
            margin: 0;
            border: none !important;
        }
        </style>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns([1, 4])
    with col1:
        logo = Image.open('RosieRagLogoLarge.png')
        st.image(logo, width=150)
    with col2:
        st.title("Advertising in Your Pocket!")

    uploaded_file = st.file_uploader("", type=['mp4', 'mov', 'avi', 'mpeg4'])
    terms_accepted = st.checkbox("Or by clicking this box, you are allowing us to search for your product videos information online!")

    st.markdown("### Product Information")
    product_name = st.text_input("Tell me the product name you are advertising for?")
    customization = st.text_input("Tell me how you want to customize your advertisement videos.")

    # Enable button if both upload and terms are accepted and text inputs are filled
    enable_download = uploaded_file and terms_accepted and product_name and customization
    
    st.download_button(
        label="Download Your Video",
        data=uploaded_file if uploaded_file else b"placeholder",
        file_name="customized_video.mp4",
        mime="video/mp4",
        disabled=not enable_download
    )

if __name__ == "__main__":
    main()