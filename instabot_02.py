from instapy import InstaPy



# Login
session = InstaPy(username="j_newroom", password="g0l0ndr1na")
session.login()

# Settings
session.set_relationship_bounds(enabled=True, max_followers=1500)
session.set_do_follow(True, percentage=50)
session.set_do_comment(True, percentage=50)
session.set_comments(["\U0001F4AA", "Nice!!", "Keep it running!!"])
session.like_by_tags(["trailrunning", "mountains"], amount=5)