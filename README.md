# GlitchGuard: Automated Test Case Generation for Python and C++

_Automate test case generation for Python and C++ with AI-powered insights!_

---

## 📌 Overview
GlitchGuard is a **CLI-based tool** that generates **comprehensive test cases** for Python and C++ files using **Google's Gemini API** (or OpenAI’s ChatGPT API). It creates test files and executes them using **Pytest for Python** and **Catch2 for C++**, ensuring code correctness and reliability.

## 💡 Features
✅ Generates unit tests automatically using AI  
✅ Supports Python (**pytest**) and C++ (**Catch2**)  
✅ Runs tests instantly after generation  
✅ Lightweight and easy to integrate into workflows  
✅ CLI-based interface for smooth execution  

---

## 📦 Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-username/glitchguard.git
cd glitchguard
```

### 2️⃣ Install Dependencies
Ensure you have **Python 3+** and `pip` installed.

```bash
pip install -r requirements.txt
```

For **C++ testing**, install Catch2:

```bash
sudo apt install catch2  # Ubuntu
brew install catch2      # macOS
```

### 3️⃣ Make `glitchguard` Executable
```bash
chmod +x glitchguard
```

### 4️⃣ Add to PATH (Optional)
To run it from any directory, add it to your `$PATH`:

```bash
export PATH=$(pwd):$PATH
```
To make this permanent, add it to your `.bashrc` or `.zshrc`:
```bash
echo 'export PATH=$(pwd):$PATH' >> ~/.bashrc
source ~/.bashrc  # Reload configuration
```

---

## 🚀 Usage

### 1️⃣ Generate & Run Tests for a Python File
```bash
glitchguard myscript.py
```
- This will generate a test file (`test_run.py`) with AI-generated **pytest** cases.
- The test file will be executed automatically.

### 2️⃣ Generate & Run Tests for a C++ File
```bash
glitchguard mycode.cpp
```
- This will generate a test file (`test_run.cpp`) with **Catch2** test cases.
- It will then compile and run the tests.

### 3️⃣ Running Tests Manually
For **Python**:
```bash
pytest test_run.py
```
For **C++**:
```bash
g++ -o test_run test_run.cpp -lcatch2 && ./test_run
```

---

## 🛠️ Configuration
To use the **Gemini API**, ensure you have a valid API key. Replace the variable within the glitchguard file with your api key:

```bash
api_key="API_KEY"
```

---

## 👥 Contributing
We welcome contributions! To contribute:

1. **Fork the repository**  
2. **Create a feature branch** (`git checkout -b feature-new`)
3. **Commit your changes** (`git commit -m "Added new feature"`)
4. **Push to GitHub** (`git push origin feature-new`)
5. **Create a Pull Request**

---

## 📄 License
This project is licensed under the **Apache 2.0 License**. See [LICENSE](LICENSE) for details.

---

## 📞 Support & Contact
📧 Email: `kushb2@illinois.edu`  
---
