# Sprint4
1.Prerequisites

Ensure you have a GitHub, GitLab, or Bitbucket account (Render connects directly to these platforms).
Install Git on your laptop if not already installed.
Have your project stored in a Git repository.

2. Push Your Project to Git Repository

3. Create a Render Account

Go to https://render.com.
Sign up using your GitHub, GitLab, or Bitbucket account.
4. Connect Your Repository

Go to your Render dashboard.
Click New + → Web Service.
Choose your repository from the connected Git account.

5. Configure the Service

Fill in the service name.
Select the branch you want to deploy (usually main or master).
Add necessary build commands(pip install streamlit & pip install -r requirements.txt)
Set the start command (streamlit run app.py)
6. Deploy the App

Click Create Web Service.
Render will automatically pull the latest code and deploy the service.
Once the deployment is complete, Render will provide a live URL for your app.

Information about Market vaules of certain vehicles
https://sprint4-g328.onrender.com