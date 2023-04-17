
import time
import telebot
from telegram.ext import Updater,CommandHandler,MessageHandler,Filters
#  bot's token obtained from BotFather
Token='6051146126:AAHDjXqH5rF--9ub5uXmy7oEHWSUH7Dss5c'
bot=telebot.TeleBot(Token)

#start conversation
@bot.message_handler(['start'])
def start(message):
    name=message.chat.first_name
    
    bot.send_message(message.chat.id,"welcome to Riya Store" + name)
    bot.send_message(message.chat.id,""" The following  commands are avaible:
    /start-> Welcome message
    /inventory-> inventory item
    /order->place order
    /help-> to  get your problem resolved
    /Jobs_opening->See openings
    /contact-> inforamtion about store """)
    
    
# inventory available
@bot.message_handler(['inventory'])

def inventory(message):
    
    
    bot.send_message(message.chat.id,"Available items ")
    inventory=[
    {'name': 'maggie', 'price': 10, 'quantity': 100, 'weight': 0.5, 'brand':'yepiee'},
    {'name': 'chips', 'price': 10, 'quantity': 110, 'weight': 1.0, 'brand':'Bingo'},
    {'name': 'biscuits', 'price': 15, 'quantity': 120, 'weight': 1.0, 'brand':'Britannia'},
    {'name':'rice','price':30,'quantity':100,'weight':50,'brand':'Bullet'},
    {'name':'dal','price':25,'quantity':100,'weight':9.0,'brand':'Cjh'},
    {'name':'Apple','price':80,'quantity':100,'weight':30,'brand':'apple'},
    {'name':'Garammasala','price':10,'quantity':90,'weight':10,'brand':'aachi'},
    {'name':'sugar','price':30,'quantity':50,'weight':20,'brand':'Madhur'},
    {'name':'kurkure','price':10,'quantity':90,'weight':0.9,'brand': 'Takatak'}
    
    ]
    print(inventory)
    
    bot.send_message(message.chat.id, "Item  Price  Quantity  Weight  Brand")
    for item in inventory:
        
        items=""
        items+= f"{item['name']} - {item['price']}Rs - {item['quantity']}left - {item['weight']} -{item['brand']}\n"
        # items+=item.name
      
        
        # bot.send_message(message.chat.id, "item  price  quantity  weight")
        bot.send_message(message.chat.id, items)
@bot.message_handler(['order'])
def order(message):

    msg=bot.send_message(message.chat.id,"what would you like to order!")
    bot.register_next_step_handler(msg,orders_step)
def orders_step(message):
    global ordd
    ordd=message.text
    inventory_items=['rice','dal','maggie','biscuit','sugar','Apple','Garam masala','chips','kurkure']
    
    if ordd in inventory_items:
        bot.send_message(message.chat.id,"great this item is availble!!")
        quant=bot.send_message(message.chat.id,"how much quantity you want")
        bot.register_next_step_handler(quant,quant_step)
    else:
        bot.send_message(message.chat.id,"Sorry!!!! not availble now")
 #function to check how much quantity is required       
def quant_step(message):
    print(ordd)
    global qu
    qu=message.text
    
    if int(qu) <=100:
        bot.send_message(message.chat.id,"ok done!!!!")
        ca=bot.send_message(message.chat.id,"Would you like to add this to cart and Checkout!!")
        bot.register_next_step_handler(ca,carts_step)
        
    else:
        bot.send_message(message.chat.id,"not available")
#function to add to cart and send order summary And send to "Store owner for confirmation"
def carts_step(message):
    global caart
    caart={}
    ans=message.text
    if ans=='yes'or'YES' or 'Yes':
        caart.update({ordd:qu})
        dict={'rice':20,'dal':10,'maggie':10,'sugar':30,'Apple':80,'chips':10,'biscuits':15,'Garam masala':10,'kurkure':10}
        for k in dict:
            if k ==ordd:
                s=dict[ordd]
                global q
                q=int(qu)*int(s)
                bot.send_message(message.chat.id,"Order Summary is:\n")
                bot.send_message(message.chat.id,"U have ordered:"+ordd+"-and your total cost is:"+str(q))
                bot.send_message(chat_id='6075950603',text="Customer has  ordered" +ordd+ "-total cost:"+str(q))#confirmation to store owner
    # bot.register_next_step_handler(ress,owner_confirm
                bot.send_message(message.chat.id,"Waiting for confirmation")
                time.sleep(2)
                bot.send_message(message.chat.id,"Hehee your order has been placed!!!")
        # bot.send_message(message.chat.id,caart)
    else:
        print("hi")
        bot.send.message(message.char.id,"Keep shoping")
    # dict={'rice':20,'dal':10,'maggie':10,'sugar':30,'Apple':80,'chips':10,'biscuits':15,'Garam masala':10}
    # for k in dict:
    #     if k ==ordd:
    #         s=dict[ordd]
    #         global q
    #         q=int(qu)*int(s)
    # bot.send_message(message.chat.id,"Order Summary is:\n")
    # bot.send_message(message.chat.id,"U have ordered:"+ordd+"-and your total cost is:"+str(q))
    # bot.send_message(chat_id='6075950603',text="Customer has  ordered" +ordd+ "-total cost:"+str(q))#confirmation to store owner
    # # bot.register_next_step_handler(ress,owner_confirm
    
    # bot.send_message(message.chat.id,"Waiting for confirmation")
    # time.sleep(2)
    # bot.send_message(message.chat.id,"Hehee your order has been placed!!!")
# def owner_confirm(message):
#     respond=message.text
#     print(respond)
#     if respond=='yes':
#         bot.send_message(message.chat.id,"your order has been placed")
#     else:
#         bot.send_message("order declined")
        
    

#     res=bot.send_message(message.chat.id,"ord")
#     bot.register_next_step_handler(res,confirmation)
# def confirmation(message):
#     answer=message.text
#     if answer=='yes'or 'Yes'or 'YES':
#         bot.send_message(message.chat.id,"Your order has been placed!! \n Thank you!! Keep Shoping")
    
    
        
# @bot.message_handler(['cart'])
# def add_cart(message):
#     bot.send_message(message.chat.id,caart)

@bot.message_handler(['price'])  
def get_price(message):
    dict={'rice':20,'dal':10,'maggie':10,'sugar':30,'Apple':80,'chips':10,'biscuits':15,'Garam masala':10}
    for k in dict:
        if k ==ordd:
            s=dict[ordd]
            global q
            q=int(qu)*int(s)
            bot.send_message(message.chat.id,q)
# Function to get notified  about job openings 
@bot.message_handler(['Jobs_opening'])
def Jobs_opening(message):
    bot.send_message(message.chat.id,"You are at the right place!!! \n We are hiring Delivery patner..\n Hurry up if u are interested contact us on 8568439217 for further details ")
 
  
             
             
        
        

        

        
    
        
bot.polling()
