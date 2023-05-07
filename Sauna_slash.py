import json
import requests
import discord
from discord.ext import commands
import io
import time
from PIL import Image, ImageDraw, ImageFont, ImageFile
from discord_slash import SlashCommand
from discord_slash.utils.manage_commands import create_choice, create_option
from discord_slash import SlashCommand, SlashContext


with open("configuracion.json") as f:
    config = json.load(f)

bot = commands.Bot(command_prefix='!', description="ayuda bot") #Comando
bot.remove_command("help") # Borra el comando por defecto !help

slash = SlashCommand(bot, sync_commands=True)
@slash.slash(
    name="sauna", description="Sauna habbo hotel",
    options=[
                create_option(
                  name="keko1",
                  description="Escribe el keko",
                  option_type=3,
                  required=True,
                ),
                create_option(
                  name="keko2",
                  description="Escribe el keko 2",
                  option_type=3,
                  required=True,
                  
                
                  
                ),create_option(
                  name="hotel",
                  description="Elige él hotel",
                  option_type=3,
                  required=True,
                  choices=[
                      create_choice(
                          name="ES - Hotel España",
                          value="es"
                      ),
                      create_choice(
                          name="BR - Hotel Brasil",
                          value="com.br"
                      ),
                      create_choice(
                          name="COM - Hotel Estados unidos",
                          value="com"
                      ),
                      create_choice(
                          name="DE - Hotel Aleman",
                          value="de"
                      ),
                      create_choice(
                          name="FR - Hotel Frances",
                          value="fr"
                      ),
                      create_choice(
                          name="FI - Hotel Finalandia",
                          value="fi"
                      ),
                      create_choice(
                          name="IT - Hotel Italiano",
                          value="it"
                      ),
                      create_choice(
                          name="TR - Hotel Turquia",
                          value="com.tr"
                      ),
                      create_choice(
                          name="NL - Hotel Holandés",
                          value="nl"
                      )
                  ]
                
               
                  
                )
             ])


async def _sauna(ctx:SlashContext, keko1:str, keko2:str, hotel:str):
    await ctx.defer()
    
    response = requests.get(f"https://www.habbo.{hotel}/api/public/users?name={keko1}")

    

    response1 = requests.get(f"https://www.habbo.{hotel}/api/public/users?name={keko2}")

   
    try:

     habbo = response.json()['figureString']
    

  

     habbo1 = response1.json()['figureString']
    except KeyError:
        await ctx.send("Uno de los kekos no existe!")
   

   
    

    
    
   
    try:

     url = "https://www.habbo.com/habbo-imaging/avatarimage?size=m&figure="+ habbo +"&action=sit&direction=4&head_direction=4&gesture=std&size=m"
     img1 = Image.open(io.BytesIO(requests.get(url).content))
     img1 = img1.resize((64,110), Image.ANTIALIAS)#tamaño del keko 1

     url1 = "https://www.habbo.com/habbo-imaging/avatarimage?size=l&figure="+ habbo1 +"&action=sit&direction=4&head_direction=4&gesture=std&size=m"
     habbol = Image.open(io.BytesIO(requests.get(url1).content))
     habbol = habbol.resize((64,110), Image.ANTIALIAS)#tamaño del keko 2
    
    
    


    
    


    

   

    

    
    
    



     img2 = img1.copy()
    
    
    ###

    


     sauna = Image.open(r"imagenes/sauna.png").convert("RGBA") #imagen
     img1 = sauna.resize((300,300), Image.ANTIALIAS)#tamaño de la sauna


     cristal = Image.open(r"imagenes/cristal-1.png").convert("RGBA") #imagen
     img1 = cristal.resize((300,300), Image.ANTIALIAS)#tamaño del cristal de la sauna


     bruma = Image.open(r"imagenes/bruma.png").convert("RGBA") #imagen
     img1 = bruma.resize((300,300), Image.ANTIALIAS)#tamaño de la bruma de la sauna 


     techosauna = Image.open(r"imagenes/techosauna.png").convert("RGBA") #imagen
     img1 = techosauna.resize((300,300), Image.ANTIALIAS)#tamaño del cristal de la sauna


    ###
  
    ###
  

    ###
   

    
    

 
   
    
    
     img1.paste(sauna,(0,0), mask = sauna) #Posicion imagen sauna
    
    
   
  
  

    
    ### 
   
     img1.paste(bruma,(0,0), mask = bruma) #Posicion imagen bruma
     img1.paste(techosauna,(0,0), mask = techosauna) #Posicion imagen techo de la sauna
     img1.paste(habbol,(145,100), mask = habbol) #Posicion del keko 2

     img1.paste(img2,(105,114), mask = img2) #Posicion del keko 1
    
    
     img1.paste(cristal,(0,0), mask = cristal) #Posicion cristal sauna 
   
    
   ###
   
    
   
    ###
    
   
 
    
    
  ####
   
  ###
    




    

    
    
    
   
    
   
       


      
    
       
      

      
    
       
            
        
        
        
       
        
     with io.BytesIO() as image_binary:
         img1.save(image_binary, 'PNG')
         image_binary.seek(0)

         await ctx.send(file=discord.File(fp=image_binary, filename='keko.png'))
    except UnboundLocalError:
        habbo=":("
         
        
        
        
        


@bot.event
async def on_ready():
    print("BOT listo!")
    
bot.run(config["tokendiscord"])   
