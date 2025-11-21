"""
Multiple Resonses depending on the mood
"""
import random

MOODS = {
    "joy":          ["(,,> ᴗ <,,)"],
    "fear":         ["(꩜ ᯅ ꩜;)"],
    "surprise":     ["( ˶°ㅁ°)!!"],
    "sadness":      ["(• ᴖ •｡)"],
    "disgust":      ["(- ~ -)"],
    "anger":        ["(｡•`ᴖ´•｡)"],
    "anticipation": ["(⊃‿⊂)"],
    "default":      ["^_^"]
}

current_mood = "default"

"""
to select faces in random from the dict
"""
def get_face():
    faces = MOODS.get(current_mood, MOODS["default"])
    return random.choice(faces)

def pick_random_mood():
    global current_mood
    current_mood = random.choice(list(MOODS.keys()))

