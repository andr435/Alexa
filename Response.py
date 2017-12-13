import random

class Response:
    api_version = "1.0"
    speach = {}
    card = None
    repromt = None
    directives = None
    session = {}
    end_session = True

    def __init__(self, text, type='text'):
        if type == 'text':
            self.speach = {"type": "PlainText", "text": text}
        else:
            self.speach = {"type": "SSML", "ssml": text}

    def set_text(self, text):
        self.speach = {"type": "PlainText", "text": text}

    def set_ssml(self, text):
        self.speach = {"type": "SSML", "ssml": text}

    def set_card(self, title, text, small_pic=None, big_pic=None):
        self.card = {"type": "Standart", "title": title, "text": text}
        if small_pic is not None and big_pic is not None:
            self.card['image'] = {"smallImageUrl": small_pic, "largeImageUrl": big_pic}

    def set_card_simple(self, title, text):
        self.card = {"type": "Simple", "title": title, "content": text}

    def set_card_link(self):
        self.card = {"type": "LinkAccount"}

    def set_repromt(self, text):
        self.repromt = {"type": "PlainText", "text": text}

    def set_repromt_ssml(self, text):
        self.repromt = {"type": "SSML", "ssml": text}

    def set_session(self, ses):
        self.session = ses

    def add_to_session(self, ses)
        for key, value in ses.items():
            if key not in self.session:
                self.session[key] = value

    def remove_from_session(self, key):
        if key in self.session:
            del self.session[key]

    def set_end_session(self, end_ses = True):
        self.end_session = end_ses

    def set_directive(self, directive):
        if self.directives is None:
            self.directives = [directive]

    def add_directive(self, directive):
        if self.directives is None:
            self.directives = [directive]
        else:
            self.directives.append(directive)

    def add_audio_directive(self, url, behavior = "REPLACE_ALL", token = None, offset = 0):
        if token is None:
            token = self.create_token()
        directive = {"type": "AudioPlayer.Play", "playBehavior": behavior, "audioItem": { "stream": { "token": token, "url": url, "offsetInMilliseconds": offset }}}
        self.add_directive(directive)

    def set_audio_directive(self, behavior)

    def create_token(self, length = 64)
        rand = list('qwertyuioplkjhgfdsazxcvbnmQWERTYUIOPLKJHGFDSAZXCVBNM1234567890')
        token = ''
        i = 0
        for i in range(length):
            token +=random.choise(rand)
        return token
        
    