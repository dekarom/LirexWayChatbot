
from concurrent.futures import thread
from ipaddress import ip_address
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer
import flask 
from flask import Flask, request, render_template


#####
#Chat Functionality
#####

chatbot = ChatBot('LirexWay')
trainer = ListTrainer(chatbot)   

trainer.train([
"Hi","Hello, how are you doing?",
"Who are you?","I am a bot assitant",
"What is Lirex Way?", "Lirex Way is a place for sharing knowledge!"])

trainer.train([
"Здравей","Привет! Как си?",
"Какво си?","Аз съм персонален чат-бот асистент",
"Какво е Lirex Way", "Lirex Way е място за споделяне на знания и интерсни нови технологии"])

# Train bot on data set
#trainer_smart = ChatterBotCorpusTrainer(chatbot)
#trainer_smart.train("chatterbot.corpus.english")


######
# Server Section
######
app = flask.Flask(__name__)
@app.route("/", methods = ["GET","POST"])

def writeToPage():
    response = ''
    if request.method == "POST":
        user_request=request.form.get("userText")
        response= chatbot.get_response(user_request)
        #print(userRequest)
        #return str(response)
    return flask.render_template("ui.html", output=response)
    

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True, threaded=True)
    