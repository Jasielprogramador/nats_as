import asyncio
import sys
import nats
from past.builtins import raw_input


async def main():
    nc = await nats.connect('demo.nats.io')
    sub = await nc.subscribe('user')

    ans = True
    while ans:
        print("""
                1.Enviar un mensaje a la cola 
                2.Enviar un mensaje con respuesta a la cola
                3.Leer el estado de la cola 
                4.Salir
                """)
        ans = raw_input("Que te gustaria hacer? ")
        if ans == "1":
            text = raw_input("Por favor, escribe el mensaje que quieres enviar: ")

            # conversor de string a bytes
            text = bytes(text, 'utf-8')
            await nc.publish('user', text)
            print('----------------------')

        elif ans == "2":
            text = raw_input("Por favor, escribe el mensaje que quieres enviar: ")
            respuesta = raw_input("Por favor, escribe la respuesta al mensaje que quieres enviar: ")

            # conversor de string a bytes
            text = bytes(text, 'utf-8')
            respuesta = bytes(respuesta, 'utf-8')
            await nc.publish('user', text, reply=respuesta)
            print('----------------------')

        elif ans == "3":
            print("\n El estado de la cola es el siguiente: ")

            while True:
                try:
                    msg = await sub.next_msg()
                except:
                    print("\n No hay ningun mensaje en la cola")
                    break
                print('----------------------')
                print('Usuario   :', msg.subject)
                print('Mensaje   :', msg.data)
                print('Respuesta :', msg.reply)

        elif ans == "4":
            await nc.close()
            print("\n Programa finalizado, ten un buen dia :)")
            sys.exit(0);

        elif ans != "":
            print("\n Por favor elige uno de estos valores [1,2,3,4]")


if __name__ == '__main__':
    asyncio.run(main())
