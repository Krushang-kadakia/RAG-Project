import subprocess

def query_mistral(prompt):
    """Uses llama.cpp to query the Mistral 7B model with optimized parameters for factual RAG."""
    command = [
        "C:\\Users\\krush\\Desktop\\Internship\\llama.cpp\\build\\bin\\Release\\llama-cli.exe",  
        "--model", "C:\\Users\\krush\\Desktop\\Internship\\llama.cpp\\mistral-7b-instruct-v0.1.Q5_K_S.gguf",
        "--prompt", prompt,
        "--n_predict", "250",
        "--temp", "0.2",
        "--top-k", "50",
        "--top-p", "0.3",
        "--repeat-penalty", "1.3",
        "--threads", "8",
        "--batch_size", "512"
    ]
    
    result = subprocess.run(command, capture_output=True, text=True)
    return result.stdout.strip()
