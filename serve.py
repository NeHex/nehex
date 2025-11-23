from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return jsonify({
        "code": 0,
        "msg": "ok"
    })

@app.route('/getPost')
def get_post():
    uid = request.args.get('uid')
    # 可选：可以加一些 uid 的校验逻辑，比如是否为数字等
    return jsonify({
        "code": 0
    })


# 自定义 404 错误：路径不存在
@app.errorhandler(404)
def not_found(error):
    return jsonify({
        "code": 1,
        "msg": "Not Found"
    }), 404

# 自定义 500 错误：服务器内部错误
@app.errorhandler(500)
def internal_error(error):
    return jsonify({
        "code": 1,
        "msg": "Internal Server Error"
    }), 500

# 捕获所有其他 HTTP 异常（可选）
@app.errorhandler(Exception)
def handle_exception(e):
    # 如果是 HTTP 异常（如 400, 403 等），Flask 会自动处理
    # 这里主要捕获非 HTTP 的异常（比如代码写错了）
    app.logger.error(f"Unhandled exception: {e}")
    return jsonify({
        "code": 500,
        "msg": "An unexpected error occurred"
    }), 500


if __name__ == '__main__':
    print("NeHex Running.")
    app.run(host='0.0.0.0', port=2333, debug=True)