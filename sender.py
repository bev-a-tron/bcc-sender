from mandrill import Mandrill
from config import MANDRILL_API_KEY


class MandrillClientSingleton:
    """Class for lazy instantiation of a Mandrill client"""
    _client = None

    @property
    def client(self):
        if self._client is None:
            key = MANDRILL_API_KEY
            self._client = Mandrill(key)
        return self._client


class Message:

    def __init__(self, **kwargs):
        self._recipient = kwargs['recipient']
        # self._from_email = kwargs['from_email']
        self._html = kwargs['html']

    def build_message(self):
        return {
            'to': [{'email': self._recipient}],
            'subject': "Letter to the editor",
            'html': self._html,
            'from_email': "anna@duosecurity.com",
            'headers': {
                'Reply-To': 'beverly.a.lau@gmail.com'
            }
        }

    def send(self):
        message = self.build_message()
        mandrill_response = MandrillClientSingleton().client.messages.send(message=message)
        print(mandrill_response)

# emails = ['vpatton@sfmediaco.com',
#           'ccnletters@bayareanewsgroup.com',
#           'wcletters@bayareanewsgroup.com',
#           'vtletters@bayareanewsgroup.com',
#           'triblet@bayareanewsgroup.com',
#           'letters@mercurynews.com',
#           'Arglet@bayareanewsgroup.com',
#           'revlet@bayareanewsgroup.com',
#           'opinion@marinij.com',
#           'letters@mercurynews.com',
#           'Letters@DAILYJOURNAL.COM',
#           'letters@smdailyjournal.com',
#           'lettertoeditor@epochtimes.com',
#           'editor@avpress.com',
#           'opinion@bakersfield.com',
#           'dlittle@chicoer.com',
#           'dhatfield@cctimes.com',
#           'letters@thedesertsun.com']

emails = ['nuxoll.anna@gmail.com',
          'beverly.a.lau@gmail.com']

input_from_email = 'beverly@karmiclabs.com'
input_html = 'lalalallalalal'

for email in emails:
    m = Message(recipient=email, html=input_html)
    m.send()

# receipt email, email body includes list of emails it was sent to
# m = Message(recipient=person_who_sent_it, html=input_html)

