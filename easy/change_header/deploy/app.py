from flask import Flask, request, jsonify, render_template

app = Flask(__name__)
app.config["JSON_AS_ASCII"] = False


@app.route("/", methods=["GET", "POST"])
def home():
    user_agent = request.headers.get("User-Agent")
    cookie = request.cookies.get("cookie")
    proxy_param = None
    if request.method == "GET":
        return (
            jsonify({"message": "bot이 아닙니다!", "hint": "/hint를 확인해 주세요!"}),
            403,
        )

    proxy_param = request.form.get("proxy")

    if user_agent != "bot":
        return jsonify({"message": "bot이 아닙니다!"}), 403
    elif cookie != "Sweat cookie~":
        return jsonify({"message": "쿠키가 올바르지 않습니다!"}), 403
    elif proxy_param != "is fun!!":
        return jsonify({"message": "프록시 파라미터가 올바르지 않습니다!"}), 403
    else:
        return jsonify({"message": "K0{M4n1pul4t1ng_c00k13s_1s_qu1t3_3z!!}"}), 200


@app.route("/hint")
def hint():
    return jsonify(
        {
            1: "User-Agent 헤더를 'bot'으로 설정하세요!",
            2: "쿠키에 'Sweat cookie~' 값을 설정하세요!",
            3: "Post 요청으로 proxy파라미터를 'is fun!!'으로 설정하세요!",
        }
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
