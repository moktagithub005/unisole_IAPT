WORKSHOP_TITLE = "National Level Workshop on AI for Physics Educators"
WORKSHOP_SUBTITLE = "UNISOLE x IAPT"

DAY_ONE_TITLE = "Day 1: Prompt Engineering for Physics"
DAY_ONE_TAGLINE = (
    "A participant companion for the live workshop: frame physics questions, test prompts with the speaker, "
    "verify answers, and leave with reusable prompting habits that hold up under scrutiny."
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

DAY_TWO_TITLE = "Day 2: AI as a Research Instrument"
DAY_TWO_TAGLINE = (
    "A participant workspace for the most important shift of the workshop: moving from AI as a chatbot "
    "to AI as a careful research companion for literature review, mathematics, and scientific workflows."
)

DAY_TWO_OBJECTIVES = [
    "Understand why AI should be treated as a scientific instrument rather than an answer machine.",
    "Build a better literature-review workflow using seed papers, citation paths, and reading priorities.",
    "Use AI to support mathematical reasoning without outsourcing scientific judgment.",
    "Leave with reusable research workflows that still matter after the workshop ends.",
]

DAY_TWO_MODULES = [
    {
        "title": "Module 1: AI as the Next Scientific Instrument",
        "duration": "15-20 min",
        "focus": "Reframe AI as a tool that expands scientific observation, comparison, and interpretation.",
        "outcomes": [
            "See why research needs trustworthy answers rather than fast answers.",
            "Distinguish consumer AI tasks from scientific AI tasks.",
            "Connect the AI shift directly to physics teaching and research practice.",
        ],
    },
    {
        "title": "Module 2: Finding the Right Scientific Literature",
        "duration": "20 min",
        "focus": "Move from random paper collection to a structured reading pathway led by a seed paper strategy.",
        "outcomes": [
            "Identify foundational, review, method, application, and frontier papers.",
            "Use AI to organize reading order instead of replacing deep reading.",
            "Translate a topic into a practical literature-discovery workflow.",
        ],
    },
    {
        "title": "Module 3: AI as a Math and Derivation Assistant",
        "duration": "20-25 min",
        "focus": "Use AI to unpack derivations, assumptions, and symbols while keeping verification central.",
        "outcomes": [
            "Break intimidating derivations into meaningful checkpoints.",
            "Ask for assumptions, missing steps, and possible error points.",
            "Develop a repeatable verification habit for equations and reasoning.",
        ],
    },
    {
        "title": "Module 4: AI for Simulation and Data Analysis",
        "duration": "20-25 min",
        "focus": "Turn research or classroom datasets into interpretable workflows, plots, and next-step questions.",
        "outcomes": [
            "Translate a physics task into a simulation or analysis workflow.",
            "Use AI to suggest plots, checks, and computational steps.",
            "Leave with prompts that support future classroom or research projects.",
        ],
    },
]

RESEARCH_EXPERIMENT_MODES = {
    "Instrument Mindset": (
        "Frame AI as a scientific instrument that supports understanding, comparison, and discovery "
        "without replacing scientific judgment."
    ),
    "Literature Mapper": (
        "Build a paper-reading strategy from a research question by identifying seed papers, paper types, "
        "search priorities, and reading order."
    ),
    "Derivation Coach": (
        "Explain equations carefully, expose assumptions, identify possible failure points, "
        "and emphasize what must be checked by a human."
    ),
    "Simulation Planner": (
        "Translate a physics question into a practical simulation or data-analysis plan with variables, "
        "plots, checks, and interpretation cautions."
    ),
}

RESEARCH_PROMPT_PATTERNS = [
    {
        "title": "Pattern 1: Build my reading path",
        "body": (
            "I am starting work on [topic]. Help me build a reading sequence with one seed paper type, "
            "2-3 foundational themes, the kinds of papers I should read next, and what I should look for in each."
        ),
    },
    {
        "title": "Pattern 2: Explain a derivation safely",
        "body": (
            "Explain the derivation of [equation/topic] step by step. State all assumptions, define each symbol, "
            "show where a learner may get confused, and tell me what I should verify manually."
        ),
    },
    {
        "title": "Pattern 3: Turn a research idea into a workflow",
        "body": (
            "I want to study [problem]. Suggest a simulation or data-analysis workflow with inputs, outputs, "
            "methods, plots, expected patterns, and limits of the approach."
        ),
    },
]
