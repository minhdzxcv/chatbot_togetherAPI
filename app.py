from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)


# Route trang chủ
@app.route('/')
def index():
    return render_template('index.html')


# Route xử lý câu hỏi
@app.route('/ask', methods=['POST'])
def ask():
    user_input = request.json['question']

    # Gửi yêu cầu đến API (hoặc bạn có thể thay bằng code logic của bạn)
    url = "https://api.together.xyz/v1/chat/completions"
    headers = {
        "Authorization": "Bearer 1a793227b79c2dc0ac84b37f68c6638fa9e0f3ba877b96605e52f30c6119582a",
        "Content-Type": "application/json"
    }
    payload = {
        "messages": [
            {"role": "user", "content": user_input}
        ],
        "model": "mistralai/Mixtral-8x7B-Instruct-v0.1"
    }

    response = requests.post(url, json=payload, headers=headers)

    if response.status_code == 200:
        answer = response.json()['choices'][0]['message']['content']
    else:
        answer = "Sorry, there was an error with the API."

    return jsonify({'answer': answer})


if __name__ == '__main__':
    app.run(debug=True)
