# eduardo

#### Interface em Python para o [Robô Ed](http://www.ed.conpet.gov.br/br/converse.php)

## Uso:

```
from eduardo import Ed

nicolas = Ed(name='Nicolas')

texto = nicolas.name + ': ' + nicolas.say('Oi.')

print(texto) # Nicolas: Olá! Tudo bem com você? Posso ajudar?
```

Vide o script `dialogo.py` para um exemplo mais elaborado.

## Argumentos:

**name**: nome do robô (Eduardo por padrão)

**port**: necessária para a interação entre robôs distintos (8085 por padrão)

**server**: "servidor" de onde partirão os requests (0.0.0.0 por padrão)

**url**: url do servidor (URL do Robô Ed por padrão)
