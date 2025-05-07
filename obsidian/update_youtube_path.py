import os
import re

# Paths
hugo_posts_dir = "./content/blogs"

# Step 1: Process each markdown file in the posts directory
for filename in os.listdir(hugo_posts_dir):
    if filename.endswith(".md"):
        filepath = os.path.join(hugo_posts_dir, filename)

        with open(filepath, "r") as file:
            content = file.read()

        # Step 2: Find all YouTube links in the format ![](https://www.youtube.com/watch?v=asdf)
        youtube_links = re.findall(
            r"(?:https?:\/\/)?(?:www\.)?(?:youtube\.com\/watch\?v=|youtu\.be\/)([a-zA-Z0-9_-]{11})", content
        )

        # Step 3: Replace YouTube links with the Hugo shortcode format
        for video_id in youtube_links:
            hugo_shortcode = f'{{{{< youtube id="{video_id}" >}}}}'
            content = content.replace(
                f"https://www.youtube.com/watch?v={video_id}", hugo_shortcode
            )

        # Step 4: Write the updated content back to the markdown file
        with open(filepath, "w") as file:
            file.write(content)

print("YouTube links updated successfully.")
