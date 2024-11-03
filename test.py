import httpx

ENDPOINT_API = "http://localhost:8000"

def create_user():
    data = {
        "name": "outro usuario comentando",
        "email": "fduysgfuydgfuds@teste.com",
        "password": "123456789"
    }

    r = httpx.post(f'{ENDPOINT_API}/users/register', json=data)

    response = r.json()

    return response['token']

def create_post(token):
    r = httpx.post(f'{ENDPOINT_API}/posts/create', headers={
        'Authorization': token,
        'Content-Type': 'application/json'
    }, json={
        'message': 'Olá mundo!'
    })
    response = r.json()
    new_post = response['post']

    return new_post['id']

def like_post(token, post_id):

    r = httpx.post(f'{ENDPOINT_API}/posts/{post_id}/like', headers={
        'Authorization': token,
        'Content-Type': 'application/json'
    })
    response = r.json()

    return response

def comment_post(token, post_id):

    message = 'test comentario'

    r = httpx.post(f'{ENDPOINT_API}/posts/{post_id}/comment', headers={
        'Authorization': token,
        'Content-Type': 'application/json'
    }, json={
        'message': message
    })
    response = r.json()

    print(response)

    return response


# TESTES

token = create_user()

post_id = create_post(token)
print('new post', post_id)

like = like_post(token, post_id)
print('like', like)

deslike = like_post(token, post_id)
print('deslike', deslike)

comment_post(token, post_id)

print('ID DO POST COM COMENTARIO', post_id)
