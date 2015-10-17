import emails
from flask import Flask, render_template, request
from sender import make_and_send_emails

app = Flask(__name__)

EXAMPLE_LETTER = """
Dear Editor,

So many of us don’t even bother to vote.  Perhaps this is because we no longer trust that our government represents us.  People across the political spectrum agree that unlimited corporate donations drown out our voices – and negatively influence US policy.

One candidate has a unique approach to fixing democracy and is worthy of more of our attention:  Lawrence Lessig.  Lessig, an activist and law professor, is running as a “referendum” candidate, promising to serve only as long as it takes to enact a package of reforms designed to restore citizen equality.  The Citizen's Equality Act, as the act is known, draws on existing proposals for fundamental reform.  Lessig intends to use the mandate of his election to get the Act passed.

The people are desperate for an “outsider” with a creative approach to fixing democracy.  More coverage of Lessig’s ideas is what is needed to make people realize that they have a voice – and someone wants to hear it.

Sincerely,


"""


@app.route('/')
def index():
    e = emails.TEST_SOURCES
    return render_template('form.html', example_letter=EXAMPLE_LETTER, emails=e)


@app.route('/submit', methods=['POST'])
def submit():
    letter = request.form['user_letter']
    from_name = request.form['user_name']
    from_email = request.form['user_email']

    sources = emails.TEST_SOURCES.copy()

    # super hacky hack
    things_to_delete = []
    for newspaper_name, newspaper_email in sources.items():
        if request.form.get(newspaper_email) != 'on':
            things_to_delete.append(newspaper_name)

    for key in things_to_delete:
        del sources[key]

    make_and_send_emails(sources=sources, from_email=from_email, from_name=from_name, html=letter)

    return render_template('end.html', emails=sources)

if __name__ == '__main__':
    app.run(debug=True)
