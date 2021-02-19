from time import sleep
from instapy import InstaPy
import db_functions

# Login
session = InstaPy(username="j_newroom", password="g0l0ndr1na")
session.login()

my_followers = session.grab_followers(username="j_newroom", amount="full", live_match=True, store_locally=True)
print(len(my_followers))
send2db("")
sleep(600)

# Settings
session.set_relationship_bounds(enabled=True, max_followers=980)
session.set_do_follow(True, percentage=0)
session.set_do_comment(True, percentage=50)
session.set_comments(["\U0001F4AA", "nice!!"])
session.like_by_tags(["trailrunning"], amount=50)