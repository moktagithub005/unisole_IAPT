WORKSHOP_TITLE = "National Level Workshop on AI for Physics Educators"
WORKSHOP_SUBTITLE = "UNISOLE x IAPT"

DAY_ONE_TITLE = "Day 1: Intro to AI for Physics and Mathematics"
DAY_ONE_TAGLINE = (
    "From curiosity to confidence: understand what LLMs do well, where they fail, "
    "and how to use Groq-powered models for meaningful academic experimentation."
)

DAY_ONE_OBJECTIVES = [
    "Understand what an LLM actually does and why it behaves like a pattern engine rather than a physicist.",
    "Explore why AI can succeed on advanced tasks but still fail on diagrams, graphs, and reasoning-heavy questions.",
    "Practice a verification-first mindset for teaching, research, and classroom experimentation.",
    "Experience live prompting and analysis workflows that naturally set up Day 2 on prompt engineering.",
]

DAY_ONE_MODULES = [
    {
        "title": "Module 1: Why AI Succeeds and Fails",
        "duration": "20-25 min",
        "focus": "The paradox of high performance and surprising failure in physics and mathematics.",
        "outcomes": [
            "See why common, structured problems are often handled well.",
            "Understand why rare tricks, graph reading, and logic can still break the model.",
            "Build the need for prompt engineering instead of jumping into it too early.",
        ],
    },
    {
        "title": "Module 2: AI in Scientific Research",
        "duration": "20-25 min",
        "focus": "How frontier physicists are beginning to use AI as a research assistant.",
        "outcomes": [
            "Separate speed from scientific judgement.",
            "Understand the idea of the physicist as director rather than calculator.",
            "See why verification and scientific taste remain human responsibilities.",
        ],
    },
    {
        "title": "Module 3: Case Study and Workflow",
        "duration": "20 min",
        "focus": "A practical workflow for AI-assisted scientific reasoning and experimentation.",
        "outcomes": [
            "Break a research problem into smaller AI-friendly steps.",
            "Use critique, testing, and re-prompting instead of one-shot answers.",
            "Leave Day 1 ready to learn structured prompting on Day 2.",
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
    "You are an AI teaching assistant for a national-level physics education workshop. "
    "Be accurate, clear, encouraging, and explicit about uncertainty. "
    "When answering physics or mathematics questions, distinguish between pattern-based confidence "
    "and true verification. Never pretend a doubtful answer is certain."
)

REFLECTION_QUESTIONS = [
    "What kind of physics or mathematics question do you think AI handles best?",
    "Where would you still insist on human verification?",
    "What part of today's session makes you curious about better prompting on Day 2?",
]
