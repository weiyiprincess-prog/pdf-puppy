from flask import Flask, render_template, request
from flask import Flask, render_template, request
import os
import uuid

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        file = request.files.get("pdf")

        if not file or file.filename == "":
            return render_template("index.html", message="請先選一個 PDF 檔案喔！")

        if not file.filename.lower().endswith(".pdf"):
            return render_template("index.html", message="只能上傳 PDF 檔案喔！")

        unique_name = str(uuid.uuid4()) + "_" + file.filename
        file_path = os.path.join(UPLOAD_FOLDER, unique_name)
        file.save(file_path)

        # 目前先做骨架：收到檔案後立刻刪除，不永久保存
        os.remove(file_path)

        return render_template(
            "index.html",
            message="狗狗成功收到 PDF！之後這裡會變成壓縮與下載功能 🐶"
        )

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)


