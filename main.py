from flask import Flask, render_template_string

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Respostas Para Quase Tudo</title>
    <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;600;700&family=Orbitron:wght@400;500&display=swap" rel="stylesheet">
    <style>
        :root {
            --space-purple: #6a00f4;
            --neon-pink: #ff00aa;
            --electric-blue: #00d4ff;
            --galaxy-yellow: #ffcc00;
            --cosmic-orange: #ff6d00;
            --starlight: #f0f8ff;
            --deep-space: #0a0021;
        }

        body {
            font-family: 'Montserrat', sans-serif;
            background: radial-gradient(ellipse at center, var(--deep-space) 0%, #1a0038 100%);
            color: var(--starlight);
            margin: 0;
            padding: 0;
            min-height: 100vh;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            overflow-x: hidden;
            background-image: 
                radial-gradient(circle at 20% 30%, rgba(255, 0, 170, 0.1) 0%, transparent 20%),
                radial-gradient(circle at 80% 70%, rgba(0, 212, 255, 0.1) 0%, transparent 20%),
                radial-gradient(circle at 40% 60%, rgba(106, 0, 244, 0.1) 0%, transparent 20%);
        }

        .love-logo {
            position: absolute;
            top: 30px;
            left: 30px;
            font-family: 'Orbitron', sans-serif;
            font-size: 2.2rem;
            font-weight: 500;
            color: var(--electric-blue);
            display: flex;
            align-items: center;
            z-index: 10;
            text-shadow: 0 0 10px var(--electric-blue);
        }

        .love-logo .heart {
            color: var(--neon-pink);
            font-size: 1.8rem;
            margin: 0 8px;
            animation: heartbeat 1.8s infinite;
            text-shadow: 0 0 15px var(--neon-pink);
        }

        @keyframes heartbeat {
            0% { transform: scale(1); }
            25% { transform: scale(1.1); }
            50% { transform: scale(1); }
            75% { transform: scale(1.2); }
            100% { transform: scale(1); }
        }

        .main-container {
            background: rgba(10, 0, 33, 0.7);
            backdrop-filter: blur(12px);
            -webkit-backdrop-filter: blur(12px);
            border-radius: 20px;
            border: 1px solid var(--space-purple);
            box-shadow: 0 0 30px rgba(106, 0, 244, 0.5),
                        inset 0 0 20px rgba(0, 212, 255, 0.2);
            padding: 40px;
            width: 85%;
            max-width: 750px;
            margin: 30px;
            position: relative;
            overflow: hidden;
            transition: all 0.5s ease;
            z-index: 1;
        }

        .main-container:hover {
            transform: translateY(-5px);
            box-shadow: 0 0 40px rgba(106, 0, 244, 0.7),
                        inset 0 0 30px rgba(0, 212, 255, 0.3);
            border-color: var(--electric-blue);
        }

        h1 {
            font-family: 'Orbitron', sans-serif;
            font-size: 2.6rem;
            margin-bottom: 30px;
            font-weight: 500;
            text-align: center;
            background: linear-gradient(90deg, var(--neon-pink), var(--electric-blue), var(--galaxy-yellow));
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            letter-spacing: 1px;
            text-shadow: 0 0 10px rgba(255, 255, 255, 0.3);
            position: relative;
        }

        h1:after {
            content: '';
            display: block;
            width: 100px;
            height: 3px;
            background: linear-gradient(90deg, var(--neon-pink), var(--electric-blue));
            margin: 15px auto;
            border-radius: 3px;
        }

        .btn {
            background: linear-gradient(135deg, var(--space-purple) 0%, var(--neon-pink) 100%);
            color: white;
            border: none;
            padding: 16px 35px;
            font-size: 1.1rem;
            border-radius: 50px;
            cursor: pointer;
            margin: 20px auto;
            display: block;
            width: fit-content;
            transition: all 0.3s cubic-bezier(0.25, 0.8, 0.25, 1);
            box-shadow: 0 0 20px rgba(106, 0, 244, 0.5);
            text-decoration: none;
            font-weight: 600;
            letter-spacing: 1px;
            position: relative;
            overflow: hidden;
            z-index: 1;
            text-transform: uppercase;
            font-family: 'Orbitron', sans-serif;
        }

        .btn:before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: linear-gradient(135deg, var(--neon-pink) 0%, var(--electric-blue) 100%);
            z-index: -1;
            opacity: 0;
            transition: opacity 0.3s ease;
        }

        .btn:hover {
            transform: translateY(-3px);
            box-shadow: 0 0 30px rgba(255, 0, 170, 0.7);
        }

        .btn:hover:before {
            opacity: 1;
        }

        .content-box {
            max-height: 55vh;
            overflow-y: auto;
            padding: 20px;
            margin: 25px 0;
            border-radius: 12px;
            background: rgba(0, 0, 0, 0.3);
            border: 1px solid var(--electric-blue);
            scrollbar-width: thin;
            scrollbar-color: var(--electric-blue) var(--deep-space);
        }

        .content-box::-webkit-scrollbar {
            width: 8px;
        }

        .content-box::-webkit-scrollbar-track {
            background: var(--deep-space);
            border-radius: 10px;
        }

        .content-box::-webkit-scrollbar-thumb {
            background-color: var(--electric-blue);
            border-radius: 10px;
            border: 2px solid var(--deep-space);
        }

        ul {
            list-style-type: none;
            padding: 0;
            margin: 0;
        }

        li {
            padding: 15px 20px;
            margin: 12px 0;
            background: rgba(0, 212, 255, 0.05);
            border-left: 3px solid var(--neon-purple);
            border-radius: 6px;
            transition: all 0.3s ease;
            position: relative;
            overflow: hidden;
        }

        li:before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            width: 3px;
            height: 100%;
            background: var(--electric-blue);
            transition: width 0.3s ease;
        }

        li:hover {
            background: rgba(0, 212, 255, 0.1);
            transform: translateX(8px);
            box-shadow: 0 0 15px rgba(0, 212, 255, 0.2);
        }

        li:hover:before {
            width: 8px;
        }

        .options-grid {
            display: grid;
            grid-template-columns: 1fr;
            gap: 15px;
            margin: 30px 0;
        }

        .option-card {
            padding: 18px;
            background: rgba(106, 0, 244, 0.1);
            border: 1px solid var(--space-purple);
            border-radius: 10px;
            color: var(--starlight);
            text-align: center;
            transition: all 0.3s cubic-bezier(0.25, 0.8, 0.25, 1);
            cursor: pointer;
            text-decoration: none;
            position: relative;
            overflow: hidden;
        }

        .option-card:before {
            content: '';
            position: absolute;
            top: -50%;
            left: -50%;
            width: 200%;
            height: 200%;
            background: radial-gradient(circle, rgba(255,0,170,0.1) 0%, transparent 70%);
            transform: rotate(45deg);
            transition: all 0.5s ease;
        }

        .option-card:nth-child(2n):before {
            background: radial-gradient(circle, rgba(0,212,255,0.1) 0%, transparent 70%);
        }

        .option-card:nth-child(3n):before {
            background: radial-gradient(circle, rgba(255,204,0,0.1) 0%, transparent 70%);
        }

        .option-card:hover {
            background: rgba(106, 0, 244, 0.2);
            transform: translateY(-5px);
            box-shadow: 0 0 20px rgba(106, 0, 244, 0.3);
            border-color: var(--electric-blue);
        }

        .option-card:hover:before {
            transform: rotate(45deg) translate(30%, 30%);
        }

        .error-message {
            color: var(--neon-blue);
            text-align: center;
            margin: 20px 0;
            font-weight: 500;
            text-shadow: 0 0 10px rgba(255, 0, 170, 0.3);
        }

        /* Efeitos espaciais */
        .space-effects {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            pointer-events: none;
            z-index: -1;
            overflow: hidden;
        }

        .star {
            position: absolute;
            background-color: white;
            border-radius: 50%;
            animation: twinkle var(--duration) infinite ease-in-out;
            opacity: 0;
        }

        .comet {
            position: absolute;
            width: 6px;
            height: 6px;
            background: linear-gradient(90deg, rgba(255,255,255,0) 0%, var(--electric-blue) 100%);
            border-radius: 50%;
            filter: blur(1px);
            animation: cometFly var(--comet-duration) linear infinite;
            opacity: 0;
        }

        @keyframes twinkle {
            0%, 100% { opacity: 0.1; transform: scale(0.8); }
            50% { opacity: 0.8; transform: scale(1.1); }
        }

        @keyframes cometFly {
            0% { 
                transform: translateX(0) translateY(0);
                opacity: 1;
            }
            100% { 
                transform: translateX(1000px) translateY(300px);
                opacity: 0;
            }
        }

        .planet {
            position: absolute;
            border-radius: 50%;
            filter: blur(1px);
            opacity: 0.1;
        }

        /* Responsividade */
        @media (max-width: 768px) {
            .main-container {
                padding: 30px;
                width: 90%;
                margin: 20px;
            }

            h1 {
                font-size: 2rem;
            }

            .love-logo {
                top: 20px;
                left: 20px;
                font-size: 1.8rem;
            }

            .btn {
                padding: 14px 30px;
                font-size: 1rem;
            }

            .content-box {
                max-height: 50vh;
            }
        }

        @media (max-width: 480px) {
            .main-container {
                padding: 25px 20px;
            }

            h1 {
                font-size: 1.8rem;
                margin-bottom: 25px;
            }

            .option-card {
                padding: 15px;
            }
        }
    </style>
</head>
<body>
    <div class="love-logo">
        <span>K</span><span class="heart">♥</span><span>Y</span>
    </div>

    <div class="space-effects" id="space-effects"></div>

    <div class="main-container">
        <h1>{{ title }}</h1>

        {% if show_start %}
        <a href="/options" class="btn">Start</a>
        {% endif %}

        {% if show_options %}
        <div class="options-grid">
            <a href="/answer/1" class="option-card">Estiver com Raiva/Triste</a>
            <a href="/answer/2" class="option-card">Estiver de TPM</a>
            <a href="/answer/3" class="option-card">Gestos no Dia a Dia</a>
            <a href="/answer/4" class="option-card">Presentes em Datas Especiais</a>
        </div>
        {% endif %}

        {% if show_answer %}
        <div class="content-box">
            <ul>
                {% for item in answer_items %}
                <li>{{ item }}</li>
                {% endfor %}
            </ul>
        </div>
        <a href="/options" class="btn">Voltar</a>
        {% endif %}

        {% if invalid_number %}
        <p class="error-message">Opção inválida. Selecione entre 1 e 4.</p>
        <a href="/options" class="btn">Voltar</a>
        {% endif %}
    </div>

    <script>
        // Criar efeitos espaciais
        function createSpaceEffects() {
            const container = document.getElementById('space-effects');
            container.innerHTML = '';

            // Estrelas
            for (let i = 0; i < 300; i++) {
                const star = document.createElement('div');
                star.className = 'star';

                const size = Math.random() * 3 + 1;
                star.style.width = `${size}px`;
                star.style.height = `${size}px`;

                star.style.left = `${Math.random() * 100}%`;
                star.style.top = `${Math.random() * 100}%`;

                star.style.setProperty('--duration', `${Math.random() * 5 + 2}s`);

                // Dar cores aleatórias para algumas estrelas
                if (Math.random() > 0.7) {
                    const colors = ['#ff00aa', '#00d4ff', '#ffcc00', '#ff6d00'];
                    star.style.backgroundColor = colors[Math.floor(Math.random() * colors.length)];
                }

                container.appendChild(star);
            }

            // Cometas
            for (let i = 0; i < 5; i++) {
                const comet = document.createElement('div');
                comet.className = 'comet';

                comet.style.left = `${Math.random() * 20}%`;
                comet.style.top = `${Math.random() * 20}%`;

                comet.style.setProperty('--comet-duration', `${Math.random() * 30 + 20}s`);

                // Variar cores dos cometas
                const colors = ['#00d4ff', '#ff00aa', '#ffcc00'];
                comet.style.background = `linear-gradient(90deg, rgba(255,255,255,0) 0%, ${colors[i % colors.length]} 100%)`;

                container.appendChild(comet);
            }

            // Planetas distantes
            for (let i = 0; i < 3; i++) {
                const planet = document.createElement('div');
                planet.className = 'planet';

                const size = Math.random() * 200 + 100;
                planet.style.width = `${size}px`;
                planet.style.height = `${size}px`;

                planet.style.left = `${Math.random() * 100}%`;
                planet.style.top = `${Math.random() * 100}%`;

                const colors = ['#6a00f4', '#ff00aa', '#00d4ff'];
                planet.style.backgroundColor = colors[i % colors.length];

                planet.style.filter = `blur(${Math.random() * 10 + 5}px)`;

                container.appendChild(planet);
            }
        }

        // Efeito de flutuação sutil
        function floatEffect() {
            const container = document.querySelector('.main-container');
            const time = Date.now() / 3000;
            const y = Math.sin(time) * 5;
            const x = Math.cos(time * 0.7) * 3;
            const rotation = Math.sin(time * 0.5) * 1;

            container.style.transform = `translate(${x}px, ${y}px) rotate(${rotation}deg)`;
            requestAnimationFrame(floatEffect);
        }

        // Inicialização
        document.addEventListener('DOMContentLoaded', () => {
            createSpaceEffects();
            floatEffect();
        });
    </script>
</body>
</html>
"""

ANSWERS = {
    1: [
        "Peça um abraço bem forte (seja espontâneo!)",
        "Um beijo na testa",
        "Bilhete com pedido de desculpas na almofada",
        "Qualquer doce com bilhetinho",
        "Organize a casa ou o quarto",
        "Banho cheiroso + convite para deitar juntinho",
        "Mensagem fofa (mesmo estando perto)",
        "UM ANEL DE NOIVADO"
    ],
    2: [
        "Compre um chocolate",
        "Faça um chocolate",
        "Prepare qualquer comida",
        "Cafuné no colo",
        "Ofereça massagem",
        "UM ANEL DE NOIVADO",
        "Todas as opções do número 1"
    ],
    3: [
        "Bilhetinhos fofos",
        "Flor (pode ser da rua ou de papel)",
        "Café da manhã pronto",
        "Bom dia carinhoso",
        "Textinho romântico",
        "Convite surpresa para passear",
        "Desenho",
        "Docinho",
        "Visita aleatória com 'Eu te amo'",
        "Lanche surpresa",
        "Pix (para um sorvete ou uma besteirinha",
        "Presente simples (até uma caneta)",
        "UM ANEL DE NOIVADO"
    ],
    4: [
        "UM ANEL DE NOIVADO",
        "Pulseira",
        "Bolsa de lado",
        "Colar",
        "Vestido escolhido por você",
        "UM ANEL DE NOIVADO",
        "Um jantar romântico (com tudo organizado por você)",
        "Relógio",
        "Sandália",
        "Sapato",
        "Buquê de flores",
        "Uma cesta de coisas( ex: danone de chocolate, morangos, bolinhos da bauducco, um vinho, fini de morango e chocolate ao leite)",
        "UM ANEL DE NOIVADO",
        "Viagem",
        "Piquenique",
        "Carta manuscrita",
        "Lanche especial com filme",
        "Noite de casal (cozinhar juntos + filme)",
        "Passeio ao ar livre",
        "UM ANEL DE NOIVADO",
        "Pelúcia",
        "Jogo de tabuleiro",
        "Brinco",
        "Álbum de recordações",
        "Presente criados por você (veja Pinterest)",
        "Produtos de beleza (cremes para cabelo e pele.)",
        "UM ANEL DE NOIVADO"
    ]
}

@app.route('/')
def home():
    return render_template_string(HTML_TEMPLATE, title="Respostas Para Quase Tudo!", show_start=True)

@app.route('/options')
def options():
    return render_template_string(HTML_TEMPLATE, title="Quando/P:", show_options=True)


@app.route('/answer/<int:option>')
def answer(option):
    if 1 <= option <= 4:
        return render_template_string(HTML_TEMPLATE, 
                                  title=f"Opção {option} - Soluções :", 
                                  show_answer=True, 
                                  answer_items=ANSWERS[option])
    else:
        return render_template_string(HTML_TEMPLATE, 
                                  title="Erro de Navegação 🛸", 
                                  invalid_number=True)

@app.route('/<path:path>')
def catch_all(path):
    return render_template_string(HTML_TEMPLATE, title="Página não encontrada no cosmos", invalid_number=True)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)