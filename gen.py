import requests
import urllib

# Generates text sitemap for GraphConnect sessions and topics
# Text sitemap is one URL per line
# Outputs to stdout.  Need to upload to neo4j.com/ to submit to google


# 2018 sessions
sched_sessions = 'https://dxk1axuhyop9u.cloudfront.net/api/session/list?apikey=acf6094f1ec29219444359c176a94fb9&role=speaker&featured=y&format=json&custom_data=y'

def gen_full_session_url(slug):
  base_url = 'https://neo4j.com/graphconnect-2018/session/'
  return '%s%s' % (base_url, slug)

def gen_full_topic_url(topic):
  base_url = 'https://neo4j.com/graphconnect-2018/session-topics/?topic='
  return '%s%s' % (base_url, urllib.quote(topic))

def get_sessions():
  r = requests.get(sched_sessions)
  sessions = r.json()
  return sessions

def get_session_urls():
  session_slugs = []
  sessions = get_sessions()
  for session in sessions:
    if 'SLUG' in session:
      session_slugs.append(session['SLUG'])
  return map(gen_full_session_url, session_slugs)

def get_session_topics():
  topics = set()
  sessions = get_sessions()
  for session in sessions:
    if 'TAGS' in session:
      tag_array = session['TAGS'].split('; ')
      for tag in tag_array:
        topics.add(tag)
  return topics

def get_topic_urls():
  topics = get_session_topics()
  return map(gen_full_topic_url, topics)
 
topic_urls = get_topic_urls()
for url in topic_urls:
  print url

session_urls = get_session_urls()
for url in session_urls:
  print url

