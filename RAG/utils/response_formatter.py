import re

def clean_response(response):
    response = response.split("[end of text]")[0].strip()
    response = re.sub(r".*=== CONTEXT END ===", "", response, flags=re.DOTALL).strip()
    response = response.replace("Context:", "").replace("[CONTEXT]:", "").strip()

    if "Answer:" in response:
        response = response.split("Answer:")[-1].strip()
    
    return response

def format_response(text):
    lines = text.strip().split("\n")
    formatted = []
    inside_table = False

    for line in lines:
        if "\t" in line:
            if not inside_table:
                formatted.append("\n📊 Table:\n")
                inside_table = True
            formatted.append(" | ".join(line.split("\t")))
        else:
            inside_table = False
            if any(kw in line.lower() for kw in ["first", "most", "introduced", "won", "record"]):
                formatted.append(f"- {line.strip()}")
            else:
                formatted.append(line.strip())

    return "\n".join(formatted)
