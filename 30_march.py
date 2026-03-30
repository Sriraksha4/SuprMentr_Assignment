# Prompt Engineer Assignment

prompt_examples = [
    {
        "task": "Resume",
        "weak": "Write a resume.",
        "strong": "Write a professional resume for a final year Computer Science Engineering student with internship experience in data science and no backlogs."
    },
    {
        "task": "Business Idea",
        "weak": "Give me a business idea.",
        "strong": "Suggest 3 low-investment business ideas for a college student in India interested in technology and online services."
    },
    {
        "task": "Study Plan",
        "weak": "Make a study plan.",
        "strong": "Create a 7-day study plan for a final year engineering student preparing for NLP and Python lab assignments."
    },
    {
        "task": "Interview Preparation",
        "weak": "Help me for interview.",
        "strong": "Provide common HR and technical interview questions for a fresher Computer Science Engineering student applying for internships."
    }
]

print("Prompt Engineer Assignment\n")

for i, item in enumerate(prompt_examples, start=1):
    print(f"Task {i}: {item['task']}")
    print(f"Weak Prompt   : {item['weak']}")
    print(f"Strong Prompt : {item['strong']}")
    print("-" * 80)

print("\nConclusion:")
print("Strong prompts are better because they are clear, specific, and provide context.")
print("Weak prompts are vague and may produce less useful outputs.")