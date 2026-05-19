from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import (
    getSampleStyleSheet
)


def generate_pdf_report(
    username,
    domain,
    score,
    performance
):

    file_name = f"{username}_report.pdf"

    document = SimpleDocTemplate(file_name)

    styles = getSampleStyleSheet()

    elements = []

    title = Paragraph(
        "HireMind AI Interview Report",
        styles["Title"]
    )

    elements.append(title)

    elements.append(Spacer(1, 20))

    elements.append(
        Paragraph(
            f"<b>Username:</b> {username}",
            styles["BodyText"]
        )
    )

    elements.append(
        Paragraph(
            f"<b>Domain:</b> {domain}",
            styles["BodyText"]
        )
    )

    elements.append(
        Paragraph(
            f"<b>Average Score:</b> {score}/10",
            styles["BodyText"]
        )
    )

    elements.append(
        Paragraph(
            f"<b>Performance:</b> {performance}",
            styles["BodyText"]
        )
    )

    elements.append(Spacer(1, 20))

    if score >= 8:

        feedback = (
            "Excellent interview performance "
            "with strong technical understanding."
        )

    elif score >= 6:

        feedback = (
            "Good performance with decent "
            "technical clarity."
        )

    elif score >= 4:

        feedback = (
            "Average performance. More "
            "practice is recommended."
        )

    else:

        feedback = (
            "Needs improvement in technical "
            "concept understanding."
        )

    elements.append(
        Paragraph(
            f"<b>AI Feedback:</b> {feedback}",
            styles["BodyText"]
        )
    )

    elements.append(Spacer(1, 20))

    elements.append(
        Paragraph(
            "Keep practicing and improving your interview skills!",
            styles["BodyText"]
        )
    )

    document.build(elements)

    return file_name