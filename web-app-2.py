import streamlit as st
# Create tabs
tab1, tab2, tab3 = st.tabs(["Tab 1: Welcome", "Tab 2: Data", "Tab 3: Chart"])

# Content for Tab 1
with tab1:
    st.header("Welcome Tab")
    st.write("This is the first tab, where you can include introductory content.")

# Content for Tab 2
with tab2:
    st.header("Data Tab")
    st.write("Upload and display data here!")
    uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])
    if uploaded_file:
        import pandas as pd
        data = pd.read_csv(uploaded_file)
        st.write("Preview of uploaded data:", data.head())

# Content for Tab 3
with tab3:
    st.header("Chart Tab")
    import matplotlib.pyplot as plt
    import numpy as np
    x = np.linspace(0, 10, 100)
    y = np.sin(x)
    fig, ax = plt.subplots()
    ax.plot(x, y)
    st.pyplot(fig)
