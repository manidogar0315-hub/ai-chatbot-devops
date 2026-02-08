def get_response(user_input):
    user_input = user_input.lower()

    if "hello" in user_input:
        return "Hello! How can I help you?"
    elif "devops" in user_input:
        return "DevOps is about automation, CI/CD, and reliable deployments."
    elif "docker" in user_input:
        return "Docker packages applications into containers."
    else:
        return "Sorry, I didn't understand that."
