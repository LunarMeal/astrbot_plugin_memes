import os
import random

memes_dict = {"高兴":"happy",
              "悲伤":"sad",
              "生气":"angry",
              "震惊":"surprise",
              "打招呼":"hello",
              "嘲讽":"taunt",
              "无奈":"helpless",
              "害怕":"fear",
              "厌恶":"dislike",
              "告别":"bye",
              "羞愧":"shame"}

def to_memes(memes_name, persona_name=None, persona_meme_rate=0.9):
    memes_name1 = memes_dict.get(memes_name, None)
    if memes_name1 is None:
        return None
    current_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
    # 公共目录
    public_directory = os.path.join(current_dir, 'data', 'memes', 'public', memes_name1)
    # 人格目录
    persona_directory = os.path.join(current_dir, 'data', 'memes', persona_name, memes_name1) if persona_name else None

    # 收集公共目录中的图片文件
    public_image_files = []
    if os.path.exists(public_directory):
        public_image_files = [os.path.join(public_directory, f) for f in os.listdir(public_directory) if f.endswith(('.jpg', '.jpeg', '.png', '.gif'))]
    
    # 收集人格目录中的图片文件
    persona_image_files = []
    if persona_directory and os.path.exists(persona_directory):
        persona_image_files = [os.path.join(persona_directory, f) for f in os.listdir(persona_directory) if f.endswith(('.jpg', '.jpeg', '.png', '.gif'))]

    # 根据概率选择表情包
    if persona_image_files and random.random() < persona_meme_rate:
        # 选择人格表情包
        return random.choice(persona_image_files)
    elif public_image_files:
        # 选择公共表情包
        return random.choice(public_image_files)
    elif persona_image_files:
        # 如果没有公共表情包，但有人格表情包
        return random.choice(persona_image_files)
    else:
        return None