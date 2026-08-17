import streamlit as st

st.set_page_config(
    page_title="Mad Libs Generator",
    layout="centered"
)

st.title("Mad Libs Generator")
st.subheader("Have Fun!")

st.write("Click any one of the Mad Libs to generate a story!")

def madlib1():
    st.header("The Photographer")

    animals = st.text_input("Enter an animal name")
    profession = st.text_input("Enter a profession name")
    cloth = st.text_input("Enter a piece of cloth name")
    things = st.text_input("Enter a thing name")
    name = st.text_input("Enter a name")
    place = st.text_input("Enter a place name")
    verb = st.text_input("Enter a verb in -ing form")
    food = st.text_input("Enter a food name")

    if st.button("Generate Photographer Story"):

        if all([animals, profession, cloth, things, name, place, verb, food]):

            story = (
                f"Say {food}, the photographer said as the camera flashed! "
                f"{name} and I had gone to {place} to get our photos taken "
                f"on my birthday. The first photo we really wanted was a "
                f"picture of us dressed as {animals} pretending to be a "
                f"{profession}. When we saw the second photo, it was exactly "
                f"what I wanted. We both looked like {things} wearing "
                f"{cloth} and {verb} -- exactly what I had in mind."
            )

            st.success("Your Story: ")
            st.write(story)

        else:
            st.warning("Please fill in all the fields!")


def madlib2():
    st.header("The Butterfly")

    adjective = st.text_input("Enter an adjective")
    color = st.text_input("Enter a color name")
    thing = st.text_input("Enter a thing name")
    place = st.text_input("Enter a place name")
    person = st.text_input("Enter a person name")
    adjective1 = st.text_input("Enter another adjective")
    insect = st.text_input("Enter an insect name")
    food = st.text_input("Enter a food name")
    verb = st.text_input("Enter a verb name")

    if st.button("Generate Butterfly Story"):

        if all([
            adjective,
            color,
            thing,
            place,
            person,
            adjective1,
            insect,
            food,
            verb
        ]):

            story = (
                f"Last night I dreamed I was a {adjective} butterfly with "
                f"{color} splotches that looked like {thing}. I flew to "
                f"{place} with my best friend and {person}, who was a "
                f"{adjective1} {insect}. We ate some {food} when we got "
                f"there and then decided to {verb}, and the dream ended "
                f"when I said -- let's {verb}."
            )

            st.success("Your Story: ")
            st.write(story)

        else:
            st.warning("Please fill in all the fields!")


def madlib3():
    st.header("Apple and Apple")

    person = st.text_input("Enter a person name")
    color = st.text_input("Enter a color")
    foods = st.text_input("Enter a food name")
    adjective = st.text_input("Enter an adjective")
    thing = st.text_input("Enter a thing name")
    place = st.text_input("Enter a place")
    verb = st.text_input("Enter a verb")
    adverb = st.text_input("Enter an adverb")
    food = st.text_input("Enter another food name")
    things = st.text_input("Enter another thing name")

    if st.button("Generate Apple Story"):

        if all([
            person,
            color,
            foods,
            adjective,
            thing,
            place,
            verb,
            adverb,
            food,
            things
        ]):

            story = (
                f"Today we picked apples from {person}'s Orchard. "
                f"I had no idea there were so many different varieties "
                f"of apples. I ate {color} apples straight off the tree "
                f"that tasted like {foods}. Then there was a {adjective} "
                f"apple that looked like a {thing}. When our bags were "
                f"full, we went on a free hay ride to {place} and back. "
                f"It ended at a hay pile where we got to {verb} {adverb}. "
                f"I can hardly wait to get home and cook with the apples. "
                f"We are going to make apple {food} and {things} pies!"
            )

            st.success("Your Story: ")
            st.write(story)

        else:
            st.warning("Please fill in all the fields!")

story = st.selectbox(
    "Choose a Mad Lib:",
    [
        "Select a story",
        "The Photographer",
        "Apple and Apple",
        "The Butterfly"
    ]
)

if story == "The Photographer":
    madlib1()

elif story == "Apple and Apple":
    madlib3()

elif story == "The Butterfly":
    madlib2()