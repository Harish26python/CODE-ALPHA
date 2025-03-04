
# Function to match user input with FAQs
                                    def get_response(user_input):
                                    user_tokens = preprocess_text(user_input)
                                            for question, answer in faq_data.items():
                                                question_tokens = preprocess_text(question)
                                                        common_words = set(user_tokens) & set(question_tokens)
                                                        if len(common_words) > 1:
# Matching threshold
                                                                    return answer
                                                                            return "I'm not sure about that. Can you rephrase your question?"

# Main chatbot loop
                                                                                    def chatbot():
                                                                                    print("Chatbot: Hello! Ask me an FAQ or type 'exit' to quit.")
                                                                        while True:
                                                                                    user_input = input("You: ")
                                                                                if user_input.lower() == "exit":
                                                                                                    print("Chatbot: Goodbye!")
                                                                                                    break
                                                                                                    response = get_response(user_input)
                                                                                                            print(f"Chatbot: {response}")

