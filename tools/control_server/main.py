# -*- coding: utf-8 -*-
"""
    Main view
"""
from flask import Flask, jsonify, render_template, request, g
from adhoc.agent import AgentBot

app = Flask(__name__)
API_version = "v1"


@app.route('/api/%s/%s' % (API_version, "execute"))
def execute_cmd():
    """Executes an ad-hoc command in the client specified"""
    print "*"*80
    to = request.args.get('node', '')
    command = request.args.get('command', '')

    # Using Ad-Hoc commands
    g.xmpp_agent.prepare_adhoc(to, command)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/connect')
def connect():
    """Connect with the server"""
    g.xmpp_agent = AgentBot("admin@localhost", "admin")

    g.xmpp_agent.register_plugin('xep_0030') # Service Discovery
    g.xmpp_agent.register_plugin('xep_0004') # Data Forms
    g.xmpp_agent.register_plugin('xep_0050') # Adhoc Commands

    if g.xmpp_agent.connect():
        g.xmpp_agent.process(block=True)
        print("Done")
    else:
        print("Unable to connect.")  

    print "_"*80
    return jsonify("success")


if __name__=='__main__':
    app.run()