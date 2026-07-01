from agent.portfolio_agent import PortfolioAgent
agent = PortfolioAgent()
# questions = [

#     # 1
#     "Tell me about yourself.",

#     # 2
#     "Where did you graduate from?",

#     # 3
#     "What is your education?",

#     # 4
#     "What programming languages do you know?",

#     # 5
#     "What frameworks do you use?",

#     # 6
#     "What AI technologies do you know?",

#     # 7
#     "What projects do you have?",

#     # 8
#     "What certifications do you have?",

#     # 9
#     "What achievements do you have?",

#     # 10
#     "Explain the ML Drift Monitor project."

# ]

# for i, question in enumerate(questions, start=1):

#     print("=" * 80)
#     print(f"QUESTION {i}")
#     print(question)
#     print("=" * 80)

#     response = agent.chat(question)

#     print(response)
#     print("\n\n")



questions = [

    # 11
    "Tell me about yourself and your skills.",

    # 12
    "Tell me about your education and projects.",

    # 13
    "What technologies were used in ML Drift Monitor?",

    # 14
    "Explain Memlore AI.",

    # 15
    "Explain CinemaSeek.",

    # 16
    "Which databases do you know?",

    # 17
    "How can I contact you?",

    # 18
    "Show all your GitHub repositories.",

    # 19
    "Which project uses FastAPI?",

    # 20
    "What is your strongest project?"

]

for i, question in enumerate(questions, start=11):

    print("=" * 80)
    print(f"QUESTION {i}")
    print(question)
    print("=" * 80)

    response = agent.chat(question)

    print(response)
    print("\n\n")