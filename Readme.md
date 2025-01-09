# **Data Tracking with DVC in GitHub Codespaces**

Assignment 4 on how to track  data using **DVC** and push these files to a remote storage (Virtual Machine ).

 Participants will learn to version datasets, ensuring reproducibility in a collaborative setting.

---

## Steps to complete the task

---



###  **1.Log in to your VM**

 Log in to your VM with the credentials shared with you. Create a new directory inside it. This will act like a remote
 storage to push the data being version controlled by DVC.

### **2.Create a python virtual environment, and activate it**

 - Run below commandtocreate a virtual environment

                           python-m venv venv

 (Format is : python-m venv <name>)

 - Run below commandtoactivate the virtual environment
 
                             source venv/bin/activate

### **3. Initialize DVC**
 
 -Run the below command to install dvc
 
 pip install dvc==3.55.2 dvc-ssh==4.1.1 asyncssh==2.18.0

### **4. Add Remote Storage**
- Configure Remote Storage (Directory present on VM)


### **5. Track Data_Main**
- Add your main data (the starting dataset) to DVC.
- Commit the changes to Git and DVC.
- Push the data to your remote VM storage and tag it as V1.

### **6.Add Monthly Data (month1, month2) Progressively**
- update the main data by running the Data_Aggregator.py file
- Note: by default Data_Aggregator.py will add Month2 data to main data, to add Month3 data, change the path of dataset2 in in the Data_Aggregator.py file.
- After running the file to add the monthly data (e.g., month1 and month2), track and push these changes using DVC.
_ tag them as v2 and v3 respecctively.

### 6. Upload Screenshots
- Take screenshots of each command and its output to show how the data is tracked, added, and pushed to remote storage.
- create a folder "Screenshots" and upload the screenshots in it.

## Notes
- link for the dataset used in this assignment : https://archive.ics.uci.edu/dataset/222/bank+marketing
- Use dvc status to check the tracking status of your files.
