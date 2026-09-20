"""
Classificador de perfil de consumo de água
==========================================

Campanha de conscientização ambiental da companhia de saneamento.

O programa pergunta o tipo de imóvel e o consumo mensal de água (em m³) e
exibe uma mensagem educativa de acordo com as regras de negócio da campanha.
"""

import math

# ----------------------------------------------------------------------------
# Constantes (regras de negócio em um só lugar, fáceis de alterar)
# ----------------------------------------------------------------------------
TIPOS_VALIDOS = ("comercial", "casa", "apartamento")

LIMITE_ECONOMICO = 10      # m³ – apartamento abaixo disso é "econômico"
LIMITE_RESIDENCIAL = 25    # m³ – limite do consumo residencial "moderado"

MSG_COMERCIAL = "Tarifa comercial aplicada – consulte o plano corporativo."
MSG_ECONOMICO = "Consumo econômico – excelente controle de água!"
MSG_MODERADO = "Consumo moderado – dentro do padrão residencial."
MSG_EXCESSIVO = "Consumo excessivo – adote medidas de economia e verifique vazamentos."


# ----------------------------------------------------------------------------
# Regra de negócio
# ----------------------------------------------------------------------------
def classificar_consumo(tipo, consumo):
    """Retorna a mensagem educativa para o tipo de imóvel e consumo (m³) informados."""
    if tipo == "comercial":
        return MSG_COMERCIAL

    if tipo == "apartamento" and consumo < LIMITE_ECONOMICO:
        return MSG_ECONOMICO

    if tipo in ("apartamento", "casa") and consumo <= LIMITE_RESIDENCIAL:
        return MSG_MODERADO

    # Qualquer outro caso: consumo residencial acima do limite
    return MSG_EXCESSIVO


# ----------------------------------------------------------------------------
# Entrada de dados (com validação)
# ----------------------------------------------------------------------------
def ler_tipo_imovel():
    """Pede o tipo de imóvel até o usuário digitar uma opção válida."""
    while True:
        tipo = input("Tipo de imóvel (comercial, casa ou apartamento): ").strip().lower()
        if tipo in TIPOS_VALIDOS:
            return tipo
        print("⚠️  Opção inválida. Digite: comercial, casa ou apartamento.")


def ler_consumo():
    """Pede o consumo mensal (m³) até o usuário digitar um número válido."""
    while True:
        texto = input("Consumo mensal de água em m³ (ex.: 12.5): ").strip().replace(",", ".")
        try:
            consumo = float(texto)
        except ValueError:
            print("⚠️  Valor inválido. Digite apenas números (ex.: 12.5).")
            continue

        if not math.isfinite(consumo) or consumo < 0:
            print("⚠️  O consumo deve ser um número maior ou igual a zero.")
            continue

        return consumo


# ----------------------------------------------------------------------------
# Programa principal
# ----------------------------------------------------------------------------
def main():
    print("💧 Campanha de Consciência Ambiental – Consumo de Água 💧")
    print("-" * 56)

    tipo = ler_tipo_imovel()
    consumo = ler_consumo()

    print()
    print(f"Imóvel: {tipo} | Consumo: {consumo:.2f} m³")
    print(classificar_consumo(tipo, consumo))


if __name__ == "__main__":
    main()
