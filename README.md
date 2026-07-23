# SnapClass AI Attendance

SnapClass is a Streamlit-based AI attendance system for classrooms. It supports teacher-led subject management, student face registration, photo-based attendance, voice-based attendance, QR/share-code enrollment, and attendance history backed by Supabase.

## Features

- Student and teacher portals
- Teacher registration and password login
- Subject creation and join-code sharing
- QR code based student enrollment
- Face registration and FaceID-style student login
- Classroom photo attendance using face embeddings and an SVM classifier
- Optional voice enrollment and voice attendance using speaker embeddings
- Attendance review before saving
- Teacher attendance records dashboard
- Supabase database integration

## Tech Stack

- Python
- Streamlit
- Supabase
- dlib and face recognition models
- scikit-learn
- librosa and resemblyzer
- pandas and NumPy
- segno for QR generation

## Project Structure

```text
.
|-- app.py
|-- requirements.txt
|-- src
|   |-- components
|   |-- database
|   |-- pipelines
|   |-- screens
|   `-- ui
`-- .streamlit
    |-- config.toml
    `-- secrets.toml.example
```

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/anshu-raj29/snapclass-ai-attendance.git
cd snapclass-ai-attendance
```

### 2. Create and activate a virtual environment

```bash
python -m venv .venv
```

On Windows:

```bash
.venv\Scripts\activate
```

On macOS/Linux:

```bash
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

If dlib installation fails on your machine, install the required C++ build tools or use a Python version compatible with the available `dlib-bin` wheel.

### 4. Configure Supabase secrets

Create `.streamlit/secrets.toml` from the example file:

```toml
SUPABASE_URL = "https://your-project.supabase.co"
SUPABASE_KEY = "your-supabase-anon-or-service-key"
```

The app expects these Supabase tables:

- `teachers`
- `students`
- `subjects`
- `subject_students`
- `attendance_logs`

At minimum, the database should store teacher login details, student face and voice embeddings, subject ownership, subject enrollments, and attendance log entries.

### 5. Run the app

```bash
streamlit run app.py
```

Open the local URL printed by Streamlit, usually `http://localhost:8501`.

## Usage

1. Open the app and choose either the Student Portal or Teacher Portal.
2. Teachers can register, log in, create subjects, share join codes, take attendance from classroom photos, use voice attendance, and review records.
3. Students can register with a face photo, optionally enroll a voice profile, join subjects using a code, and view attendance.
4. Attendance results are reviewed before they are saved to Supabase.

## Environment Notes

- Keep `.streamlit/secrets.toml` private.
- Do not commit virtual environments, Python cache files, local media recordings, or generated artifacts.
- Large demo videos should be uploaded to a release, cloud storage, or Git LFS instead of regular Git history.

## License

Add a license file if you plan to distribute this project publicly.
