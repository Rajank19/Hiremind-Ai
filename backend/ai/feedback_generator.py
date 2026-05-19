def generate_ai_feedback(score):

    if score >= 8:

        return (
            "Excellent technical explanation "
            "with strong clarity."
        )

    elif score >= 6:

        return (
            "Good answer but can include "
            "more technical depth."
        )

    elif score >= 4:

        return (
            "Average answer. Try explaining "
            "concepts with examples."
        )

    else:

        return (
            "Weak answer. Focus on core "
            "concept understanding."
        )