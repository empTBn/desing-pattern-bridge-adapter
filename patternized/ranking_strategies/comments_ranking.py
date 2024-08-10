class CommentsRanking:
    def rank(self, photos):
        return sorted(photos, key=lambda x: x['comments'], reverse=True)
