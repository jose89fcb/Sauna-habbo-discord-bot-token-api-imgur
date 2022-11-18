import json
import requests
import discord
from discord.ext import commands
import io
import time
from PIL import Image, ImageDraw, ImageFont, ImageFile



with open("configuracion.json") as f:
    config = json.load(f)

bot = commands.Bot(command_prefix='!', description="ayuda bot") #Comando
bot.remove_command("help") # Borra el comando por defecto !help

@bot.command()
async def sauna(ctx,   keko, *, keko2):
    await ctx.message.delete()
    await ctx.send("Generando Sauna de habbo...", delete_after=0)
    time.sleep(3)
    
    response = requests.get(f"https://www.habbo.es/api/public/users?name={keko}")

    

    response1 = requests.get(f"https://www.habbo.es/api/public/users?name={keko2}")

   
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
