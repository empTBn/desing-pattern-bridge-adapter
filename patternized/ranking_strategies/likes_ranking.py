class LikesRanking:
    def rank(self, photos):
        return sorted(photos, key=lambda x: x['likes'], reverse=True)
