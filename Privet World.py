import tkinter as tk
import random

# 俄文字母分類
russian_vowels = 'аеёиоуыэюя'
russian_consonants = 'бвгджзйклмнпрстфхцчшщ' #子音
russian_alphabet = russian_vowels + russian_consonants #母音

# 造字函式
"""
🧠俄語造字原則簡述
• 	音節結構：俄語常見音節為 CV（子音+母音）、CVC、V（少見）。
• 	子音群：俄語允許複雜的子音群，但通常不超過三個連續子音。
• 	母音分布：俄語單字中母音分布均衡，避免太多子音堆疊。
• 	字首字尾：常見字首如 “пр”, “по”, “на”；字尾如 “-ий”, “-ов”, “-ка”。

"""
def generate_fake_word(length=None):
    """
    生成一個類似俄語的假字。

    邏輯說明：
    - 若未指定長度，則隨機選擇 4 到 8 之間的整數作為目標字長。
    - 重複生成音節，直到組合後的字長達到或超過指定長度。
    - 每個音節由一個子音 + 一個母音組成，有 50% 機率在尾端再加一個子音。
    - 所有音節合併後，截斷至指定長度並將首字母大寫。
    - 回傳這個假字。
    """
    length = length or random.randint(4, 8)
    syllables = []
    while len(''.join(syllables)) < length:
        syllable = random.choice(russian_consonants)
        syllable += random.choice(russian_vowels)
        if random.random() < 0.5:
            syllable += random.choice(russian_consonants)
        syllables.append(syllable)
    word = ''.join(syllables)[:length]
    return word.capitalize()

# 造句函式
"""
主語（主格） → 動詞（人稱變化） → 補語（受格、副詞）
"""
def generate_fake_sentence():
    # 模擬俄語詞尾
    noun_suffixes = ['а', 'ий', 'о', 'я', 'ь']
    verb_suffixes = ['у', 'ет', 'ешь', 'им', 'ют']
    complement_suffixes = ['у', 'ом', 'е', 'ой', 'ю']
    adverb_suffixes = ['о', 'е', 'и']

    # 主語：名詞 + 主格尾碼
    subject = generate_fake_word(random.randint(4, 6)) + random.choice(noun_suffixes)
    # 動詞：動詞詞幹 + 人稱尾碼
    verb = generate_fake_word(random.randint(3, 5)) + random.choice(verb_suffixes)
    # 補語：2–4 個詞，每個加上受格或副詞尾碼
    complements = [
        generate_fake_word(random.randint(3, 5)) + random.choice(complement_suffixes)
        for _ in range(random.randint(1, 3))
    ]
    # 副詞：1 個詞 + 副詞尾碼
    adverb = generate_fake_word(random.randint(3, 5)) + random.choice(adverb_suffixes)

    # 隨機選擇句型結構
    pattern = random.choice([
        ['S', 'V', 'C'],        # 主語 + 動詞 + 補語
        ['S', 'V'],             # 主語 + 動詞
        ['V', 'C'],             # 動詞 + 補語
        ['S', 'V', 'C', 'Adv'], # 主語 + 動詞 + 補語 + 副詞
        ['S', 'V', 'C', 'C']    # 主語 + 動詞 + 雙補語
    ])

    sentence = []
    for part in pattern:
        if part == 'S':
            sentence.append(subject)
        elif part == 'V':
            sentence.append(verb)
        elif part == 'C':
            sentence.append(complements.pop(0) if complements else generate_fake_word(4) + random.choice(complement_suffixes))
        elif part == 'Adv':
            sentence.append(adverb)

    return ' '.join(sentence)



#  這邊無瓜  只是UI
def create_ui():
    def on_generate_one():
        sentence = generate_fake_sentence()
        result_label.config(text="生成句子：\n" + sentence)

    def on_generate_five():
        sentences = [generate_fake_sentence() for _ in range(5)]
        result_label.config(text="生成句子：\n" + "\n".join(sentences))

    window = tk.Tk()
    window.title("俄語假句子生成器")
    window.geometry("400x300")

    title_label = tk.Label(window, text="點擊按鈕生成俄語風格假句子", font=("Arial", 14))
    title_label.pack(pady=10)

    button_frame = tk.Frame(window)
    button_frame.pack(pady=5)

    generate_one_button = tk.Button(button_frame, text="生成 1 句", command=on_generate_one, font=("Arial", 12))
    generate_one_button.pack(side="left", padx=10)

    generate_five_button = tk.Button(button_frame, text="生成 5 句", command=on_generate_five, font=("Arial", 12))
    generate_five_button.pack(side="left", padx=10)

    result_label = tk.Label(window, text="", font=("Arial", 12), wraplength=380, justify="left")
    result_label.pack(pady=10)

    window.mainloop()


# 執行介面
if __name__ == "__main__":
    create_ui()

