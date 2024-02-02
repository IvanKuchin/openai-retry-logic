def call_api(prompt, model="gpt-3.5.-turbo"):
    try:
        response = openai.Completion.create(
            engine=model,
            prompt=prompt,
            max_tokens=100
        )
        return response.choices[0].text.strip()
    except openai.error.RateLimitError as e:
        retry_after = int(e.headers.get("Retry-After", 60))
        print(f"Rate limited. Retrying after {retry_after} seconds.")
        time.sleep(retry_after)
        return call_api(prompt, model)