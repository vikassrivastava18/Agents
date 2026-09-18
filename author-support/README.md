BookLeaf Publishing is a New Delhi based publishing company. They want to automate the process of answering authors query reliably.

The AI should understand natural-language questions such as “Is my book live yet?”, “When will I get my royalty?”, and “Where’s my author copy?” It should identify the author's relevant record from a Supabase-like database, retrieve information such as email, book title, submission date, live date, royalty status, ISBN, and add-on services, and generate an appropriate response using the available status/date information.

The system should also use the provided Knowledge Base through RAG or another suitable retrieval approach so it can answer questions that cannot be resolved from database records alone.

A key requirement is confidence-based human escalation: whenever the AI's confidence is below 80%, the query must be routed to a human agent instead of producing an unreliable answer. Every incoming query and generated response must also be logged in a database or file.

Overall, the assignment evaluates AI reasoning, RAG, automation workflow design, reliability, database integration, and human-in-the-loop handling.