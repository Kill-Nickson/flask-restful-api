# flask-restful-api

#### Project's modules:
 * **users_generator** - a module, which create a certain amount of random users, using a randomuser.me API, then creates a postgres database and fills the database with the users.
 * **app** - a module, which specifies a basic Flask RESTful API interface and handles requests (get all users, get a specified user by id, delete a certain user by id).
 * **Dockerfile and docker-compose.yml** - files, containing instructions for running setting and running 2 containers.The first, contains the postgres database, while the second one is for running the app.
