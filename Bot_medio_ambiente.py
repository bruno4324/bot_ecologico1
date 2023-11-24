import discord
import random

intents = discord.Intents.default()

intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Hemos iniciado sesión como {client.user}')
    
@client.event
async def on_message(message):
    
    if message.author == client.user:
        return
    
    #comando /idea ecologica
    if message.content.startswith('/idea ecologica'):
        eleccion_del_bot = random.randint(1, 3)
        if eleccion_del_bot == 1:
            await message.channel.send("Macetas con botellas de plástico 🌱: Puedes transformar las botellas de plástico en macetas para tus plantas 🌼 con un poco de creatividad y pintura. Los pasos son: 1.-Corta la parte superior de una botella de plástico y haz algunos agujeros en el fondo para el drenaje . 2.-Decora la botella con pintura, pegatinas, cintas o lo que quieras. 3.-Rellena la botella con tierra y planta una semilla o un esqueje de tu planta favorita. 4.-Coloca la botella en un lugar con luz y riega la planta regularmente.")
        if eleccion_del_bot == 2:
            await message.channel.send("Organizador con rollos de papel higiénico ✏️✒️🖋️🖊️🖌️🖍️: Puedes aprovechar los rollos de papel higiénico vacíos 🧻 para hacer un organizador para tus lápices, bolígrafos, tijeras y otros objetos. Los pasos son: 1.-Corta los rollos de papel higiénico en diferentes longitudes según el tamaño de los objetos que quieras guardar. 2.-Pega los rollos entre sí con pegamento o cinta adhesiva formando una estructura que se adapte al espacio que tengas disponible. 3.-Forra los rollos con papel de colores, tela, cartulina o lo que prefieras para darle un toque personal. 4.-Coloca el organizador en tu escritorio, estantería o donde quieras y ordena tus objetos dentro de los rollos.")
        if eleccion_del_bot == 3:
            await message.channel.send("Velas decorativas con tapones de botellas de vino 🍾 : Puedes aprovechar los tapones de corcho de las botellas de vino para hacer unas velas decorativas y aromáticas 🌺. Los pasos son: 1.-Corta los tapones de corcho por la mitad y hazles un agujero en el centro con un clavo o un sacacorchos. 2.-Introduce una mecha de vela en el agujero y asegúrala con un poco de pegamento. 3.-Derrite cera de vela en un recipiente al baño maría y añade unas gotas de aceite esencial del aroma que prefieras. 4.-Vierte la cera derretida sobre los tapones de corcho, llenando el agujero y cubriendo la superficie. 5.-Deja que la cera se seque")
        await message.channel.send("si quieres repasar la lista de comandos ♻️. envia lo siguente: /help")
        
        #comando /help
    if message.content.startswith('/help'):
        await message.channel.send("/help: ayuda de los comandos 🎯")
        await message.channel.send("/idea ecologica: idéa aleatoria para armar cosas a partir de objetos desechables (en su mayoría) ♻️")
        

