GITHUB_PROFILE_PROMPT = """
Extract developer information from a GitHub Profile README.

Ignore decorative content (badges, images, GIFs, emojis, visitor counters).

Return ONLY this JSON:

{
  "summary": "",
  "skills": [],
  "programming_languages": [],
  "frameworks": [],
  "libraries": [],
  "databases": [],
  "cloud": [],
  "devops": [],
  "tools": [],
  "ai_ml": [],
  "currently_learning": [],
  "interests": [],
  "socials": {
    "github": "",
    "linkedin": "",
    "portfolio": "",
    "twitter": "",
    "email": ""
  }
}

Extract only explicit information.
Do not invent values.
Remove duplicates.
Use empty lists or strings when unavailable.
"""