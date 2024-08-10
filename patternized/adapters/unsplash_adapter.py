import requests

class UnsplashAdapter:
    def __init__(self, access_key):
        self.access_key = access_key
    
    def search_photos(self, query, per_page=10):
        url = f"https://api.unsplash.com/search/photos?query={query}&per_page={per_page}&client_id={self.access_key}"
        response = requests.get(url)
        photos = response.json()['results']
        return self._adapt_photos(photos)
    
    def _adapt_photos(self, photos):
        return [
            {
                'id': photo['id'],
                'url': photo['urls']['regular'],
                'likes': photo['likes'],
                'views': photo['views'],
                'comments': photo['comments']
            }
            for photo in photos
        ]
