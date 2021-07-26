<!--
repo name: multipurpose-app
description: Simple e-commerce website with blog
github name:  karolchmiel94
link: https://github.com/karolchmiel94/multipurpose_app
logo path:
screenshot:
email: karolch94@gmail.com
-->

<!-- PROJECT LOGO -->
<br/>
<p align="center">
    <!-- <a href="https://github.com/karolchmiel94/multipurpose_app">
        <img src="" alt="Logo" width="80" height="80">
    </a> -->
    <h3 align="center"><a href="https://github.com/karolchmiel94/multipurpose_app">multipurpose-app</a></h3>
    <p align="center">
        Simple e-commerce website with blog
        <br />
        <br />
    </p>
</p>

<!-- TABLE OF CONTENTS -->
## Table of Contents

- [Table of Contents](#table-of-contents)
- [About The Project](#about-the-project)
- [Technologies used](#technologies-used)
- [Functionalities description](#functionalities-description)
  - [Blog](#blog)
  - [Shop](#shop)
- [TO-DO](#to-do)

<!-- ABOUT THE PROJECT -->
## About The Project

As most of my Django projects were utilizing REST API to exchange data with frontend applications, I wanted to strengthen and learn more about Django's functionalities to present data with dynamic HTML templates. Moreover, I wanted to move my focus on topics of caching, message brokers, tests, and project localization and internalization.
The result of it is a simple blog and shop.


<!-- Technologies used -->
## Technologies used

- PostgreSQL,
- Celery,
- Redis


<!-- Functionalities description -->
## Functionalities description

Short description of things this project consist of.

### Blog

Blog is as simple as it gets. Posts have their authors and tags linked to them. Users can browse posts, filter them, add comments to them and share them via e-mail.

* RSS

Users can subscribe to blog feed using feed aggregator and have latest posts fetched as XML.

* Sitemap

Blog has sitemap generated on a weekly basis to help crawlers index it's content.

* Full-text search

Posts can be searched against their titles and descriptions. Search vectors for them are weighted, with title being the primary one. Stemming provides better search results so users can spend more time reading posts, instead of looking for something to read.

### Shop

Shop is a place where users can browse products, add them to cart and finish checkout
process by placing order.

* Product catalog

Products can be added via admin panel. Users can browse them on a website, filter them by category and order them by their price.

* Cart

Products added to cart are saved in session so users don't have to be logged in to create cart with products. To being able to show user his cart overview on each page, cart is added to each request through context processor.

User can add coupon code to his cart, applying a discount to his next order.

* Orders

Once user goes through checkout, order is being placed. As test payment processor is disabled, user is just being shown that transaction went through and an email is being send to him using asynchronous task using Celery.

* Orders admin panel

Orders application provides additional functionalities consisting of:
- action exporting selected orders to CSV file,
- custom view for order detail,
- generating invoice for selected order.

* Translation

Project is translated into Polish and English language. HTML files, forms and part of model fields names have added translation to them. Text for both languages are saved in .po files and compiled to .mo ones. Users can switch between languages with navbar link.

Rosetta library has been added and configured so internalization can be done through admin panel.

As static texts on website are translated, model fields should be available in both Polish and English languages as well. Translation is being achieved with django-parler creating separate tables for each model that contains translations.

Localization formatts dates and prices numeral system.

* Product recommendations

After user places an order, products from cart are being paired up and saved in Redis. This allows to show pairs of products as 'bought together' and be shown on a product detail page or on a checkout page.

<!-- TO-DO -->
## TO-DO

Things I'm plannig to add to this project consists of:

* Populating database with random data:

Websites always look better when they're full of content. I'm planning to create custom admin action for each application model which will generate given number of random objects. For that reason, I can use Faker library.

* Tests:

As the project grows larger and larger, I feel more and more guilty that I haven't written tests for the code yet.

* Docker:

To speed up the process of writing the code, I haven't dockerize my application.
I need to configure docker.

* Styling:

Current UI version of the project was given very little time of polishing and need to be styled to not evoke feeling of frightening and disgust in user's eyes.