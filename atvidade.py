def escolher_raca():
    racas = ["Humano", "Anão", "Elfo", "Goblin", "Orc", "Dragonato"]
    print("Escolha uma raça:")
    for i, raca in enumerate(racas, 1):
        print(f"{i}. {raca}")

    escolha = input("Digite o número correspondente: ")
    return racas[int(escolha) - 1] if escolha.isdigit() and 1 <= int(escolha) <= len(racas) else "Escolha inválida"

def criar_ficha(raca):
    bonus = {
        "Humano": {"Força": 1, "Destreza": 1, "Constituição": 1, "Inteligência": 1, "Sabedoria": 1, "Carisma": 1},
        "Anão": {"Força": 1, "Constituição": 1},
        "Elfo": {"Destreza": 1, "Inteligência": 1},
        "Goblin": {"Destreza": 2},
        "Orc": {"Força": 2},
        "Dragonato": {"Constituição": 2}
    }
    atributos_base = {
        "Força": 10, "Destreza": 10, "Constituição": 10, "Inteligência": 10, "Sabedoria": 10, "Carisma": 10
    }
    if raca in bonus:
        for atributo, valor in bonus[raca].items():
            atributos_base[atributo] += valor
    return atributos_base

def customizar_atributos():
    pontos_disponiveis = [8, 10, 12, 13, 14, 15]
    atributos = ["Força", "Destreza", "Constituição", "Inteligência", "Sabedoria", "Carisma"]
    distribuicao = {}

    print("Distribua os seguintes valores entre os atributos: 8, 10, 12, 13, 14, 15")
    for atributo in atributos:
        while True:
            valor = input(f"Atribua um valor para {atributo}: ")
            if valor.isdigit() and int(valor) in pontos_disponiveis:
                distribuicao[atributo] = int(valor)
                pontos_disponiveis.remove(int(valor))
                break
            else:
                print("Valor inválido ou já utilizado. Escolha outro valor.")

    return distribuicao

raca_selecionada = escolher_raca()
if raca_selecionada != "Escolha inválida":
    ficha = criar_ficha(raca_selecionada)
    print(f"Você escolheu: {raca_selecionada}")
    print("Atributos iniciais com bonus de raça:", ficha)

    atributos_customizados = customizar_atributos()
    print("Atributos personalizados:", atributos_customizados)
else:
    print(raca_selecionada)
