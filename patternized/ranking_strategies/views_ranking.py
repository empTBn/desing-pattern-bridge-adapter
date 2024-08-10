class ViewsRanking:
    def rank(self, photos):
        return sorted(photos, key=lambda x: x['views'], reverse=True)
