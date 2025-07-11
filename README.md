# carton-caps

## Running this project
### Prerequisites
* [Docker Desktop](https://docs.docker.com/desktop/)
* [UV](https://github.com/astral-sh/uv)
* An Open AI [API Key](https://platform.openai.com/api-keys). After creating, create a `.env.local` file at the root of your workspace and add the line `OPENAI_API_KEY={your key}`

### Run
- `make setup`
- `make dev`

After Docker Compose starts up the server, you can access the API Explorer at http://0.0.0.0:8000/docs.