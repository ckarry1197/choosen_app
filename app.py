import streamlit as st
import choosen
import choosen_2

st.set_page_config(page_title="學餐推薦系統",layout="centered")
st.title("學餐推薦系統")

page = st.selectbox("請選擇功能", ["餐廳推薦", "預算推薦"])

if page == "餐廳推薦":
    st.header("隨機推薦一間餐廳")

    try:
        restaurants = choosen.restaurant_load()
        categories = list(restaurants.keys())

        selected_category = st.selectbox("請選擇分類",categories)

        if st.button("推薦我！", key="random"):
            restaurant = choosen.recommend_restaurant(restaurants, selected_category)
            if restaurant:
                st.success(f"分類：{selected_category}")
                st.markdown(f"🍽️ 推薦店家：**{restaurant['餐廳名稱']}**\n\n📍 位置：{restaurant['餐廳位置']}")
            else:
                st.warning("這個分類下沒有餐廳資料。")
    except FileNotFoundError:
        st.error("找不到 restaurant.json，請確認檔案是否放在資料夾中。")


elif page == "預算推薦":
    st.header("根據預算推薦店家")

    categories = list(choosen_2.restaurants.keys())
    selected_categories = st.multiselect("請選擇想吃的分類", categories)
    budget = st.number_input("請輸入預算（元）", min_value=0, step=10)

    if st.button("找店家！", key="budget"):
        if not selected_categories:
            st.warning("⚠️ 請至少選擇一個分類")
        else:
            result = choosen_2.select_lunch(budget, selected_categories)
            if result:
                st.success(result)
            else:
                st.warning(f"找不到符合預算的店家，試試提高預算或換分類 😢")
