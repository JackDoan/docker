from flask import Flask, render_template_string
from deployo.src.kickstarts.kickstart_generator import KickstartGenerator
import deployo.src.docker.swarm as swarm

app = Flask(__name__)

kick_gen = KickstartGenerator()


@app.route('/')
def bopis():
    return "<h1>Buy online, pick up in store!</h1>"


@app.route('/debug')
def do_debug_shell():
    raise Exception


@app.route('/docker/swarm/join')
def get_swarm_token():
    return swarm.get_join_cmd()


@app.route('/ksfile/<spec>')
def get_ks_file(spec):
    # needed for baseurl generation
    return render_template_string(kick_gen.get(spec).__str__(), spec=spec)


@app.route('/ksfile/<spec>/firstboot')
def get_firstboot_script(spec):
    return kick_gen.get_firstboot(spec).__str__()


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
