# mad lib generator
import tkinter
from tkinter import *
import random

root = Tk()
root.geometry("700x500")
root.title("MAD LIB GENERATOR")
root.resizable(False, False)

image1 = tkinter.PhotoImage(file="image1.png.png")
bkg = tkinter.Label(root, image=image1)
bkg.place(x=0, y=0)

title = tkinter.Label(text="MADLIB GENERATOR", font=("Times", 40))
title.place(x=80, y=190)

# creating an array for the entry widget
entry_name = []
entry_place = []
entry_food = []
entry_verb = []
entry_things = []


# creating new window
def open_window():
    global image2, image3, image4
    window = Toplevel(root)
    window.resizable(FALSE, FALSE)
    window.geometry("805x450")
    window.title("MAD LIB GENERATOR")

    image2 = tkinter.PhotoImage(file="image2.png")
    image3 = tkinter.PhotoImage(
        file="image3_1_760x410.png")

    bkg1 = tkinter.Label(window, image=image2)
    bkg2 = tkinter.Label(window, image=image3)

    bkg1.place(x=0, y=0)
    bkg2.place(x=20, y=15)

    # text 1 "HOME"
    title1 = tkinter.Label(window, text="HOME", font=("Times", 20))
    title1.place(x=25, y=15)

    title2 = tkinter.Label(window, text="GENERATED STORY", font=("Times", 28))
    title2.place(x=390, y=25)

    # input text
    name_text = tkinter.Label(window, text="Enter bunch of names below", font=("Helvetica", 11))
    things_text = tkinter.Label(window, text="Enter bunch of things below", font=("Helvetica", 11))
    place_text = tkinter.Label(window, text="Enter bunch of place below", font=("Helvetica", 11))
    verb_text = tkinter.Label(window, text="Enter bunch of verb below", font=("Helvetica", 11))
    food_text = tkinter.Label(window, text="Enter bunch of food below", font=("Helvetica", 11))

    name_text.place(x=25, y=60)
    things_text.place(x=25, y=120)
    place_text.place(x=25, y=180)
    verb_text.place(x=25, y=240)
    food_text.place(x=25, y=300)

    # entry widget
    name = tkinter.Entry(window, width=30)
    things = tkinter.Entry(window, width=30)
    place = tkinter.Entry(window, width=30)
    verb = tkinter.Entry(window, width=30)
    food = tkinter.Entry(window, width=30)

    name.place(x=50, y=90)
    things.place(x=50, y=150)
    place.place(x=50, y=210)
    verb.place(x=50, y=270)
    food.place(x=50, y=330)

    def name1():
        global entry_name
        value_name = name.get()
        entry_name.append(value_name)
        random_name1 = random.choice(entry_name)
        random_name2 = random.choice(entry_name)
        return random_name1, random_name2

    def place1():
        global entry_place
        value_place = place.get()
        entry_place.append(value_place)
        random_place = random.choice(entry_place)
        return random_place

    def food1():
        global entry_food
        value_food = food.get()
        entry_food.append(value_food)
        random_food = random.choice(entry_food)
        return random_food

    def verb1():
        global entry_verb
        value_verb = verb.get()
        entry_verb.append(value_verb)
        random_verb = random.choice(entry_verb)
        return random_verb

    def things1():
        global entry_things
        value_things = things.get()
        entry_things.append(value_things)
        random_things = random.choice(entry_things)
        return random_things

    def story():
        random_name1, random_name2 = name1()
        random_place = place1()
        random_verb = verb1()
        random_food = food1()
        random_things = things1()

        story1 = "One sunny day " + random_name1 + " decided to take a vacation in " + random_place + ". In her stay " \
                 "she met " + random_name2 + " they eat together a " + random_food + " while " + random_verb + \
                 " with their " + random_things + "."

        story2 = random_name1 + " and " + random_name2 + " are best friends. They take a break going to " + random_place \
                 + ". They bring their favorite " + random_food + " together with their " + random_things + \
                 " and spend the day " + random_verb

        story3 = "At the " + random_place + " there are always bunch of tourist. " + " This is where " + random_name1 \
                 + " and " + random_name2 + " met. While touring they tried the famous " + random_food + \
                 " and enjoyed it while " + random_verb + ". They bought a " + random_things + " for souvenirs for " \
                 "their family. "

        story4 = random_name1 + " and " + random_name2 + " are in a relationship for 4 years. They are already at the " \
                 + random_place + " where they realize that they forgot their " + random_things + " in condo. So " + \
                 random_name1 + " go back to the apartment. However " + random_name1 + " did not return to the " + \
                 random_place + " instead " + random_name1 + " is " + random_verb + " all day."

        story5 = random_food + " is " + random_name2 + " favorite. However while eating, " + random_name2 + \
                 " was disturbed by " + random_name1 + ". So " + random_name2 + " put a " + random_things + " in " \
                 + random_name1 + " mouth and it results to " + random_name1 + " " + random_verb

        story6 = random_place + " is a famous for tourist spot. There is where various souvenirs are located. While "+ random_name1 \
                + " is buying a " + random_things + " a thief stole her " + random_things + " . Fortunately, " + random_name2 \
                + " a wrestler was there to take down the thief. For token of appreciation " + random_name1 + " gives a " \
                + random_food + " to " + random_name2 + " ."

        story7 = "One sunny day " + random_name1 + " decided to marry " + random_name2 + " for fun. They decided to" \
                + " have a " + random_things + " for their souvenirs and they gave " + random_food + " for their visitors."

        story8 = random_verb + " is " + random_name2 + " favorite thing to do while eating a " + random_food + \
                " together with " + random_name1 + "."

        random_choice = [story1, story2, story3, story4, story5, story6, story7, story8]
        random_story = random.choice(random_choice)
        story_text.delete('1.0', tkinter.END)
        story_text.insert(tkinter.END, random_story)

    # button for accepting input
    button1 = tkinter.Button(window, text="Add name", command=name1)
    button2 = tkinter.Button(window, text="Add things", command=things1)
    button3 = tkinter.Button(window, text="Add place", command=place1)
    button4 = tkinter.Button(window, text="Add verb", command=verb1)
    button5 = tkinter.Button(window, text="Add food", command=food1)
    generator_button = tkinter.Button(window, text="Generate Story", width=13, height=3, command=story)

    button1.place(x=250, y=85)
    button2.place(x=250, y=145)
    button3.place(x=250, y=205)
    button4.place(x=250, y=265)
    button5.place(x=250, y=325)
    generator_button.place(x=130, y=360)

    story_text = tkinter.Text(window, width=40, height=10, wrap=tkinter.WORD, font=("Arial", 12))
    story_text.place(x=390, y=120)


button = Button(root, text="Start", font=("Times", 20), command=open_window)
button.place(x=300, y=350)

root.mainloop()
