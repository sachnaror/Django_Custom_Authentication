# Django Custom Authentication | Registration, Login, Logout, ResetPassword, UserProfile And AdminProfile

This repository contains a Django project for a registration form. The project is set up with a SQLite database and includes a number of Django's built-in apps for functionality such as authentication and admin interface.

## Project Structure

The project is structured as follows:

- `registrationForm`: This is the main Django project directory. It contains the settings for the project, including database configuration, installed apps, middleware, and other settings.

- `enroll`: This is a Django app within the project. It is currently empty, but this is where you would add models, views, templates, and other code related to the registration form.

## Setup

To set up the project, you will need to have Python and Django installed. You can then clone the repository and install the required packages.

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/registrationForm.git
   ```
2. Navigate to the project directory:
   ```
   cd registrationForm
   ```
3. Apply database migrations:
    ```
    python manage.py makemigrations
    python manage.py migrate
    ```
4. Run the server:
   ```
   python manage.py runserver
   ```

## Configuration

The project is configured with a SQLite database, which is suitable for development but not for production. For a production environment, you would need to configure a different database in the `DATABASES` setting in `settings.py`.

The `SECRET_KEY` setting is currently set to a placeholder value. For a production environment, you should replace this with a secret key that is kept secure.

The `DEBUG` setting is currently set to `True`. This should be set to `False` in a production environment.


## Contributing

Contributions are welcome! Please fork the repository and create a pull request with your changes.



<img width="289" alt="image" src="https://github.com/sachnaror/Django_Custom_Authentication/assets/9551754/54825d14-90ef-416b-a587-d8376cffbab7">


<img width="498" alt="image" src="https://github.com/sachnaror/Django_Custom_Authentication/assets/9551754/96ce7ff4-8564-4845-af0c-ebee9534a6e9">


<img width="308" alt="image" src="https://github.com/sachnaror/Django_Custom_Authentication/assets/9551754/aa0ce0ee-0244-4369-b115-d62af887e337">


