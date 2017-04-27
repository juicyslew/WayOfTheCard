"""
This code starts creating the images for the cards.

Step 1. create edit an image based on a word.

idea: blend the images,
turn them into lists of tupples,
 loop through tuples replace them with 255,255,255 if origional image is that
 turn list of tuples back into an image.
make image into 16:9 ratio
9l/16 = x
 """
import random
import math
import colorsys
from PIL import Image


dict_special_children = {"frozen": "whole Image", "hellhound":"needs to be added onto top and right","titan":"needs to have black background replaced","black": "needs to have a stronger blend", "demon":"needs to be cropped from bottom and right", "siren": "needs to be cropped only from bottom"}
b = "both"
x = "x"
y = "y"

dict_paded = {"spell1":(1,b), "angel":(0,b), "bear":(0,b), "cat":(0,b),"giant":(0,x), "griffin":(0,b), "person": (0,x), "golem":(0,x),
              "shaman":(0,x),"prophet":(0,x),"succubis":(0,x), "hydra":(0,x), "basilisk":(0,x), "satyr":(0,x),"minotaur":(0,x), "fish": (0,y),
              "wolf":(0,x), "ooze":(0,x), "protector":(0,x),"goblin":(0,x), "destroyer": (0,y),"ape":(0,x),"roc":(0,x), "beast":(0,x),"colossus":(0,x),"dwarf":(0,x),"sphinx":(0,x),
              "ravager":(0,x),"rogue":(0,x),"knight":(0,x),"tiger":(0,x),"unicorn":(0,x),"eater":(0,x),
              "king":(0,x),"gremlin":(0,x),"orc":(0,x),"fungus":(0,x),"god":(0,x),"leviathan":(0,x),
              "cleric":(0,x),"sprite":(0,x), "vagabond":(0,x), "reaper":(0,x),"eagle":(0,y),"sheild":(0,x), "fairy":(0,x),"elemental":(0,x)}

#1 = black
#0 = white
blend_back = ["griffin","shaman","prophet","hydra","basilisk","satyr", "minotaur",
              "fish", "ooze","protector","ape","beast","colossus","dwarf","sphinx",
              "ravager","rogue","king","god","cleric","sprite","vagabond","demon","acid","angel","giant"]

problem_children = []

blend_whole = ["frozen"]

noun_list= ["sofa","cat","mage","horror","bear","warrior", "soldier","shade",
            "angel","demon","elf","elemental","phoenix","hero","wizard",
            "dragon","fairy","hellkite","horse","leech","troll","giant","griffen",
            "person","golem","shaman","prophet", "siren",
            "succubis", "hydra","basilisk", "satyr", "minotaur", "fish","gargoyle", "wolf", "ooze", "protector",
            "goblin", "destroyer","ape","roc","beast","colossus", "titan","dwarf","sphinx",
            "ravager","hellhound", "rogue","knight","tiger","unicorn","eater","king","gremlin"
            ,"orc","fungus","god","leviathan","cleric","vagabond","reaper","eagle","sprite"
            ]

name_list = ["fire", "slash", "ice", "sword", "destruction",
             "absolute", "death", "black", "abyssal", "growth", "charm",
             "cloud", "rain", "flame", "flare", "horror",
             "aegis", "honor", "mystic", "barrier", "burst", "aether",
             "meltdown", "rift", "shockwave", "lightning", "thunder",
             "hell", "storm", "ancient", "agility", "warp",
             "nature", "damaged", "wrath", "sun",
             "shadow", "light", "dark", "destiny", "ruin", "soul",
             "broke", "frozen", "earth","smite","edge","shield", "acid", "charge","shock", "tide","renegade","aim",
             "vengeance", "sudden", "frozen", "absolute","acid","charge","destiny", "frozen",
             "honor", "mystic", "slash", "wrath"]

special_adj = [ "scornful", "vengeful", "colossal",  "minor", "major","virtuous",  "earth","forgotten","frozen","fungal","black","ancient","ice","fire","crafty","white","unholy","dark","deadly","wandering","red","flushed","brutal",]

overlay = ["unholy","deadly","wandering","virtuous","vengeful"]
#wadering has a watermark so be careful


name_blend_ratios_special= {"aegis": 0.25,"black":0.75}
special = ["siren","hellhound"]

def fix_image(filename,name):
    """This function fixes the image up into the right size and shape for the card
    It also saves the origional image

    It can:
        1. crop
            - can specify from where to crop
        2. pad image
            - can specify which axis
            - can specify which color
            - use image paste to paste image onto a resized version of of the image.
    """
    image = Image.open(filename)
    image.save("ImageStuff/untouched/"+name.lower()+ ".jpg")
    size = image.size
    if name in dict_paded.keys():
        #checking to see if I need to pad the image instead of cropping it.
        boop = dict_paded[name]
        #set the touple to a variable because I am lazy and do not want to write dict_padded a bunch
        if boop[0] == 1:
            #we need to have a black packground pad.
            backdrop = Image.open("imagelib/box_black.jpg")
            #backdrop is a plain black image
            if boop[1]== b:
                #not sure what to do yet. need to pad 'both'
                print("moo")
            elif boop[1] == x:
                #need to pad x with black
                new_width = int(16*size[1]/9)
                backdrop = backdrop.resize((new_width,size[1]))
                backdrop.paste(image,((new_width-size[0])//2,0))
                fin = backdrop.resize((480,270))
                fin.save(filename)
            else:
                #need to pad y with black.
                new_height = int(9*size[0]/16)
                backdrop = backdrop.resize((size[0],new_height))
                backdrop.paste(image,(0,(new_height-size[1])//2))
                fin = backdrop.resize((480,270))
                fin.save(filename)
        else:
            #we need to have a white background pad.
            backdrop = Image.open("ImageStuff/imagelib/box_white.jpg")
            #backdrop is a plain white image
            if boop[1] == x or boop[1] == b:
                #need to pad x with white
                new_width = int(16*size[1]/9)
                backdrop = backdrop.resize((new_width,size[1]))
                backdrop.paste(image,((new_width-size[0])//2,0))
                fin = backdrop.resize((480,270))
                fin.save(filename)
            else:
                #need to pad y with white.
                new_height = int(9*size[0]/16)
                backdrop = backdrop.resize((size[0],new_height))
                backdrop.paste(image,(0,(new_height-size[1])//2))
                fin = backdrop.resize((480,270))
                fin.save(filename)
    elif name in special:
        if name == "hellhound":
            backdrop = Image.open("ImageStuff/imagelib/box_white.jpg")
            new_width = int(16*size[1]/9)
            backdrop = backdrop.resize((new_width,size[1]))
            backdrop.paste(image,(0,0))
            fin =backdrop.resize((480,270))
            fin.save(filename)
        elif name == "siren":
            newheight = int(9*size[0]/16)
            cropped = image.crop((0,0,size[0],((newheight))))
            fin = cropped.resize((480, 270))
            fin.save(filename)
    else:
        newheight = int(9*size[0]/16)
        cropped = image.crop((0,((size[1]-newheight)//2),size[0],size[1]-((size[1]-newheight)//2)))
        fin = cropped.resize((480, 270))
        fin.save(filename)
    return fin



def genimage_dudes(adj, adj2= 'NONE', noun= "sofa",adj_s = 'NONE'):
    """adj are the adjictives from noun_name in randGen
    adj_s are the adjictives in ajictive list"""
    nounnam = noun
    adj1nam = adj
    if adj == "NONE":
        adj = noun
    if noun == "NONE":
        noun = random.choice(noun_list)
        if adj== "NONE":
            adj = random.choice(name_list)
    blendy = (0.5,0.5)
    noun_name  ="ImageStuff/imagelib/"+ noun.lower() + ".jpg"
    adj_name ="ImageStuff/imagelib/"+adj.lower() + ".jpg"
    adj1_i =  Image.open(adj_name)
    noun_image = Image.open(noun_name)
    nam3 = ""
    if noun_image.size != (480,270):
        noun_image = fix_image(noun_name,noun)
    if adj1_i.size != (480,270):
        adj1_i = adj1_i.resize((480,270))
        adj1_i.save(adj_name)
    if adj2 != 'NONE':
        adj2_name ="ImageStuff/imagelib/"+adj2 + ".jpg"
        adj2_i= Image.open(adj2_name)
        if adj2_i.size != (480,270):
            adj2_i = adj2_i.resize((480,270))
            adj2_i.save(adj2_name)
        effect_image =  Image.blend(adj1_i,adj2_i, blendy[0])
        nam2 = adj2
        blendy = (blendy[0],0.6)
    else:
        effect_image = adj1_i
        nam2 = ""
    if noun.lower() in blend_back or noun.lower() == "acid":
        blendy = (blendy[0],0.99)
    noun_image = noun_image.convert('RGB')
    effect_image = effect_image.convert('RGB')
    final =Image.blend(noun_image,effect_image,blendy[1])
    pix = final.load()
    size = (480,270)
    almost_white = 220
    if noun.lower() == 'angel'or noun.lower()=='beast' or noun.lower() == "god" or noun.lower() == "prophet":
        almost_white = 230
    super_white = ["sofa", "cleric","sphinx"]
    if noun.lower() == "sofa" or noun.lower()=="cleric" or noun.lower == "sphinx":
        almost_white = 250
    if noun.lower() in blend_back:
        for i in range(size[0]):
            for j in range(size[1]):
                origional = noun_image.getpixel((i,j))
                average =  (origional[0]+origional[1]+ origional[2])/3
                if average < almost_white:
                    pix[i,j]= (origional)
    elif noun.lower() == "titan" :
        for i in range(size[0]):
            for j in range(size[1]):
                origional = noun_image.getpixel((i,j))
                if origional == (0,0,0):
                    pix[i,j]= (0,0,0)
    elif  noun.lower() not in blend_back and not noun.lower()=="titan":
        for i in range(size[0]):
            for j in range(size[1]):
                origional = noun_image.getpixel((i,j))
                average =  (origional[0]+origional[1]+ origional[2])/3
                if average > almost_white:
                    pix[i,j]= (255,255,255)

    if adj_s != 'NONE':
        nam3 = adj_s
        if adj_s in overlay:
            nam3 = adj_s
            if nam3 == "ancient":
                adj_s = "ancient2"
            adj_s_i = Image.open("ImageStuff/imagelib/"+adj_s+".jpg")
            if adj_s_i.size != (480,270):
                adj_s_i = adj_s_i.resize((480,270))
                adj_s_i.save("ImageStuff/imagelib/"+adj_s+".jpg")
            if nam3 in overlay:
                prefinal = Image.blend(final,adj_s_i,0.99)
                pix2 = prefinal.load()
                for i in range(size[0]):
                    for j in range(size[1]):
                        origional = final.getpixel((i,j))
                        overlay2 = adj_s_i.getpixel((i,j))
                        average = (overlay2[0]+overlay2[1]+overlay2[2])/3
                        if average > almost_white :
                            pix2[i,j]= origional
                final = prefinal
        else:
            if adj_s == "ancient":
                adj_s = "ancient2"
            adj_s_i = Image.open("ImageStuff/imagelib/"+adj_s+".jpg")
            adj_s_i= adj_s_i.resize((480,270))
            final = Image.blend(final,adj_s_i,0.4)
    final.convert("RGBA")
    final.save("ImageStuff/finimages/"+nounnam+adj1nam+nam2+nam3+".jpg")
    return final
    #final.save("")




def genimage_does():
    """ This does spell Generation"""
    pass


def wipe_folder():
    """ this wipes the folder of all images.  """
    pass

if __name__ == '__main__':
    for n in range(50):
        genimage_dudes(random.choice(name_list), adj2 = random.choice(name_list),noun = random.choice(noun_list),adj_s = random.choice([random.choice(special_adj),"NONE","NONE"]))
