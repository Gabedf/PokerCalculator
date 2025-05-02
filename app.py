import streamlit as st

st.set_page_config(page_title="Poker Interativo", page_icon="🃏")
st.markdown("""
    <style>
        .stApp {
            background-color: #f5f5f5;
            color: #111111;
        }
        img {
            transition: transform 0.1s ease, box-shadow 0.2s ease;
        }
        img:hover {
            transform: scale(1.05);
            box-shadow: 0 0 10px rgba(0,0,0,0.3);
        }
    </style>
""", unsafe_allow_html=True)

from treys import Card
from components.card_selector_img import selecionar_carta_por_imagem
from components.show_card import mostrar_carta
from poker_logic import simular_probabilidades
st.title("🃏 Simulador de Poker - Rodadas Interativas")

# === Inicialização do estado ===
if "fase" not in st.session_state:
    st.session_state.fase = "inicio"
if "mao" not in st.session_state:
    st.session_state.mao = []
if "flop" not in st.session_state:
    st.session_state.flop = []
if "turn" not in st.session_state:
    st.session_state.turn = []
if "river" not in st.session_state:
    st.session_state.river = []
if "n_oponentes" not in st.session_state:
    st.session_state.n_oponentes = 0
if "resultado_preflop" not in st.session_state:
    st.session_state.resultado_preflop = (0, 0)
if "resultado_flop" not in st.session_state:
    st.session_state.resultado_flop = (0, 0)
if "resultado_turn" not in st.session_state:
    st.session_state.resultado_turn = (0, 0)
if "resultado_river" not in st.session_state:
    st.session_state.resultado_river = (0, 0)

# === Fase: início ===
if st.session_state.fase == "inicio":
    st.header("1. Selecione suas Cartas")
    carta1 = selecionar_carta_por_imagem("Carta 1")
    carta2 = selecionar_carta_por_imagem("Carta 2")

    st.session_state.n_oponentes = st.slider("Número de Oponentes (Pré-Flop)", 1, 8, 4)

    if st.button("Começar Simulação (Pré-Flop)"):
        if carta1 and carta2:
            mao = [Card.new(carta1), Card.new(carta2)]
            st.session_state.mao = mao
            st.session_state.resultado_preflop = simular_probabilidades(
                mao, flop=None, n_oponentes=st.session_state.n_oponentes
            )
            st.session_state.fase = "mostrar_preflop"
        else:
            st.warning("Selecione as duas cartas do jogador para continuar.")

# === Mostrar resultado do pré-flop ===
elif st.session_state.fase == "mostrar_preflop":
    st.subheader("Cartas do Jogador")
    col1, col2 = st.columns(2)
    with col1:
        mostrar_carta(Card.int_to_str(st.session_state.mao[0]), tamanho=120)
    with col2:
        mostrar_carta(Card.int_to_str(st.session_state.mao[1]), tamanho=120)

    win, tie = st.session_state.resultado_preflop
    st.success(f"Pré-Flop — Vitória: {win*100:.2f}%, Empate: {tie*100:.2f}%")
    if st.button("Continuar para o Flop"):
        st.session_state.fase = "flop"

# === Fase: Flop ===
elif st.session_state.fase == "flop":
    st.header("2. Flop")
    flop1 = selecionar_carta_por_imagem("Flop 1")
    flop2 = selecionar_carta_por_imagem("Flop 2")
    flop3 = selecionar_carta_por_imagem("Flop 3")

    n_flop = st.slider("Jogadores ainda na mesa (Flop)", 0, st.session_state.n_oponentes, st.session_state.n_oponentes)

    if st.button("Calcular Probabilidade do Flop"):
        if flop1 and flop2 and flop3:
            flop = [Card.new(flop1), Card.new(flop2), Card.new(flop3)]
            st.session_state.flop = flop
            st.session_state.n_oponentes = n_flop
            st.session_state.resultado_flop = simular_probabilidades(
                st.session_state.mao, flop=flop, n_oponentes=n_flop
            )
            st.session_state.fase = "mostrar_flop"
        else:
            st.warning("Selecione todas as cartas do flop.")

# === Mostrar resultado do flop ===
elif st.session_state.fase == "mostrar_flop":
    st.subheader("Mesa - Flop")
    cols = st.columns(3)
    for i, carta in enumerate(st.session_state.flop):
        with cols[i]:
            mostrar_carta(Card.int_to_str(carta), tamanho=100)

    win, tie = st.session_state.resultado_flop
    st.success(f"Após o Flop — Vitória: {win*100:.2f}%, Empate: {tie*100:.2f}%")
    if st.button("Continuar para o Turn"):
        st.session_state.fase = "turn"

# === Fase: Turn ===
elif st.session_state.fase == "turn":
    st.header("3. Turn")
    turn_card = selecionar_carta_por_imagem("Turn")
    n_turn = st.slider("Jogadores ainda na mesa (Turn)", 0, st.session_state.n_oponentes, st.session_state.n_oponentes)

    if st.button("Calcular Probabilidade do Turn"):
        if turn_card:
            turn = [Card.new(turn_card)]
            st.session_state.turn = turn
            st.session_state.n_oponentes = n_turn
            st.session_state.resultado_turn = simular_probabilidades(
                st.session_state.mao,
                flop=st.session_state.flop + turn,
                n_oponentes=n_turn
            )
            st.session_state.fase = "mostrar_turn"
        else:
            st.warning("Selecione a carta do Turn.")

# === Mostrar resultado do turn ===
elif st.session_state.fase == "mostrar_turn":
    st.subheader("Mesa - Turn")
    cartas = st.session_state.flop + st.session_state.turn
    cols = st.columns(len(cartas))
    for i, carta in enumerate(cartas):
        with cols[i]:
            mostrar_carta(Card.int_to_str(carta), tamanho=100)

    win, tie = st.session_state.resultado_turn
    st.success(f"Após o Turn — Vitória: {win*100:.2f}%, Empate: {tie*100:.2f}%")
    if st.button("Continuar para o River"):
        st.session_state.fase = "river"

# === Fase: River ===
elif st.session_state.fase == "river":
    st.header("4. River")
    river_card = selecionar_carta_por_imagem("River")
    n_river = st.slider("Jogadores ainda na mesa (River)", 0, st.session_state.n_oponentes, st.session_state.n_oponentes)

    if st.button("Finalizar e Calcular Resultado"):
        if river_card:
            river = [Card.new(river_card)]
            st.session_state.river = river
            st.session_state.n_oponentes = n_river
            st.session_state.resultado_river = simular_probabilidades(
                st.session_state.mao,
                flop=st.session_state.flop + st.session_state.turn + river,
                n_oponentes=n_river
            )
            st.session_state.fase = "mostrar_river"
        else:
            st.warning("Selecione a carta do River.")

# === Mostrar resultado do river ===
elif st.session_state.fase == "mostrar_river":
    st.subheader("Mesa Completa")
    cartas = st.session_state.flop + st.session_state.turn + st.session_state.river
    cols = st.columns(len(cartas))
    for i, carta in enumerate(cartas):
        with cols[i]:
            mostrar_carta(Card.int_to_str(carta), tamanho=100)

    win, tie = st.session_state.resultado_river
    st.success(f"Após o River — Vitória: {win*100:.2f}%, Empate: {tie*100:.2f}%")
    if st.button("🔁 Reiniciar Simulação"):
        for key in list(st.session_state.keys()):
            del st.session_state[key]
        st.rerun()
