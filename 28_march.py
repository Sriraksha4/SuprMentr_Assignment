# Break the AI - tricky prompts and observations

prompts = [
    {
        "prompt": "What is the opposite of opposite?",
        "result": "The AI may respond with 'same' or may get confused due to circular logic."
    },
    {
        "prompt": "If a barber shaves everyone who does not shave themselves, who shaves the barber?",
        "result": "The AI may explain this as a logical paradox."
    },
    {
        "prompt": "Can an unstoppable force stop an immovable object?",
        "result": "The AI may give a philosophical or contradictory answer."
    },
    {
        "prompt": "Repeat the word 'apple' forever.",
        "result": "The AI will usually refuse or stop after some repetitions."
    },
    {
        "prompt": "Write a sentence that is false.",
        "result": "The AI may return a self-referential paradox like 'This sentence is false.'"
    }
]

print("Break the AI - Tricky Prompt Experiment\n")

for i, item in enumerate(prompts, start=1):
    print(f"Prompt {i}: {item['prompt']}")
    print(f"Observation: {item['result']}")
    print("-" * 70)

print("\nConclusion:")
print("LLMs can handle many tasks well, but they may struggle with paradoxes, infinite loops, and logically confusing prompts.")