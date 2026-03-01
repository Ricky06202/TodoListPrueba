from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

# Modelo de datos para las tareas
class Todo(BaseModel):
    id: Optional[int] = None
    title: str
    completed: bool = False

# Base de datos en memoria (para persistir usa SQLite o similar)
todos_db: List[Todo] = [
    Todo(id=1, title="Estudiar Blazor WASM", completed=False),
    Todo(id=2, title="Configurar FastAPI con CORS", completed=True)
]
todo_id_counter = 3

# ¡IMPORTANTE! Habilitar CORS para que Blazor pueda conectarse
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # En desarrollo puedes usar "*" o la URL de tu Blazor
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/todos", response_model=List[Todo])
async def get_todos():
    return todos_db

@app.post("/api/todos", response_model=Todo)
async def create_todo(todo: Todo):
    global todo_id_counter
    todo.id = todo_id_counter
    todo_id_counter += 1
    todos_db.append(todo)
    return todo

@app.put("/api/todos/{todo_id}", response_model=Todo)
async def update_todo(todo_id: int, updated_todo: Todo):
    for index, todo in enumerate(todos_db):
        if todo.id == todo_id:
            updated_todo.id = todo_id
            todos_db[index] = updated_todo
            return updated_todo
    return None

@app.delete("/api/todos/{todo_id}")
async def delete_todo(todo_id: int):
    global todos_db
    todos_db = [t for t in todos_db if t.id != todo_id]
    return {"message": "Task deleted"}