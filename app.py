from fastapi import FastAPI, File, UploadFile, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
import random
import os

# ============================================
# CONFIGURACIÓN
# ============================================

app = FastAPI(title="Duck Detector API", version="1.0.0")

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Archivos estáticos
app.mount("/static", StaticFiles(directory="static"), name="static")

# Especies simuladas
DUCK_SPECIES = [
    "Ánade Real (Mallard)",
    "Porrón Europeo (Tufted Duck)",
    "Cerceta Común (Common Teal)",
    "Pato Joyuyo (Whistling Duck)",
    "Pato Colorado (Red Shoveler)"
]

# ============================================
# RUTAS
# ============================================

@app.get("/", response_class=HTMLResponse)
async def index():
    """Página principal - HTML directo sin templates"""
    html_content = """
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=yes">
        <title>Duck Detector - Identifica especies de patos</title>
        <link rel="stylesheet" href="/static/css/style.css">
        <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
    </head>
    <body>
        <div class="container">
            <header class="header">
                <div class="logo">
                    <span class="logo-icon">🦆</span>
                    <h1>Duck Detector</h1>
                </div>
                <p class="tagline">Sube una foto de un pato y descubre qué especie es</p>
            </header>

            <main class="main">
                <div class="upload-area" id="uploadArea">
                    <div class="upload-icon">📸</div>
                    <p class="upload-text">Haz clic o arrastra una imagen</p>
                    <p class="upload-hint">JPG, PNG o WEBP · Máx. 16MB</p>
                    <input type="file" id="imageInput" accept="image/jpeg,image/png,image/webp" hidden>
                    <button class="btn btn-primary" id="uploadBtn">Seleccionar imagen</button>
                </div>

                <div class="preview-area" id="previewArea" style="display: none;">
                    <div class="image-preview">
                        <img id="previewImage" alt="Vista previa">
                        <button class="btn-clear" id="clearBtn" title="Cambiar imagen">✕</button>
                    </div>
                    <button class="btn btn-success" id="analyzeBtn">🔍 Analizar pato</button>
                </div>

                <div class="loading" id="loading" style="display: none;">
                    <div class="spinner"></div>
                    <p>Analizando imagen...</p>
                </div>

                <div class="results" id="results" style="display: none;">
                    <div class="result-card">
                        <div class="result-icon" id="resultIcon">🦆</div>
                        <h3>Resultado</h3>
                        <p class="result-species" id="resultSpecies">-</p>
                        <div class="confidence-bar">
                            <div class="confidence-fill" id="confidenceFill" style="width: 0%"></div>
                        </div>
                        <p class="confidence-text" id="confidenceText">Confianza: 0%</p>
                        <p class="result-message" id="resultMessage"></p>
                        <button class="btn btn-secondary" id="newImageBtn">Nueva imagen</button>
                    </div>
                </div>

                <div class="error" id="error" style="display: none;">
                    <div class="error-icon">⚠️</div>
                    <p class="error-message" id="errorMessage"></p>
                    <button class="btn btn-secondary" id="errorRetryBtn">Intentar de nuevo</button>
                </div>
            </main>

            <footer class="footer">
                <p>Duck Detector v1.0 | Proyecto Programación III</p>
            </footer>
        </div>

        <script src="/static/js/main.js"></script>
    </body>
    </html>
    """
    return HTMLResponse(content=html_content)

@app.get("/health")
async def health():
    """Verificar que la API funciona"""
    return {"status": "ok", "message": "Duck Detector API ready"}

@app.post("/predict")
async def predict(image: UploadFile = File(...)):
    """Endpoint que simula la predicción"""
    
    if not image:
        raise HTTPException(status_code=400, detail="No image provided")
    
    if image.filename == "":
        raise HTTPException(status_code=400, detail="No image selected")
    
    allowed = ["jpg", "jpeg", "png", "webp"]
    ext = image.filename.split('.')[-1].lower()
    if ext not in allowed:
        raise HTTPException(
            status_code=400,
            detail=f"Invalid format. Use: {', '.join(allowed)}"
        )
    
    await image.read()
    
    especie = random.choice(DUCK_SPECIES)
    confianza = round(random.uniform(0.65, 0.98), 2)
    confianza_baja = confianza < 0.70
    
    return {
        "success": True,
        "especie": especie,
        "confianza": confianza,
        "confianza_porcentaje": int(confianza * 100),
        "confianza_baja": confianza_baja,
        "mensaje": f"🦆 Identificado: {especie}" if not confianza_baja else "⚠️ Especie no clara, intenta otra imagen"
    }

# ============================================
# EJECUCIÓN
# ============================================

if __name__ == "__main__":
    import uvicorn
    print("🦆 Duck Detector corriendo en: http://localhost:8000")
    print("📚 Documentación API: http://localhost:8000/docs")
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)