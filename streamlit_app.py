import streamlit as st

# =====================================
# KONFIGURASI HALAMAN
# =====================================

st.set_page_config(
    page_title="Kalkulator Indeks Kualitas Air",
    page_icon="💧",
    layout="centered"
)

# =====================================
# JUDUL
# =====================================

st.title("💧 Kalkulator Indeks Kualitas Air")

st.write(
    "Aplikasi ini digunakan untuk menghitung indeks kualitas air berdasarkan parameter BOD, COD, dan suhu."
)

st.divider()

# =====================================
# INPUT USER
# =====================================

st.subheader("📥 Input Parameter")

bod = st.number_input(
    "Masukkan nilai BOD (mg/L)",
    min_value=0.0,
    step=0.1
)

cod = st.number_input(
    "Masukkan nilai COD (mg/L)",
    min_value=0.0,
    step=0.1
)

suhu = st.number_input(
    "Masukkan suhu air (°C)",
    min_value=0.0,
    step=0.1
)

st.divider()

# =====================================
# FUNGSI PENILAIAN
# =====================================

def skor_bod(bod):
    if bod <= 2:
        return 100
    elif bod <= 6:
        return 80
    elif bod <= 12:
        return 60
    elif bod <= 20:
        return 40
    else:
        return 20


def skor_cod(cod):
    if cod <= 10:
        return 100
    elif cod <= 25:
        return 80
    elif cod <= 50:
        return 60
    elif cod <= 100:
        return 40
    else:
        return 20


def skor_suhu(suhu):
    if 25 <= suhu <= 30:
        return 100
    elif 20 <= suhu < 25 or 30 < suhu <= 35:
        return 80
    elif 15 <= suhu < 20 or 35 < suhu <= 40:
        return 60
    else:
        return 40

# =====================================
# TOMBOL HITUNG
# =====================================

if st.button("🔍 Hitung"):

    nilai_bod = skor_bod(bod)
    nilai_cod = skor_cod(cod)
    nilai_suhu = skor_suhu(suhu)

    indeks = (nilai_bod + nilai_cod + nilai_suhu) / 3

    # =====================================
    # KATEGORI
    # =====================================

    if indeks >= 80:
        kategori = "Sangat Baik"
        warna = "green"

    elif indeks >= 60:
        kategori = "Baik"
        warna = "blue"

    elif indeks >= 40:
        kategori = "Tercemar Ringan"
        warna = "orange"

    else:
        kategori = "Tercemar Berat"
        warna = "red"

    # =====================================
    # OUTPUT
    # =====================================

    st.subheader("📊 Hasil")

    st.metric(
        "Indeks Kualitas Air",
        f"{indeks:.2f}"
    )

    st.markdown(
        f"<h2 style='color:{warna};'>Kategori: {kategori}</h2>",
        unsafe_allow_html=True
    )

    st.divider()

    # =====================================
    # DETAIL PARAMETER
    # =====================================

    st.subheader("📋 Detail Parameter")

    st.write(f"BOD : {bod} mg/L → Skor {nilai_bod}")
    st.write(f"COD : {cod} mg/L → Skor {nilai_cod}")
    st.write(f"Suhu : {suhu} °C → Skor {nilai_suhu}")

    st.divider()

    # =====================================
    # ANALISIS
    # =====================================

    st.subheader("🧪 Analisis")

    if kategori == "Sangat Baik":
        st.success(
            "Kualitas air sangat baik berdasarkan parameter yang diuji."
        )

    elif kategori == "Baik":
        st.info(
            "Kualitas air masih tergolong baik dan aman."
        )

    elif kategori == "Tercemar Ringan":
        st.warning(
            "Air mulai mengalami pencemaran ringan."
        )

    else:
        st.error(
            "Air tergolong tercemar berat dan perlu penanganan."
        )
