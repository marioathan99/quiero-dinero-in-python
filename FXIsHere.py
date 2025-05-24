'''
You just got home from a fun trip to South America, specifically Colombia, Peru, and Brazil. There's some leftover cash in:

🇨🇴 Colombian pesos
🇵🇪 Peruvian soles
🇧🇷 Brazilian reais

Let's translate those amounts to € :D
'''
pesos = int(input("How much do you have left in pesos? "))
soles = int(input("How much do you have left in soles? "))
reais = int(input("How much do you have left in reais? "))
euros = (pesos * 0.046) + (soles * 0.24) + (reais * 0.16)
print("Are you rich or something? Because all your residual money equals to:", euros, "€!")