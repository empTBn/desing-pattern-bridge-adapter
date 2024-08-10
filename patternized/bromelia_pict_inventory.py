from adapters.pixabay_adapter import PixabayAdapter
from adapters.unsplash_adapter import UnsplashAdapter
from ranking_strategies.likes_ranking import LikesRanking
from ranking_strategies.views_ranking import ViewsRanking
from ranking_strategies.comments_ranking import CommentsRanking

class BromeliaPictInventory:
    def __init__(self, pixabay_api_key, unsplash_access_key, ranking_strategy):
        self.pixabay_adapter = PixabayAdapter(pixabay_api_key)
        self.unsplash_adapter = UnsplashAdapter(unsplash_access_key)
        self.ranking_strategy = ranking_strategy
    
    def get_top_photos(self, query):
        pixabay_photos = self.pixabay_adapter.search_photos(query)
        unsplash_photos = self.unsplash_adapter.search_photos(query)
        all_photos = pixabay_photos + unsplash_photos
        top_photos = self.ranking_strategy.rank(all_photos)
        return top_photos[:10]
