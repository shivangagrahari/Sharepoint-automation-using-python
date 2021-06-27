# Sharepoint-automation-using-python

1. Request a free trial and then install Connect Bridge

2. Install Python for Windows ver. 3.7+ along with pyodbc module 4.0.26+

3. Run Connect Bridge Management Studio and in it:


4.1. Using the credentials I mentioned earlier, add an account for SharePoint (Accounts – Add account).

4.2. Open the option New Query and then the Connection Browser. Look for the SharePoint Connector and expand it until you see the DefaultConnection. Right-click it and choose Get Connection string. Copy the ODBC connection string. You will pass it to the script further on.
4.3. Use the New Query option to test out a query that will obtain the data you need in SharePoint. I will present an example query here, but this is something you should change. Once you have clicked the New Query option, open the Connection Browser. Find the SharePoint connector and open it until you see the Tables option. You can see that the schema contains a "table" called Site_Pages. We can create our query as


SELECT UniqueId, ContentType, Created, Modified, ContentVersion FROM Site_Pages LIMIT 20;
