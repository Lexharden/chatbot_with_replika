import json
import time
import env
import asyncio
import googletrans
import websockets
from googletrans import *

translator = Translator()


async def sendRequest(message):
    uri = 'wss://ws.replika.com/v17'
    async with websockets.connect(uri) as websocket:
        data = env.generateData(message)
        await websocket.send(json.dumps(data))
        while True:
            try:
                answer = await asyncio.wait_for(websocket.recv(), timeout=10)
                json_response = json.loads(answer)
                message_final = json_response['payload']['content']['text']

                # respuesta=answer[10]
                response = translator.translate(message_final, dest='es')
                return (response.text)
            except BaseException as error:
                print(error)
                print("Se perdio la comunicacion.")


msg = input("Introduce mensaje: ")
asyncio.run(sendRequest(msg))

