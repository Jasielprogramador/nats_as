import asyncio
import sys
import nats
from past.builtins import raw_input


async def main():
    nc = await nats.connect('demo.nats.io')

    ans = True

    chivato = True
    while chivato:
        user = raw_input("Quien eres? ")
        if user == "":
            print("\n Por favor pon el nombre del usuario")
        else:
            chivato = False

    sub = await nc.subscribe(user)

    while ans:
        print("""
                1.Enviar un mensaje a la cola 
                2.Leer el estado de la cola 
                3.Salir
                """)
        ans = raw_input("Que te gustaria hacer? ")
        if ans == "1":
            text = raw_input("Por favor, escribe el mensaje que quieres enviar: ")

            # conversor de string a bytes
            text = bytes(text, 'utf-8')
            await nc.publish(user, text)
            print('----------------------')

        elif ans == "2":
            print("\n El estado de la cola es el siguiente: ")

            cola = False

            while True:
                try:
                    msg = await sub.next_msg()
                except:
                    if(cola == False):
                        print("\n La cola de mensajes esta vacia")
                    break

                print('----------------------')
                print('Usuario   :', msg.subject)
                data = msg.data.decode("utf-8")
                mezua = data.split("'")[0]
                print('Mensaje   :', mezua)
                cola = True
                print('----------------------')

        elif ans == "3":
            await nc.close()
            print("\n Programa finalizado, ten un buen dia :)")
            sys.exit(0);

        elif ans != "":
            print("\n Por favor elige uno de estos valores [1,2,3,4]")


if __name__ == '__main__':
    asyncio.run(main())
