import config
import emails
from mandrill import Mandrill


class MandrillClientSingleton:
    """Class for lazy instantiation of a Mandrill client"""
    _client = None

    @property
    def client(self):
        if self._client is None:
            key = config.MANDRILL_API_KEY
            self._client = Mandrill(key)
        return self._client


class Message:

    def __init__(self, *, recipient, from_email, html, newspaper_name, from_name):
        self._recipient = recipient
        self._from_email = from_email
        self._html = html
        self._newspaper_name = newspaper_name
        self._from_name = from_name

    def build_message(self):
        return {
            'to': [{'email': self._recipient}],
            'subject': "Letter to the editor of " + self._newspaper_name,
            'text': self._html,
            'from_email': self._from_email,
            'from_name': self._from_name
        }

    def send(self):
        message = self.build_message()
        mandrill_response = MandrillClientSingleton().client.messages.send(message=message)
        print(mandrill_response)


def make_and_send_emails(*, sources, from_email, from_name, html):
    for newspaper_name, email in sources.items():
        m = Message(recipient=email, newspaper_name=newspaper_name, from_email=from_email,
                    from_name=from_name, html=html)
        m.send()


if __name__ == "__main__":

    e = emails.TEST_SOURCES
    input_from_email = emails.TEST_FROM_EMAIL
    input_html = 'lalalallalalal'

    for newspaper_name, email in e.items():
        m = Message(recipient=email, newspaper_name=newspaper_name, from_email=input_from_email,
                    html=input_html, from_name='Beverlyyyyyy')
        m.send()

    # receipt email, email body includes list of emails it was sent to
    # m = Message(recipient=person_who_sent_it, html=input_html)

