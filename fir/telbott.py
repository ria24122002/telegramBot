
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
    /cart->  item present in cart
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
    {'name': 'maggie', 'price': 10, 'quantity': 100, 'weight': 0.5, 'type': 'Type 1', 'brand': 'Brand 1'},
    {'name': 'chips', 'price': 10, 'quantity': 110, 'weight': 1.0, 'type': 'Type 2', 'brand': 'Brand 2'},
    {'name': 'biscuits', 'price': 15, 'quantity': 120, 'weight': 1.0, 'type': 'Type 3', 'brand': 'Brand 3'},
    {'name':'rice','price':30,'quantity':100,'weight':50},
    {'name':'dal','price':25,'quantity':100,'weight':9.0},
    {'name':'Apple','price':80,'quantity':100,'weight':30},
    {'name':'Garam masala','price':10,'quantity':150,'weight':10},
    {'name':'sugar','price':30,'quantity':50,'weight':20}
    
    ]
    print(inventory)
    
    bot.send_message(message.chat.id, "item  price  quantity  weight")
    for item in inventory:
        
        # items=""
        items+= f"{item['name']} - {item['price']}Rs - {item['quantity']}left - {item['weight']} \n"
        # items+=item.name
      
        print(items)
        # bot.send_message(message.chat.id, "item  price  quantity  weight")
        bot.send_message(message.chat.id, items)
@bot.message_handler(['order'])
def order(message):

    msg=bot.send_message(message.chat.id,"what would you like to order!")
    bot.register_next_step_handler(msg,orders_step)
def orders_step(message):
    global ordd
    ordd=message.text
    inventory_items=['rice','dal','maggie','biscuit','sugar','Apple','Garam masala','chips']
    
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
    
    if int(qu) <100:
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
        dict={'rice':20,'dal':10,'maggie':10,'sugar':30,'Apple':80,'chips':10,'biscuits':15,'Garam masala':10}
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
    
    
        
@bot.message_handler(['cart'])
def add_cart(message):
    bot.send_message(message.chat.id,caart)

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
 
  
             
             
        
        

        

        
    
        
        

    
    
#     print(items)
# def inventory_handler(update,context):
#     message="inventory item\n item price quantity weight\n"
#     for item in inventory:
#          message += f"{item['name']} - ${item['price']} - {item['quantity']}left - {item['weight']} \n"
         
#     update.message.reply_text(message)
        
# def content(update,context):
#     update.message.reply_text("rice 20rs , dal 30rs , sweet 50rs, biscuit 10rs")
# def contact(update,context):
#     update.message.reply_text("you can contact us on @riyastore.com for any quries")
# def handle_message(update,context):
#     update.message.reply_text("you saide{update.message.text}")
# def order_handler(update, context):
#     context.user_data['order'] = []
#     update.message.reply_text(text='What would you like to order?')
#     item_name = update.message.text.lower()
#     print(item_name)
# def add_item_handler(update, context):
#     update.message.reply_text("what u want?")
#     item_name = update.message.text.lower()
#     print(item_name)
#     if item_name in inventory:
#         context.bot.send_message( chat_id=update.effective_chat.id,text=f"{item_name} added to your order")
            
#     else:
#          context.bot.send_message(chat_id=update.effective_chat.id, text="Sorry, that item is not available")
            



    
    
# updater=Updater('6051146126:AAHDjXqH5rF--9ub5uXmy7oEHWSUH7Dss5c', use_context=True)
# disp=updater.dispatcher
# disp.add_handler(CommandHandler("start",start))
# disp.add_handler(CommandHandler("help",help))
# disp.add_handler(CommandHandler("item",content))
# disp.add_handler(CommandHandler("contact",contact))
# disp.add_handler(CommandHandler("inventory",inventory_handler))
# disp.add_handler(CommandHandler("order",order_handler))
# disp.add_handler(CommandHandler("add",add_item_handler))
# disp.add_handler(MessageHandler(Filters.text, add_item_handler))
 


# import telegram
# from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# # Define the inventory items and their attributes
# inventory = [
#     {'name': 'Product 1', 'price': 10, 'quantity': 100, 'weight': 0.5, 'type': 'Type 1', 'brand': 'Brand 1'},
#     {'name': 'Product 2', 'price': 20, 'quantity': 50, 'weight': 1.0, 'type': 'Type 2', 'brand': 'Brand 2'},
#     {'name': 'Product 3', 'price': 15, 'quantity': 80, 'weight': 0.8, 'type': 'Type 3', 'brand': 'Brand 3'},
#     # Add more inventory items as necessary
# ]

# # Define the function to display the inventory items
# def inventory_handler(update, context):
#     message = 'Inventory Items:\n'
#     for item in inventory:
#         message += f"{item['name']} - ${item['price']} - {item['quantity']} left\n"
#     context.bot.send_message(chat_id=update.effective_chat.id, text=message)

# # Define the function to initiate the order process
# def order_handler(update, context):
#     context.user_data['order'] = []
#     context.bot.send_message(chat_id=update.effective_chat.id, text='What would you like to order?')

# # Define the function to add an item to the order
# def add_item_handler(update, context):
#     item_name = update.message.text
#     for item in inventory:
#         if item['name'] == item_name:
#             context.user_data['order'].append(item)
#             context.bot.send_message(chat_id=update.effective_chat.id, text=f"{item_name} added to your order")
#             break
#     else:
#         context.bot.send_message(chat_id=update.effective_chat.id, text="Sorry, that item is not available")

# # Define the function to display the final order confirmation message
# def confirm_order_handler(update, context):
#     message = 'Order:\n'
#     total_cost = 0
#     for item in context.user_data['order']:
#         message += f"{item['name']} - ${item['price']}\n"
#         total_cost += item['price']
#     message += f"Total Cost: ${total_cost}"
#     context.bot.send_message(chat_id=update.effective_chat.id, text=message)

# # Define the function to send a message to the store owner
# def send_order_handler(update, context):
#     message = 'New Order:\n'
#     total_cost = 0
#     for item in context.user_data['order']:
#         message += f"{item['name']} - ${item['price']}\n"
#         total_cost += item['price']
#     message += f"Total Cost: ${total_cost}"
#     context.bot.send_message(chat_id=STORE_OWNER_CHAT_ID, text=message)

# # Define the function to display the order status
# def status_handler(update, context):
#     # Implement the logic to retrieve the order status from the store owner or a database
#     order_status = "Order Placed"
#     context.bot.send_message(chat_id=update.effective_chat.id, text=order_status)

# # Set up the bot with the handlers
# TOKEN = '6051146126:AAHDjXqH5rF--9ub5uXmy7oEHWSUH7Dss5c'
# STORE_OWNER_CHAT_ID = 'your_store_owner_chat_id_here'
# updater = Updater(token=TOKEN, use_context=True)
# dispatcher = updater.dispatcher
# dispatcher.add_handler(CommandHandler('inventory', inventory_handler))
# dispatcher.add_handler(CommandHandler('order', order_handler))



# updater.start_polling()
# updater.idle()







bot.polling()
