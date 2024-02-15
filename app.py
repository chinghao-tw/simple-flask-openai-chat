from flask import Flask, render_template, request
import openai

app = Flask(__name__)

# Set OpenAI API key
openai.api_key = 'YOUR_OPENAI_API_KEY'


@app.route('/', methods=['GET', 'POST'])
def index():
    user_input = None
    model_output = None

    if request.method == 'POST':
        user_input = request.form['user_input']
        # Use GPT-3.5-turbo generate output text
        completion = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{
                "role": "user",
                "content": user_input
            }]
        )
        model_output = completion.choices[0].message.content

    return render_template(
        'index.html',
        user_input=user_input,
        model_output=model_output)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
