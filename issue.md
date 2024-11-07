I'm creating a post to test the patching functionality of the API.
```
curl -X POST http://127.0.0.1/unsubscribe -d '{"email": "test; SELECT * FROM users;"}'
```
and I'm getting more results than I expected.