# Make use of request module in python to send a request to https://jsonplaceholder.typicode.com
# using Thread.



import requests
import threading
base_url = 'https://jsonplaceholder.typicode.com'
def get_post(post_id):
    response = requests.get(f'{base_url}/posts/{post_id}')
    print(f'GET Post {post_id}:', response.json())
def create_post(post_data):
    response = requests.post(f'{base_url}/posts', json=post_data)
    print('POST:', response.json())
def update_post(post_id, post_data):
    response = requests.put(f'{base_url}/posts/{post_id}', json=post_data)
    print('PUT Post {post_id}:', response.json())
def patch_post(post_id, post_data):
    response = requests.patch(f'{base_url}/posts/{post_id}', json=post_data)
    print('PATCH Post {post_id}:', response.json())
def delete_post(post_id):
    response = requests.delete(f'{base_url}/posts/{post_id}')
    print('DELETE Post {post_id}:', response.status_code)
def main():
    threads = []
    threads.append(threading.Thread(target=get_post, args=(1,)))
    threads.append(threading.Thread(target=create_post, args=({'title': 'New Post', 'body': 'This is a new post.', 'userId': 1},)))
    threads.append(threading.Thread(target=update_post, args=(1, {'title': 'Updated Post', 'body': 'This post has been updated.'})))
    threads.append(threading.Thread(target=patch_post, args=(1, {'title': 'Patched Post'})))
    threads.append(threading.Thread(target=delete_post, args=(1,)))
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
if __name__ == "__main__":
    main()
