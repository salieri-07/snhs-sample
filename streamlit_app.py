import streamlit as st

st.title("ㅇㅅㅎ임")
st.info("뭘 보노")
st.write("알라라라라라랄ㄹㄻㄴㅇㅁㄴㅇ")
st.markdown("---") 

age = st.number_input("나이가 몇이노", min_value=0, max_value=120, step=1)

if(age<=19 and age>=17):
    st.write("공부나 해라.")
    st.image("https://image.yes24.com/momo/TopCate88/MidCate08/8777166.jpg", use_container_width=True)

if(age>19):
    st.write("만수무강 하세요.")
    st.image("https://cdn.imweb.me/upload/S202112291accec1828d10/c5544d56fee70.png", use_container_width=True)


st.markdown("---") 


