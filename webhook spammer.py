#imports:
from discord_webhook import DiscordWebhook
import time
from random import randint
def logo():
	print("  _    _                 ")
	time.sleep(0.5)
	print(" | |  | |                ")
	time.sleep(0.5)
	print(" | |__| | ___  _ __ ___  ")
	time.sleep(0.5)
	print(" |  __  |/ _ \| '_ ` _ \ ")
	time.sleep(0.5)
	print(" | |  | | (_) | | | | | |")
	time.sleep(0.5)
	print(" |_|  |_|\___/|_| |_| |_|")
	time.sleep(0.5)
	print("by Hom#2913")
	print("https://github.com/afkHom")
def main():
	#who and what will be spammed
	logo()
	target =input("webhook: " )
	msg = input("Spam msg:  ")
	amount = int(input("Amount: "))
	n = 0
	while n < amount:
		tsleep = randint(1 , 2 )
		webhook = DiscordWebhook(url=target, content=msg)
		time.sleep(tsleep)
		response = webhook.execute()
		n = n+1
main()
#external modules needed: discord webhook
#installed with the following comand :
#pip install discord-webhook 
