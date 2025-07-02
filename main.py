from utils import classify_text

def print_result(result: dict):
    print("\n🔎 Classification Result\n" + "-"*30)
    print(f"🟢 Sentiment         : {result.get('sentiment', 'N/A')}")
    print(f"🗣️ Language          : {result.get('language', 'N/A')}")
    print(f"🎭 Style             : {result.get('style', 'N/A')}")
    print(f"📚 Covered Topics    : {', '.join(result.get('topics', [])) if result.get('topics') else 'N/A'}")
    print(f"🏛️ Political Tendency: {result.get('political_tendency', 'N/A')}")
    print("-"*30)

if __name__ == "__main__":
    while True:
        user_input = input("\nEnter text to classify (or type 'exit' to quit):\n")
        if user_input.lower() == 'exit':
            break
        result = classify_text(user_input)
        if result:
            print_result(result)
        else:
            print("❌ Classification failed. Please try again.")
