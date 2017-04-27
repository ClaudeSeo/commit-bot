# -*- coding: utf-8 -*-
import random
import telegram
from datetime import datetime, timedelta
from github import Github, Branch
from github.GithubException import UnknownObjectException
from emoji import emojize
from config import config


MESSAGES = [
    u'%s 커밋은 하고 가지? :rage:',
    u'%s 저기여, 커밋인데여. 오늘 커밋 안하세여? :scream:',
    u'%s 일해라 핫산! :fearful:',
    u'%s 갈때 가더라도, 커밋 한개정도 괜찮잖아? :grimacing:',
    u'%s 커밋은 하고 자야지? :wink:',
    u'%s 커밋좀요 :cold_sweat:'
]

def send_message_to_telegram(mentions=''):
    bot = telegram.Bot(token=config['telegram']['token'])
    random.shuffle(MESSAGES)
    message = random.choice(MESSAGES) % (mentions)
    bot.send_message(chat_id=config['telegram']['chat_id'], text=emojize(message, use_aliases=True))

def get_total_count_of_commits(commits) :
    return len(list(commits))

def handle(event, context):
    client = Github(config['github']['id'], config['github']['password'])
    utcnow = datetime.utcnow() + timedelta(hours=9)
    today = datetime(utcnow.year, utcnow.month, utcnow.day)

    for k, v in config['github']['branch'].iteritems():
        try:
            repo = client.get_repo(k)
            commits = repo.get_commits(since=today)
            if get_total_count_of_commits(commits) < 1:
                mentions = ', '.join(v) if isinstance(v, (list, tuple)) else ''
                send_message_to_telegram(mentions)
        except UnknownObjectException as e:
            print 'Not Found Repository: %s' % k
        except Exception as e:
            raise(e)
