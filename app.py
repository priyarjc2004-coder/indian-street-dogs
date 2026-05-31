from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Indian Street Dogs</title>
        <style>
            body{
                font-family: Arial, sans-serif;
                background-color: #f5f5f5;
                text-align:center;
                padding:20px;
            }
            h1{
                color:#d35400;
            }
            img{
                width:300px;
                border-radius:10px;
            }
            .card{
                background:white;
                padding:20px;
                margin:auto;
                max-width:800px;
                border-radius:15px;
                box-shadow:0 0 10px rgba(0,0,0,0.2);
            }
        </style>
    </head>
    <body>
        <div class="card">
            <h1>🐕 Indian Street Dogs</h1>

            <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/8/87/Indian_Pariah_Dog.jpg/640px-Indian_Pariah_Dog.jpg">

            <h2>About Indian Street Dogs</h2>

            <p>
                Indian street dogs, also known as Indian Pariah Dogs,
                are intelligent, loyal, and well-adapted to the Indian climate.
                They play an important role in maintaining ecological balance.
            </p>

            <h2>How You Can Help</h2>

            <ul style="text-align:left;">
                <li>Provide clean water.</li>
                <li>Feed responsibly.</li>
                <li>Support vaccination drives.</li>
                <li>Promote adoption.</li>
                <li>Help injured dogs reach veterinarians.</li>
            </ul>

            <h2>Adopt, Don't Shop ❤️</h2>
        </div>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)