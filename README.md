# Cloudwiry File Storage 

  In this project we tried to build an Cloud storage system where users can store and access their files.<br/>
  We have used python as a backend for this project ( Flask Framework).
  <br/>
  <br/>
# Features<br/>
<br/>
1. User Authentication and Session Management<br/>
 We used mongoDB to store the user credentilas and from there we retrieve the user details whenever<br/>
 they try to login and verify the details if the details are valid then a session will be created to<br/>
 that particular user.<br/><br/>
2. Implementation of blob storage server<br/>
For the file storage we are using the server itself as a database.<br/>
whenever a new user registers then a directory will be created for them and they will be given access to it.<br/><br/>
3. Client Application (Web based) for file upload,download,rename and delete<br/>
When the user successfully logins then a home page is displayed with all the files that <br/>
they have on their server and options like rename,delete,share and download were provided along with this.<br/><br/>
4. File sharing<br/>
Unfortunately we didn't implement any role based file sharing.But we tried in other way.<br/>
A user can share a file to other person by using his/her username.They just need to enter <br/>
username to whom it has to be shared and then it will be sent to them<br/><br/>
5. Deploy<br/>
"Heroku Hosted Link": https://cloudwiry-filestoring.herokuapp.com/ <br/><br/>

  

  
  
