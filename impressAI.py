import mysql.connector
import os
import random
import telegram
from telegram.ext import Updater, MessageHandler, Filters

def Msg(update,context):
    
    chat_id = update.effective_chat.id
    message_id = update.message.message_id
    user_msg = update.message.text 
    u_name= update.message.from_user.username
    #print(u_name)
    mycursor.execute("SELECT user FROM impress")
    bt = mycursor.fetchall()
    dta=[]
    tt=[]
    for row in bt:
        dta.append(list(row))
    for row in dta:
        tt=row
        #print(tt)
    if len(tt)>0:
        check=tt[0]
    else:
        check= None
    #print(check)
    tot = []
    stp=[]
    ft=[]
    dmp=[]
    data=[]
    mycursor.execute("SELECT TOTAL FROM ai")
    result = mycursor.fetchall()
    for row in result:
        data.append(list(row))
    for row in data:
        tot=row
    val=tot[0]
    mycursor.execute("SELECT stupid FROM ai")
    resul = mycursor.fetchall()
    dat = []
    for row in resul:
        dat.append(list(row))
    for row in dat:
        stp=row
    a=stp[0]
    mycursor.execute("SELECT fat FROM ai")
    resu = mycursor.fetchall()
    da = []
    for row in resu:
        da.append(list(row))
    for row in da:
        ft=row
    b=ft[0]
    mycursor.execute("SELECT dump FROM ai")
    res = mycursor.fetchall()
    d = []
    for row in res:
        d.append(list(row))
    for row in d:
        dmp=row
    c=dmp[0]
    #print(user_msg)
    stu=1
    fa=1
    dmp=1
    #print(check,"sdfsdfsdf")
    if check == u_name:
        mycursor.execute("SELECT stupid FROM impress")
        install = mycursor.fetchall()
        l = []
        for row in install:
            l.append(list(row))
        for row in l:
            sp=row
        stup=sp[0]
        mycursor.execute("SELECT fat FROM impress")
        insta = mycursor.fetchall()
        m = []
        for row in insta:
            m.append(list(row))
        for row in m:
            ft=row
        ffat=ft[0]
        mycursor.execute("SELECT dumb FROM impress")
        ins = mycursor.fetchall()
        n = []
        for row in ins:
            n.append(list(row))
        for row in n:
            db=row
        dumbb=db[0]
        
        if (user_msg=="/stupid"):
            stupid=["""Yo' Mama is so stupid, she needs a recipe to make ice cubes.""",
                """Yo' Mama is so stupid, she thinks DNA is the National Dyslexics Association"""]
            messg=random.choice(stupid)
            update.message.reply_text(messg)
            w=a+1
            tt=val+1
            stupidd=stup+1
            #print(a,val)
            mycursor.execute("UPDATE ai SET stupid=%s where stupid=%s",(w,a))
            mycursor.execute("UPDATE ai SET total=%s where total=%s",(tt,val))
            mycursor.execute("UPDATE impress SET stupid=%s where stupid=%s",(stupidd,stup))
            mydb.commit()
        elif (user_msg=="/fat"):
            fat=["""Yo' Mama is so fat, when she goes to a restaurant, instead of a menu, she gets an estimate.""",
             """ Yo' Mama is so fat, when the cops see her on a street corner, they yell, "Hey you guys, break it up!" """]
            messg=random.choice(fat)
            update.message.reply_text(messg)
            w=b+1
            tt=val+1
            fatt=ffat+1
            #print(a,val)
            mycursor.execute("UPDATE ai SET fat=%s where fat=%s",(w,b))
            mycursor.execute("UPDATE ai SET total=%s where total=%s",(tt,val))
            mycursor.execute("UPDATE impress SET fat=%s where fat=%s",(fatt,ffat))
            mydb.commit()
        elif(user_msg=="/dumb"):
            dumb=["""Yo' Mama is so dumb, when God was giving out brains, she thought they were milkshakes and asked for extra thick.""",
                  """Yo' Mama is so dumb, she locked her keys inside her motorcycle."""]
            messg=random.choice(dumb)
            update.message.reply_text(messg) 
            w=c+1
            tt=val+1
            ddumb=1+dumbb
            #print(a,val)
            mycursor.execute("UPDATE ai SET dump=%s where dump=%s",(w,c))
            mycursor.execute("UPDATE ai SET total=%s where total=%s",(tt,val))
            mycursor.execute("UPDATE impress SET dumb=%s where dumb=%s",(ddumb,dumbb))
            mydb.commit()
        else:
            update.message.reply_text("Invalid message")  
        #check=mycursor.execute(f"SELECT * FROM ai WHERE chatid LIKE '%{chat_id}%'") 
        
    else:
        if (user_msg=="/stupid"):
            stupid=["""Yo' Mama is so stupid, she needs a recipe to make ice cubes.""",
                    """Yo' Mama is so stupid, she thinks DNA is the National Dyslexics Association"""]
            messg=random.choice(stupid)
            update.message.reply_text(messg)
            w=a+1
            tt=val+1
            mycursor.execute("UPDATE ai SET stupid=%s where stupid=%s",(w,a))
            mycursor.execute("UPDATE ai SET total=%s where total=%s",(tt,val))
            mycursor.execute("INSERT INTO impress (id ,user , stupid) VALUES (%s,%s,%s)",(chat_id,u_name,stu))
            mydb.commit()
            
        elif (user_msg=="/fat"):    
            fat=["""Yo' Mama is so fat, when she goes to a restaurant, instead of a menu, she gets an estimate.""",
                 """ Yo' Mama is so fat, when the cops see her on a street corner, they yell, "Hey you guys, break it up!" """]
            messg=random.choice(fat)
            update.message.reply_text(messg)
            w=b+1
            tt=val+1
            mycursor.execute("UPDATE ai SET fat=%s where fat=%s",(w,b))
            mycursor.execute("UPDATE ai SET total=%s where total=%s",(tt,val))
            mycursor.execute("INSERT INTO impress (id ,user , fat) VALUES (%s,%s,%s)",(chat_id,u_name,fa))
            mydb.commit()
        elif(user_msg=="/dumb"):
            dumb=["""Yo' Mama is so dumb, when God was giving out brains, she thought they were milkshakes and asked for extra thick.""",
                  """Yo' Mama is so dumb, she locked her keys inside her motorcycle."""]
            messg=random.choice(dumb)
            update.message.reply_text(messg) 
            w=c+1
            tt=val+1
            mycursor.execute("UPDATE ai SET dump=%s where dump=%s",(w,c))
            mycursor.execute("UPDATE ai SET total=%s where total=%s",(tt,val))
            mycursor.execute("INSERT INTO impress (id ,user , dumb) VALUES (%s,%s,%s)",(chat_id,u_name,dmp))
            mydb.commit()
        else:
            update.message.reply_text("Invalid message")  
        
        #print(u_name)
        
        
bot_token = "5928864582:AAGJDMFWEnWemP5wAr_zjLBSD-2jKKzpFIY"
try:
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="impressai")
except error as e:
    print("error")   
mycursor = mydb.cursor()

#mycursor.execute("UPDATE ai SET total=0, WHERE Name='Kriti'")
updater = Updater(bot_token, use_context=True)
dispatcher = updater.dispatcher
dispatcher.add_handler(MessageHandler(Filters.text, Msg))
updater.start_polling()
updater.idle()



'''import telebot
import random

bot_token ='6211989392:AAF04yaB3IP0fKeacWm-mPnLrLqORRWg9fQ'

bot= telebot.TeleBot(token=bot_token)

lang1= ['Hola','Konnichiwa','Bonjour','Namaste']

# Handle normal messages
@bot.message_handler()
def send_welcome(message):

    # Detect Messages
    if message.text == 'hi' or message.text == 'hello':
        bot.send_message(message.chat.id, (random.choice(lang1)))
    elif message.text == 'Test':
        bot.send_message(message.chat.id, 'Test succeeded')
    else:
        bot.send_message(message.chat.id, 'Sorry I don\'t get it!')

'''