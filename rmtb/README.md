# rmtb.py
A library for making rmtb bots in python.
WARNING: VOICE AND FILES ARE NOT SUPPORTED... YET

## How to install
Just use pypi like
```
pip3 install rmtb
```
## Documentation
The rmtb module only has a class, the Bot class.
This class requires 2 values. Name and color. A third option is optional for if you want to have the bot badge.
### Events
events use the decorator "bot.event"
There is one event that is not in the rmtb documentation which is the connect event (requires no args).
Every event returns 1 arg containing the json of the data.
```py
from rmtb import Bot

bot = Bot("rmtb.py","red")
@bot.event
def connect():
	print("bot connected")
bot.run()
```
The events have been modified so they can be in the names of the functions.
Here is a list of events:
```
user joined                   user_joined
user left                       user_left
message                           message
update users                 update_users
user change nick         user_change_nick
get_voice_users           get_voice_users
getvoice                        get_voice
typing                             typing
reaction_add                 reaction_add
reaction_remove           reaction_remove
reaction_update           reaction_update
lts_msgid                       lts_msgid
```
## Actions
Ofcourse you can also do stuff, not just listen. Like send messages and react.
Here is all you can do:
### rename(name, color, bot=True)
If you ever want to have a different name.
### send(content)
Sends messages.
### delete()
Deletes the last message (documentation may be a bit out of date).
Deleting specific messages coming soon too.
### editlast(newcontent)
Edits the last message.
### edit(id, newcontent)
Edits the message with the id.
### start_typing()
Sends to rmtb server that your bot is starting to type.
### stop_typing()
Opposite of start_typing (duh)
### react(ID, img)
React to a message with the ID with the img given.
### unreact(ID, img)
Opposite of react()
### join_room(name, passwd=None)
Will make your bot join that room (password is optional).
### create_room(name, passwd=None)
Creates a room
## May not work
### request_rooms()
Will call event room_list_resp which contains all the rooms
### request_current_room()
Will call event room_current_resp which contains the room your bot is in