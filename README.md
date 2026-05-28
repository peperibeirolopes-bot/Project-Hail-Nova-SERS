# 🛰️ Project HAIL NOVA

Sistema inteligente de monitoramento energético para missões espaciais experimentais.

---

## 👥 Equipe

- Pedro Ribeiro Lopes — RM: 570083

- Lucas Furquim Lima — RM: 568690

- Diogo Chiaradia Santos — RM: 570246

---

## 📋 Sobre o Projeto

O **Project HAIL NOVA** é uma solução computacional de monitoramento em tempo real para missões espaciais simuladas. O sistema interpreta dados de sensores, detecta condições críticas, gera alertas automáticos e aciona respostas inteligentes — tudo com foco na gestão de energia renovável (painéis solares) e sustentabilidade operacional.

Desenvolvido como parte do desafio **Soluções em Energias Renováveis e Sustentáveis**, o projeto aplica conceitos de programação, algoritmos, pensamento computacional e IA introdutória na construção de uma plataforma funcional de análise operacional espacial.

---

## 🚀 Funcionalidades

- **Monitoramento em tempo real** de temperatura, energia solar, bateria, comunicação e status dos módulos
- **Geração automática de alertas** para condições críticas (superaquecimento, bateria crítica, falha de comunicação, etc.)
- **IA de monitoramento** com tomada de decisão baseada em regras (modo economia, resfriamento, redirecionamento de sinal)
- **Simulação de eventos espaciais** com impacto real nos sensores (tempestade solar, impacto de meteoro, falha no motor)
- **Relatório energético** com cálculo de chance de sucesso da missão
- **3 missões consecutivas** com dados gerados aleatoriamente a cada rodada

---

## ⚙️ Como Funciona

O sistema segue uma ordem de execução cuidadosamente planejada a cada missão:

```
Gerar sensores → Aplicar evento → Exibir painel → Disparar alertas → IA reage → Relatório
```

Essa ordem garante que a IA sempre enxergue o estado real dos sensores **após** o impacto dos eventos — e não antes.

---

## 🌱 Conexão com Energias Renováveis

A fonte principal de energia da missão são os **painéis solares**. O sistema gerencia a energia de forma adaptativa:

| Condição | Modo de Operação |
|---|---|
| Energia solar > 70% | Alto desempenho |
| Energia solar entre 30–70% | Operação padrão |
| Energia solar < 30% | Suporte por bateria |
| Bateria < 20% | Economia total |

Essa lógica reflete princípios reais de gestão energética sustentável: priorizar fontes renováveis e usar reservas apenas quando necessário.

---

## 🤖 IA de Monitoramento

A inteligência do sistema é baseada em **regras de decisão automatizadas**:

- 🔋 Bateria crítica → Ativa modo economia
- ☀️ Baixa geração solar → Utiliza energia armazenada
- 🌡️ Superaquecimento → Aciona resfriamento
- 📡 Sinal instável → Ajusta estabilidade
- 📡 Sinal comprometido → Redireciona sinal
- 🛰️ Módulo offline → Isola o módulo afetado

---

## 🗂️ Estrutura do Código

```
hail_nova.py
│
├── inicializar()        → Tela de boot e ativação dos módulos
├── gerar_sensores()     → Geração aleatória dos dados dos sensores
├── gerar_evento()       → Sorteio de evento espacial com pesos
├── aplicar_evento()     → Aplica os efeitos do evento nos sensores
├── exibir_painel()      → Painel operacional com os dados da missão
├── exibir_evento()      → Exibe o evento ocorrido na missão
├── exibir_alertas()     → Alertas automáticos por condição crítica
├── exibir_ia()          → Respostas automatizadas da IA
├── calcular_sucesso()   → Relatório energético e chance de sucesso
└── main()               → Loop principal das 3 missões
```

---

## 🖥️ Como Executar

**Pré-requisitos:** Python 3.x instalado

```bash
# Clone o repositório
git clone https://github.com/seu-usuario/project-hail-nova.git

# Entre na pasta
cd project-hail-nova

# Execute o sistema
python hail_nova.py
```

Nenhuma biblioteca externa é necessária — o projeto usa apenas módulos nativos do Python (`time`, `random`, `os`).

---
