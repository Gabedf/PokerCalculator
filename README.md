
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
</head>
<body>

<h1>🃏 Simulador de Poker com Streamlit</h1>

<p>
    Este projeto é um simulador interativo de Poker Texas Hold'em feito em Python com Streamlit.  
    Ele permite acompanhar a evolução da probabilidade de vitória a cada rodada: Pré-Flop, Flop, Turn e River.
</p>

<h2>🚀 Funcionalidades</h2>
<ul>
    <li>Escolha interativa das cartas (com selectbox)</li>
    <li>Simulação contra 1 a 8 oponentes</li>
    <li>Cálculo de probabilidade de vitória e empate</li>
    <li>Fluxo de jogo realista em rodadas (Flop, Turn, River)</li>
</ul>

<h2>📁 Estrutura do Projeto</h2>
<pre><code>poker_simulador/
├── app.py                 
├── poker_logic.py         
└── components/
    └── card_selector.py   
    └── show_card.py
</code></pre>

<h2>✅ Como usar</h2>
<ol>
    <li><strong>Clone o repositório:</strong>
        <pre><code>git clone https://github.com/seu-usuario/poker_simulador.git
cd poker_simulador</code></pre>
    </li>
    <li><strong>Instale as dependências:</strong>
        <pre><code>pip install -r requirements.txt</code></pre>
    </li>
    <li><strong>Execute o aplicativo:</strong>
        <pre><code>streamlit run app.py</code></pre>
    </li>
</ol>

<h2>🧠 Como funciona</h2>
<p>
    A simulação utiliza o pacote <code>treys</code> para avaliar a força das mãos de poker.  
    O algoritmo realiza simulações Monte Carlo para estimar a chance de vitória contra o número informado de oponentes.
</p>

<h2>📌 Requisitos</h2>
<ul>
    <li>Python 3.7 ou superior</li>
    <li>streamlit</li>
    <li>treys</li>
</ul>

<h2>👤 Autor</h2>
<p>
    Desenvolvido por <strong>Gabriel Fonseca</strong>.  
    Sinta-se livre para contribuir, adaptar ou usar esse projeto como base para algo maior. 🎲
</p>

</body>
</html>
