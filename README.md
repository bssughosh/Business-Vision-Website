# Business Vision
##### This is an e-commerce website for sellers who wish to sell goods in wholesale
###### [Installation Instructios?](#installation)
This is a website built using Django, HTML, CSS and Javascript. The repository contains 5 django applications, namely,

1. _accounts_
1. _carts_
1. _customer_
1. _search_
1. _seller_

------------------
### Accounts
It has the following functionalities - 

1. Login
1. Customer Registration
1. Seller Registration
1. Password Reset incase user forgets password

_Note: The seller is only registered if the GST number matches with the details of company entered_

------------------
### Carts
It has the following functionalitites - 

1. Display contents of cart
1. Remove items in cart

------------------
### Customer
It has the following functionalitites - 

1. Display all products
1. Show details of a product
1. Show customer's profile
1. Rate any seller

_Note: The details of the product are shown by default of the seller whose selling price is the least. However, the user may select a different seller to view the details given by other seller._

------------------
### Search
It has the following functionalities - 

1. Search for a product

------------------
### Seller
It has the following functionalities - 

1. Add a product
1. Update / Delete a product
1. Show seller's profile
1. View all your products
1. Browse all products
1. Show details of a product

_Note: The details of the product are shown by default of the seller whose selling price is the least. However, the user may select a different seller to view the details given by other seller._

------------------

## Installation
1. For installing using conda : 
  > conda env create -f virtual_platform.yml
1. For installation using pip :
  > pip install -r requirements.txt
