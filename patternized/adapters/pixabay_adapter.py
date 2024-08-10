import requests

class PixabayAdapter:
    def __init__(self, api_key):
        self.api_key = api_key
    
    def search_photos(self, query, per_page=10):
        url = f"https://pixabay.com/api/?key={self.api_key}&q={query}&per_page={per_page}"
        response = requests.get(url)
        photos = response.json()['hits']
        return self._adapt_photos(photos)
    
    def _adapt_photos(self, photos):
        return [
            {
                'id': photo['id'],
                'url': photo['largeImageURL'],
                'likes': photo['likes'],
                'views': photo['views'],
                'comments': photo['comments']
            }
            for photo in photos
        ]
