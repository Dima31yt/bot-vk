import vk_api, json
from vk_api.longpoll import VkLongPoll, VkEventType
from config import main_token

vk_session = vk_api.VkApi(token = main_token)
longpoll = VkLongPoll(vk_session)

def get_keyboard(buts):
	global get_but
	nb = []
	color = ''
	for i in range(len(buts)):
		nb.append([])
		for k in range(len(buts[i])):
			nb[i].append(None)
	for i in range(len(buts)):
		for k in range(len(buts[i])):
			text = buts[i][k][0]
			if buts[i][k][1] == 'p':
				color = 'positive'
			elif buts[i][k][1] == 'n':
				color = 'negative'
			nb[i][k] = {
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"" + "1" + "\"}",
                    "label": f"{text}"
                },
                "color": f"{color}"
            }
	first_keyboard = {
	    'one_time': False,
	    'buttons': nb
	    }
	first_keyboard = json.dumps(first_keyboard, ensure_ascii=False).encode('utf-8')
	first_keyboard = str(first_keyboard.decode('utf-8'))
	return first_keyboard

keyboard1 = get_keyboard(
	[
		
	]
)

def sender(id, text):
	vk_session.method('messages.send', {'chat_id' : id, 'message' : text, 'random_id' : 0, 'keyboard' : keyboard1})

for event in longpoll.listen():
	if event.type == VkEventType.MESSAGE_NEW:
		if event.to_me:
			if event.from_chat:

				msg = event.text.lower()
				id = event.chat_id

				if msg in ['бот кинь хентай']:
					sender(id, f'https://rt.pornhub.com/categories/hentai'),

				if msg in ['что учить будем']:
					sender(id, f'Лесника'),

				if msg in ['кто на трассе']:
					sender(id, f'Паша'),

				if msg in ['найти басиста','на трассе','паша']:
					sender(id, f'@xarek1008'),

				if msg in ['найти солиста','димон','дима']:
					sender(id, f'@salam_alekum410'),

				if msg in ['найти саню','санёк','саша','саня']:
					sender(id, f'@kavaliski'),

				if msg in ['найти илью','илья','орлов']:
					sender(id, f'@orlllove'),

				if msg in ['найти захария','захар','жмын','захарий']:
					sender(id, f'@ztrek00'),

				if msg in ['найти вику','вика','бибика','вика бибика','хочу трахнуть']:
					sender(id, f'@id540472612'),

				if msg in ['позвать всех','все','all']:
					sender(id, f'@all'),

				if msg in ['Да не этот','не тот','не этот','другой']:
					sender(id, f'Ну ладно'),

				if msg in ['когда сборы','сегодня идём','сегодня приходить','когда приходить','сегодня во сколько','когда сборы?','сегодня идём?','сегодня приходить?','когда приходить?','сегодня во сколько?']:
					sender(id, f'Вторник, четверг в 16:00, можно раньше')

				if msg in ['кто пидор']:
					sender(id, f'Саня говорит что Паша')
