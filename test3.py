def run_quiz():
    # Preprocess
    questions = prepare_questions()

    # Process (main loop)
    num_correct = 0
    for question in questions:
        num_correct += ask_question(question)

    # Postprocess
    print(f"\nYou got {num_correct} correct")