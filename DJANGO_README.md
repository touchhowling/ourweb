# MediaX Django Application

This is the Django version of the MediaX website, converted from React to use plain HTML templates with Tailwind CSS.

## Prerequisites

- Python 3.8 or higher
- Virtual environment (venv) - already activated

## Installation

The dependencies should already be installed if you have Django running. If not, run:

```bash
pip install -r requirements.txt
```

## Running the Development Server

1. **Apply migrations** (first time only):
   ```bash
   python manage.py migrate
   ```

2. **Run the development server**:
   ```bash
   python manage.py runserver
   ```

3. **Access the application**:
   Open your browser and navigate to: `http://127.0.0.1:8000/`

## Available Routes

- `/` - Homepage with all main sections
- `/about-us/` - About Us (placeholder)
- `/solutions/` - Solutions (placeholder)
- `/projects/` - Projects (placeholder)
- `/newsroom/` - Newsroom (placeholder)
- `/careers/` - Careers (placeholder)
- `/connect/` - Connect (placeholder)

## Project Structure

```
pixel-hub/
├── mediax_project/          # Django project settings
│   ├── settings.py          # Main configuration
│   ├── urls.py              # URL routing
│   └── wsgi.py              # WSGI configuration
├── web/                     # Main web application
│   ├── views.py             # View functions
│   └── urls.py              # App URL patterns
├── templates/               # HTML templates
│   ├── base.html            # Base template
│   ├── index.html           # Homepage
│   ├── placeholder.html     # Placeholder pages
│   ├── 404.html             # 404 error page
│   └── components/          # Reusable components
│       ├── header.html
│       └── footer.html
├── static/                  # Static files
│   ├── css/
│   │   └── custom.css       # Custom styles
│   └── js/
│       └── main.js          # JavaScript functionality
├── requirements.txt         # Python dependencies
└── manage.py                # Django management script
```

## Features

- **Responsive Design**: Works on mobile, tablet, and desktop
- **Tailwind CSS**: Via CDN for easy styling
- **Custom Fonts**: Inter, Raleway, and Roboto from Google Fonts
- **Animations**: Client logo scrolling, hover effects
- **Mobile Menu**: Functional mobile navigation
- **404 Page**: Custom error handling

## Static Files

For development, static files are served automatically. For production:

```bash
python manage.py collectstatic
```

## Creating a Superuser (Optional)

To access the Django admin panel:

```bash
python manage.py createsuperuser
```

Then visit `http://127.0.0.1:8000/admin/`

## Deployment Notes

1. Set `DEBUG = False` in `settings.py`
2. Update `ALLOWED_HOSTS` with your domain
3. Run `python manage.py collectstatic`
4. Use a production server like Gunicorn or uWSGI
5. Configure a reverse proxy (Nginx, Apache)

## Technologies Used

- **Django 5.x**: Python web framework
- **Tailwind CSS**: Utility-first CSS framework (via CDN)
- **Whitenoise**: Static file serving
- **Vanilla JavaScript**: No frameworks, just plain JS

## Notes

- The original React files remain untouched
- All UI/UX matches the original React application
- No build process required - just Python!
