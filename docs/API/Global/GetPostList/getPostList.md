
/api/v1/getPostList?<page_id>

> return

```json
{
    "code": 0,
    "pageid": 0,
    "articles": [
        {
            "pid": 101,
            "title": "Hello World!",
            "date": 1763872870,
            "tags": ["default", "test", "NeHex"],
            "class": "default",
            "author": "admin",
            "cover": "./static/cover.png"
        },
        {
            "pid": 102,
            "title": "Test",
            "date": 1763872870,
            "tags": ["test"],
            "class": "default",
            "author": "admin",
            "cover": "./static/cover.png"
        }
    ]
}
```

/api/v1/getPostList?<post_class>
/api/v1/getPostList?<post_tag>
