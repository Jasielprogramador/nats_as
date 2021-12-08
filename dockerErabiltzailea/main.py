import asyncio
import sys
from nats.aio.client import Client as NATS


async def main():
    nc = NATS()
    #Te conectas al servidor
    await nc.connect(servers=['nats://localhost:4222'])
    ans = True

    chivato = True
    while chivato:
        try:
            user = input("Por favor escribe tu nombre de usuario: ")
        except EOFError:
            return

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

        try:
            ans = input("Que te gustaria hacer? ")
        except EOFError:
            return
        if ans == "1":

            try:
                text = input("Por favor, escribe el mensaje que quieres enviar: ")
            except EOFError:
                return

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
