#3-1
lista = ['ville', 'juhani', 'kristian', 'jestila']
print(lista[0])
print(lista[1])
print(lista[2])
print(lista[3])

#3-2
message1 = f"nimeni yksi osa on {lista[0].title()}\n"
message2 = f"nimeni yksi osa on {lista[1].title()}\n"
message3 = f"nimeni yksi osa on {lista[2].title()}\n"
message4 = f"nimeni yksi osa on {lista[3].title()}\n"
print(message1)
print(message2)
print(message3)
print(message4)

#3-3
lista2 = ['pyora', 'auto', 'linja-auto']
messagePyora = f"\nHaluan ajaa kesat {lista2[0]}lla"
messageAuto = f"\nTalvisin {lista2[1]}lla on mukavin kulkea."
messageLinja = f"\nKuljen kuitenkin {lista2[2]}lla koska se on edullisinta."
print(messagePyora)
print(messageAuto)
print(messageLinja)

#3-4
vierasLista = ['elvis presley', 'michael jackson', 'andy mcCoy']
messageE = f"\nYou, {vierasLista[0].title()} have been invited to Ville's dinner party"
messageM = f"\nYou, {vierasLista[1].title()} have been invited to Ville's dinner party"
messageA = f"\nYou, {vierasLista[2].title()} have been invited to Ville's dinner party"

print(messageE)
print(messageM)
print(messageA)

#3-5
eiPaase = f"Sadly, {vierasLista[2].title()} can't come to your dinner party."
print(eiPaase)

del vierasLista[2]
vierasLista.insert(2, 'hulk hogan')

messageE = f"\nYou, {vierasLista[0].title()} have been invited to Ville's dinner party"
messageM = f"\nYou, {vierasLista[1].title()} have been invited to Ville's dinner party"
messageA = f"\nYou, {vierasLista[2].title()} have been invited to Ville's dinner party"

print(messageE)
print(messageM)
print(messageA)

#3-6
messageE = f"Hello, {vierasLista[0].title()} we're pleased to inform you that the dinner tables gotten bigger!"
messageM = f"Hello, {vierasLista[1].title()} we're pleased to inform you that the dinner tables gotten bigger!"
messageA = f"Hello, {vierasLista[2].title()} we're pleased to inform you that the dinner tables gotten bigger!"

print(messageE)
print(messageM)
print(messageA)

vierasLista.insert(0, 'rocky balboa')
vierasLista.insert(2, 'rambo')
vierasLista.append('batman')

messageE = f"\nYou, {vierasLista[0].title()} have been invited to Ville's dinner party"
messageM = f"\nYou, {vierasLista[1].title()} have been invited to Ville's dinner party"
messageA = f"\nYou, {vierasLista[2].title()} have been invited to Ville's dinner party"
messageRB = f"\nYou, {vierasLista[3].title()} have been invited to Ville's dinner party"
messageR = f"\nYou, {vierasLista[4].title()} have been invited to Ville's dinner party"
messageB = f"\nYou, {vierasLista[5].title()} have been invited to Ville's dinner party"

print(messageE)
print(messageM)
print(messageA)
print(messageRB)
print(messageR)
print(messageB)

#3-7
poppedVieras = vierasLista.pop()
messagePOP = f"The new table hasn't arrvied yet so your'e out of the dinner party {poppedVieras.title()}"
print(messagePOP)
poppedVieras = vierasLista.pop()
messagePOP = f"The new table hasn't arrvied yet so your'e out of the dinner party {poppedVieras.title()}"
print(messagePOP)
poppedVieras = vierasLista.pop()
messagePOP = f"The new table hasn't arrvied yet so your'e out of the dinner party {poppedVieras.title()}"
print(messagePOP)
poppedVieras = vierasLista.pop()
messagePOP = f"The new table hasn't arrvied yet so your'e out of the dinner party {poppedVieras.title()}"
print(messagePOP)
print(vierasLista)