# import streamlit as st

# st.title("🎈변해라")
# st.write(
#     '안녕하세요, 저는 뭡니까'
# )
# st.info(
#     '링딩동 링딩동 링디기링디기 링딩동'
# )
# st.markdown(
#     '**나는야 배포를 하는 배포가 큰 사람**'
# )
# st.latex(
#     r'F=ma'
# )
# st.image('https://media.istockphoto.com/id/1324356458/ko/%EB%B2%A1%ED%84%B0/%EA%B7%B8%EB%A6%BC-%EC%95%84%EC%9D%B4%EC%BD%98%EC%9E%85%EB%8B%88%EB%8B%A4-%EC%82%AC%EC%A7%84-%ED%94%84%EB%A0%88%EC%9E%84-%EA%B8%B0%ED%98%B8-%EA%B0%80%EB%A1%9C-%EA%B8%B0%ED%98%B8%EC%9E%85%EB%8B%88%EB%8B%A4-%EC%82%AC%EC%A7%84-%EA%B0%A4%EB%9F%AC%EB%A6%AC-%EB%A1%9C%EA%B3%A0-%EC%9B%B9-%EC%9D%B8%ED%84%B0%ED%8E%98%EC%9D%B4%EC%8A%A4-%EB%B0%8F-%EC%9D%91%EC%9A%A9-%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%A8-%EB%B2%84%ED%8A%BC%EC%9E%85%EB%8B%88%EB%8B%A4-%EB%B2%A1%ED%84%B0-%EC%9D%BC%EB%9F%AC%EC%8A%A4%ED%8A%B8-%EC%9D%B4%EB%AF%B8%EC%A7%80%EC%9E%85%EB%8B%88%EB%8B%A4.jpg?s=612x612&w=0&k=20&c=e-sF2jw4_4cqj8QF3A9uztSb9880xiox6bMhYhHbtV4=')
# st.image('https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExNGhheDNmam1ybWcwODgzaXZ6dmg5ZGVqeGdwc2syNnA2aHFzNTI5YSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/bN4Gf6GEs9OtW/giphy.gif')
# st.code('import streamlit as st\nst.title("🎈변해라")',language='python')

# col1, col2 = st.columns(2)
# with col1:
#     st.write("청기")
# with col2:
#     st.write("백기")
# nickname=st.text_input('닉네임을 입력해주세요')
# if st.button('결정'):
#     st.write('닉네임을',nickname,'으로 하신걸 보니 당신의 본명은 김알잘딱깔센입니다.')

# import openai

# user_api_key=st.text_input('키를 입력해주세요.')

# from openai import OpenAI

# client = OpenAI(api_key = user_api_key)
# prompt = st.text_input("프롬프트를 입력해주세요.")

# completion = client.chat.completions.create(
#     model="gpt-3.5-turbo",
#     messages=[{"role": "user", "content": prompt}]
# )
# st.markdown("### 💡 GPT의 답변:")
# st.write(completion.choices[0].message.content)

import streamlit as st
from openai import OpenAI

# --- 페이지 설정 ---
st.set_page_config(page_title="변해라 App", page_icon="🎈")

st.title("🎈 변해라 App")

# --- 탭 구성 ---
tab1, tab2, tab3, tab4 = st.tabs(["🏠 소개", "🖼️ 이미지 & 코드", "🎭 닉네임", "🤖 GPT 사용"])

# --- 탭 1: 소개 ---
with tab1:
    st.subheader("👋 안녕하세요, 저는 뭡니까")
    st.info("🔔 링딩동 링딩동 링디기링디기 링딩동")
    st.markdown("**💼 나는야 배포를 하는 배포가 큰 사람**")
    st.latex(r'F = ma')

# --- 탭 2: 이미지 & 코드 ---
with tab2:
    st.image(
        "https://media.istockphoto.com/id/1324356458/ko/%EB%B2%A1%ED%84%B0/%EA%B7%B8%EB%A6%BC-%EC%95%84%EC%9D%B4%EC%BD%98%EC%9E%85%EB%8B%88%EB%8B%A4-%EC%82%AC%EC%A7%84-%ED%94%84%EB%A0%88%EC%9E%84-%EA%B8%B0%ED%98%B8-%EA%B0%80%EB%A1%9C-%EA%B8%B0%ED%98%B8%EC%9E%85%EB%8B%88%EB%8B%A4-%EC%82%AC%EC%A7%84-%EA%B0%A4%EB%9F%AC%EB%A6%AC-%EB%A1%9C%EA%B3%A0-%EC%9B%B9-%EC%9D%B8%ED%84%B0%ED%8E%98%EC%9D%B4%EC%8A%A4-%EB%B0%8F-%EC%9D%91%EC%9A%A9-%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%A8-%EB%B2%84%ED%8A%BC%EC%9E%85%EB%8B%88%EB%8B%A4-%EB%B2%A1%ED%84%B0-%EC%9D%BC%EB%9F%AC%EC%8A%A4%ED%8A%B8-%EC%9D%B4%EB%AF%B8%EC%A7%80%EC%9E%85%EB%8B%88%EB%8B%A4.jpg?s=612x612&w=0&k=20&c=e-sF2jw4_4cqj8QF3A9uztSb9880xiox6bMhYhHbtV4="
    )
    st.image(
        "https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExNGhheDNmam1ybWcwODgzaXZ6dmg5ZGVqeGdwc2syNnA2aHFzNTI5YSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/bN4Gf6GEs9OtW/giphy.gif"
    )

    with st.expander("🧑‍💻 코드 보기"):
        st.code('import streamlit as st\nst.title("🎈변해라")', language='python')

    # 컬럼 배치
    col1, col2 = st.columns(2)
    with col1:
        st.write("🟥 청기")
    with col2:
        st.write("⬜ 백기")

# --- 탭 3: 닉네임 입력 ---
with tab3:
    st.markdown("## 🧑 닉네임 설정")
    nickname = st.text_input("닉네임을 입력해주세요")

    if st.button("결정", key="nickname_button"):
        st.success(f"닉네임을 **{nickname}**(으)로 하신 걸 보니, 당신의 본명은 **김알잘딱깔센**입니다!")

# --- 탭 4: OpenAI GPT 연동 ---
with tab4:
    st.markdown("## 🔐 OpenAI GPT 사용해 보기")

    user_api_key = st.secrets['openai']['api_key']
    prompt = st.text_input("✍️ 프롬프트를 입력해주세요")

    if user_api_key and prompt:
        client = OpenAI(api_key=user_api_key)
        try:
            completion = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt}]
            )
            st.markdown("### 💡 GPT의 답변:")
            st.write(completion.choices[0].message.content)
        except Exception as e:
            st.error(f"⚠️ 에러 발생: {e}")
