#! python3.7

from dialog_bot_sdk.bot import DialogBot
import grpc

def on_msg(*params):
	global bot_owner
	if params[0].message.textMessage.text == "/start" and bot_owner == None:
		bot_owner = [[params[0].peer, params[0].sender_uid]]
	elif params[0].message.textMessage.text != "" and bot_owner[0] != [params[0].peer, params[0].sender_uid]:
		bot.messaging.reply(bot_owner[0][0], [params[0].mid])
		bot.messaging.send_message(params[0].peer, "Благодарю за отзыв!")

if __name__ == "__main__":
	bot = DialogBot.get_secure_bot(
		"hackathon-mob.transmit.im",
		grpc.ssl_channel_credentials(),
		"TOKEN"
	)
	bot_owner = None #stores peer and id of bot owner
	bot.messaging.on_message(on_msg)
