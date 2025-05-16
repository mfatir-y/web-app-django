# Django Blog Web Application

A feature-rich blog web application built with Django, featuring user authentication, blog post management, and user profiles.

## Features

- User Authentication (Register, Login, Logout)
- User Profiles with Profile Pictures
- Create, Read, Update, and Delete Blog Posts
- Responsive Design
- Media File Handling
- User-specific Content Management

## Blog Application Features

### Post Management
- Create new blog posts with title and content
- View posts with pagination (8 posts per page on home page)
- Update and delete your own posts
- Automatic timestamp and author tracking
- User-specific post listings
- Detailed post view with author information

### Security Features
- Authentication required for creating posts
- Users can only edit/delete their own posts
- Built-in CSRF protection
- Secure user authentication

### User Interface
- Clean and intuitive post layout
- Responsive design for all screen sizes
- User-friendly navigation
- Latest posts sidebar
- About page with dynamic content

### Post Features
- Rich text content support
- Automatic date/time stamping
- Author attribution
- Permalink system for sharing
- User profile integration

### Technical Implementation
- Class-based views for efficient code organization
- Common mixins for shared functionality
- Custom user authentication checks
- Pagination for better performance
- URL routing for clean links
- Template inheritance for consistent design

## Technologies Used

- Python 3.x
- Django Web Framework
- SQLite Database
- HTML/CSS
- Bootstrap for Styling
- JavaScript

## Project Structure

```
webApp_coreyschafer/
├── blog/                   # Blog application
├── users/                  # User management application
├── media/                  # User uploaded files
├── webApp_coreyschafer/    # Project settings
├── manage.py              # Django management script
└── requirements.txt       # Project dependencies
```

## Setup and Installation

1. Clone the repository:
```bash
git clone <repository-url>
```

2. Create a virtual environment and activate it:
```bash
python -m venv venv
source venv/Scripts/activate  # On Windows
source venv/bin/activate      # On Unix or MacOS
```

3. Install the required dependencies:
```bash
pip install -r requirements.txt
```

4. Apply database migrations:
```bash
python manage.py migrate
```

5. Create a superuser (Admin):
```bash
python manage.py createsuperuser
```

6. Run the development server:
```bash
python manage.py runserver
```

The application will be available at `http://localhost:8000`

## Usage

1. Register a new account or login with existing credentials
2. Create, edit, and delete your blog posts
3. Update your profile information and profile picture
4. View and interact with posts from other users

## Admin Interface

Access the admin interface at `http://localhost:8000/admin` to manage:
- Users
- Blog Posts
- User Profiles
- Media Files

## Contributing

1. Fork the repository
2. Create a new branch for your feature
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Based on Corey Schafer's Django tutorial series
- Django Documentation
- Bootstrap Documentation 