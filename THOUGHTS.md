# THOUGHTS.md

## Technical Decisions and Observations

### 1. Project Structure
- The project was organized modularly to separate responsibilities:
  - `models/` → table definitions using SQLAlchemy.
  - `schemas/` → data validation and serialization using Pydantic.
  - `repositories/` → data access layer (CRUD operations).
  - `routers/` → FastAPI endpoints organized by domain (`user`, `transaction`).
  - `error/` → custom exception definitions and handlers.
  - `middlewares/` → centralized exception handling middleware.
- This approach follows the **Separation of Concerns** principle, making maintenance and scalability easier.

---

### 2. Exception Middleware
- `ExceptionMiddleware` was created to catch custom exceptions (`GenericError`) and return consistent messages.
- Pydantic validation handlers were configured to return structured errors with fields and messages, improving the API consumer experience.
- This approach allows adding new exception types in the future without changing the endpoints.

---

### 3. Testing Strategy
- Pure tests using mockito to mock repository methods.
- No database or external API calls are performed.
- Validates internal logic and object handling.

---

### 4. Architecture Principles
- Separation of concerns: routers, repositories, schemas, and connectors are clearly separated.
- Follows SOLID principles:
- Repositories isolate data access.
- Routers handle API logic only.
- Middleware centralizes error handling.
- Extensible design allows adding new transaction types, endpoints, or external providers with minimal impact.