from classifier_chain import chain
import time

def classify_text(text: str) -> dict:
    for attempt in range(3):
        try:
            return chain.invoke({"text": text})
        except Exception as e:
            print(f"Attempt {attempt+1}/3 - Error:", e)
            time.sleep(2)
    return {}
