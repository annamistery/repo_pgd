import streamlit as st
from pgd_bot import PGD_Person_Mod, PGD_Pair

# ✅ Эта строка должна быть первой Streamlit-командой
st.set_page_config(page_title="Диагностика личности и пары", layout="wide")

# ============================
# 👤 Личная диагностика
# ============================

st.title("🧬 Личная диагностика по дате рождения")
st.markdown("Введите данные для расчёта личной диагностики:")

with st.form("personal_form"):
    name = st.text_input("Имя")
    date = st.text_input("Дата рождения (ДД.ММ.ГГГГ)")
    sex = st.radio("Пол", ["Ж", "М"])
    submit_personal = st.form_submit_button("Рассчитать личную диагностику")

if submit_personal:
    try:
        person = PGD_Person_Mod(name, date, sex)
        points = person.calculate_points()
        tasks = person.tasks()
        periods = person.periods_person()

        st.subheader(f"📌 Результаты для {name}")

        st.markdown("### 🔹 Точки личности")
        for group, values in points.items():
            st.markdown(f"**{group}**")
            for key, value in values.items():
                st.write(f"• {key}: `{value}`")

        st.markdown("### 🌟 Сверхзадачи")
        for key, value in tasks.items():
            st.write(f"• {key}: `{value}`")

        st.markdown("### 🧭 Бизнес-периоды")
        for key, value in periods["Бизнес периоды"].items():
            st.write(f"• {key}: `{value}`")

    except Exception as e:
        st.error(f"Ошибка в личной диагностике: {e}")

# ============================
# 👨‍👩‍👧‍👦 Диагностика пары
# ============================

st.title("❤️ Диагностика пары")
st.markdown("Введите данные для расчёта совместимости пары:")

with st.form("pair_form"):
    name1 = st.text_input("Имя первого человека")
    date1 = st.text_input("Дата рождения первого (ДД.ММ.ГГГГ)")
    name2 = st.text_input("Имя второго человека")
    date2 = st.text_input("Дата рождения второго (ДД.ММ.ГГГГ)")
    submit_pair = st.form_submit_button("Рассчитать диагностику пары")

if submit_pair:
    try:
        pair = PGD_Pair(name1, date1, name2, date2)
        points = pair.main_pair()
        tasks = pair.tasks()
        periods = pair.periods_pair()
        partner_tasks = pair.tasks_business()

        st.subheader(f"📌 Результаты для пары: {name1} и {name2}")

        st.markdown("### 🔹 Точки пары")
        for group, values in points.items():
            st.markdown(f"**{group}**")
            for key, value in values.items():
                st.write(f"• {key}: `{value}`")

        st.markdown("### 🌟 Сверхзадачи")
        for key, value in tasks["Сверхзадачи"].items():
            st.write(f"• {key}: `{value}`")

        st.markdown("### 🧭 Бизнес-периоды")
        for key, value in periods["Бизнес периоды"].items():
            st.write(f"• {key}: `{value}`")

        st.markdown("### 🔧 Задачи партнёров в паре")
        for key, value in partner_tasks.items():
            st.write(f"• {key}: `{value}`")

    except Exception as e:
        st.error(f"Ошибка в диагностике пары: {e}")
