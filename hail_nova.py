import time
import random
import os

# Funções

def gerar_sensores():

    return {
        "temperatura": random.randint(15, 95),
        "bateria": random.randint(0, 100),
        "energia_solar": random.randint(0, 100),
        "comunicacao": random.choice(["Estável", "Instável", "Comprometida"]),
        "status": random.choice(["Online", "Manutenção", "Offline"]),
    }


def gerar_evento():

    return random.choices(
        ["Nenhum", "Tempestade solar", "Meteoro pequeno", "Falha no motor"],
        weights=[60, 20, 12, 8]
    )[0]

# 1. Gera sensores - 2. Aplica evento - 3. IA reage - 4. Relatório

def aplicar_evento(sensores, evento):

    if evento == "Tempestade solar":
        sensores["energia_solar"] = max(0, sensores["energia_solar"] - 30)
        sensores["comunicacao"] = "Instável"

    elif evento == "Meteoro pequeno":
        sensores["bateria"] = max(0, sensores["bateria"] - 15)
        sensores["status"] = "Manutenção"

    elif evento == "Falha no motor":
        sensores["bateria"] = max(0, sensores["bateria"] - 25)
        sensores["status"] = "Offline"

    return sensores


def exibir_painel(sensores):

    print("======= PAINEL OPERACIONAL =======")
    print(f"🌡 Sensor térmico:   {sensores['temperatura']}°C")
    print(f"☀  Painéis solares:  {sensores['energia_solar']}%")
    print(f"📡 Comunicação:      {sensores['comunicacao']}")
    print(f"🔋 Bateria:          {sensores['bateria']}%")
    print(f"🛰 Status:           {sensores['status']}")
    print("===================================")


def exibir_alertas(sensores):

    print("\n======= ALERTAS =======\n")

    alertas = [
        (sensores["temperatura"] >= 80,          "🚨 Superaquecimento detectado!"),
        (sensores["energia_solar"] < 30,         "🚨 Baixa geração solar!"),
        (sensores["bateria"] < 20,               "🚨 Bateria crítica!"),
        (sensores["comunicacao"] == "Instável",  "🚨 Oscilação no sinal!"),
        (sensores["comunicacao"] == "Comprometida", "🚨 Comunicação comprometida!"),
        (sensores["status"] == "Manutenção",     "🚨 Módulos em manutenção!"),
        (sensores["status"] == "Offline",        "🚨 Módulos fora de operação!"),
    ]

    houve_alerta = False
    for condicao, mensagem in alertas:
        if condicao:
            print(mensagem)
            houve_alerta = True

    if not houve_alerta:
        print("✅ Nenhum alerta no momento.")


def exibir_ia(sensores):

    print("\n======== IA DE MONITORAMENTO ========\n")

    acoes = [
        (sensores["bateria"] < 20,               "🤖 Ativando modo economia"),
        (sensores["energia_solar"] < 30,          "🤖 Utilizando energia armazenada"),
        (sensores["temperatura"] >= 80,            "🤖 Acionando resfriamento"),
        (sensores["comunicacao"] == "Instável",   "🤖 Ajustando estabilidade do sinal"),
        (sensores["comunicacao"] == "Comprometida", "🤖 Redirecionando sinal"),
        (sensores["status"] == "Offline",         "🤖 Isolando módulo afetado"),
        (sensores["status"] == "Manutenção",      "🤖 Reduzindo atividades secundárias"),
    ]

    acao_tomada = False
    for condicao, mensagem in acoes:
        if condicao:
            print(mensagem)
            acao_tomada = True

    if not acao_tomada:
        print("🤖 Todos os sistemas operando normalmente")


def exibir_evento(evento):

    print("\n======= EVENTO DA MISSÃO =======\n")

    mensagens = {
        "Nenhum":           "🟢 Condições espaciais estáveis",
        "Tempestade solar": "⚠  Tempestade solar detectada!",
        "Meteoro pequeno":  "☄  Impacto de meteoro pequeno!",
        "Falha no motor":   "🚨 Falha no motor detectada!",
    }

    print(mensagens.get(evento, "❓ Evento desconhecido"))


def calcular_sucesso(sensores, evento):

    bateria = sensores["bateria"]
    energia_solar = sensores["energia_solar"]
    comunicacao = sensores["comunicacao"]
    status = sensores["status"]

    # Modo energético
    if bateria < 20:
        modo = "Economia total"
    elif energia_solar > 70:
        modo = "Alto desempenho"
    elif energia_solar < 30:
        modo = "Suporte por bateria"
    else:
        modo = "Operação padrão"

    # Situação geral
    if bateria < 20 or status == "Offline":
        situacao = "CRÍTICA"
    elif energia_solar < 30 or comunicacao != "Estável":
        situacao = "ATENÇÃO"
    else:
        situacao = "ESTÁVEL"

    # Cálculo de sucesso
    sucesso = 100
    penalidades = [
        (bateria < 20,               25),
        (sensores["temperatura"] >= 80, 15),
        (comunicacao != "Estável",   15),
        (status == "Manutenção",     15),
        (status == "Offline",        35),
        (evento == "Tempestade solar", 10),
        (evento == "Meteoro pequeno",  15),
        (evento == "Falha no motor",   25),
    ]

    for condicao, penalidade in penalidades:
        if condicao:
            sucesso -= penalidade

    sucesso = max(0, sucesso)

    print("\n======= RELATÓRIO ENERGÉTICO =======\n")
    print("☀  Fonte principal: Energia Solar")
    print(f"🔋 Energia armazenada: {bateria}%")
    print(f"⚡ Sistema operando em modo: {modo}")
    print(f"📊 Situação energética geral: {situacao}")

    print("\n======= STATUS DA MISSÃO =======\n")
    print(f"🎯 Chance de sucesso da missão: {sucesso}%")


# Loop

def inicializar():

    print("====================================")
    print("      PROJECT HAIL NOVA v1.0")
    print("====================================")

    etapas = [
        "Inicializando IA...",
        "Conectando sensores...",
        "Verificando módulos...",
        "Sistema iniciado com sucesso",
    ]

    for etapa in etapas:
        print(etapa)
        time.sleep(0.7)

    time.sleep(0.3)
    print("====================================")
    print("Bem-vindo ao Project HAIL NOVA")
    print("Missão espacial NOVA")
    print("====================================")

    print("\nMódulos conectados:\n")
    modulos = [
        "☀  Painéis solares: ONLINE",
        "🔋 Sistema de baterias: ONLINE",
        "📡 Comunicação: ONLINE",
        "🌡 Sensores térmicos: ONLINE",
        "🤖 IA de monitoramento: ONLINE",
    ]
    for m in modulos:
        print(m)

    time.sleep(2)
    print("\n🚀 INICIANDO MODO TEMPO REAL...")


def main():
    inicializar()

    for missao in range(1, 4):
        os.system("cls" if os.name == "nt" else "clear")

        print("====================================")
        print(f"🚀 MISSÃO {missao}/3")
        print("====================================\n")

        sensores = gerar_sensores()
        evento = gerar_evento()
        sensores = aplicar_evento(sensores, evento)

        exibir_painel(sensores)
        exibir_evento(evento)
        exibir_alertas(sensores)
        exibir_ia(sensores)
        calcular_sucesso(sensores, evento)

        print("\n====================================")
        time.sleep(6)

    print("\n✅ Todas as missões concluídas")
    print("🤖 IA encerrando sistema...")
    time.sleep(2)


main()
