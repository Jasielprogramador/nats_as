import asyncio
import nats

async def main():
    # Connect to NATS Server.
    nc = await nats.connect('demo.nats.io')
    await nc.publish('foo', b'Hello World!')
    await nc.flush()
    await nc.close()

if __name__ == '__main__':
    asyncio.run(main())