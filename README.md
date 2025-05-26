О, вот это уровень!
Лови фирменный README.md для **AKUMA Credential Extractor** в том же духе.
В стиле “неоновых теней пентеста” и с чётким описанием для github.

---

````markdown
AKUMA CREDENTIAL EXTRACTOR - 悪魔のクレデンシャル解剖刀

"In the binary twilight of breached domains, AKUMA parses your trophies… and feeds on secrets."

🚀 概要 (Overview)

AKUMA Credential Extractor — это не просто скрипт, а цифровой дезинтегратор для дампов Cobalt Strike.  
Он бережно разрывает экспорт credentials, отделяя кровь (пароли), кости (хэши) и души (логины) ваших целей.

Для red team, пентестеров и тёмных рыцарей оффера: ни одного лишнего байта — только трофеи.

# 起動コマンド (Activation Sequence)

```bash
python3 credentials.py
````

🔥 特徴 (Features)

* **Surgical Splitter**: Отделяет пользователей, пароли и NTLM/LM-хэши с хирургической точностью.
* **Demon Logic**: Пароли и хэши различаются по уникальным биометрическим признакам (анализ по hex, длине и структуре).
* **Clean Drop**: Гарантированное отсутствие дублей — только уникальные данные.
* **Ultra-Fast**: Переварит даже огромный экспорт за считаные секунды.

🗂️ 出力ファイル (Output Files)

* **users.txt** — все уникальные логины из дампа.
* **pass.txt** — только реальные пароли (открытый текст).
* **hash.txt** — только хэши (NTLM, LM, LM\:NTLM).

システム要件 (System Requirements)

* Python 3.x
* Руководство демона (руки, прямые или кривые — значения не имеет)

# 地獄の依存関係 (Dependencies from Hell)

Нет внешних зависимостей. Всё, что нужно — уже внутри Python.

🗡️ 使用方法 (Usage)

## 1. Подготовь файл из Cobalt Strike

Экспортируй credentials в TSV:
**Cobalt Strike → Credentials → Export → TSV (.tsv)**

Переименуй файл в `credentials_hash.tsv` или укажи своё имя в скрипте.

## 2. Пробуждение демона

```bash
python3 credentials.py
```

## 3. Сбор крови и костей

```bash
cat users.txt    # Логины жертв (уникальные)
cat pass.txt     # Пароли в открытом виде
cat hash.txt     # Только хэши (NTLM/LM/LM:NTLM)
```

🌌 出力例 (Sample Output)

```bash
$ cat users.txt
b_valenzuela
kot3
uros
...
$ cat pass.txt
chevelle11
Avokado1337!
tBDYpntwAGlNnasz
...
$ cat hash.txt
e19ccf75ee54e06b06a5907af13cef42
aad3b435b51404eeaad3b435b51404ee:e19ccf75ee54e06b06a5907af13cef42
...
```

⚡ Демон объясняет:
Все хэши определяются как строки из 32+ hex-символов или формата `LM:NTLM`. Всё остальное — пароли.

⚠️ 免責事項 (Disclaimer)

Этот скрипт — лишь инструмент для легального аудита безопасности.
"The demon bites both ways — use responsibly. Secrets, like demons, are best left unchained only with purpose."

```
      _  _                  _  _            
     / \/ \   _   _   _   / \/ \    _   _  
    / /\_/\ / \ / \ / \ / /\_/\ \ / \ / \ 
    \/      \_/ \_/ \_/ \/      \/ \_/ \_/ 
    悪魔は詳細を見る...
```

Github: [https://github.com/sweetpotatohack/AKUMA\_cred\_extractor](https://github.com/sweetpotatohack/AKUMA_cred_extractor)
License: BSD 3-Clause "New" or "Revised" License (血の誓約)

```
