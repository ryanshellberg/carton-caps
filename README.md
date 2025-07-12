# carton-caps

## Prototype limitations
* This prototype uses a single hardcoded user ID, as authentication and authorization are out of scope for the project. 
* The Knowledge Base isn't a real vector database, it just returns the full text of both PDF documents.
* Additional user context is also mocked out. In the future information like a users school or purchase history could be included in LLM prompts to generate more helpful responses. For now we have this mocked as a fake purchase history.

## Running this project
### Prerequisites
* [Docker Desktop](https://docs.docker.com/desktop/)
* [UV](https://github.com/astral-sh/uv)
* An Open AI [API Key](https://platform.openai.com/api-keys). After creating, create a `.env.local` file at the root of your workspace and add the line `OPENAI_API_KEY={your key}`

### Running the API server
- `make setup`
- `make dev`

After Docker Compose starts up the server, you can access the API Explorer at http://0.0.0.0:8000/docs.

## Testing
**Unit tests** run automatically on push, and can be run manually through `make test`.

**Integration tests** can be run with `make integration-test`. Make sure the API server is running. 