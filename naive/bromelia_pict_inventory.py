import requests

class BromeliaPictInventory:
    def __init__(self):
        self.pixabay_api_key = 'PIXABAY_API_KEY'
        self.unsplash_access_key = 'UNSPLASH_ACCESS_KEY'
    
    def search_photos_pixabay(self, query, per_page=10):
        url = f"https://pixabay.com/api/?key={self.pixabay_api_key}&q={query}&per_page={per_page}"
        response = requests.get(url)
        return response.json()['hits']
    
    def search_photos_unsplash(self, query, per_page=10):
        url = f"https://api.unsplash.com/search/photos?query={query}&per_page={per_page}&client_id={self.unsplash_access_key}"
        response = requests.get(url)
        return response.json()['results']
    
    def rank_photos_result(self, pixabay_photos, unsplash_photos):
        all_photos = pixabay_photos + unsplash_photos
        ranked_photos = sorted(all_photos, key=lambda x: x['likes'], reverse=True)
        return ranked_photos[:10]

    def get_top_photos(self, query):
        pixabay_photos = self.search_photos_pixabay(query)
        unsplash_photos = self.search_photos_unsplash(query)
        top_photos = self.rank_photos_result(pixabay_photos, unsplash_photos)
        return top_photos
