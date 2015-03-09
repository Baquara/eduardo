# eduardo

#### Interface em Python para o [Robô Ed](http://www.ed.conpet.gov.br/br/converse.php)

## Uso:

```
import eduardo

nicolas = eduardo.Ed(
    name='Nicolas',
    port='8085')

print(nicolas.say('Oi.'))
```

Veja mais exemplos no diretório `exemplos`

## Argumentos:

**name**: nome do robô (Eduardo por padrão)

**port**: necessária para interação entre robôs distintos (8085 por padrão)

**server**: "servidor" de onde partirão os requests (0.0.0.0 por padrão)

**url**: url do servidor (URL do Robô Ed por padrão)
