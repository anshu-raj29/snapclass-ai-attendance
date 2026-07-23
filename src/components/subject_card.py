import streamlit as st
def subject_card(name, code, section, stats=None, footer_callback=None):
    html = f"""
        <div style="background:linear-gradient(145deg, rgba(15,23,42,0.98), rgba(17,24,39,0.98)); border-left: 8px solid #EB459E; padding:25px; border-radius: 18px; border: 1px solid rgba(148,163,184,0.22); margin-bottom:20px; box-shadow:0 20px 48px rgba(0,0,0,0.28);">
        <h3 style="margin:0; color: #F8FAFC; font-size: 1.5rem ">{name}</h3>
        <p style="color:#CBD5E1; margin:10px 0;">Code : <span style="background:rgba(99,102,241,0.18); color:#C4B5FD; padding:2px 8px; border-radius:5px; border:1px solid rgba(196,181,253,0.20);">{code} </span> | Section : {section}</p>
        
        """
    
    if stats:
        html+= """
        <div style="display:flex; gap:8px; flex-wrap:wrap;">
        """
        for icon, label, value in stats:
            html+= f'<div style="background: rgba(236,72,153,0.12); color:#E5E7EB; padding:5px 12px; border-radius:12px; border:1px solid rgba(236,72,153,0.18); font-size:0.9rem">{icon} <b>{value}</b> {label} </div>'
        
        html+= "</div>"

    st.markdown(html, unsafe_allow_html=True)

    if footer_callback:
        footer_callback()
