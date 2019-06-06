
class TwitterIntentClient:

    def __init__(self, *, text=None, shere_url=None, via=None, hashtags=None, related=None):

        self.__BASE_URL = 'https://twitter.com/intent/tweet'
        self.text = text
        self.via = via
        self.shere_url = shere_url
        self.hashtags = hashtags
        self.related = related

        self.url = self.__BASE_URL
        if text != None or shere_url != None or via != None or hashtags != None or related != None:
            query = []
            if text != None:
                query.append(('text=' + text))
            if shere_url != None:
                query.append(('url=' + shere_url))
            if via != None:
                query.append(('via=' + via))
            if hashtags != None:
                query.append(('hashtags=' + hashtags))
            if related != None:
                query.append(('related=' + related))
            
            query = '&'.join(query) if len(query) >= 2 else query[0]
            self.url = self.__BASE_URL + '?' + query
        