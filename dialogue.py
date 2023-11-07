# Speech is a dictionary so the number of different types of speech can be unique to the Character

class Interaction:
    def __init__(self, id, multiple_options, method, dialogue):
        self.__id = id
        self.__multiple_options = multiple_options
        self.__method = method
        self.__speech = dialogue
        
    def get_id(self):
        return self.__id
    
    def get_multiple_options(self):
        return self.__multiple_options
    
    def get_method(self):
        return self.__method
    
    def get_speech(self):
        return self.__speech
    
dracula_speech = { 
    "base dialogue": ["Hello Victor, it is good to see you again.", "I would ask how your travels went, but since you are back... well I'm sure you learnt something.", "You're here for the monster aren't you?. Again?", "Do you ever learn Victor? Don't revive dead things.", "I will not see that monster again, which is why I have hidden a leg from you. He will not be reassembled."],
    
    "dialogue one": ["You need to be careful Victor, life and death is not to be meddled with.", "You: I'll be careful, he is a huge scientific masterpiece.","If you're sure you will be careful, do not make the same mistakes again.", "You: Only a fool would make the same mistakes twice.","If he is rebuilt, it should be as a memento, a warning to not meddle outside the human domain. I will give you the leg to rebuild him, but you must promise me.", "You: I promise."],
    
    "dialogue two": ["You do not want to fight me. This is a war you will not win, it is not worth it to rebuild a monster. Fighting you is a necessary evil to prevent the monster resurfacing."],

    "repeat dialogue": ["You got your limb Victor, remember to be careful."]
} 

dracula_interaction = Interaction("dracula", True, "talk", dracula_speech)
 
pennywise_speech = {
    "base dialogue": ["Hey Victor...", "Good luck getting the leg, you'll have to go through me first...", "You'll die if you try to fight me Victor...", """You: But don't you see, I know your weakness Pennywise, you can't handle those with solid friendships, those with a backbone
willing to shout until you finally leave them alone.""", "Be careful, the weapon you need may not be what you're thinking of."]  
}

pennywise_interaction = Interaction("pennywise", False, "fight", pennywise_speech)

grim_reaper_speech = {
    
    "gift": "soul jar",
    
    "base dialogue": ["Greetings, mortal. I am the one called Death, a harbinger of inevitable demise.","Be warned, this creature you seek to revive is a blasphemy to life itself.", "You: I'll do anything to get this, I need to build this monster again, he is a scientific masterpiece."],
    
    "successful dialogue": ["This is a good offering, it contains the essence of a life I sought to take long ago. A soul should never be separated from its holder. I shall give you the torso you desire."],
    
    "unsuccessful dialogue": ["Do not play with me mortal, for you need to offer more than that to appease me."],

    "repeat dialogue": ["You have the limb now, do not continue to bother me."]
}

grim_interaction = Interaction("the grim reaper", False, "deal", grim_reaper_speech)
    
freddy_speech = {
    "gift": "pizza",
    
    "base dialogue": ["Hello Victor...", "You can't get the leg... I won't let you.", "This theatre room is my domain... If you try taking the leg, you won't leave here alive..."],

    "romance dialouge": ["smut"],

    "successful dialogue": ["Oh my how did you know i love pizza"] ,

    "unsuccessful dialogue": ["har har har har har huar huar huar har har har har har har, har har har har pm um um am um am um am am um am um am u am um am am um am um um um am um um um am am"],

    "repeat dialogue": ["huband"]

}

freddy_interaction = Interaction("freddy fazbear", True, "romance", freddy_speech)

slenderman_speech = {
    "base dialogue": ["Standing against the backdrop of the verdant green foliage, the tall, thin figure of Slenderman stalks the landscape", "His long, lanky frame casts a menacing shadow on the plants below, and his emotionless face stares blankly into the distance", "Behind him lays a severed head.", "You feel terrified to approach, let alone fight him.", "Maybe those pages could help..."]
}

slenderman_interaction = Interaction("slenderman", False, "fight", slenderman_speech)

