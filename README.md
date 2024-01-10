# Script Python - Dia da Semana

Este é um script Python simples que determina o dia da semana para uma data específica usando o módulo `calendar`.

## Uso

1. **Configuração:**
   - Abra o script `dia_semana.py` em um editor de texto.

2. **Execução:**
   - Certifique-se de ter o Python instalado em seu ambiente.
   - Execute o script usando o comando `python dia_semana.py`.

3. **Configuração da Data:**
   - No script, você pode ajustar os valores de `ano`, `mes` e `dia` para a data desejada.

4. **Resultado:**
   - O script imprimirá o dia da semana correspondente à data fornecida.

## Exemplo

No script fornecido:

```python
import calendar

ano = 2024
mes = 9
dia = 9

dia_semana = calendar.weekday(ano, mes, dia)

if dia_semana == 0:
    print('Segunda-Feira')
elif dia_semana == 1:
    print('Terça-Feira - Meu Niver')
elif dia_semana == 2:
    print('Quarta-Feira')
elif dia_semana == 3:
    print('Quinta-Feira')
elif dia_semana == 4:
    print('Sexta-Feira')
elif dia_semana == 5:
    print('Sábado')
else:
    print('Domingo')
