def evaluate_answer(user_answer, expected_answer):

    user_answer = user_answer.lower()
    expected_answer = expected_answer.lower()

    important_keywords = []

    for word in expected_answer.split():

        if len(word) > 4:
            important_keywords.append(word)

    matched_keywords = 0

    for keyword in important_keywords:

        if keyword in user_answer:
            matched_keywords += 1

    total_keywords = len(important_keywords)

    if total_keywords > 0:

        similarity = matched_keywords / total_keywords

    else:

        similarity = 0

    score = int(similarity * 10)

    word_count = len(user_answer.split())

    if word_count >= 8:
        score += 2

    elif word_count >= 5:
        score += 1

    score = min(score, 10)

    if score >= 8:

        feedback = "Excellent answer with strong technical explanation."

    elif score >= 6:

        feedback = "Good answer with relevant technical points."

    elif score >= 4:

        feedback = "Average answer. Try adding more technical details."

    else:

        feedback = "Weak answer. Try explaining concepts more clearly."

    return score, feedback