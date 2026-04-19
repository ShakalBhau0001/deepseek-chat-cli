# 🤖 DeepSeek-Chat-CLI 💬

A Python-based **DeepSeek AI Command Line Chat Interface** that allows you to **chat with DeepSeek AI models directly from your terminal.**
This project is designed as a **learning lab** to improve:
- API & session handling logic
- CLI tool structuring
- HTTP request handling & response parsing
- AES-based cookie authentication

It is especially useful for **exploring AI models**, **CLI tool development**, and **understanding how web sessions and authentication work**.

---

## 🧱 Project Structure

```bash
deepseek-chat-cli/
│
├── main.py                 # Main CLI application
├── 
└── README.md               # Project documentation
```

---

## ✨ Features

### 🤖 Multi-Model Support
- Choose from **18 DeepSeek AI models**
- Includes DeepSeek-V1 through V3, R1, Prover, Coder, and more
- Interactive model selection table at startup

### 💬 Real-Time Chat Interface
- Send messages and receive AI responses in real time
- Tracks query count per session
- Type `exit`, `quit`, or `bye` to end the session

### 🎨 Rich Terminal UI
- Colorful and interactive interface powered by `rich`
- Animated loading spinners while AI is thinking
- Styled panels for responses

---

## 🛠 Technologies Used

| Technology | Role |
| --- | --- |
| **Python 3** | Core programming language |
| **requests** | HTTP session & API communication |
| **pycryptodome** | AES cookie decryption for session auth |
| **rich** | Beautiful terminal UI |
| **regex (re)** | HTML response parsing |

---

## 📌 Requirements

```bash
Python 3.7+
```

Install required libraries:

```bash
pip install requests pycryptodome rich
```

---

## ▶️ How to Run

### 1️⃣ Clone the repository

```bash
git clone https://github.com/ShakalBhau0001/deepseek-chat-cli.git
```

### 2️⃣ Enter the project directory

```bash
cd deepseek-chat-cli
```

### 3️⃣ Install dependencies

```bash
pip install requests pycryptodome rich
```

### 4️⃣ Run the CLI tool

```bash
python main.py
```

---

## ▶️ Usage

After running the program, you will see a model selection table:

```
╔═════╦═══════════════════════════════════╦══════════╗
║  №  ║  🤖 Model Name                   ║  Status  ║
╠═════╬═══════════════════════════════════╬══════════╣
║  1  ║  DeepSeek-V1                      ║ ✅ Ready ║
║  2  ║  DeepSeek-V2                      ║ ✅ Ready ║
║ ... ║  ...                              ║ ✅ Ready ║
╚═════╩═══════════════════════════════════╩══════════╝
```

## 💬 Chat Example

**Input:**
```
📝 You: What is Python?
```

**Output:**
```
🤖 DeepSeek-V3 Response:
Python is a high-level, interpreted programming language known for...
```

---

## ⚙️ How It Works

### 1️⃣ Session Initialization
- A `requests.Session` is created with a browser-like User-Agent
- The tool connects to the proxy server and solves an **AES-based cookie challenge** to authenticate the session

### 2️⃣ Model Selection
- User picks a model from the list
- Selected model is passed with each request to the backend

### 3️⃣ Chat Loop
- User message is sent via HTTP POST to the proxy
- Response HTML is parsed using regex to extract the AI reply
- Reply is displayed in a styled terminal panel

---

## ⚠️ Limitations

- Requires an active internet connection
- Dependent on third-party proxy server availability
- Model names may not reflect exact backend models
- Not suitable for sensitive or confidential conversations

---

## 🌟 Future Enhancements

- Conversation history saving to file
- Color-theme customization
- Direct Official DeepSeek API support
- Multi-turn context memory
- Export chat as `.txt` or `.md`

---

## ⚠️ Disclaimer

> **Please read carefully before use.**

- This is an **unofficial, community-made project** and is **NOT affiliated with DeepSeek AI** in any way.
- This tool routes requests through a **third-party proxy server** (`asmodeus.free.nf`), which is **not controlled** by the developer of this project.
- **Do NOT enter any personal, sensitive, financial, or confidential information** while using this tool.
- All conversations **may be logged** by the third-party proxy server operator. The developer takes **no responsibility** for any data shared.
- The model names listed are for selection purposes only and may not reflect exact models on the backend.
- This project is intended for **educational and personal use only**.
- For production or professional use, please use the [Official DeepSeek API](https://platform.deepseek.com/).

---

#### 🪪 Author

> **Creator: Shakal Bhau**

> **GitHub: [ShakalBhau0001](https://github.com/ShakalBhau0001)**

---
