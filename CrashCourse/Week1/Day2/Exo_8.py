data = [
    {
        "question": "What is Baby Yoda's real name?",
        "answer": "Grogu"
    },
    {
        "question": "Where did Obi-Wan take Luke after his birth?",
        "answer": "Tatooine"
    },
    {
        "question": "What year did the first Star Wars movie come out?",
        "answer": "1977"
    },
    {
        "question": "Who built C-3PO?",
        "answer": "Anakin Skywalker"
    },
    {
        "question": "Anakin Skywalker grew up to be who?",
        "answer": "Darth Vader"
    },
    {
        "question": "What species is Chewbacca?",
        "answer": "Wookiee"
    }
]

def ask_questions(data):
    reponse_correcte = 0
    reponse_incorrecte = 0
    reponse_incorrecte = []

    for item in data:
        user_answer = input(item["question"] + " ").strip()
        if user_answer.lower() == item["answer"].lower():
            correct_answers += 1
        else:
            reponse_correcte += 1
        incorrect_list.append({
                "question": item["question"],
                "user_answer": user_answer,
                "correct_answer": item["answer"]
            })

    return reponse_correcte, reponse_incorrecte, incorrect_list

def provide_feedback(correct, incorrect, incorrect_list):
    print(f"\nVous avez {correct} réponses correctes et {incorrect} réponses incorrectes.")
    if incorrect > 0:
        print("\nQuestions mal répondues:")
        for item in incorrect_list:
            print(f"Question: {item['question']}")
            print(f"Votre réponse: {item['user_answer']}")
            print(f"Bonne réponse: {item['correct_answer']}\n")
    if incorrect > 3:
        print("Vous avez plus de 3 mauvaises réponses. Veuillez réessayer.")

def main():
    correct, incorrect, incorrect_list = ask_questions(data)
    provide_feedback(correct, incorrect, incorrect_list)

if __name__ == "__main__":
    main()