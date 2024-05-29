import discord
from discord.ext import commands
import os
import random
import requests

intents = discord.Intents.default()
intents.message_content = True


client = discord.Client(intents=intents)




@client.event
async def on_ready():
    print(f'{client.user} olarak giriş yaptık')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$help'):
        await message.channel.send('sorabileceğiniz sorular: \n 1.çevre kirliliği nedir \n 2.çevre kirliliği hakkında birkaç görsel göster \n 3.çevre kirliliğini azaltma yolları nelerdir \n UYARI!!!:lütfen soruların önüne $ işareti koyunuz')

    elif message.content.startswith('$çevre kirliliği nedir'):
        await message.channel.send('Çevrenin canlı ögelerinin hayat aktivitelerini olumsuz yönde etkileyen, cansız ögelerin üzerinde ise yapısal zararlar meydana getiren ve niteliklerini bozan yabancı maddelerin hava, su ve toprağa yoğun bir şekilde karışması olayına çevre kirliliği denir. Hızla artan insan nüfusu ihtiyaçları arttırmakta, insan eliyle yaratılan kirliliğin tabiata ve çevreye verdiği zararın boyutu her geçen gün artmaktadır. Yaşamı daha mükemmel bir hale getirmek, daha sağlıklı ve uzun bir ömür sağlayabilmek amacına dönük bazı gelişmelerin, kırsal ve kentsel alanlarda doğal kaynaklarını bozduğu, su, hava, toprak kirlenmesine yol açtığı, bitki ve hayvan varlığına ve sağlığına zarar verdiği açıkça görülebilen bir gerçek haline gelmiştir.')

    elif message.content.startswith('$çevre kirliliğini azaltma yolları nelerdir'):
        await message.channel.send(f'Çevre kirliliğinin önüne geçmek için ekolojik dengenin korunması ve duyarlılığın artırılması son derece önemlidir. Çöplerin kesinlikle doğaya bırakılmaması, kağıt, cam ve plastik gibi atıkların geri dönüşüm sürecine dahil edilmesi son derece önemlidir. Geri dönüştürülebilen maddelerin doğaya bırakılması, doğada bu zararlı maddelerin binlerce yıl kalmasına neden olmaktadır.')

    elif message.content.startswith('$çevre kirliliği hakkında birkaç görsel göster'):
        dosya =os.listdir("resimler")
        image = random.choice(dosya)
        with open(f"resimler/{image}", "rb") as f:
            image = discord.File(f)
            await message.channel.send(file=image)


        
client.run("YOUR DISCORD TOKEN")

