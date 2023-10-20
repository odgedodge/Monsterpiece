#Dialogue is executed in the execute_talk() function in game.py. Dracula has two options, to talk or to fight, the others only have one option.
#Fighting just has the character speak and then the player is put into combat mode after
#Talking has preset responses that are put into the text with the villains text. It reads slowly as seen in the execute_talk() function.
#When a character is fought it dies and cannot be interacted with again, for those spoken to they have a repeat dialogue which will print if the character tries to talk to them again


dialogue_dracula = {
    "id": "dracula",
    
    "multiple options": True, #Can both
    
    "base dialogue": ["Hello Henry, it is good to see you again.", "I would ask how your travels went, but since you are back... well I'm sure you learnt something.", "You're here for the monster aren't you?. Again?", "Do you ever learn Henry? Don't revive dead things.", "I will not see that monster again, which is why I have hidden a leg from you. He will not be reassembled."],
    
    "dialogue one": ["You need to be careful Henry, life and death is not to be meddled with.", "You: I'll be careful, he is a huge scientific masterpiece.","If you're sure you will be careful, do not make the same mistakes again.", "You: Only a fool would make the same mistakes twice.","If he is rebuilt, it should be as a memento, a warning to not meddle outside the human domain. I will give you the leg to rebuild him, but you must promise me.", "You: I promise."],
    
    "dialogue two": ["You do not want to fight me. This is a war you will not win, it is not worth it to rebuild a monster. Fighting you is a necessary evil to prevent the monster resurfacing."],
    
    "repeat dialogue": ["You got your limb Henry, remember to be careful."]
}

dialogue_pennywise = {
    "id": "pennywise",
    
    "multiple options": False, #Can only fight

    "method": "fight",
    
    #add something to hint to the player that the way to beat him is not with a physical weapon but by shouting at him
    "base dialogue": ["Blah"]
    
}

dialogue_grim = {
    "id": "the grim reaper",
    
    "multiple options": False, #Can only talk

    "method": "talk",
    
    "base dialogue": ["Greetings, mortal. I am the one called Death, a harbinger of inevitable demise.","Be warned, mortal. This creature you seek to revive is a blasphemy to life itself.", "To obtain and possess a human torso is a grave sin, one that will surely bring down divine wrath. I, the grim reaper, must halt your misdeeds.", "Your time has come to an end, and nothing can prevent what is written in the book of death", "Mortal, you are meddling in forces you do not understand.", "I must intervene. Do not proceed, lest you wish to face the wrath of the grim reaper."],

    "repeat dialogue": ["You have the limb now, do not continue to bother me."]
}


dialogue_freddy = {
    "id": "freddy fazbear",
    
    "multiple options": False, #Can only fight

    "method": "fight",
    
    "base dialogue": ["Hello Henry...", "You can't get the leg... I won't let you.", "This theatre room is my domain... If you try taking the leg, you won't leave here alive..."]
}

#slenderman doesn't talk but there should be commentary on his behaviour and hints to the player for how to beat him
dialogue_slenderman = {
    "id": "slenderman",
    
    "multiple options": False, #Can only fight
    
    "method": "fight",
    
    "base dialogue": []
}