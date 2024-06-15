## Base templates
```python

{% extends 'html/base.html' %}

# Title if not passed will be replaced by the Server Name
{% block title %}...{% endblock %}

# Description if not passed will be replaced by default description
{% block description %}...{% endblock %}

# Head Content
{% block head %}...{% endblock %}

# Body Content
{% block body %}...{% endblock %}

```

## Development
- constants configuration - Important
```python
# settings.py
BOT_TOKEN = BOT TOKEN
SERVER_ID = SERVER ID 
```

- setting Up a Django Project
```sh
python3 -m venv venv
unix: source venv/bin/activate
windows:  venv\Scripts\activate
pip install -r requirements.txt
```
