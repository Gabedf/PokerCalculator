import streamlit as st

# Mapas de conversão para os códigos do Treys
valores = {
    "A": "A", "K": "K", "Q": "Q", "J": "J", "10": "T",
    "9": "9", "8": "8", "7": "7", "6": "6", "5": "5",
    "4": "4", "3": "3", "2": "2"
}
naipes = {
    "♠ Espadas": "s",
    "♥ Copas": "h",
    "♦ Ouros": "d",
    "♣ Paus": "c"
}

def selecionar_carta(label="Carta"):
    col1, col2 = st.columns(2)

    with col1:
        valor = st.selectbox(
            f"Valor da {label}",
            options=["-"] + list(valores.keys()),
            key=f"valor_{label}"
        )

    with col2:
        naipe = st.selectbox(
            f"Naipe da {label}",
            options=["-"] + list(naipes.keys()),
            key=f"naipe_{label}"
        )

    # Verifica se os dois foram escolhidos
    if valor == "-" or naipe == "-":
        return None  # ainda não selecionado

    return valores[valor] + naipes[naipe]
