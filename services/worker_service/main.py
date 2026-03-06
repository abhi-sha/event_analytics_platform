import asyncio
from .worker import Worker

async def main():
    worker=Worker()
    await worker.start()

if __name__=="__main__":
    asyncio.run(main())