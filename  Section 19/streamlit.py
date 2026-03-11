# import streamlit as st
# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt
# st.title("Hello Sanjeev")
# st.header("Hello Sanjeev")
# st.subheader("Hello Sanjeev")
# st.text("Hello, I am good.")
# st.write("this is sanjeev")

# st.markdown("**Bold Text**")

# import pandas as pd

# df = pd.DataFrame({
#     "First Column":[1,2,3],
#     "Second Column":[4,5,6]
# })

# st.write(df)

# chart_data = pd.DataFrame(
#     np.random.randn(20,3),
#     columns=["A","B","C"]
# )
# st.line_chart(chart_data)

# data = np.random.randn(20,3)
# st.line_chart(data)
# st.area_chart(data)
# st.bar_chart(data)


# name = st.text_input("enter your name")
# if name: 
#     st.write("hello", name)
    
    
# age = st.slider("Select your age",0,100,25)
# st.write("your age is",age)


# options = ["python", "java", "C++","javascript"]

# choice = st.selectbox("choose your fav. programming language",options)

# st.write("You selected",choice)

# uploaded_file = st.file_uploader(
#     "Chose a CSV file",type="CSV"
# )

# if uploaded_file is not None:
#     df = pd.read_csv(uploaded_file)
#     st.write(df)
    
# fig, ax = plt.subplots()
# ax.plot([1,2,3], [4,5,6])

# st.pyplot()

# if st.checkbox("Show Data"):
#     st.write(df)

# choice = st.radio("Choose Option",["Option 1","Option 2"])


# if st.checkbox("Show Data", key="data_checkbox"):
#     st.write(data)
    
# if st.button("Click Me"):
#     st.write("Button Clicked")
    
    
# col1,col2 = st.columns(2)

# with col1:
#     st.write("Column 1")
# with col2:
#     st.write("Column 2")
    
    
# st.sidebar.title("Menu")
# option = st.sidebar.selectbox(
#     "choose model",["model 1","model 2"]
# )

# with st.expander("See Explanation"):
#     st.write("Detailed information")
    
# if "count" not in st.session_state:
#     st.session_state.count = 0

# if st.button("Increment"):
#     st.session_state.count += 1
# st.write(st.session_state.count)

