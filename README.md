# Playing with Django Context Processors


## Creating Your Own Context Processor

Create a new file &mdash; context_processors.py &mdash; inside your application. In this case, the application name is `main`.

```bash
touch main/context_processors.py
```

Put whatever info you like in your custom context processor.

```python
def avengers(request):
    return {
        'avengers': {
            'Tony Stark': 'Iron Man',
            'Peter Parker': 'Spider-Man',
            'Clint Barton': 'Hawkeye',
            'Bruce Banner': 'Professor Hulk',
            'Scott Lang': 'Ant-Man',
            'Natasha Romanoff': 'Black Widow',
            'Steve Rogers': 'Captain America'
        }
    }

```

Modify your `settings.py` so that it would look something like this.

```python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'main.context_processors.avengers', # new context processor
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```

You could refer to [templates/main/index.html](/templates/main/index.html) for using the context in your template. Your browser should look something like this.

![screenshot_01](/images/screenshot_01.png)
