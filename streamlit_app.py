import streamlit as st

st.title("ㅇㅅㅎ")
st.info("뭘 봐")
st.write("이름과 나이 좀")
st.markdown("---") 

name=st.text_input("이름이 뭐노")

age = st.number_input("나이가 몇이노", min_value=0)


if(age<=19 and age>=17):
    st.write(name+"공부나 해라.")
    st.link_button("도움될 영상", 'https://youtu.be/HN4entAhwNc?si=JaZ_RJmCGJX6mBQq')
    st.image("https://image.yes24.com/momo/TopCate60/MidCate10/5993229.jpg", use_container_width=True)

if(age>19):
    st.write(name+"님 만수무강 하세요.")
    st.link_button("도움될 영상", 'https://youtu.be/bwAcu7YGlFA?si=vpHyHTet7NUV-6RQ')
    st.image("https://cdn.imweb.me/upload/S202112291accec1828d10/c5544d56fee70.png", use_container_width=True)
    st.balloons()

if(age>120):
    st.write(name+"님 가실 나이 입니다다.")

st.markdown("---") 






