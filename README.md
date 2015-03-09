# eduardo

#### Interface em Python para o [Robô Ed](http://www.ed.conpet.gov.br/br/converse.php)

## Uso:

```
import eduardo

nicolas = ed.Ed(
    name='Nicolas',
    port='8085')

print(nicolas.say('Oi.'))
```

Argumentos:

**name**: nome do robô

**port**: necessária para interação entre robôs distintos (8085 por padrão)
