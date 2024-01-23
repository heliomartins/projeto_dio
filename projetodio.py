def nivel_de_heroi():
    nome = str(input("Qual o seu nome, herói?"))
    xp = int(input("Quanto xp foi adquirido na última jornada?"))

    if xp <= 1000:
        xp = "ferro!"
    elif 1001 < xp <= 2000:
        xp = "bronze!"
    elif 2001 < xp <= 5000:
        xp = "prata!"
    elif 5001 < xp <= 7000:
        xp = "ouro!"
    elif 7001 < xp <= 8000:
        xp = "platina!"
    elif 8001 < xp <= 9000:
        xp = "ascendente!"
    elif 9001 < xp <= 10000:
        xp = "imortal!"
    else: 
        xp > 10001
        xp = "radiante!"

    print("O herói de nome", nome,"está no ranking",xp)

nivel_de_heroi()

