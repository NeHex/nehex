/api/v1/getPost?<postid>

> return

``` json
{
    "code": 0,
    "info": {
        "pid": 101,
        "title": "Hello World!",
        "date": 1763872870,
        "tags": ["default", "test", "NeHex"],
        "class": "default",
        "author": "admin",
        "cover": "./static/cover.png",
        "intro": "This is the default article of NeHex"
    },
    "article": {
        "ai_summary": "This is the default article of NeHex.",
        "main": "This is the default article of NeHex. You can edit this article or create a new one for preview. NeHex is a very powerful web blog program based on Python and Vue. It has a wonderful engine!!!",
        "footer": "Subscribe to me at -> ueg.ee"
    }
}
```