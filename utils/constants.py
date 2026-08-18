WORKSHOP_TITLE = "National Level Workshop on AI for Physics Educators"
WORKSHOP_SUBTITLE = "UNISOLE x IAPT"

DAY_ONE_TITLE = "Day 1: Prompt Engineering for Physics"
DAY_ONE_TAGLINE = (
    "A participant companion for the live workshop: frame physics questions, test prompts with the speaker, "
    "verify answers, and leave with reusable prompting habits."
)

DAY_ONE_OBJECTIVES = [
    "Use the app alongside the lecture instead of passively watching the session.",
    "Frame physics and mathematics problems clearly before asking the model for help.",
    "Compare weak prompts with stronger prompts in real time during the workshop.",
    "Develop a trust-but-verify habit that participants can reuse after the workshop.",
]

DAY_ONE_MODULES = [
    {
        "title": "Module 1: Foundations and Failure Modes",
        "duration": "20-25 min",
        "focus": "Understand why LLMs can sound brilliant in one moment and unreliable in the next.",
        "outcomes": [
            "Notice where AI handles common structured tasks well.",
            "Spot where diagrams, logic, and uncommon reasoning can still break the answer.",
            "Recognize why better prompting matters before asking harder questions.",
        ],
    },
    {
        "title": "Module 2: Persona, Context, and Constraints",
        "duration": "20-25 min",
        "focus": "Learn how better instructions change the quality, depth, and safety of the output.",
        "outcomes": [
            "Turn vague questions into well-scoped academic prompts.",
            "Use role, context, and limits to shape more useful answers.",
            "See how prompting affects explanation quality and correctness.",
        ],
    },
    {
        "title": "Module 3: Guided Practice for Participants",
        "duration": "20 min",
        "focus": "Practice on your own examples so the tool becomes useful beyond the workshop hall.",
        "outcomes": [
            "Frame a classroom, research, or concept-explanation problem clearly.",
            "Test one prompt, improve it, and compare the difference.",
            "Leave ready for Day 2 with your own starting prompt patterns.",
        ],
    },
]

EXPERIMENT_MODES = {
    "Concept Builder": (
        "Explain a physics or mathematics topic in accessible workshop language, "
        "with one real-life analogy and one warning about common misconceptions."
    ),
    "Trust but Verify": (
        "Answer the question carefully, show the reasoning steps, then explicitly list "
        "what must be checked by a human before trusting the answer."
    ),
    "Day 2 Teaser": (
        "Compare a weak prompt with a stronger prompt and explain why prompt structure "
        "changes the quality of the model's response."
    ),
}

DEFAULT_SYSTEM_PROMPT = (
    "You are an AI learning companion for participants in a national-level physics workshop. "
    "Help them ask better questions, understand responses clearly, and verify uncertain claims. "
    "Be accurate, clear, and explicit about uncertainty. Never pretend a doubtful answer is certain."
)

REFLECTION_QUESTIONS = [
    "Which prompt change improved the answer most for you today?",
    "What kind of problem will you still verify manually or from a trusted source?",
    "What would you like to learn tomorrow to make your prompting more reliable?",
]
