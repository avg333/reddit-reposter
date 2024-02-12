class NoPostsFoundException(Exception):
    def __init__(self, message="No posts found"):
        self.message = message
        super().__init__(self.message)
