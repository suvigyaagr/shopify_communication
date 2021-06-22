# Shopify Communication
Repo: https://github.com/suvigyaagr/shopify_communication

Steps for setup after cloning:
 - Create a new python(3.6.10) environment
 - Activate the created python-env
 - `pip install -r requirements.txt`  - This install the dependencies required
 - `python manage.py migrate` - Install the migrations
 - `python manage.py crontab add` & allow if asked for any permission - This add the ShopifyFetchProducts CRON
 - `python manage.py runserver` 
 
Endpoints built:
 - `/health` : [GET] Health check endpoint
 - `/admin` : [GET] Django Admin Site
 - `/shopify/get_products` : [GET] Fetching the list of products from Shopify (same as cron) - Built as can be used to call crons using 3rd Party (like Cronicle)
 - `/shopify/create_order` : [POST] For creating an order on Shopify (needs `variant_id` & `quantity` in body)
 - `/products` : [GET] Lists of products saved in dB. (Optional params: limit:<int>, page:<int>)