# Progya
Bridging the gap between the classroom lecture and the student’s desk.
# 🎓 Progya (প্রজ্ঞা) - The Ultimate AI Classroom Ecosystem

> **"Transforming the 'Aura' of the classroom into structured digital wisdom."**

Progya (Bengali: প্রজ্ঞা - meaning "Wisdom" or "Deep Insight") is an ambitious, next-generation AI ecosystem designed to bridge the gap between physical lectures and digital learning. It isn't just a recorder; it's a bridge that ensures no word of wisdom is ever lost in the classroom.

---

## 🌟 The Vision
Our goal is to build the world’s most intuitive **AI Classroom Assistant**. 
The traditional classroom is full of valuable "Code-Switching" (Bangla + English) discussions that often vanish after the bell rings. **Progya** captures this atmosphere, transcribes the bilingual complexity, and delivers it directly to the student's fingertips.

### 🚀 Future Goal: The Progya Mobile App
We are currently building the core AI engine. The next phase of Progya is a **Mobile Integration** where:
- **Teachers** can start/stop recordings with a single tap.
- **Students** receive real-time summarized push notifications after class.
- **Searchable Knowledge Base:** Search for "that one thing the teacher said 3 weeks ago" directly from your phone.

---

## ✨ Key Features (Current & Upcoming)

- [x] **Bilingual Scribe:** Native support for "Benglish" (Mixed Bangla & English) using OpenAI Whisper.
- [x] **Interval-Based Recording:** Automated 5-minute chunking to ensure data safety and easy processing.
- [x] **Context-Aware Transcription:** Uses initial prompting to keep technical terms (like 'Python', 'Array', 'Database') in their original English script.
- [ ] **LLM Summarizer (In Progress):** Turning 60-minute lectures into 5-point summaries using Gemini/GPT models.
- [ ] **Auto-Mail System:** Instant delivery of lecture notes to registered student emails.
- [ ] **Mobile Integration:** A cross-platform app for seamless classroom management.

---

## 🛠️ Technical Stack

- **Core Engine:** Python 3.14.2
- **AI Model:** OpenAI Whisper (optimized for Intel UHD Graphics)
- **Document Generation:** Python-Docx
- **Audio Processing:** Pydub & Audioop-LTS
- **Environment:** Arch Linux

---

## 📂 Project Structure

```text
Progya/
├── mp3_recordings/     # Local store for processed audio & transcripts
├── scripts/
│   ├── record.py       # The Listener: High-quality interval recording
│   └── mp3totext.py    # The Scribe: Bilingual AI Transcription engine
├── .gitignore          # Keeping the noise (large mp3s) out of GitHub
└── README.md           # The Vision
