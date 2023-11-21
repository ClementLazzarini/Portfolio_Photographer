# Photographer portfolio Website using Django


## Project Overview

This website is a portfolio for a photographer developed with the Django web framework in Python. The primary goal of this project is to create a platform where the photographer can showcase his work, and users can find information about prices. The photographer has the ability to add, delete, and modify pictures and text on the website.

## Features

- Dynamic Portfolio: Display a collection of the photographer's work with the ability to add, delete, and modify images.
- Price Information: Provide information about the photographer's pricing for different services.
- Editable Content: Allow the photographer to change text and images on the website easily.
- Admin Panel: Utilize Django's admin panel to manage portfolio content efficiently.

## Technologies Used

- Django: A high-level Python web framework.
- Python: The programming language used for backend development.
- HTML/CSS/JS: Frontend design and layout.
- SQLite: Database management for storing products, orders, and user data.

## Installation and Usage

1. Clone this repository: `git clone https://github.com/yourusername/portfolio-project.git`
2. Create a virtual environment: `python -m venv venv`
3. Activate the virtual environment: `source venv/bin/activate` (Linux/macOS) or `venv\Scripts\activate` (Windows)
4. Install dependencies: `pip install -r requirements.txt`
5. Set up the database: `python manage.py migrate`
6. Create a superuser for admin access: `python manage.py createsuperuser`
7. Start the development server: `python manage.py runserver`
8. Access the website at `http://localhost:8000/`

## Contributing

Contributions are welcome! If you find any issues or want to add new features, please submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

---

For more details, check out the [GitHub repository](https://github.com/ClementLazzarini/Portfolio_Photographer) of the project.
