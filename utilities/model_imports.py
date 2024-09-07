def import_models_for_migrations():
    from models.user_model import User
    from models.post_model import Post
    from models.like_and_comment_model import LikeAndComment
    from models.dummy_model import Dummy

    # Just a dummy function to keep linter quiet
    return User, Post, LikeAndComment, Dummy
