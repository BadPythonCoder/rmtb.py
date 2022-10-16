import rmtb.rmtb as rmtb

bot = rmtb.Bot("rmtb.py", "red")

@bot.event
def connect():
	print("Bot on!")

@bot.event
def message(d):
	print(d["msg"])
	if d["msg"] == "py!test":
		bot.send("finally, done")
	elif d["msg"] == "py!room":
		print("doing")
		bot.send(bot.currroom)
	elif d["msg"] == "py!rooms":
		bot.send(str(bot.rooms))

# print(bot.events)

bot.run()