# 👋 Welcome to Synapse

**Synapse** is an open-source platform built with Django that fosters discussions around **coding**, **technology**, and everything in between.

Whether you're a developer looking to dive into Django, or someone passionate about contributing to meaningful tech communities — you're in the right place!

---

## 🚀 Features

- 🧩 Powered by Django
- 🗃️ Uses SQLite as the default database
- 🧠 Built for discussions on coding and technology
- 🌱 Beginner-friendly and open for contributions

---

# Step-by-Step Guide to Set Up the Synapse Project Locally

Based on the command history, here's a comprehensive guide to setting up the Synapse Django project on your local machine:

## Prerequisites
- Python 3.x installed
- Git installed
- PowerShell (or terminal of your choice)

## Setup Steps

### 1. Clone the Repository
```powershell
git clone https://github.com/<username>/synapse.git
cd synapse
```

### 2. Create and Activate Virtual Environment
```powershell
python -m venv env
```

For PowerShell (you may need to set execution policy first):
```powershell
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
.\env\Scripts\Activate.ps1
```

For Command Prompt:
```cmd
.\env\Scripts\activate
```

### 3. Install Required Dependencies
```powershell
pip install django
pip install djangorestframework
pip install django-cors-headers
pip install Pillow
```

### 4. Set Up the Database
```powershell
python manage.py migrate
```

### 5. Create a Superuser (Optional)
```powershell
python manage.py createsuperuser
```

### 6. Run the Development Server
```powershell
python manage.py runserver
```

### 7. Access the Application
Open your browser and go to:
```
http://127.0.0.1:8000/
```

## Troubleshooting Common Issues

1. **Virtual Environment Activation Fails**:
   - Make sure you're in the correct directory
   - Check if the `env` folder exists
   - Try the full path: `.\synapse\env\Scripts\Activate.ps1`

2. **Missing Dependencies**:
   - If you get errors about missing modules, install them with pip:
     ```powershell
     pip install module-name
     ```

3. **Database Issues**:
   - If models have changed, run:
     ```powershell
     python manage.py makemigrations
     python manage.py migrate
     ```

4. **Static Files Not Loading**:
   - Collect static files:
     ```powershell
     python manage.py collectstatic
     ```

## Project Structure Overview

Key directories and files:
- `Synapse/` - Main project settings
- `base/` - App containing core functionality
- `templates/` - HTML templates
- `manage.py` - Django management script

## Development Workflow

1. Make changes to the code
2. Test locally with `python manage.py runserver`
3. Stage changes:
   ```powershell
   git add .
   ```
4. Commit changes:
   ```powershell
   git commit -m "Your commit message"
   ```
5. Push to GitHub:
   ```powershell
   git push origin main
   ```

## Additional Notes

- The project uses Django REST Framework for APIs
- CORS headers are configured for cross-origin requests
- Pillow is required for image handling (avatars)
- The virtual environment keeps project dependencies isolated

Remember to always activate your virtual environment before working on the project and to install any new dependencies within the activated environment.

## 🧩 Contributing
We love contributions! 💖 Whether it's a bug fix, a new feature, or even fixing a typo — every bit helps.
To Contribute:
1. Fork this repository
2. Create a new branch:
   ```bash
   git checkout -b your-feature-name
   ```
3. Make your changes

4. Commit your changes:
   ```bash
   git commit -m "Add your message here"
   ```
5. Push to your fork:
   ```bash
   git push origin your-feature-name
   ```
6. Open a Pull Request and describe your changes
   Please follow best practices, and refer to our code style and guidelines.

## 🙋‍♀️ Issues & Discussions
Have an idea or found a bug? Feel free to:
- Open an issue
- Start a discussion to share suggestions or questions
  
## 📄 License
This project is licensed under the MIT License. Feel free to use, share, and modify it with proper attribution

## 🤝 Acknowledgements
Thanks to all the open-source contributors and the Django community for making this project possible!

## 🌐 Connect
If you'd like to stay updated or ask questions, you can:
- Open an issue
- Join future community discussions
- Share your feedback

Together, let’s make Synapse an awesome space for tech talks and collaboration! 🚀
