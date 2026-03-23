import streamlit as st
import PyPDF2

st.set_page_config(page_title="AI CV Analyzer", page_icon="📄")

st.title("📄 Yapay Zeka Destekli Özgeçmiş Analiz Aracı ve Kariyer Danışmanı")
st.write("CV'ni yükle, sistem içeriğini analiz ederek güçlü yönlerini, eksiklerini ve sana uygun kariyer alanlarını belirlesin. 👇")

uploaded_file = st.file_uploader("CV yükle (PDF)", type=["pdf"])

if uploaded_file is not None:
    pdf = PyPDF2.PdfReader(uploaded_file)

    text = ""
    for page in pdf.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text

    text_lower = text.lower()

    # 🎯 MESLEK TAHMİNİ
    meslek = "genel"

    if "engineer" in text_lower or "mühendis" in text_lower:
        meslek = "mühendis"
    elif "software" in text_lower or "developer" in text_lower or "yazılım" in text_lower:
        meslek = "yazılım"
    elif "business" in text_lower or "işletme" in text_lower or "management" in text_lower:
        meslek = "işletme"
    elif "design" in text_lower or "designer" in text_lower or "tasarım" in text_lower:
        meslek = "tasarım"

    st.write(f"🧾 Tespit edilen alan: **{meslek.upper()}**")

    # 📊 GENEL ANALİZ
    st.subheader("📊 CV Analizi")
    st.write(f"📄 CV uzunluğu: {len(text)} karakter")

    # 🤖 AKILLI ANALİZ
    st.subheader("🤖 Yapay Zeka Tespitleri")

    if meslek in ["yazılım", "mühendis"]:
        if "python" not in text_lower:
            st.warning("Teknik becerilerini artırman önerilir.")
        if "project" not in text_lower and "proje" not in text_lower:
            st.warning("Proje deneyimi eklemelisin.")

    elif meslek == "işletme":
        if "management" not in text_lower and "yönetim" not in text_lower:
            st.warning("Yönetim becerilerini vurgulamalısın.")
        if "communication" not in text_lower and "iletişim" not in text_lower:
            st.warning("İletişim becerilerini eklemelisin.")

    elif meslek == "tasarım":
        if "portfolio" not in text_lower:
            st.warning("Portfolyo eklemen önemli.")
        if "design" not in text_lower:
            st.warning("Tasarım araçlarını belirtmelisin.")

    else:
        st.info("Genel analiz modu kullanıldı.")

    # 🧠 DETAYLI ANALİZ
    st.subheader("🧠 Detaylı Analiz")

    guclu = []
    zayif = []
    alan = []

    # 💪 Güçlü yönler
    if "python" in text_lower:
        guclu.append("Python bilgisi")
    if "project" in text_lower or "proje" in text_lower:
        guclu.append("Proje deneyimi")
    if "github" in text_lower:
        guclu.append("GitHub kullanımı")
    if "machine learning" in text_lower or "yapay zeka" in text_lower:
        guclu.append("Yapay zeka bilgisi")

    # ⚠️ Zayıf yönler
    if "intern" not in text_lower and "staj" not in text_lower:
        zayif.append("Staj deneyimi eksik")
    if "english" not in text_lower and "ingilizce" not in text_lower:
        zayif.append("İngilizce seviyesi belirtilmemiş")
    if "github" not in text_lower:
        zayif.append("GitHub profili eksik")

    # 🎯 Kariyer alanı
    if meslek == "yazılım":
        alan.append("Yazılım Geliştirme")
    elif meslek == "mühendis":
        alan.append("Mühendislik")
    elif meslek == "işletme":
        alan.append("İşletme / Yönetim")
    elif meslek == "tasarım":
        alan.append("Tasarım")
    else:
        alan.append("Genel kariyer alanları")

    # 💪 Güçlü yönler
    st.subheader("💪 Güçlü Yönler")
    if guclu:
        for g in guclu:
            st.success(g)
    else:
        st.write("Belirgin güçlü yön bulunamadı")

    # ⚠️ Zayıf yönler
    st.subheader("⚠️ Geliştirilmesi Gerekenler")
    if zayif:
        for z in zayif:
            st.warning(z)
    else:
        st.write("Zayıf yön tespit edilmedi")

    # 🎯 Alan
    st.subheader("🎯 Uygun Kariyer Alanları")
    for a in alan:
        st.info(a)

    # 📌 GENEL YORUM (FIXED)
    st.subheader("📌 Genel Yorum")

    if len(guclu) >= len(zayif) + 2:
        st.success("CV'in çok güçlü görünüyor, bu şekilde devam et!")
    elif len(guclu) >= len(zayif):
        st.info("CV'in iyi durumda, birkaç geliştirme ile daha güçlü olabilir.")
    else:
        st.warning("CV'ni geliştirmen gerekiyor, eksik alanlara odaklanmalısın.")

    # 🚀 ÖNERİLER
    st.subheader("🚀 Kariyer Önerileri")

    st.write("✔ GitHub projelerini artır")
    st.write("✔ En az 2 proje ekle")
    st.write("✔ İngilizce CV hazırla")
    st.write("✔ Teknik becerilerini net yaz")

    # 📏 UZUNLUK
    if len(text) < 1000:
        st.error("CV çok kısa, daha fazla detay eklemelisin.")
    else:
        st.success("CV uzunluğu iyi seviyede.")

    st.markdown("---")
    st.caption("© 2026 AI CV Analyzer | Emine")

else:
    st.info("Analiz için bir CV yükle.")