import json

memory_file = "telegram-bot/memory.json"

def load_memory():
    try:
        with open(memory_file, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def save_memory(data):
    with open(memory_file, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def generate_response(user_id, user_text):
    memory = load_memory()
    uid = str(user_id)
    if uid not in memory:
        memory[uid] = []
    memory[uid].append(user_text)
    save_memory(memory)
    return f"🤖 {uid}-д хариу: {user_text[::-1]}"
