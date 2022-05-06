import rmtb.rmtb as rmtb

bot = rmtb.Bot("rmtb.py", "red")

@bot.event
def connect():
	print("Bot on!")

@bot.event
def message(d):
	if d["msg"] == "py!test":
		bot.send("finally, done")

bot.run()