from server.model import encode_questions, fetch_question

encode_questions()
res = fetch_question('Props in React are inputs passed to components, allowing data flow from parent to child for dynamic rendering and reusability.')
print(res)