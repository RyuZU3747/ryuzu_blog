#!/bin/bash
SYNC_POSTS=C:/git/ryuzu_blog/obsidian/sync_posts.py
HANDLE_IMGES=C:/git/ryuzu_blog/obsidian/handle_images.py
YOUTUBE_PATH=C:/git/ryuzu_blog/obsidian/update_youtube_path.py

python $SYNC_POSTS
python $HANDLE_IMGES
python $YOUTUBE_PATH

git add .
git commit -am "update blog"
git push