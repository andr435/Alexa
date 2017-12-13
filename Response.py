class Response:
    api_version = "1.0"
    speach = {}
    card = None
    repromt = None
    directives = None

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
        skip

    def set_card_simple(selftitle, text):
        skip
    
        