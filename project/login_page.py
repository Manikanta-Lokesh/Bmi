from tkinter import *
import tkinter as tk 
from tkinter import ttk 
from tkinter import messagebox
from PIL import Image,ImageTk
import ast

root=Tk()
root.title('Login')
root.geometry('925x500+300+200')
root.configure(bg='#fff')
root.resizable(False,False)

def signin() :
    username=user.get()
    password=code.get()
    
    file=open('datasheet.txt','r')
    d=file.read()
    r=ast.literal_eval(d)
    file.close()
    
    # print(r.keys())
    # print(r.values())
    
    if username in r.keys() and password==r[username] :
        # import sample
        # screen=Toplevel(root)
        # screen.title("App")
        # screen.geometry('925x500+300+200')
        # screen.config(big="white")
        
        # Label(screen,text="Hello Everyone!",bg='#fff',font=('Calibri(Body)',50,'bold')).pack(expand=True)
        # # Label(screen,text="Hello").pack()
        # screen.mainloop()

        root =Tk()
        root.title("MakeMyDiet")
        root.geometry("470x580+300+200")
        root.resizable(False,False)
        root.configure(bg="#f0f1f5")



        def BMI():
            h=float(Height.get())
            w=float(Weight.get())
            
            m=h/100
            bmi=round(float(w/m**2),2)
            label1.config(text=f"{bmi}"+"Kg/m^2")
            
            
            if bmi<=18.5:
                label2.config(text="Underweight")
                label3.config(text="You have lower weight then normal body!")
            
            elif bmi>18.5 and bmi<=25:
                label2.config(text="Normal!")
                label3.config(text="It indicates that you are healthy!")
            elif bmi>25 and bmi<=30:
                label2.config(text="Overweight")
                label3.config(text="It indicates that a person is \n slighty overweight !\n A doctor may advise to lose some \n weight for health reasons!")
            else:
                label2.config(text="Obes!")
                label3.config(text="Health may be at risk ,if they do not \n lose weight!")
            
            def menu():
                
                new=Tk()
                new.title("MakeMyDiet")
                # new.attribute("-fullscreen",True)
                new.configure(bg="#f0f1f5")
                new.geometry("200x200")
                new.state("zoomed")
                new.rowconfigure(0,weight=1)
                new.columnconfigure(0,weight=1)
                
                # image_icon=tk.PhotoImage(file="python_pratice/Python_App/App_icon.png")
                # new.iconphoto(False,image_icon)
                def show_frame(frame):
                    frame.tkraise()
                
                
            
                frame1=Frame(new,width=600,height=400)
                # frame1.pack()
                # frame1.place(anchor='center',relx=0.5,rely=0.5)
                # img=ImageTk.PhotoImage(Image.open("python_pratice/Python_App/pullups.jpg"))
                # label=Label(frame1,image=img)
                # label.pack()
                frame2=Frame(new,bg='white')
                frame3=Frame(new,bg='white')
                frame4=Frame(new,bg='white')
                for frame in (frame1,frame2,frame3,frame4):
                    frame.grid(row=0,column=0,sticky="nsew")
                
                
                
        ####################### Frame 1 code #######################       
                
                frame1_diet=tk.Button(frame1,text="Exercise",height=5,width=20,background="lightgreen",fg="black",command=lambda:show_frame(frame2))
                frame1_diet.place(x=550,y=400)
                # frame1_exercise=Button(frame1,image=diet_image,command=lambda:show_frame(frame3))
                frame1_exercise=Button(frame1,text=' diet',height=5,width=20,background="lightgreen",fg="black",command=lambda:show_frame(frame3))
                frame1_exercise.place(x=850,y=400)
                # show_frame(frame1)
                frame2_next=Button(frame2,text='Back',height=5,width=20,fg="black",command=lambda:show_frame(frame1))
                frame2_next.place(x=300,y=700)
        ####################### Frame 1 code #######################       
                
                frame2_back=Button(frame2,text = 'Next',height=5,width=20,fg="black",command=lambda:show_frame(frame4))
                frame2_back.place(x=500,y=700)
                frame3_back=Button(frame3,text = 'BACK',command=lambda:show_frame(frame1))
                frame3_back.place(x=300,y=770)
                frame4_back=Button(frame4,text = 'BACK',command=lambda:show_frame(frame2))
                frame4_back.place(x=600,y=700)
                
                if bmi<=18.5:
                    frame1_title=Label(frame1, text="You are Under weight",font="bold 20 italic",bg="red")
                    frame1_title.pack(fill='x')
                    Label(frame2,text="EXERCISE PLAN UNDERWEIGHT TO NORMAL WEIGHT",font="arial 15",bg="lightblue").pack()#place(x=8,y=28)
                    text1='''Female and male bodies store fat Trusted Source and distribute  muscle massTrusted Source differently.
                    Focus on the exercises that give you the most promising results for your body type.                  
                    '''
                    Label(frame2,text=text1,font="arial 15",bg='white').place(x=12,y=32)
                    Label(frame2,text="Pushups:\n",font="arial 15 bold",bg="white").place(x=10,y=110)
                    Label(frame2,text="Pushups are simple and help build muscle in your arms and shoulders.To do a pushup:",font="arial 15",bg="white").place(x=12,y=140)
                    text='''
                    1.	Lie face down on the ground.
        2.	Put your hands on the ground, palms flat, with your arms out at your sides and your hands shoulder-width apart.
        3.	Slowly push your body up until your arms are fully extended. Keep your back and legs straight so that your body makes a straight line.
        4.	Slowly lower yourself back down until your nose nearly touches the floor.
        5.	Repeat as many times as you feel comfortable.

                    '''
                    Label(frame2,text=text,font="arial 15",bg="white").place(x=25,y=165)
                    Label(frame2,text="Pullups:\n",font="arial 15 bold",bg="white").place(x=10,y=310)
                    Label(frame2,text="You'll need some kind of pullup bar or sturdy cylindrical object to do pullups. Otherwise, this exercise is a simple way to build arm and shoulder muscles:",font="arial 15",bg="white").place(x=12,y=340)
                    text='''1.	Grip the pullup bar with both hands. Your palms should face away from you. Keep your arms shoulder-width apart.
        2.	Pull yourself up enough to hang off the bar so that your feet aren't touching the ground and your arms are straight.
        3.	Continue to pull yourself up until your chin is above the bar.
        4.	Slowly lower yourself down so that your arms are straight again.
        5.	Repeat as many times as you want.
        '''
                    Label(frame2,text=text,font="arial 15",bg="white").place(x=25,y=370)
                    
                    Label(frame2,text="Squats:\n",font="arial 15 bold",bg="white").place(x=10,y=480)
                    Label(frame2,text="You'll need some kind of pullup bar or sturdy cylindrical object to do pullups. Otherwise, this exercise is a simple way to build arm and shoulder muscles.",font="arial 15",bg="white").place(x=12,y=510)
                    text='''
                    1.	Grip the pullup bar with both hands. Your palms should face away from you. Keep your arms shoulder-width apart.
        2.	Pull yourself up enough to hang off the bar so that your feet aren't touching the ground and your arms are straight.
        3.	Continue to pull yourself up until your chin is above the bar.
        4.	Slowly lower yourself down so that your arms are straight again.
        5.	Repeat as many times as you want.

        '''
                    Label(frame2,text=text,font="arial 15",bg="white").place(x=25,y=540)
                    Label(frame4,text="Lunges:\n",font="arial 15 bold",bg="white").place(x=10,y=20)
                    Label(frame4,text="You can do this exercise anywhere. It's great for bulking up and toning your leg and butt muscles.",font="arial 15",bg="white").place(x=12,y=50)
                    text='''1.	Stand up straight, flexing your abdominal muscles.
        2.	Extend one leg like you're taking a step, then lean forward like you're kneeling until your knees are at 90-degree angles.
        3.	Push back on your heel to lift yourself back up to your initial position.
        4.	Repeat as many times as you feel comfortable on one leg.
        5.	Repeat for the other leg.
        '''
                    Label(frame4,text=text,font="arial 15",bg="white").place(x=20,y=75)
                    
                    # pullups=PhotoImage(file="python_pratice/Python_App/pullups.png")
                    # pullups_image=Label(frame4,image=pullups)
                    # pullups_image.grid(row=0,column=0,padx=5,pady=5)
                    # pullups_image.place(x=30,y=350)
                    
                    
                    
                    Label(frame3,text="DIET PLAN  FOR UNDERWEIGHT TO NORMAL WEIGHT",font="arial 15",bg="lightblue").pack()#place(x=8,y=28)
                    text='''
                    It's not hard to gain weight by eating more. But be mindful of what you to eat 
                gain healthy weight. A diet to bulk up mainly consists of healthy fats, proteins, 
                and complex carbohydrates that help build muscle and use fat to burn energy.
                    '''
                    Label(frame3,text="What to eat to bulk up\n",font="arial 15 bold",bg="white").place(x=8,y=35)
                    Label(frame3,text=text,font="arial 15",bg="white").place(x=15,y=70)
                
                    Label(frame3,text="Try some of the following foods:",font="arial 15",bg="white").place(x=12,y=190)

                    text=''' 
        1.lean proteins, such as chicken and fish
        2.red meat with no growth hormones, such as grass-fed beef
        3.eggs
        4.full-fat dairy, such as whole milk and full-fat Greek yogurt
        5.fat-rich fruits, such as avocados
        6.nuts, such as almonds
        7.whole-grain breads       
                    '''
                    Label(frame3,text=text,font="arial 15",bg="white").place(x=15,y=220)
                    text='''
        Take notes of what you eat in a journal or an app that tracks nutrients.
        It's surprisingly hard to know exactly how much you eat unless you write 
        it down. You may find that you aren't consuming enough calories or that your food 
        choices aren't nutritious enough for a healthy diet.

        Keeping track of your habits in a journal can help you optimize your intake of healthy
        fats and proteins, cut out junk food, and track your calorie consumption over time.

        Talk to a doctor, nutritionist, or personal trainer about achieving a healthy weight gain.
        A holistic approach will get you the best results. Get in reasonable and regular amounts of
        exercises targeted at building muscle, eat healthy fats and proteins, and build a lifestyle around 
        rest, relaxation, and self-care.

                    '''
                    Label(frame3,text=text,font="arial 15",bg="white").place(x=10,y=420)
                    
                elif bmi>18.5 and bmi<=25:
                    frame1_title=Label(frame1, text="You are normal weight",font="bold 20 italic",bg="red")
                    frame1_title.pack(fill='x')
                    Label(frame2,text="EXERCISE PLAN FOR MAINTAINING NORMAL WEIGHT",font="arial 15",bg="lightblue").pack()#place(x=8,y=28)
                    Label(frame2,text="1.Swimming:\n",font="arial 15 bold",bg="white").place(x=10,y=35)
                    text='''Swimming gives the body a complete workout. It increases both muscular and cardiovascular fitness, but can also be a fun social activity.
        During a swimming session, you burn lots of calories and build up more muscle mass because of the resistance that the water gives.
        Water is around 800 times denser than air. Since your muscles have to work much harder in the pool, 
        your heart and lungs must work harder to pump oxygen around the body. This work is what improves your cardiovascular health.
        Swimming is an ideal physical activity, especially for those who suffer from arthritis. This is because the water can take up to 90% of your body weight. 

        This means that swimming will cause less strain on your joints than jogging, for example. It also helps by toning up the joints’ supporting muscles.
        As going for a swim can be quite enjoyable, it can also improve your general mood. It can also improve your social life as you become a regular at the leisure centre, 
        meeting new people who enjoy swimming as much as you do.There are other sport and fitness activities that get you into the pool as well, such as water polo,aqua aerobics.
        '''
                    Label(frame2,text=text,font="arial 15",bg='white').place(x=12,y=60)
                    Label(frame2,text="2.Cycling:\n",font="arial 15 bold",bg="white").place(x=10,y=300)
                    text='''Going for a Cycle ride is a great way of keeping in shape while reducing the risk of chronic illnesses, 
        as well as being a great form of transport to the shops or to work.Riding a bike burns more calories than going for a jog and also has less impact on your joints, 
        especially the knees. This is because cycling puts less pressure on them. Cycling works the whole body and can help you lose weight in the process, 
        whilst keeping all your joints moving in a fun, outdoor workout.Alongside the health benefits, cycling will also help to save you money.You can ride your bike as a form
        of transport, rather than using the petrol in your car or paying for a bus or taxi. What’s more, fewer cars on the road helps the environment by reducing harmful emissions.

        '''
                    Label(frame2,text=text,font="arial 15",bg='white').place(x=12,y=325)

                    Label(frame2,text="3.Nordic Walking\n", font="arial 15 bold",bg="white").place(x=10,y=480)
                    text='''If you’re looking for something a little more intense than regular walking, Nordic Walking may be for you. 
        This activity provides you with a full-body workout through the use of specially designed walking poles.The poles help you harness the power of the upper body
        to propel you forward as you walk. Nordic Walking can help you burn up to 46% more calories than regular walking and also helps to improve your posture and gait.
        Again, like regular walking, there are groups around the country that have instructors on hand to help you get to grips with the proper technique.
        Remember to consult your doctor before starting a new sport and fitness hobby. 
        Take it slow and steady at first. It’s better to gradually improve your fitness, rather than start off too intensely and injure yourself.

        '''
                    Label(frame2,text=text,font="arial 15",bg='white').place(x=12,y=520)
                    
                    Label(frame4,text=text,font="arial 15",bg='white').place(x=12,y=325)

                    Label(frame4,text="4.Walking Football\n", font="arial 15 bold",bg="white").place(x=10,y=20)
                    text='''Walking football is specifically for those over the age of 50, who may have believed that their footballing days were over. 
        The rules are similar to that of a regular five-a-side game except of course for the most important rule: NO RUNNING. 
        If the referee catches any player running, then the other team receives a free kick.Walking football gives you the chance to play the beautiful game with a twist. 
        Despite the ban on running, it still helps to keep your legs moving in a good cardiovascular workout.
        Above all, walking football means you can exercise without the fear of overdoing it and putting your health at risk.

        '''
                


                    Label(frame4,text=text,font="arial 15",bg='white').place(x=12,y=45)
                    
                    Label(frame3,text="DIET PLAN  FOR MAINTAIN NORMAL WEIGHT",font="arial 15",bg="lightblue").pack()#place(x=8,y=28)
                    
                    text='''
        Maintaining a healthy weight is important for our overall well-being. It also helps us 
        avoid chronic illnesses and provides a better standard of living. At times, however, we 
        find ourselves a little heavier than we would like and need to drop a few pounds.

        What foods provide the good nutrients our body needs, are filling and also help us with
        our goal of losing weight? Here are eight foods that fit the bill.
                    '''
                    
                    Label(frame3,text=text,font="arial 15",bg='white').place(x=12,y=30)

                    text='''
                    1.	Beans - They are high in fiber and filling. Beans also stimulate production
                    of hormones in your gut that act as an appetite suppressant. A veggie chili or 
                    bean-based stew is filling without making you feel heavy.
                    
                    2.	Salmon - It's a great source of protein and an excellent source of 
                    heart-healthy fats. People who eat salmon report that they have fewer food 
                    cravings throughout the day and don't crave late-night snacks.
                    
                    3.	Eggs – Two eggs for breakfast is better than a bagel because it requires
                    more energy to break down a protein than a starch. If high cholesterol is a 
                    concern, ditch the yolks and have an egg white omelet
                    
                    4.	Nuts – Nuts are rich in protein and fiber. They are also high in healthy
                    fats. Research shows that people who regularly eat nuts have higher levels of
                    serotonin, which is an appetite-decreasing hormone. The best nuts to add to your
                    diet are almonds, cashews and pistachios. Limit yourself to a handful, which is 
                    about 150 calories.
                    
                    6.	Greek yogurt – It has twice the protein and less sugar than most other yogurts.
                    It is also a good source of calcium, which can help in your weight-loss goals.
                    '''
                    Label(frame3,text=text,font="arial 15",bg='white').place(x=20,y=210)
                    
                    

                elif bmi>25 :
                    frame1_title=Label(frame1, text="You are over weight",font="bold 20 italic",bg="red")
                    frame1_title.pack(fill='x')
                    Label(frame2,text="EXERCISE PLAN FOR OVERWEIGHT TO NORMAL WEIGHT",font="arial 15",bg="lightblue").pack()#place(x=8,y=28)
                    Label(frame2,text="1.Walking:\n",font="arial 15 bold",bg="white").place(x=10,y=40)
                    text='''
                    It should come as no surprise that walking is one of the best exercises to focus on if 
                    you're looking to improve your fitness and lose weight. While the benefits of walking 
                    vary depending on sex and weight, walking 1 mile can burn approximately 100 calories.
                    
                    While you may think you need to jog or run to experience the benefits of this type of
                    cardio, the truth that walking is just as beneficial. Even walking slowly may be able
                    to help you get your heart rate up, and this is what is necessary for having a great
                    cardio exercise
                    '''
                    Label(frame2,text=text,font="arial 15",bg='white').place(x=12,y=70)
                    Label(frame2,text="2.Riding a Stationary Bike:\n",font="arial 15 bold",bg="white").place(x=10,y=300)
                    text='''Stationary bikes can come with backrests, providing additional support and a more comfortable experience.
        Riding a stationary bike helps strengthening your heart and lungs while also improving your body's ability to use oxygen.
        It's also a great way to give your lower body a workout and to burn some calories.

        One study found that a person weighing 185 pounds will burn 311 calories during 30 minutes of moderate riding,and will burn 466 calories during vigorous riding.
        While you'll want to do some of the other exercises listed here as well, this is one effective cardio exercise you should consider adding into your routine. 
        '''
                    Label(frame2,text=text,font="arial 15",bg='white').place(x=12,y=330)
                    Label(frame2,text="3.Side Leg Lifts:\n",font="arial 15 bold",bg="white").place(x=10,y=470)
                    text='''Side leg lifts, or side-lying hip abduction exercises, are one of the best types you may want to give a shot.
        Side leg lifts can be extremely beneficial for your lower body and will be helpful for having a well-rounded exercise session. 
        They have been shown to reduce pain and increase muscle performance

        To do these leg lifts you'll need to lay on your side, placing the hand from your elevated side onto the floor and your other behind your head.
        Lift your top leg up as high as it will go and then gently bring it back down. Then repeat the exercise for the opposite side of the body.
        '''
                    Label(frame2,text=text,font="arial 15",bg='white').place(x=12,y=500)

                    Label(frame4,text="4. Bridges:\n",font="arial 15 bold",bg="white").place(x=10,y=40)
                    text='''Performing bridges will strengthen your core and build your lower back and gluteus muscles.
        For this exercise, you'll need to get down on the floor, laying on your back with your knees bent.
        Then, you'll need to lift up your hips off of the floor and then slowly back down.

        If done regularly, doing glute bridges can have a great effect over time and will help you to strengthen your core while also reducing knee and back pain. 
        Because bridges can be done while lying down, they can be a great way to get started with an exercise routine.
        '''
                    Label(frame4,text=text,font="arial 15",bg='white').place(x=12,y=70)

                    Label(frame4,text="5. Knee Lifts With Ball:\n",font="arial 15 bold",bg="white").place(x=10,y=220)
                    text='''For this next exercise, you'll need to have a small weight of some kind that you can hold in your hands. A regular ball usually works great for this exercise, 
                    but you can use a small dumbbell or another weighted item as an alternative.When performing knee lifts, you'll start by holding the ball above your head. 
                    Simultaneously bring the ball down in front of you while also bringing one knee up to meet it. Then, return to the starting position. Then repeat, using the other knee.
                    
        This exercise will do a great job of working out your core and can be a good workout to try if you're overweight. 
        Performing knee exercises is important for reducing pain, building strength, and losing weight and can be especially beneficial for anyone who suffers from osteoarthritis.
        '''
                    Label(frame4,text=text,font="arial 15",bg='white').place(x=12,y=250)
                    Label(frame3,text="DIET PLAN  FOR UNDERWEIGHT TO NORMAL WEIGHT",font="arial 15",bg="lightblue").pack()#place(x=8,y=28)
                    Label(frame3,text="1.Eat varied, colorful, nutritionally dense foods",font="arial 15 bold",bg='white').place(x=12,y=28)

                    text='''
                    Healthful meals and snacks should form the foundation of the human diet. A simple way to create a meal plan is to make sure that each meal consists of 50 percent 
                    fruit and vegetables, 25 percent whole grains, and 25 percent protein. Total fiber intake should be 25-30 gramsTrusted Source (g) daily..
                    '''
                    Label(frame3,text=text,font="arial 15",bg='white').place(x=12,y=55)
                    
                    Label(frame3,text="The following foods are healthful and often rich in nutrients:",font="arial 15",bg='white').place(x=12,y=140)
                    text='''
        1.fresh fruits and vegetables
        2.fish
        3.legumes
        4.nuts
        5.seeds
        '''
                    Label(frame3,text=text,font="arial 15",bg='white').place(x=12,y=170)

                    Label(frame3,text="Foods to avoid eating include:",font="arial 15",bg='white').place(x=12,y=320)
                    
                    text='''
        1.foods with added oils, butter, and sugar
        2.fatty red or processed meats
        3.baked goods
        4.bagels
        5.white bread
        6.processed foods
        '''
                    Label(frame3,text=text,font="arial 15",bg='white').place(x=12,y=350)
                
                    Label(frame3,text="2.Keep a food and weight diary",font="arial 15 bold",bg='white').place(x=12,y=530)
                    text='''Self-monitoring is a critical factor in successfully losing weight. 
                    People can use a paper diary, mobile app, or dedicated website to record every item of food that they consume each day. 
                    They can also measure their progress by recording their weight on a weekly basis.

        Those who can track their success in small increments and identify physical changes are much more likely to stick to a weight loss regimen.
        People can also keep track of their body mass index (BMI) using a BMI calculator.
        '''
                    Label(frame3,text=text,font="arial 15",bg='white').place(x=12,y=555)
                    
                    


                show_frame(frame1)
            
                new.mainloop()
                
                
                
                
            Button(root,text="Show Diet and exersice",width=20,height=2,font="arial 10 bold",bg="#1f6e68",fg="white",command=menu).place(x=190,y=520)
            
            
            
            
        # # icon
        # image_icon=tk.PhotoImage(file="App_icon.png")
        # root.iconphoto(False,image_icon)


        # top
        # top=PhotoImage(file="app_top.png")
        # top_image=Label(root,image=top,background="#f0f1f5")
        # top_image.place(x=65,y=-10)
        top=Label(root,text="BMI CALCULATOR",font="arial 25 bold",fg="black",bg="#f0f1f5").place(x=100,y=20)

        #bottom box
        Label(root,width=72,height=20,bg="lightblue").pack(side="bottom")

        # # scale
        scale=ImageTk.PhotoImage(file="scale1.gif")
        Label(root,image=scale,bg="lightblue").place(x=18,y=273)


        # scale=Image.open("scale1.png")
        # ph=ImageTk.PhotoImage(scale)
        # label=Label(root,image=scale,bg="lightblue").place(x=18,y=273)
        # label.image=ph

        # two boxes


        box=ImageTk.PhotoImage(file="box.png")

        # box1=box.resize((900,300))
        # box2=PhotoImage(box1)
        Label(root,image=box).place(x=30,y=100)
        Label(root,image=box).place(x=250,y=100)


        ########################Slider1########################

        def get_current_value():
            return '{: .2f}'.format(current_value.get())

        def slider_changed(event):
            Height.set(get_current_value())
            size=int(float(get_current_value()))
            img=(Image.open("man.png"))
            resized_image=img.resize((50,10+size))
            photo2=ImageTk.PhotoImage(resized_image)
            secondimage.config(image=photo2)
            secondimage.place(x=70,y=550-size)
            secondimage.image=photo2
            
        style = ttk.Style()
        style.configure("TScale",background="grey")
        current_value=tk.DoubleVar()
        slider=ttk.Scale(root,from_=0, to=220,orient="horizontal",style="TScale",
                        command=slider_changed,variable=current_value)
        slider.place(x=70,y=205)


        ######################################################

        ########################Slider2########################

        current_value2=tk.DoubleVar()

        def get_current_value2():
            return '{: .2f}'.format(current_value2.get())

        def slider_changed(event):
            Weight.set(get_current_value2())
            
        style2 = ttk.Style()

        style2.configure("TScale",background="grey")

        slider2=ttk.Scale(root,from_=0, to=220,orient="horizontal",style="TScale",
                        command=slider_changed,variable=current_value2)
        slider2.place(x=280,y=205)


        ######################################################

        # Entry box
        Height=StringVar()
        Weight=StringVar()
        Label(root,text="Height",font="arial 20",bg="white").place(x=80,y=110)
        Label(root,text="Weight",font="arial 20",bg="white").place(x=290,y=110)

        height=Entry(root,textvariable=Height,width=4,font="arial 30",bg="#fff",fg="#000",bd=0,justify=CENTER)
        height.place(x=65,y=150)
        Height.set(get_current_value())
        weigth=Entry(root,textvariable=Weight,width=4,font="arial 30",bg="#fff",fg="#000",bd=0,justify=CENTER)
        weigth.place(x=285,y=150)
        Weight.set(get_current_value2()) 


        # man image
        secondimage=Label(root,bg="lightblue")
        secondimage.place(x=70,y=530)


        Button(root,text="View Report",width=15,height=2,font="arial 10 bold",bg="#1f6e68",fg="white",command=BMI).place(x=190,y=310)

        label1=Label(root,font="arial 25 bold",bg="lightblue",fg='#fff')
        label1.place(x=170,y=370)

        label2=Label(root,font="arial 20 bold",bg="lightblue",fg='#3b3a3a')
        label2.place(x=200,y=415)
        label3=Label(root,font="arial 10",bg="lightblue")
        label3.place(x=170,y=470)

        root.mainloop()

       
    else :
        messagebox.showerror('Invalid','invalid username or password ')
        
    # elif username != 'admin' and password!='1234' :
    #     messagebox.showerror("Invalid","invalid username and password")
    # elif password != '1234' :
    #     messagebox.showerror("Invalid","invalid password")
    # elif username!='admin' :
    #     messagebox.showerror("Invalid","invalid username")
    
    
###########@@@@@@@@@@@@@
def signup_command() :
    window=Toplevel(root)
    window.title("SignUp")
    window.geometry('925x500+300+200')
    window.configure(bg='#fff')
    window.resizable(False,False)

    # img = PhotoImage(file='C:\\Python\\GUI\\Tkinter\\SignUp.py')
    # Label(window,image=img,border=0,bg='white').place(x=50,y=90)
    # frame=Frame(window,width=350,height=390,bg='red')
    # frame.place(x=480,y=50)
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    img = Image.open('SignUp_img.jpeg')
    img=img.resize((300,300),Image.ANTIALIAS)

    photoimg=ImageTk.PhotoImage(img) #setting the above pic

    f_lbl=Label(window,image=photoimg) #creating a label image
    f_lbl.place(x=0,y=0,width=500,height=500) #placing the image label
    frame = Frame(window,width=350,height=350,bg="white")
    frame.place(x=480,y=70)

    heading=Label(frame,text='Sign Up',fg='#57a1f8',bg='white',font=('Microsoft yaHei UI Light',23,'bold'))
    heading.place(x=100,y=5)

    def signup():
        username=user.get()
        password=code.get()
        conform_password=conform_code.get()
        
        if(password==conform_password):
            try:
                file=open('datasheet.txt','r+')
                d=file.read()
                r=ast.literal_eval(d)
                dict2={username:password}
                r.update(dict2)
                file.truncate(0)
                file.close()

                file=open('datasheet.txt','w')
                w=file.write(str(r))

                messagebox.showinfo('Signup','Successfully Sign Up')
                window.destroy()
                
            except:
                file=open('datasheet.txt','w')
                pp=str({'Username':'password'})
                file.write(pp)
                file.close()
        else:
            messagebox.showerror('Invalid',"Both Password Should Match")


    def sign() :
        window.destroy()





    def on_enter(e):
        code.delete(0,'end')
    def onleave(e):
        if(code.get()==''):
            code.insert(0,'Password')

    code=Entry(frame,width=25,fg='black',border=0,bg='white',font=('Microsoft Yahei UI Light',11))
    code.place(x=30,y=150)
    code.insert(0,'Password')
    code.bind("<FocusIn>",on_enter)
    code.bind("<FocusOut>",onleave)
    Frame(frame,width=295,height=2,bg='black').place(x=25,y=177)

    def on_enter(e):
        conform_code.delete(0,'end')
    def onleave(e):
        if(conform_code.get()==''):
            conform_code.insert(0,'Conform Password')

    conform_code=Entry(frame,width=25,fg='black',border=0,bg='white',font=('Microsoft Yahei UI Light',11))
    conform_code.place(x=30,y=220)
    conform_code.insert(0,'Conform Password')
    conform_code.bind("<FocusIn>",on_enter)
    conform_code.bind("<FocusOut>",onleave)
    Frame(frame,width=295,height=2,bg='black').place(x=25,y=247)


    def on_enter(e):
        user.delete(0,'end')
    def onleave(e):
        if(user.get()==''):
            user.insert(0,'Username')

    user=Entry(frame,width=25,fg='black',border=0,bg='white',font=('Microsoft Yahei UI Light',11))
    user.place(x=30,y=80)
    user.insert(0,'Username')
    user.bind("<FocusIn>",on_enter)
    user.bind("<FocusOut>",onleave)
    Frame(frame,width=295,height=2,bg='black').place(x=25,y=107)
    ###########--------------------------
    Button(frame,width=39,pady=7,text='Sign Up',bg='#57a1f8',fg='white',border=0,command=signup).place(x=35,y=280)
    label=Label(frame,text='I have an account',fg='black',bg='white',font=('Microsoft YaHei UI Light',9))
    label.place(x=90,y=320)

    signin=Button(frame,width=6,text='Sign in',border=0,bg='white',cursor='hand2',fg='#57a1f8',command=sign)
    signin.place(x=200,y=320)
    window.mainloop()
######@@@@@@@@@@@@@@@@@@@
    
    
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
img = Image.open('login.jpg')
img=img.resize((500,500),Image.LANCZOS) 
# Label(root,image=img,bg='white').place(x=50,y=50)
photoimg=ImageTk.PhotoImage(img) #setting the above pic

f_lbl=Label(root,image=photoimg) #creating a label image
f_lbl.place(x=0,y=0,width=500,height=500) #placing the image label
frame = Frame(root,width=350,height=350,bg="white")
frame.place(x=480,y=70)

heading=Label(frame,text='Sign in',fg='#57a1f8',bg='white',font=('Microsoft yaHei UI Light',23,'bold'))
heading.place(x=100,y=5)
#######-----------------------------------------

def on_enter(e) :
    user.delete(0, 'end')
    
def on_leave(e) :
    name=user.get()
    if name=='' :
        user.insert(0,'Username')
        
user = Entry(frame,width=25,fg='black',border=0,bg='white',font=('Microsoft yaHei UI Light',11))
user.place(x=30,y=80)
user.insert(0,'Username')
user.bind('<FocusIn>', on_enter)
user.bind('<FocusOut>', on_leave)

Frame(frame,width=295,height=2,bg='black').place(x=25,y=107)
######-------------------------------------------

def on_enter(e) :
    code.delete(0, 'end')
    
def on_leave(e) :
    name=code.get()
    if name=="" :
        code.insert(0,'Password')
        
code = Entry(frame,width=25,fg='black',border=0,bg='white',font=('Microsoft yaHei UI Light',11))
code.place(x=30,y=150)
code.insert(0,'Password')
code.bind('<FocusIn>', on_enter)
code.bind('<FocusOut>', on_leave)

Frame(frame,width=295,height=2,bg='black').place(x=25,y=177)
#######-----------------------------------------------

Button(frame,width=39,pady=7,text='Sign in',bg='#57a1f8',fg='white',border=0,command=signin).place(x=35,y=204)
label=Label(frame,text="Don't have an account?",fg='black',bg='white',font=('Microsoft yaHei UI Light',9))
label.place(x=75,y=270)

sign_up=Button(frame,width=6,text='Sign up',border=0,bg='white',cursor='hand2',fg='#57a1f8',command=signup_command)
sign_up.place(x=215,y=270 )

root.mainloop()