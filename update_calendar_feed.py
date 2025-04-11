
import os
from datetime import datetime
from xml.etree.ElementTree import Element, SubElement, tostring
import xml.dom.minidom as minidom

# Your static to-do list (can be modified or loaded from a file)
todo_list = [
    {"title": "Write up student", "due": "2025-04-10T08:00:00"},
    {"title": "Call Skip", "due": "2025-04-11T10:00:00"},
    {"title": "Clean the floors", "due": "2025-04-12T17:00:00"},
    {"title": "Pack for trip", "due": "2025-04-14T18:00:00"},
    {"title": "Make extra BandMan37 reels", "due": "2025-04-14T20:00:00"},
    {"title": "Message Skip", "due": "2025-04-13T15:00:00"},
    {"title": "Update to-do list and prep for spring concert", "due": "2025-04-17T10:00:00"},
    {"title": "Practice guitar for church", "due": "2025-04-13T19:00:00"},
]

# Generate XML calendar feed
rss = Element('rss', version='2.0')
channel = SubElement(rss, 'channel')
SubElement(channel, 'title').text = "ChatGPT Synced To-Do Calendar"
SubElement(channel, 'description').text = "Auto-generated events from ChatGPT task list"
SubElement(channel, 'link').text = "https://github.com/samdotson505/chatgptcalendar"

for task in todo_list:
    item = SubElement(channel, 'item')
    SubElement(item, 'title').text = task["title"]
    SubElement(item, 'description').text = f"Auto-added task: {task['title']}"
    SubElement(item, 'pubDate').text = task["due"]
    SubElement(item, 'guid').text = task["title"] + "_" + task["due"]

# Beautify and save XML
xml_data = minidom.parseString(tostring(rss, 'utf-8')).toprettyxml(indent="  ")
with open("chatgptcalendar.xml", "w") as f:
    f.write(xml_data)

# Git add, commit, and push
os.system("git add chatgptcalendar.xml")
os.system("git commit -m 'Auto-update calendar feed from local script'")
os.system("git push origin main")

print("✅ Calendar feed updated and pushed to GitHub.")
