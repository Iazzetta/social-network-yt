import httpx

token = "vjw4jETwGlwojtyq5jrtv7JwMcs"

def create_post():
    r = httpx.post(f'http://localhost:8000/posts/create', headers={
        'Authorization': token,
        'Content-Type': 'application/json'
    }, json={
        'message': 'Olá mundo!'
    })
    response = r.json()

    print(r.status_code)
    print('create_post', response)

def like_post(post_id):

    r = httpx.post(f'http://localhost:8000/posts/{post_id}/like', headers={
        'Authorization': token,
        'Content-Type': 'application/json'
    })
    response = r.json()

    print(r.status_code)
    print('like_post', response)


# create_post()
like_post(1)