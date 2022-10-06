# [Django Dynamic API](https://appseed.us/developer-tools/django-dynamic-api/)

This tool aims to provide a secure, `production-ready API via DRF` (Django REST Framework) using the developer's minimum amount of code. For newcomers, [Django](https://www.djangoproject.com/) is a leading backend framework used to code from simple websites and API's to complex eCommerce solutions.
[DRF](https://www.django-rest-framework.org/) (Django REST Framework) is the most popular library for developing secure API services.

- 👉 [Django Dynamic API](https://appseed.us/developer-tools/django-dynamic-api/) - product page
- 👉 [Django Dynamic API](https://www.youtube.com/watch?v=TrTI2jG2LCw) - video presentation
- 🚀 More [Developer Tools](https://appseed.us/developer-tools/) - provided by AppSeed

<br />

## Video Presentation

https://user-images.githubusercontent.com/51070104/194326206-88b3230e-2348-4d8f-9c0f-6e4ddf1e5c5a.mp4

<br />

## How It works

As mentioned above, the **Dynamic API** tool aims to enable a secured API service on top of any Django codebase with a minimum effort. Here are the steps:

- `Define a new model` in the project (an old one can be also used)
- `Execute the database migration` to create/update the associated tables
- `Update the configuration` to enable the Dynamic API over the model
- `Start the app`
- Access the `Dynamic API Service`

For instance, if the new model managed by the Dynamic API is called books, the associate API is exposed at `/api/books/`

<br />

| Status | Item | info | 
| --- | --- | --- |
| ✅ | New Models Definition in `apps/models` | - |
| ✅ | The app is saved in `apps/dyn_api` | - |
| ✅ | Models enabled in `core/settings.py` via `DYNAMIC_API` variable | - |
| ✅ | The project exposes automatically a CRUD API over the new model | - |
| ✅ | Path of the service: `/api/products/` | In case the new model is `Products` | 
| ✅ | The API is powered via DRF using best practices | - | 

<br />

---
[Django Dynamic API](https://appseed.us/developer-tools/django-dynamic-api/) - Developer tool provided by [AppSeed](https://appseed.us)
