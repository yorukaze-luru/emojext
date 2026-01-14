import re
from typing import List, Literal
import discord

class Emojext:
    """
    Discordメッセージから絵文字を抽出し、リアクションとして付けるクラス。
    インスタンス生成時にメッセージを渡すと、自動で絵文字を抽出・保存します。
    """

    _UNICODE_PATTERN = re.compile(
        r'('
        r'(?:[\U0001F1E6-\U0001F1FF]{2})|'  # 国旗
        r'(?:[\U0001F600-\U0001F64F])|'     # 顔文字
        r'(?:[\U0001F300-\U0001F5FF])|'     # 記号
        r'(?:[\U0001F680-\U0001F6FF])|'     # 乗り物
        r'(?:[\U0001F700-\U0001F77F])|'     # アルケミー
        r'(?:[\U0001F780-\U0001F7FF])|'     # 幾何学
        r'(?:[\U0001F800-\U0001F8FF])|'     # 補助矢印
        r'(?:[\U0001F900-\U0001F9FF])|'     # 拡張顔文字
        r'(?:[\U0001FA00-\U0001FAFF])|'     # 補助記号
        r'(?:[\u2600-\u26FF])|'             # その他記号
        r'(?:[\u2700-\u27BF])'              # 装飾記号
        r')(\uFE0F|\u200D[\w\u200D]+)*',
        flags=re.UNICODE
    )

    _CUSTOM_PATTERN = re.compile(r'<a?:\w+:\d+>')

    def __init__(self, message: discord.Message):
        """
        メッセージを受け取り、絵文字を抽出して保存する。
        """
        self.message = message
        self.unicode_emojis: List[str] = []
        self.custom_emojis: List[str] = []
        self._extract_emojis()

    def _extract_emojis(self) -> None:
        """
        メッセージ内容から絵文字を抽出して保存する（内部用）。
        """
        content = self.message.content
        unicode_matches = self._UNICODE_PATTERN.findall(content)
        self.unicode_emojis = [''.join(match) for match in unicode_matches]
        self.custom_emojis = self._CUSTOM_PATTERN.findall(content)

    async def react(
        self,
        emoji_type: Literal["all", "unicode", "custom"] = "all"
    ) -> None:
        """
        抽出済みの絵文字をリアクションとして付ける。

        Args:
            emoji_type: "unicode", "custom", "all" のいずれか
        """
        if emoji_type == "unicode":
            targets = self.unicode_emojis
        elif emoji_type == "custom":
            targets = self.custom_emojis
        else:
            targets = self.unicode_emojis + self.custom_emojis

        for emoji in targets:
            try:
                await self.message.add_reaction(emoji)
            except Exception:
                continue
