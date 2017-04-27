# commit-bot
Daily push with a telegram for committing and coding

## Setup
1. Setting the AWS credentials.
    - Follow [Setting AWS Credentials](https://github.com/apex/apex/blob/master/docs/aws-credentials.md)

2. Modify project.json
```json
{
    ...
    "profile": "...",
    "role": "..."
    ...
}
```

3. Modify functions/push/config.py
```python
config = {
    'github': {
        'branch': {
            'faustring/kec-app-server': ['@Claude']
        },
        'id': '',
        'password': ''
    },
    'telegram': {
        'token': '',
        'chat_id': ''
    }
}
```

## Deploy & Test

```bash
# deploy
$ apex deploy

# test
$ apex invoke push
```

## TODO
- [ ] Automate Setup

## Refs
- [mingrammer](https://mingrammer.com/dev-commit-alarm-bot)