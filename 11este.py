import streamlit as st

st.set_page_config(page_title="Vigilante Samambaia", page_icon="📍")

st.title("📍 Vigilante Samambaia")
st.subheader("Rua Vitor Meirelles")

tab1, tab2 = st.tabs(["Painel Inicial", "Nova Ocorrência"])

with tab1:
    st.button("➕ REGISTRAR NOVA OCORRÊNCIA", use_container_width=True)
    st.write("### Últimos relatos na rua:")
    st.info("💡 Iluminação: Lâmpada poste 42 (Pendente)")
    st.success("🛡️ Segurança: Veículo suspeito (Verificado)")
    st.image("https://docs.streamlit.io/images/tutorials/map.png", caption="Mapa de Alertas")

with tab2:
    st.header("Nova Ocorrência")
    tipo = st.selectbox("1. Tipo de Incidente", ["Segurança", "Infraestrutura", "Limpeza", "Outros"])
    desc = st.text_area("2. Descrição do Problema")
    loc = st.text_input("3. Localização (GPS)", value="Rua Vitor Meirelles, nº ")
    foto = st.file_uploader("4. Evidência (Foto)", type=['jpg', 'png'])
    if st.button("ENVIAR PARA ASSOCIAÇÃO", type="primary"):
        st.success("Enviado!")
        
        
        #streamlit run 11este.py