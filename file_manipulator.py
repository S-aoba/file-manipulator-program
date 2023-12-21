import sys

# print(sys.argv)

# 操作するコマンド名を取得する
command = sys.argv[1]

# reverse: inputpath にあるファイルを受け取り、outputpath に inputpath の内容を逆にした新しいファイルを作成します。
if command == "reverse":
    input_path = sys.argv[2]
    output_path = sys.argv[3]

    content = ""
    
    # input_pathを読み込んで、中身を取得
    with open(input_path, "r") as f:
        content = f.read() 
    # output_pathを読み込んで、contentをreverseさせて書き込む
    with open(output_path, "w") as f:
        # contentの中身を逆にする
        reverse_content = content[::-1]
        # 書き込む
        f.write(reverse_content)

elif command == "copy":
    input_path = sys.argv[2]
    output_path = sys.argv[3]

    content = ""

    with open(input_path, "r") as f:
        content = f.read()

    with open(output_path, "w") as f:
        f.write(content)

elif command == "duplicate-contents":
    input_path = sys.argv[2]
    n_str = sys.argv[3]
    n = int(n_str)

    content = ""
    with open(input_path, "r") as f:
        content = f.read()

    with open(input_path, "w") as f:
        for i in range(n):
            f.write(content)

elif command == "replace-string":
    input_path = sys.argv[2]
    neefle = sys.argv[3]
    new_string = sys.argv[4]

    content = ""

    with open(input_path, "r") as f:
        content = f.read()

        replace_content = content.replace(neefle, new_string)
    with open(input_path, "w") as f:
        f.write(replace_content)
else:
    print("コマンドが正しくありません")