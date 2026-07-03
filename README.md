# 🤖 Portfolio AI Agent

An intelligent, agent-based AI assistant built to power my personal portfolio.

The system, called **ResuME**, answers questions about my background, education, technical skills, projects, certifications, achievements, personal interests, and developer profile. Instead of relying on a single static knowledge source, it dynamically plans requests, selects the appropriate tool, retrieves relevant information, and generates natural conversational responses.

## ✨ Overview

Portfolio AI Agent is designed as a modular AI system that combines:

- AI-based query planning
- Dynamic tool selection
- GitHub API integration
- Resume extraction and parsing
- Portfolio source-code parsing
- Developer profile extraction
- Structured personal profile data
- Repository resolution
- Context-aware response generation
- In-memory caching
- Graceful handling of unsupported questions

The assistant uses **Groq-hosted LLMs** for planning, structured extraction, and conversational response generation.

## 🧠 How It Works

```text
User Question
      │
      ▼
┌──────────────────┐
│     Planner      │
│  Creates a plan  │
└────────┬─────────┘
         │
         ▼
┌──────────────────┐
│     Executor     │
│ Executes actions │
└────────┬─────────┘
         │
         ▼
┌─────────────────────────────────────┐
│               Tools                 │
├──────────┬──────────┬───────────────┤
│  Resume  │  GitHub  │    Profile    │
│   Tool   │   Tool   │     Tool      │
└──────────┴──────────┴───────────────┘
         │
         ▼
┌──────────────────┐
│    Services      │
│ Fetch + Process  │
└────────┬─────────┘
         │
         ▼
┌──────────────────┐
│     Context      │
│    Formatter     │
└────────┬─────────┘
         │
         ▼
┌──────────────────┐
│     Response     │
│    Generator     │
└────────┬─────────┘
         │
         ▼
 Natural Conversation
```

If no available tool can answer a question, the planner returns an empty execution plan and the assistant responds gracefully without making unnecessary tool or LLM calls.

## 🛠️ Available Tools

### 📄 Resume Tool

Retrieves professional information from my resume.

Supports:

- Professional summary
- Education
- Experience
- Contact information

The resume is fetched from the portfolio repository, parsed from PDF, converted into structured information, and cached for reuse.

### 🐙 GitHub Tool

Retrieves live developer and project information through the GitHub API.

Supports:

- Developer profile
- Technical skills
- Programming languages
- Frameworks and libraries
- Portfolio sections
- Repository discovery
- Specific project details
- Repository metadata
- Repository languages
- README content

### 👤 Profile Tool

Retrieves structured personal information that does not naturally belong in a resume or GitHub profile.

Supports information such as:

- Hobbies
- Interests
- Strengths
- Weaknesses
- Motivation
- Career goals
- Favorites
- Sports and games
- Work style
- Languages spoken
- ResuME identity

## 🧩 Agent Architecture

The project follows a modular architecture with clear separation of responsibilities.

```text
Portfolio AI Agent
│
├── agent/
│   ├── planner.py
│   ├── executor.py
│   ├── registry.py
│   ├── router.py
│   ├── context_formatter.py
│   ├── response_generator.py
│   └── portfolio_agent.py
│
├── api/
│   ├── routes.py
│   └── schemas.py
│
├── clients/
│   └── github_client.py
│
├── core/
│   ├── config.py
│   └── repository_resolver.py
│
├── data/
│   └── profile.json
│
├── llm/
│   ├── client.py
│   └── models.py
│
├── parsers/
│   ├── github_profile_parser.py
│   ├── github_readme_parser.py
│   ├── portfolio_parser.py
│   └── resume_parser.py
│
├── services/
│   ├── github_service.py
│   ├── portfolio_service.py
│   ├── profile_service.py
│   └── resume_service.py
│
├── tools/
│   ├── base_tool.py
│   ├── github_tool.py
│   ├── portfolio_tool.py
│   ├── profile_tool.py
│   └── resume_tool.py
│
├── utils/
│   └── json_parser.py
│
├── app.py
├── Dockerfile
├── requirements.txt
└── README.md
```

## 🔄 Request Flow

A typical request follows this pipeline:

```text
1. User sends a question
          ↓
2. Planner analyzes intent
          ↓
3. Planner creates minimal execution plan
          ↓
4. Executor runs selected tools
          ↓
5. Services retrieve relevant information
          ↓
6. Parsers convert raw content into structured data
          ↓
7. Context Formatter prepares execution context
          ↓
8. Response Generator creates a natural answer
          ↓
9. API returns the final response
```

For example:

```text
"What technologies do you use?"
          ↓
Planner
          ↓
GitHub Tool → Profile Action
          ↓
GitHub Profile Data
          ↓
Structured Context
          ↓
Natural Response
```

## ⚡ Caching Strategy

The system uses in-memory caching to avoid repeated network requests and unnecessary LLM processing.

Cached resources include:

- Parsed resume data
- Parsed GitHub profile
- Portfolio sections
- Project information
- Repository lists

Example:

```text
First Request
GitHub → Fetch README → Parse → Cache → Return

Later Requests
Cache → Return
```

This reduces:

- API calls
- LLM token usage
- Response latency
- Repeated parsing work

## 🛡️ Empty Plan Handling

The planner can intentionally return:

```json
{
  "plan": []
}
```

when none of the available tools can answer the question.

For example:

```text
Who won yesterday's IPL match?
```

Instead of incorrectly searching GitHub repositories or sending irrelevant context to the LLM, the system returns a graceful out-of-scope response.

This prevents:

- Incorrect tool routing
- Unnecessary API calls
- Oversized LLM requests
- Token waste
- Rate-limit failures

## 📦 Context Optimization

Raw external API responses can be extremely large. The system reduces unnecessary context before passing information to the response model.

For example, GitHub repository responses are reduced to relevant fields such as:

```json
{
  "name": "repository-name",
  "description": "Repository description",
  "language": "Python",
  "url": "repository-url"
}
```

This helps keep LLM requests efficient and focused.

## 🚀 Tech Stack

### Backend

- Python
- FastAPI
- Uvicorn
- Pydantic

### AI & LLM

- Groq API
- Llama 3.3 70B
- Prompt-based planning
- Structured JSON generation
- Context-aware response generation

### Data & Parsing

- PyMuPDF
- PyPDF
- Regular Expressions
- RapidFuzz
- JSON-based structured profiles

### Integrations

- GitHub REST API
- GitHub repository content
- Portfolio source code
- Resume PDF

### Deployment

- Docker
- Hugging Face Spaces

## 🌐 API

### Health Check

```http
GET /
```

### Chat

```http
POST /chat
```

Request:

```json
{
  "message": "What are your skills?"
}
```

Example response:

```json
{
  "success": true,
  "answer": "I have experience with Python, Java, C++, JavaScript, SQL, machine learning, deep learning, NLP, FastAPI, React.js, and other technologies."
}
```

## 💬 Example Questions

You can ask ResuME questions such as:

- Tell me about yourself.
- What did you study?
- What are your technical skills?
- What AI technologies do you work with?
- Explain the ML Drift Monitor project.
- Tell me about Memlore AI.
- What certifications have you completed?
- What are your coding achievements?
- What are your hobbies?
- What is your favorite AI field?
- Do you prefer working alone or in a team?
- How can I contact you?
- Who created ResuME?

## ⚙️ Local Setup

### 1. Clone the repository

```bash
git clone <your-repository-url>
cd Portfolio-AI-Agent
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

Activate it on Linux or macOS:

```bash
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file:

```env
APP_NAME=Portfolio AI Agent
APP_VERSION=1.0.0
DEBUG=True
HOST=0.0.0.0

GROQ_API_KEY=your_groq_api_key
GITHUB_TOKEN=your_github_token
GITHUB_USERNAME=your_github_username

MODEL_NAME=llama-3.3-70b-versatile
```

> Never commit `.env` or API keys to version control.

### 5. Start the API

```bash
uvicorn app:app --reload
```

The API will be available at:

```text
http://127.0.0.1:8000
```

Interactive API documentation:

```text
http://127.0.0.1:8000/docs
```

## 🐳 Docker Deployment

Build the image:

```bash
docker build -t portfolio-ai-agent .
```

Run the container:

```bash
docker run -p 7860:7860 \
  -e GROQ_API_KEY=your_groq_api_key \
  -e GITHUB_TOKEN=your_github_token \
  -e GITHUB_USERNAME=your_github_username \
  portfolio-ai-agent
```

## 🤗 Hugging Face Spaces

The project is configured for deployment as a Docker-based Hugging Face Space.

Required secrets:

```text
GROQ_API_KEY
GITHUB_TOKEN
```

Required environment variable:

```text
GITHUB_USERNAME
```

The Docker container runs FastAPI with Uvicorn on port `7860`.

## 🔐 Security

Sensitive credentials are managed through environment variables.

The following files should never be committed:

```text
.env
__pycache__/
*.pyc
```

For production deployment, API keys are stored using Hugging Face Space Secrets.

## 🗺️ Future Improvements

Potential improvements include:

- Persistent cache storage
- Multi-provider LLM fallback
- Smarter JSON fallback responses
- Improved planner routing
- Streaming responses
- Conversation memory
- Tool execution observability
- Automated cache invalidation
- Expanded portfolio integrations
- Response-level caching

## 👨‍💻 Author

**Bhargav Sri Harshith Chintakindi**

AI and Data Science graduate focused on building practical AI systems, intelligent assistants, machine learning solutions, and full-stack AI applications.

## 📄 License

This project is intended for portfolio, learning, and demonstration purposes.