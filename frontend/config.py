BACKEND_URL = "http://127.0.0.1:8000"

# ==============================
# Authentication
# ==============================

REGISTER_URL = f"{BACKEND_URL}/register"
LOGIN_URL = f"{BACKEND_URL}/login"
ME_URL = f"{BACKEND_URL}/me"

# ==============================
# Sessions
# ==============================

CREATE_SESSION_URL = f"{BACKEND_URL}/sessions"
GET_SESSIONS_URL = f"{BACKEND_URL}/sessions"

# ==============================
# Chat History
# ==============================

SESSION_HISTORY_URL = f"{BACKEND_URL}/sessions"

# ==============================
# AI Endpoints
# ==============================

CHAT_URL = f"{BACKEND_URL}/chat"
UPLOAD_URL = f"{BACKEND_URL}/upload"
PDF_CHAT_URL = f"{BACKEND_URL}/pdf-chat"
CIRCUIT_ANALYSIS_URL = f"{BACKEND_URL}/analyze-circuit"
CIRCUIT_CHAT_URL = f"{BACKEND_URL}/circuit-chat"
CODE_REVIEW_URL = f"{BACKEND_URL}/review-code"

CLEAR_CHAT_URL = f"{BACKEND_URL}/sessions"
CLEAR_ALL_CHATS_URL = f"{BACKEND_URL}/sessions"