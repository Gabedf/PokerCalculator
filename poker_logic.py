from treys import Card, Deck, Evaluator

def simular_probabilidades(mao_jogador, flop=None, n_oponentes=1, n_simulacoes=1000):
    """
    Simula múltiplas rodadas de poker para estimar a chance de vitória
    e empate da mão do jogador contra adversários aleatórios.

    Parâmetros:
    - mao_jogador: lista com 2 cartas no formato Treys (inteiros)
    - flop: lista de 0 a 5 cartas comunitárias já conhecidas (opcional)
    - n_oponentes: número de oponentes restantes na mão
    - n_simulacoes: quantas simulações aleatórias serão feitas

    Retorna:
    - (prob_vitoria, prob_empate): valores entre 0 e 1
    """

    vitorias = 0
    empates = 0
    evaluator = Evaluator()

    for _ in range(n_simulacoes):
        deck = Deck()

        # Remover cartas do jogador do baralho
        for carta in mao_jogador:
            if carta in deck.cards:
                deck.cards.remove(carta)

        # Adicionar flop se existir
        cartas_comunitarias = []
        if flop:
            for carta in flop:
                if carta in deck.cards:
                    deck.cards.remove(carta)
                cartas_comunitarias.append(carta)

        # Comprar mãos para oponentes
        oponentes_maos = []
        for _ in range(n_oponentes):
            mao_oponente = [deck.draw(1)[0], deck.draw(1)[0]]
            oponentes_maos.append(mao_oponente)

        # Completar mesa com 5 cartas totais
        while len(cartas_comunitarias) < 5:
            cartas_comunitarias.append(deck.draw(1)[0])

        # Montar mão total
        total_cartas = mao_jogador + cartas_comunitarias

        # 🔐 Proteção total contra falhas
        if not all(isinstance(c, int) for c in total_cartas):
            raise ValueError(f"Cartas inválidas detectadas: {total_cartas}")

        if len(total_cartas) != 7:
            raise ValueError(
                f"Erro crítico: esperado 7 cartas (2 jogador + 5 mesa), recebeu {len(total_cartas)}.\n"
                f"Jogador: {mao_jogador}\nMesa: {cartas_comunitarias}"
            )

        # Avaliar mão do jogador
        rank_jogador = evaluator.evaluate(mao_jogador, cartas_comunitarias)

        venceu = True
        empate = False

        for mao_oponente in oponentes_maos:
            rank_oponente = evaluator.evaluate(mao_oponente, cartas_comunitarias)

            if rank_oponente < rank_jogador:
                venceu = False
                break
            elif rank_oponente == rank_jogador:
                empate = True

        if venceu:
            vitorias += 1
        elif empate:
            empates += 1

    return vitorias / n_simulacoes, empates / n_simulacoes
