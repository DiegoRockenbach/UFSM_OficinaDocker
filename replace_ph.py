path = r'C:\PROGRAMACAO\UFSM_OficinaDocker\Aula 1\Oficina Docker - Aula 1 -editavel-.html'

with open(path, encoding='utf-8') as f:
    t = f.read()

old = '>oficina-docker \u00b7 aula 01<'
new = '>@DiegoRockenbach \u00b7 oficina-docker \u00b7 aula 01<'

count = t.count(old)
t = t.replace(old, new)

with open(path, 'w', encoding='utf-8') as f:
    f.write(t)

print(f'Replaced {count} occurrences.')
