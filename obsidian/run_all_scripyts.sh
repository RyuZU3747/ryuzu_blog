#!/bin/bash

SYNC_POSTS=./obsidian/sync_post.py
HANDLE_IMGES=./obsidian/handle_images.py
YOUTUBE_PATH=./obsidian/update_youtube_path.py

python $SYNC_POSTS
python $HANDLE_IMGES
python $YOUTUBE_PATH

git add .
git commit -am "update blog"
git push