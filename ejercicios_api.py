from ast import Index
import requests, os, json

path_base = os.path.dirname(os.path.abspath(__file__))
BASE_URL = 'http://127.0.0.1:5000/'

def get_posts():
    r = requests.get(f'{BASE_URL}posts')
    if r.status_code == 200:
        return r.json()
    return []

def get_posts_by_user_id(user_id, posts):
    user_posts = []
    for post in posts:
        if post['userId'] == user_id:
            user_posts.append(post)
    return user_posts

def edit_post(post_id, title = None, body = None, user_id = None):
    update_data = {}
    if title is not None:
        update_data['title'] = title
    if body is not None:
        update_data['body'] = body
    if user_id is not None:
        update_data['userId'] = user_id
    r = requests.put(f'{BASE_URL}posts/{post_id}', json=update_data)
    if r.status_code == 200:
        return True
    return False

def new_post(title, body, user_id):
    post_data = {
        'title': title,
        'body': body,
        'userId': user_id
    }
    r = requests.post(f'{BASE_URL}posts', json=post_data)
    if r.status_code == 200:
        return r.json()['id']
    return -1

def delete_post(post_id):
    r = requests.delete(f'{BASE_URL}posts/{post_id}')
    if r.status_code == 200:
        return True
    return False

def delete_user_posts(user_id, posts):
    for post in posts:
        if post['userId'] == user_id:
            delete_post(post['id'])


def get_comments():
    r = requests.get(f'{BASE_URL}comments')
    if r.status_code == 200:
        return r.json()
    return []

def delete_comment(comment_id):
    r = requests.delete(f'{BASE_URL}comments/{comment_id}')
    if r.status_code == 200:
        return True
    return False

def delete_comentarios_sin_post(posts, comments, save=True):
    posts_ids = [post['id'] for post in posts]
    deleted = []
    for comment in comments:
        if comment['postId'] not in posts_ids:
            deleted.append(comment)
            delete_comment(comment['id'])
    if save:
        with open(f'{path_base}/deleted.json', 'w',  encoding='UTF-8') as archivo:
            archivo.write(json.dumps(deleted, indent=4))
def getCommentsPost(id_post):
    post_comments = []
    for comment in get_comments():
        if comment['postId'] == id_post:
            post_comments.append(comment)
    return post_comments

def getPostUser(id_user):
    postsUser = []
    # OBTENGO LOS POSTS POR USUARIO
    postsUser = get_posts_by_user_id(id_user,get_posts())
    # OBTENGO LOS COMMENTS POR POST
    
    # CREO UN JSON CON LA INFORMACIÓN PEDIDA
    listaFinal = {
        "id_user":id_user,
        "posts":[]
    }
    for post in postsUser:
        commentsPost = []
        for comment in getCommentsPost(post['id']):
            del comment['postId']
            commentsPost.append(comment)
        post['comments']=commentsPost
        del post['userId']
        listaFinal["posts"].append(post)
        
    with open(f'{path_base}/userPosts.json', 'w',  encoding='UTF-8') as archivo:
            archivo.write(json.dumps(listaFinal, indent=4))
    
    


posts = get_posts()
with open(f'{path_base}/posts.json', 'w',  encoding='UTF-8') as archivo:
            archivo.write(json.dumps(posts,indent=4)) 
# user_posts = get_posts_by_user_id(1, posts)
# # edit_post(user_posts[0]['id'], title='Cambio', body='hola')
# # print(new_post('Nuevo', 'nuevo post', 7))
# # delete_post(101)
# delete_user_posts(2, posts)
# posts = get_posts()
# comments = get_comments()
# delete_comentarios_sin_post(posts, comments)
# with open(f'{path_base}/userPosts.json', 'w',  encoding='UTF-8') as archivo:
#             archivo.write(json.dumps(get_posts(),indent=4))
getPostUser(1);



# {
#     'id': user_id,
#     'posts': [
#         {
#             'id': post_id,
#             'title': title,
#             'body': body,
#             'comments': [
#                 {
#                     'id': post_id,
#                     'title': title,
#                     'body': body,
#                 },
#                 ...
#             ]
#         },
#         ...
#     ]
# }