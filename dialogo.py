# Inspirado por https://gist.github.com/Fedalto/5017878
import eduardo, time

nicolas = eduardo.Ed(
    name='Nicolas',
    port='8088',
    server='127.0.0.1',
    url='http://bot.insite.com.br/cgi-bin/bot_gateway.cgi')

jesus = eduardo.Ed(
    name='Jesus',
    port='8085')

msg='Oi'
while True:
    print(jesus.name + ': ' + msg)
    msg = nicolas.say(msg)
    time.sleep(1)
    print(nicolas.name + ': ' + msg)
    msg=jesus.say(msg)
