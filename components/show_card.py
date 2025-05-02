import streamlit as st

valores_map = {
    "A": "ace", "K": "king", "Q": "queen", "J": "jack", "T": "10",
    "9": "9", "8": "8", "7": "7", "6": "6", "5": "5", "4": "4", "3": "3", "2": "2"
}
naipes_map = {
    "s": "spades",
    "h": "hearts",
    "d": "diamonds",
    "c": "clubs"
}

def mostrar_carta(codigo, tamanho=100):
    """
    Exibe imagem da carta no formato 'As', 'Td', etc.
    """
    if len(codigo) != 2:
        st.error(f"Código inválido de carta: {codigo}")
        return

    valor, naipe = codigo[0], codigo[1]
    valor_extenso = valores_map.get(valor.upper())
    naipe_extenso = naipes_map.get(naipe.lower())

    if not valor_extenso or not naipe_extenso:
        st.error(f"Código de carta inválido: {codigo}")
        return

    nome_arquivo = f"{valor_extenso}_of_{naipe_extenso}.png"
    caminho = f"assets/{nome_arquivo}"
    st.image(caminho, width=tamanho)
