import datetime
import requests
import random
import subprocess
import json

def teste(audio_path):
        
    f = audio_path
    sufix = random.choice(range(0,10000))


    local_path = f"audio/{sufix}Cath" 
    i_path = local_path + ".ogg"

    response = requests.get(f,stream=True)

    if response.status_code == 200:
        with open(i_path, 'wb') as audio_file:
            for chunk in response.iter_content(chunk_size=128):
                audio_file.write(chunk)

        print(f"Downloaded {f} to {i_path}")

        return i_path


    else:
        print(f"Failed to download {f}. Status code: {response.status_code}")

def get(file):

    sufix = random.choice(range(0,10000))


    local_path = f"{sufix}Cath.wav"

    response = requests.get(file,stream=True)

    if response.status_code == 200:
        with open(local_path, 'wb') as audio_file:
            for chunk in response.iter_content(chunk_size=128):
                audio_file.write(chunk)

        print(f"Downloaded {file} to {local_path}")


    else:
        print(f"Failed to download {file}. Status code: {response.status_code}")

    return local_path

def conv():
    audio_path = "https://blipmediastore.blip.ai/secure-medias/Media_7ac449c6-1627-41fc-8bfa-a24eea634478AwACAgEAAxkBAAICKWWkWVbPMDhBxeBBc3ujtv6aD7cDAAJtAwACnpIgRTJfi16RTieXNAQ?sv=2019-07-07&st=2024-01-14T21%3A44%3A53Z&se=2024-01-14T22%3A14%3A53Z&sr=b&sp=r&sig=Vg9WkLVIAF6mNng505D0sOWiWbmDriUPX0ZfDCrr18M%3D&secure=true"
    body = {"apikey": "44953355ae0885b61f01031d688c1297", "file":audio_path, "outputformat":"wav"}
    b = json.dumps(body)
    #44953355ae0885b61f01031d688c1297
    response = requests.post("https://api.convertio.co/convert",b)
    print(response.status_code)
    result = json.loads(response.content)
    print(result)
    id = result["data"]["id"]
    print(result)

    response2 = requests.get(f"https://api.convertio.co/convert/{id}/status")
    print(response2.status_code)
    result2 = json.loads(response2.content)
    print(result2)
    if result2["data"]["step"] == "finish":
        f = result2["data"]["output"]["url"]
        get(f)

def consult():
    response2 = requests.get(f"https://api.convertio.co/convert/30e3dec87785da222a3d66024622f5f7/status")
    print(response2.status_code)
    result2 = json.loads(response2.content)
    print(result2)
   

