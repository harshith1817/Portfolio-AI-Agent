RESUME_PARSER_PROMPT = """
You are an expert resume parser.

Extract the resume into the following JSON structure.

Return ONLY valid JSON.

{
    "summary": "",
    "education": [],
    "skills": [],
    "projects": [],
    "experience": [],
    "certifications": [],
    "achievements": [],
    "contact": {}
}

Rules:

- Do not invent information.
- Preserve all project names.
- Preserve all certification names.
- Preserve all technologies.
- Preserve all education details.
- Preserve links if present.
- Return valid JSON only.
"""