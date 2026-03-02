<!-- GENERATED:MODEL -->
---
tags: [odoo, enterprise, generated, model]
---

# social.stream.post

- Module: [[docs/Enterprise Addons/social_twitter/social_twitter|social_twitter]]
- Scope: Enterprise Addons
- Defined in module: extension only
- Source files: `models/social_stream_post.py`
- Python classes: `SocialStreamPost`

## Field footprint

- Detected fields: 16
- Field types: `Boolean` x 2, `Char` x 10, `Integer` x 3, `Text` x 1
- Relation fields: 0

## Sample fields

- `twitter_author_id`: `Char` (comodel `X Author ID`)
- `twitter_can_retweet`: `Boolean` (comodel `X Repost Permission`, compute `_compute_twitter_can_retweet`)
- `twitter_comments_count`: `Integer` (comodel `X Replies`)
- `twitter_conversation_id`: `Char` (comodel `X Conversation ID`)
- `twitter_likes_count`: `Integer` (comodel `X Likes`)
- `twitter_profile_image_url`: `Char` (comodel `X Profile Image URL`)
- `twitter_quoted_tweet_author_link`: `Char` (comodel `Quoted post author Link`)
- `twitter_quoted_tweet_author_name`: `Char` (comodel `Quoted post author Name`)
- `twitter_quoted_tweet_id_str`: `Char` (comodel `X Quoted post ID`)
- `twitter_quoted_tweet_message`: `Text` (comodel `Quoted post message`)
- `twitter_quoted_tweet_profile_image_url`: `Char` (comodel `Quoted post profile image URL`)
- `twitter_retweet_count`: `Integer` (comodel `Reposts`)
- `twitter_retweeted_tweet_id_str`: `Char` (comodel `X Repost ID`)
- `twitter_screen_name`: `Char` (comodel `X Screen Name`)
- `twitter_tweet_id`: `Char` (comodel `X Post ID`)
- `twitter_user_likes`: `Boolean` (comodel `X User Likes`)

## Method hints

- Detected methods: 13
- Action methods: none
- Compute methods: `_compute_author_link`, `_compute_is_author`, `_compute_post_link`, `_compute_twitter_can_retweet`
- Onchange methods: none

## Navigation

- **Parent:** [[docs/Enterprise Addons/social_twitter/Models]]

<!-- GENERATED:MODEL -->
