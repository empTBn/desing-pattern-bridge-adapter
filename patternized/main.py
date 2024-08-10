from bromelia_pict_inventory import BromeliaPictInventory
from ranking_strategies.likes_ranking import LikesRanking

inventory = BromeliaPictInventory(
    pixabay_api_key='YOUR_PIXABAY_API_KEY',
    unsplash_access_key='YOUR_UNSPLASH_ACCESS_KEY',
    ranking_strategy=LikesRanking()  
)

top_photos = inventory.get_top_photos('nature')
for photo in top_photos:
    print(photo['url'])
