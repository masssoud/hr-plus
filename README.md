<h1>HR Plus</h1>
HR Plus is a web application for HR purposes

<h2>Env Files</h2>
<ul>
<li>
Inside the root directory copy <code>.env.example</code> file and name it <code>.env</code>. Then complete the data before running the project.
</li>
<li>
Inside panel directory copy <code>.env.example</code> file and name it <code>.env</code>. Then complete the data before running the project.
</li>
</ul>

<h2>Run the Project for Development</h2>
Run ```docker-compose -f docker-compose.yml -f docker-compose.dev.yml up```
<br><br>
The panel is accessible through http://localhost:8080 and the apis are accessible through http://localhost:8888

<h2>Run the Project for Production</h2>
Run ```docker-compose -f docker-compose.yml -f docker-compose.prod.yml up```
<br><br>
The panel is accessible through http://localhost:8888/panel/ and the apis are accessible through http://localhost:8888
<br><br>
> Be careful as the production docker file may not be optimized for production!