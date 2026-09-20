<h1 align="center">💧 Consumo de Água – Classificador de Perfil</h1>

<p align="center">
  Script em Python para a campanha de conscientização ambiental da companhia de saneamento.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8%2B-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/GitHub-Reposit%C3%B3rio-181717?style=for-the-badge&logo=github&logoColor=white" alt="GitHub">
  <img src="https://img.shields.io/badge/Git-Versionamento-F05032?style=for-the-badge&logo=git&logoColor=white" alt="Git">
  <img src="https://img.shields.io/badge/%F0%9F%92%A7-%C3%81gua-0EA5E9?style=for-the-badge" alt="Água">
  <img src="https://img.shields.io/badge/%F0%9F%8C%B1-Sustentabilidade-2E7D32?style=for-the-badge" alt="Sustentabilidade">
  <img src="https://img.shields.io/badge/Status-Conclu%C3%ADdo-success?style=for-the-badge" alt="Status">
</p>

---

## 📌 Sobre o projeto

O **Consumo de Água** é um programa de terminal que ajuda a companhia de saneamento a **classificar o perfil de consumo** dos imóveis e a **emitir alertas educativos** aos moradores.

O usuário informa o **tipo do imóvel** e o **consumo mensal de água (m³)**; o programa responde com uma mensagem de acordo com as regras da campanha, incentivando o uso consciente da água e a detecção de vazamentos.

## 🎯 Objetivos

- 🏠 Identificar o perfil de consumo por tipo de imóvel.
- 📢 Emitir mensagens educativas e claras para o morador.
- 🔎 Alertar sobre consumo excessivo e possíveis vazamentos.
- 🌎 Contribuir para a conscientização ambiental.

## 🛠️ Tecnologias

| Tecnologia | Uso no projeto |
|:--|:--|
| 🐍 **Python 3.8+** | Linguagem do programa (somente biblioteca padrão, sem dependências) |
| 🧪 **unittest** | Testes automatizados das regras de negócio |
| 🐙 **Git e GitHub** | Versionamento e publicação do código |

## 📋 Regras de negócio

As regras são avaliadas **nesta ordem**; vale a primeira que for verdadeira:

| # | Condição | Mensagem exibida |
|:-:|:--|:--|
| 1 | Tipo **comercial** (qualquer consumo) | `Tarifa comercial aplicada – consulte o plano corporativo.` |
| 2 | **Apartamento** com consumo **< 10 m³** | `Consumo econômico – excelente controle de água!` |
| 3 | **Apartamento** ou **casa** com consumo **≤ 25 m³** | `Consumo moderado – dentro do padrão residencial.` |
| 4 | Qualquer outro caso (residencial acima de 25 m³) | `Consumo excessivo – adote medidas de economia e verifique vazamentos.` |

> 💡 **Observação:** o consumo "econômico" (regra 2) existe apenas para apartamentos. Uma casa com consumo baixo é classificada como "moderada".

## ▶️ Como executar

### Pré-requisito

- [Python 3.8 ou superior](https://www.python.org/downloads/) instalado. Para conferir: `python --version`

### Passo a passo

```bash
# 1. Clone o repositório
git clone https://github.com/SEU-USUARIO/NOME-DO-REPOSITORIO.git

# 2. Entre na pasta do projeto
cd NOME-DO-REPOSITORIO/consumo-agua

# 3. Execute o programa
python app.py
```

> No Linux/macOS, se `python` não funcionar, use `python3 app.py`.

## 💻 Exemplos de uso

**Apartamento com consumo econômico**
```text
Tipo de imóvel (comercial, casa ou apartamento): apartamento
Consumo mensal de água em m³ (ex.: 12.5): 8,5

Imóvel: apartamento | Consumo: 8.50 m³
Consumo econômico – excelente controle de água!
```

**Casa com consumo moderado**
```text
Tipo de imóvel (comercial, casa ou apartamento): casa
Consumo mensal de água em m³ (ex.: 12.5): 18

Imóvel: casa | Consumo: 18.00 m³
Consumo moderado – dentro do padrão residencial.
```

**Casa com consumo excessivo**
```text
Tipo de imóvel (comercial, casa ou apartamento): casa
Consumo mensal de água em m³ (ex.: 12.5): 32.4

Imóvel: casa | Consumo: 32.40 m³
Consumo excessivo – adote medidas de economia e verifique vazamentos.
```

**Imóvel comercial**
```text
Tipo de imóvel (comercial, casa ou apartamento): comercial
Consumo mensal de água em m³ (ex.: 12.5): 120

Imóvel: comercial | Consumo: 120.00 m³
Tarifa comercial aplicada – consulte o plano corporativo.
```

**Entradas inválidas são tratadas** (o programa pergunta de novo)
```text
Tipo de imóvel (comercial, casa ou apartamento): predio
⚠️  Opção inválida. Digite: comercial, casa ou apartamento.
Tipo de imóvel (comercial, casa ou apartamento): Apartamento
Consumo mensal de água em m³ (ex.: 12.5): abc
⚠️  Valor inválido. Digite apenas números (ex.: 12.5).
Consumo mensal de água em m³ (ex.: 12.5): -3
⚠️  O consumo deve ser um número maior ou igual a zero.
Consumo mensal de água em m³ (ex.: 12.5): 12,5

Imóvel: apartamento | Consumo: 12.50 m³
Consumo moderado – dentro do padrão residencial.
```

## 🧪 Testes

As regras de negócio possuem testes automatizados, incluindo os valores-limite (9,99 · 10 · 25 · 25,01 m³):

```bash
python -m unittest -v
```

## 📁 Estrutura do repositório

```text
.
├── README.md
└── consumo-agua/
    ├── app.py          # programa principal
    ├── test_app.py     # testes das regras de negócio
    └── README.md       # este arquivo
```

## ✅ Decisões de implementação

- **Função `classificar_consumo`** separada da entrada/saída, o que facilita testar e reutilizar a regra.
- **Constantes** para limites (10 m³ e 25 m³) e mensagens, fáceis de alterar em um só lugar.
- **Validação de entrada:** o tipo aceita maiúsculas/minúsculas e espaços extras; o consumo aceita vírgula ou ponto como separador decimal e rejeita texto e valores negativos.
- **Interpretação da regra 3:** o limite de 25 m³ vale tanto para casa quanto para apartamento; assim, um apartamento também pode receber o alerta de consumo excessivo.

## 👩‍💻 Autor(a)

Desenvolvido por **Seu Nome** como atividade da Agenda 7 – Desenvolvimento de Sistemas.

<p>
  <a href="https://github.com/SEU-USUARIO">
    <img src="https://img.shields.io/badge/GitHub-SEU--USUARIO-181717?style=flat&logo=github&logoColor=white" alt="GitHub do autor">
  </a>
</p>

---

<p align="center">💙 Cada gota conta. Use a água com consciência! 🌎</p>
