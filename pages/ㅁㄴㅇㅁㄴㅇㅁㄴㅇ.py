import streamlit as st
from openai import OpenAI

# 페이지 기본 설정
st.set_page_config(page_title="나이별 조언 GPT", page_icon="🤖", layout="centered")

# 헤더
st.title("🤖 나이별 조언 + GPT 응답 앱")
st.info("👀 뭐 보니? 이왕 온 김에 작성해!")

st.markdown("---")

# 사용자 입력
name = st.text_input("📝 이름을 입력하세요", placeholder="예: 철수")

age = st.number_input("🎂 나이를 입력하세요", min_value=0, step=1)

# 나이별 조건 출력
if name:
    if 17 <= age <= 19:
        st.warning(f"📚 {name}님, 공부나 열심히 하세요!")
        st.link_button("📺 도움이 될 영상", 'https://youtu.be/HN4entAhwNc?si=JaZ_RJmCGJX6mBQq')
        st.image("https://image.yes24.com/momo/TopCate60/MidCate10/5993229.jpg", use_container_width=True)

    elif 20 <= age <= 120:
        st.success(f"🎉 {name}님, 만수무강 하세요!")
        st.link_button("📺 도움이 될 영상", 'https://youtu.be/bwAcu7YGlFA?si=vpHyHTet7NUV-6RQ')
        st.image("https://cdn.imweb.me/upload/S202112291accec1828d10/c5544d56fee70.png", use_container_width=True)
        st.balloons()

    elif age > 120:
        st.error(f"👻 {name}님… 가실 나이입니다. 이제 놓아드릴게요.")

st.markdown("---")

# GPT-4 응답 받기
st.subheader("💬 GPT-4에게 물어보기")

user_api_key = st.text_input("🔑 OpenAI API 키를 입력하세요", type="password")

prompt = st.text_area("✍️ GPT에게 물어볼 내용을 작성하세요", placeholder="예: 10살 아이가 이해할 수 있도록 블랙홀 설명해줘")

# 응답 요청
if user_api_key and prompt:
    try:
        client = OpenAI(api_key=user_api_key)

        with st.spinner("GPT가 답변을 생성 중입니다..."):
            completion = client.chat.completions.create(
                model="gpt-4o",
                messages=[{"role": "user", "content": prompt}]
            )

        st.success("✅ GPT의 답변:")
        st.write(completion.choices[0].message.content)

    except Exception as e:
        st.error(f"❌ 에러 발생: {e}")

# 푸터
st.markdown("---")
st.caption("🧠 Made with ❤️ by Streamlit 초보 but 열정 가득한 개발자")