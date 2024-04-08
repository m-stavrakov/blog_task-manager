This is a personal diary/ task manager website application. Here the user will have the chance to register using their first, last name and email and a specific password unique to them. When the user logs in they can go and create their personal diary entry. The user can also modify the text by using bold, italic and underline styling and also change the font size of the text. These entries will be stored in the blog page of the website and the user will be able to view, edit, delete the entry or create a new one. On the calendar page the user will see a calendar on the right side of the page and they can select a date and create a task for that date. they can change the time according to their plans. Again the user will be able to edit and delete their tasks. All the data such as user information, diary entries and tasks are stored safely in a database. 

#How to deploy/access
1. Upload the project folder to your own github.
2. Clone this git repository https://github.com/m-stavrakov/blog_task-manager
3. Access by this IP address: https://blog-task-manager.onrender.com
Create an account in render.com.
Clone the project from my github link.
Link your github account to your render account so you can access all your projects.
Once logged select > "New" > "Web Service"
Clone a repository from your github
Create a name for the deploy, select a region and install requirement file.
After that create the database select > "New" > "PostgreSQL"
Select a name for your database, select a region and make sure the version of your postgreSQL is the same as the one on Render.
After that go back to your Web Service and go to "Environment". Create two keys, the 1st one is "RENDER" with value "True". What this does is saying if on Render use a specific database. This is previously set in the config.py file: 
if os.environ.get('RENDER'):
    connection_string = os.environ.get('DATABASE_URL', 'postgresql://martinstavrakov:TSf5xv9xpIBIfvc2bbGmS6hTv81RHgXu@dpg-co9hhmdjm4es73avgd8g-a/fs_blog_tasks:5432')
else:
    connection_string = os.environ.get('DATABASE_URL', default_connection_string)

The default string is the local postgreSQL database URL. The URL for the Render PostgreSQL can be accessed from the PostgreSQL database created on Render by copying the Internal Database URL.
The second key is "DATABASE_URL" with value the Render PostgreSQL Internal Database URL (postgresql://martinstavrakov:TSf5xv9xpIBIfvc2bbGmS6hTv81RHgXu@dpg-co9hhmdjm4es73avgd8g-a/fs_blog_tasks).
Modifications that I had to do so the database was running is instead of 'postgres://' I changed it to 'postgresql://'. The default one does not work. Also in the config file i not only changed postgresql, but also added the port number at the end.
This should be enough to deploy the application.