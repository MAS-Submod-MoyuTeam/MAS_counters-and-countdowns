#first prompt
"I want to start a countdown."

#names the countdown for future reference
m "Oh! Okay!"
m "It always makes me feel important when you ask me for help with daily stuff like this."
m "Ehehehe~ Anyways!"
m "What should I name the counter?"

#asks 
m "When will the countdown end?"

m "Okay..."
m "I'll make sure to remember that, [player]!"

#second prompt
"I want to see my countdowns."
#shows list of countdowns by name, and upon clicking:

m "Okay..."
m "[countdown]: [number] [days] remaining..."
m "Hope that helped, [player]!"

#inside list of countdowns:
"I want to delete a countdown."
m "Which countdown do you want to delete?"
#show list (like the bookmark list)

#on the day of the countdown ending
m "[player]! "
extend "The countdown we were keeping track of ended!"
m "The countdown was... [countdown]."
#ask if player wants to restart the countdown (in case of birthdays or something)
m "Do you want me to restart it?"

"Yes":
#restarts

"No":
"Ah, okay!"
