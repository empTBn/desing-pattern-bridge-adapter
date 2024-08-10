from bromelia_pict_inventory import BromeliaPictInventory

inventory = BromeliaPictInventory()
top_photos = inventory.get_top_photos('nature')
for photo in top_photos:
    print(photo['url'])