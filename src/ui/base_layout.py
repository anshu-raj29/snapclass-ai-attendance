import streamlit as st



def style_background_home():

    st.markdown("""
        <style>

                .stApp {
                    background:
                        radial-gradient(circle at top left, rgba(88,101,242,0.20), transparent 34rem),
                        radial-gradient(circle at bottom right, rgba(235,69,158,0.14), transparent 30rem),
                        #070b16 !important;
                }

                .stApp div[data-testid="stColumn"]{
                    background: linear-gradient(145deg, rgba(21,28,48,0.95), rgba(14,19,34,0.95)) !important;
                    padding:2.5rem !important;
                    border-radius: 1.5rem !important;
                    border: 1px solid rgba(148,163,184,0.22) !important;
                    box-shadow: 0 24px 70px rgba(0,0,0,0.35) !important;
                    }
        </style>  

                """
            ,unsafe_allow_html=True)
    

def style_background_dashboard():

    st.markdown("""
        <style>

                .stApp {
                    background:
                        radial-gradient(circle at top right, rgba(88,101,242,0.15), transparent 32rem),
                        radial-gradient(circle at bottom left, rgba(235,69,158,0.10), transparent 28rem),
                        #070b16 !important;
                }

        </style>  

                """
            ,unsafe_allow_html=True)
    

    

def style_base_layout():
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Climate+Crisis:YEAR@1979&display=swap');
        @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@100..900&display=swap');

                
         /* Hide Top Bar of streamlit */
                
            #MainMenu, footer, header {
                visibility: hidden;
            }
                
            .block-container {
                padding-top:1.5rem !important;
                padding-bottom:2rem !important;
                max-width: 1180px !important;
            }

            html, body, .stApp, [data-testid="stAppViewContainer"] {
                color: #e5e7eb !important;
                font-family: 'Outfit', sans-serif !important;
            }

            h1 {
                font-family: 'Climate Crisis', sans-serif !important;
                font-size: 3.25rem !important;
                line-height:1.08 !important;
                margin-bottom:0rem !important;
                letter-spacing: 0 !important;
            }
                

            h2 {
                font-family: 'Climate Crisis', sans-serif !important;
                font-size: 2rem !important;
                line-height:0.9 !important;
                margin-bottom:0rem !important;
                letter-spacing: 0 !important;
            }
                
            h3, h4, h5, h6, p, label, span, div {
                font-family: 'Outfit', sans-serif;
            }

            h1, h2, h3, h4, h5, h6,
            [data-testid="stMarkdownContainer"],
            [data-testid="stText"],
            label,
            p {
                color: #e5e7eb !important;
            }

            h3 {
                font-size: 1.45rem !important;
                font-weight: 800 !important;
            }

            .st-emotion-cache-1kyxreq,
            [data-testid="stImage"] {
                border-radius: 1rem !important;
            }

            [data-testid="stHeader"] {
                background: transparent !important;
            }

            [data-testid="stToolbar"] {
                color: #e5e7eb !important;
            }

            [data-testid="stVerticalBlockBorderWrapper"],
            [data-testid="stExpander"],
            div[data-testid="stForm"],
            div[data-testid="stPopoverBody"],
            div[data-testid="stDialog"] > div {
                background: rgba(15,23,42,0.94) !important;
                border: 1px solid rgba(148,163,184,0.22) !important;
                border-radius: 1.25rem !important;
                box-shadow: 0 22px 60px rgba(0,0,0,0.34) !important;
            }

            div[data-testid="stDialog"] div[role="dialog"] {
                background: #0f172a !important;
                border: 1px solid rgba(148,163,184,0.26) !important;
                border-radius: 1.25rem !important;
                box-shadow: 0 28px 90px rgba(0,0,0,0.48) !important;
            }

            div[data-testid="stDialog"] div[role="dialog"] * {
                color: #e5e7eb !important;
            }

            div[data-testid="stTextInput"] input,
            div[data-testid="stTextArea"] textarea,
            div[data-baseweb="select"] > div,
            div[data-testid="stNumberInput"] input {
                background: #111827 !important;
                color: #f8fafc !important;
                border: 1px solid rgba(148,163,184,0.30) !important;
                border-radius: 0.9rem !important;
                box-shadow: none !important;
            }

            div[data-testid="stTextInput"] input::placeholder,
            div[data-testid="stTextArea"] textarea::placeholder {
                color: #94a3b8 !important;
                opacity: 1 !important;
            }

            div[data-testid="stTextInput"] input:focus,
            div[data-testid="stTextArea"] textarea:focus,
            div[data-baseweb="select"] > div:focus-within,
            div[data-testid="stNumberInput"] input:focus {
                border-color: #818cf8 !important;
                box-shadow: 0 0 0 3px rgba(129,140,248,0.18) !important;
            }

            [data-testid="stCameraInput"],
            [data-testid="stFileUploader"],
            [data-testid="stAudioInput"] {
                background: rgba(15,23,42,0.76) !important;
                border: 1px solid rgba(148,163,184,0.22) !important;
                border-radius: 1.1rem !important;
                padding: 1rem !important;
            }

            [data-testid="stDataFrame"],
            [data-testid="stTable"] {
                border-radius: 1rem !important;
                overflow: hidden !important;
                border: 1px solid rgba(148,163,184,0.22) !important;
                background: #0f172a !important;
            }

            [data-testid="stAlert"] {
                background: rgba(15,23,42,0.92) !important;
                color: #e5e7eb !important;
                border: 1px solid rgba(148,163,184,0.22) !important;
                border-radius: 1rem !important;
            }

            hr {
                border-color: rgba(148,163,184,0.22) !important;
                margin: 1.5rem 0 !important;
            }
                

            button{
                border-radius: 0.85rem !important;
                background: linear-gradient(135deg, #6366f1, #8b5cf6) !important;
                color: white !important;
                padding: 0.68rem 1rem !important;
                border: none !important;
                font-weight: 800 !important;
                box-shadow: 0 14px 34px rgba(99,102,241,0.25) !important;
                transition: transform 0.18s ease, box-shadow 0.18s ease, filter 0.18s ease !important;
                }

            button[kind="secondary"]{
                border-radius: 0.85rem !important;
                background: linear-gradient(135deg, #ec4899, #f97316) !important;
                color: white !important;
                padding: 0.68rem 1rem !important;
                border: none !important;
                font-weight: 800 !important;
                box-shadow: 0 14px 34px rgba(236,72,153,0.22) !important;
                transition: transform 0.18s ease, box-shadow 0.18s ease, filter 0.18s ease !important;
                }

            button[kind="tertiary"]{
                border-radius: 0.85rem !important;
                background: #1f2937 !important;
                color: white !important;
                padding: 0.68rem 1rem !important;
                border: 1px solid rgba(148,163,184,0.28) !important;
                font-weight: 800 !important;
                transition: transform 0.18s ease, border-color 0.18s ease, filter 0.18s ease !important;
                }

            button:hover{
                transform: translateY(-1px);
                filter: brightness(1.06);
            }

            button:disabled,
            button[disabled] {
                background: #334155 !important;
                color: #94a3b8 !important;
                box-shadow: none !important;
                opacity: 0.75 !important;
            }

            [data-testid="stSpinner"] {
                color: #c4b5fd !important;
            }

            code {
                color: #c4b5fd !important;
                background: #111827 !important;
                border: 1px solid rgba(148,163,184,0.22) !important;
                border-radius: 0.7rem !important;
            }
        </style>  

                """
            ,unsafe_allow_html=True)
