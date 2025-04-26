from .comment import register_comment_admin
from .post import register_post_admin

registers = [register_post_admin, register_comment_admin]

for reg in registers:
    reg()
