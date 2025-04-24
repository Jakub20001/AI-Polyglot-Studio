# === Stage 1: Frontend construction === 
FROM node:18 AS frontend-build

WORKDIR /app/frontend

COPY frontend/package*.json ./
RUN npm install

COPY frontend/ ./
RUN npm run build
# === Stage 2: Backend construction ===
FROM python:3.11-slim AS backend-build

WORKDIR /app/backend

COPY backend/requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY backend/ ./

# === Stage 3: Final image (Nginx + Uvicorn) ===
FROM python:3.11-slim


WORKDIR /app

# ✅ Copy the backend
COPY --from=backend-build /app/backend /app/backend

# ✅ Copy the frontend
COPY --from=frontend-build /app/frontend/build /app/frontend/build

# ✅ Install backend dependencies
RUN pip install --no-cache-dir -r /app/backend/requirements.txt

# ✅ Set environment variable
ENV PYTHONUNBUFFERED=1

# ✅ Expose the port (for Uvicorn API + frontend)
EXPOSE 8000

# ✅ Run Backend (FastAPI + static frontend)
CMD ["uvicorn", "backend.main:app", "--host", "0.0.0.0", "--port", "8000"]

