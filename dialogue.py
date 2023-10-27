#Dialogue is executed in the execute_talk() function in game.py. Dracula has two options, to talk or to fight, the others only have one option.
#Fighting just has the character speak and then the player is put into combat mode after
#Talking has preset responses that are put into the text with the villains text. It reads slowly as seen in the execute_talk() function.
#When a character is fought it dies and cannot be interacted with again, for those spoken to they have a repeat dialogue which will print if the character tries to talk to them again


dialogue_dracula = {
    "id": "dracula",
    
    "multiple options": True, #Can both
    
    "method": "talk",
    
    "base dialogue": ["Hello Victor, it is good to see you again.", "I would ask how your travels went, but since you are back... well I'm sure you learnt something.", "You're here for the monster aren't you?. Again?", "Do you ever learn Victor? Don't revive dead things.", "I will not see that monster again, which is why I have hidden a leg from you. He will not be reassembled."],
    
    "dialogue one": ["You need to be careful Victor, life and death is not to be meddled with.", "You: I'll be careful, he is a huge scientific masterpiece.","If you're sure you will be careful, do not make the same mistakes again.", "You: Only a fool would make the same mistakes twice.","If he is rebuilt, it should be as a memento, a warning to not meddle outside the human domain. I will give you the leg to rebuild him, but you must promise me.", "You: I promise."],
    
    "dialogue two": ["You do not want to fight me. This is a war you will not win, it is not worth it to rebuild a monster. Fighting you is a necessary evil to prevent the monster resurfacing."],
    
    #if player interacts with him after already talking/fighting
    "repeat dialogue": ["You got your limb Victor, remember to be careful."]
}

dialogue_pennywise = {
    "id": "pennywise",
    
    "multiple options": False, #Can only fight

    "method": "fight",
    
    #added something to hint to the player that the way to beat him is not with a physical weapon but by shouting at him
    "base dialogue": ["Hey Victor...", "Good luck getting the leg, you'll have to go through me first...", "You'll die if you try to fight me Victor...", """You: But don't you see, I know your weakness Pennywise, you can't handle those with solid friendships, those with a backbone
willing to shout until you finally leave them alone.""", "Be careful, the weapon you need may not be what you're thinking of."]
    
}

dialogue_grim = {
    "id": "the grim reaper",
    
    "multiple options": False, #Can only talk

    "method": "deal",
    
    "gift": "soul jar",
    
    "base dialogue": ["Greetings, mortal. I am the one called Death, a harbinger of inevitable demise.","Be warned, this creature you seek to revive is a blasphemy to life itself.", "You: I'll do anything to get this, I need to build this monster again, he is a scientific masterpiece.", "You must may a price, I do not give without cause. I shall only accept something of equivalence to the creation of new life."],
    
    "successful dialogue": ["This is a good offering, it contains the essence of a life I sought to take long ago. A soul should never be separated from its holder. I shall give you the torso you desire."],
    
    "unsuccessful dialogue": ["Do not play with me mortal, for you need to offer more than that to appease me."],

    #if player interacts with him after already talking
    "repeat dialogue": ["You have the limb now, do not continue to bother me."]
}


dialogue_freddy = {
    "id": "freddy fazbear",
    
    "multiple options": False, #Can only fight

    "method": "fight",
    
    "base dialogue": ["Hello Victor...", "You can't get the leg... I won't let you.", "This theatre room is my domain... If you try taking the leg, you won't leave here alive..."]
}

#slenderman doesn't talk but there should be commentary on his behaviour and hints to the player for how to beat him
dialogue_slenderman = {
    "id": "slenderman",
    
    "multiple options": False, #Can only fight
    
    "method": "fight",
    
    "base dialogue": ["Standing against the backdrop of the verdant green foliage, the tall, thin figure of Slenderman stalks the landscape", "His long, lanky frame casts a menacing shadow on the plants below, and his emotionless face stares blankly into the distance", "Behind him lays a severed head.", "You feel terrified to approach, let alone fight him.", "Maybe those pages could help..."]
}
