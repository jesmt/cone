import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="Laboratório de Cones", layout="wide")

st.title("📐 Laboratório Interativo: Projeto de Filtros Cônicos")

# Colunas para organizar a tela: Vídeo à esquerda, Simulador à direita
col1, col2 = st.columns([1.5, 1])

with col1:
    st.subheader("📺 A Aula: Geometria do Cone")
    # Aqui você hospedaria seu vídeo finalizado no YouTube/Vimeo ou local
    #st.video("seu_video_editado_no_capcut.mp4") 
    
    st.info("""
    **O que aprendemos nesta aula:**
    1. Como a Geometria Espacial (Cone) se conecta com a Plana (Setor).
    2. A relação de Pitágoras entre $h, r$ e $g$.
    3. Como calcular o ângulo de corte para fabricação real.
    """)

with col2:
    st.subheader("🛠️ Simulador de Fabricação")
    st.write("Insira as dimensões desejadas para o filtro:")
    
    # Inputs do usuário
    raio_base = st.slider("Raio da Base (r) em cm", 5, 100, 30)
    altura = st.slider("Altura do Cone (h) em cm", 5, 100, 40)
    
    # Cálculos Matemáticos (O que você ensinou no vídeo)
    geratriz = np.sqrt(raio_base**2 + altura**2)
    comprimento_arco = 2 * np.pi * raio_base
    angulo_setor_rad = comprimento_arco / geratriz
    angulo_setor_graus = np.degrees(angulo_setor_rad)
    area_lateral = np.pi * raio_base * geratriz
    
    # Exibição dos resultados
    st.success(f"**Geratriz (g):** {geratriz:.2f} cm")
    st.success(f"**Ângulo de Corte:** {angulo_setor_graus:.2f}°")
    st.success(f"**Área de Chapa Necessária:** {area_lateral:.2f} cm²")

    # Visualização 2D do Molde (Matplotlib)
    st.write("### Molde para Corte (Planificação)")
    fig, ax = plt.subplots(figsize=(4,4))
    
    # Desenha o setor circular
    theta = np.linspace(0, angulo_setor_rad, 100)
    x = geratriz * np.cos(theta)
    y = geratriz * np.sin(theta)
    
    ax.plot([0, x[0]], [0, y[0]], color='red') # Linha inicial
    ax.plot(x, y, color='blue')               # Arco
    ax.plot([0, x[-1]], [0, y[-1]], color='red') # Linha final
    ax.fill_between(x, y, color='skyblue', alpha=0.3)
    
    ax.set_aspect('equal')
    plt.axis('off')
    st.pyplot(fig)
