# emojext

emojext は、Discord メッセージから Unicode 絵文字とカスタム絵文字（<:name:id> / <a:name:id>）を抽出し、リアクションとして自動で付ける Python ライブラリです。  
抽出・除外・リアクション処理をクラスベースで簡潔に扱えるよう設計されています。

---

🔧 特長

- Unicode 絵文字とカスタム絵文字を正規表現で抽出
- 除外したい絵文字を指定可能
- 抽出した絵文字を Discord メッセージにリアクションとして順に付与
- エラー（権限不足・存在しない絵文字など）は自動でスキップ

---

📦 インストール

GitHub から直接インストール：

```bash
pip install git+https://github.com/yorukaze-luru/emojext.git
```

---

🚀 使い方

```python
from discord.ext import commands
from emojext import Emojext

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())

@bot.event
async def on_message(message):
    if message.author.bot:
        return
    exclude = ["🎉", "<:ng:123456789012345678>"]
    handler = Emojext(message, exclude=exclude)
    await handler.react(emoji_type="all")```

---

⚙️ クラス仕様

Emojext(message, exclude=None)

| 引数       | 型              | 説明                                      |
|------------|------------------|-------------------------------------------|
| message  | discord.Message| 対象の Discord メッセージオブジェクト     |
| exclude  | List[str]      | 除外したい絵文字（Unicode またはカスタム）|

react(emoji_type="all")

| 引数         | 値           | 説明                                |
|--------------|---------------|-------------------------------------|
| emoji_type | "unicode"   | Unicode 絵文字のみリアクション       |
|              | "custom"    | カスタム絵文字のみリアクション       |
|              | "all"       | 両方の絵文字にリアクション（デフォルト）|

---

🧪 動作環境

- Python 3.8 以上
- discord.py 2.0 以上
