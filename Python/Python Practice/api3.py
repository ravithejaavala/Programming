from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample in-memory data
posts = [
    {"id": 1, "title": "Hello World", "body": "This is my first post!"},
    {"id": 2, "title": "REST API", "body": "Learning REST APIs with Flask!"}
]

# Get all posts
@app.route('/posts', methods=['GET'])
def get_posts():
    return jsonify(posts)

# Get a single post by ID
@app.route('/posts/<int:post_id>', methods=['GET'])
def get_post(post_id):
    for post in posts:
        if post['id'] == post_id:
            return jsonify(post)
    return jsonify({'message': 'Post not found'}), 404

# Create a new post
@app.route('/posts', methods=['POST'])
def create_post():
    new_post = request.json
    new_post['id'] = len(posts) + 1
    posts.append(new_post)
    return jsonify(new_post), 201

# Update an existing post
@app.route('/posts/<int:post_id>', methods=['PUT'])
def update_post(post_id):
    for post in posts:
        if post['id'] == post_id:
            post.update(request.json)
            return jsonify(post)
    return jsonify({'message': 'Post not found'}), 404

# Delete a post
@app.route('/posts/<int:post_id>', methods=['DELETE'])
def delete_post(post_id):
    for index, post in enumerate(posts):
        if post['id'] == post_id:
            deleted = posts.pop(index)
            return jsonify(deleted) 
    return jsonify({'message': 'Post not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
