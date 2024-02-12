
 1. Project title :- ERP


 2. Project Description :-

					ERP is comprehensive E-commerce web-based website. grocery is basically used to build an application program which help Admin and Customer to interact with each other, solve query’s, take feedbaks provide product which is healthy to make customer life healthier.
					An ERP provides users fresh and quality checked products related vegen. The project consists of list of products displayed in various models and designs. The user may browse through these products . If the user likes a products he may direcly buy that product by homepage buy button. To buy product customer must register on the site first. He can login using same id password next time. The resister is then the customer buy the product. Now he may pay through a credit card or cash on delivery. Once the user makes a successful transaction he gets a copy of the shopping receipt on his email id.  The frontend code is made in python by django framework and Postgresql as a backend 
to store product’s lists and inventory data. The online ERP project brings an healthy edible product online and makes it easy for both buyer and seller to make healthy edible product’s offer.

3. Models (Tables) :-
	
	3.1 Table Customer

    			Field					Description

   			 id 						id
  		  customer_name    		Customer name
   		  customer_address  		Customer address
   		  customer_contact  		Customer contact
    		  customer_mail  			Customer mail
    		  customer_user  			Username
    		  customer_password 		Password   

	
	3.2 Table Supplier

		      Field					Description

			id 						id    		
		supplier_name 			Supplier name
    		supplier_address 			Supplier address
    		supplier_contact 			Supplier contact
    		supplier_mail 			Supplier mail
    		supplier_comp_name 		Supplier company name
    		supplier_comp_address 	Supplier company address
    		supplier_comp_mail 		Supplier company mail  
    		supplier_comp_bank 		Supplier company bank
    		supplier_comp_acc 		Supplier company account no
	    	supplier_user 			username
	    	supplier_password 		password


	3.3 Table Product

		      Field					Description

			id 						id    
    		product_name 			Product name
    		product_price 			Product price
    		product_category 			Product category
    		product_unit 				Product unit
    		product_stock 			Product stock


	3.4 Table Stock

		      Field					Description

			id 						id    
		product_id 				Product	id   
    		product_name 			Product name
    		product_price 			Product price
    		product_category 			Product category
    		product_unit 				Product unit
    		product_stock 			Product stock
    		Stock_date 				Stock added date


	3.5 Table Order

		      Field					Description

			id 						id    
    		user_name				Username
    		customer_name 			Customer name
    		customer_address 		Customer address
    		customer_mobile 			Customer mobile
		product_id 				Product id   
    		product_name 			Product name
    		product_price 			Product price
    		product_Qty 				Product category
    		order_total 				Order unit
    		order_date 				Order date


	3.6 Table Feedback

		      Field					Description
  
			id 						id   
    		fullname 			 	Full name
    		email 					Email
    		feedback 				Feedback


4. How to install and run project :-
	4.1. Install django :-  search to google or any other search engin "download vscode" or "pycharm" then download setup file of your prefferd website or do by follwing step
     		Steps for vscode website is :- go to "https://code.visualstudio.com/download" ==> click on window 10 or 11(select your oprating system) ==> it automatically download 			setup file ==> after 100 % download double click on setup file and complete installation ==> open vscode and search extemsions ==> install Python (by Microsoft), 				Django (by Baptiste) ==> done
	4.2. Install postgresql :- search to google or any other search engin "download postgresql" then download setup file of your prefferd website or do by follwing step 
     		Steps for postgresql website is :- go to "https://www.enterprisedb.com/downloads/postgres-postgresql-downloads" ==> 	Windows x86-64	or Windows x86-32(select your 			oprating system) ==> it automatically download setup file ==> after 100 % download double click on setup file and complete installation ==> in setup you have to create 		your password so create password ==> open pgadmin by search bar ==> done

5. How to use project :-
	This project have three panel admin , customer and erp project panel the description of each panel are following :-
	5.1. erp project panel :- this panel is accessable for every person following are pages of erp project panle
		5.1.1. home page :- In this  page you wiil see product which ther users to buy by clicking buy button if you have allready logged in then it will take you to the order page 				but your not logged in you it will go to login page so you have to login first to buy product
		5.1.2. signup :- this page used for create customer login by filling some information by signup form.it have validation where username will be unique
		5.1.2. login :- this page used for user login.
		5.1.2. admin login :- this page used for admin login.
		5.1.2. feedback : In this page you can share your feedback by feedback form.
	5.2. User panel :- this panel is for your where user can see all activities which done between user and erp system.following are their pages
		5.2.1. home :- in this page customer can buy now products.
		5.2.2. profile :- In this page you can see your profile.
		5.2.3. update :- In this page you can update your profile.
		5.2.4. order :- In this page you will see your order reports and also you can get your pdf receipt.
		5.2.5. logout :- In this page you can logout from account.
		5.2.6. feedback :- In this page you can give feedback.
	5.3. User panel :- this panel is for your where user can see all activities which done between user and erp system.following are their pages
		5.3.1. product add :- In this page admin can add new products.
		5.3.2. all product :- In this page admin will see all product .this page provided search option so admin can search specific product as well as delete product opration also 					provided.
		5.3.3. stock :- After login admin will see this page first this page is use for adding stock of product and it will show you product which stock have below 5 as well as thier 				also search facility provided so admin can search easily specific product and add their stock.
		5.3.4. user profile :- In this page admin can see customer profile as well as he can save specific user data in pdf format.
		5.3.5. add supplier :- In this page admin can add supplier to erp system.
		5.3.6. supplier profile :- In this page admin can see supplier profile as well as he can delete specific supplier.
		5.3.7. order :- In this page admin can see all orders as well as he can save specific order data in pdf format.
		5.3.7. feedback :- In this page admin can see all feedback.
		5.3.8. logout :- Admin can logout account by this page.

6. Contribution :-
		This project only made by my self
		refference :- google, youtube

  

