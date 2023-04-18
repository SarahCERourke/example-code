# Data Ingestion Pipeline - Pre Implementation Phase

>_current as of August 22, 2021_

Sat - I have questions about sftp server designation regarding transition

Customer SFTP hosted-zone in aws-retail - **client.sftp.xsell.io**
Customer SFTP Role - s3-sftp-upload
policy - s3-customer-sftp-upload

## Collect Necessary Insights

Customer:

Business Sector:

Expected Date of Completion:

Point of Contact/Internal:

When establishing a new data ingestion pipeline consider the following questions and points of action. The questions in the first phase can be answered by the Customer's point of contact within XSell. Ask for this information ASAP to ensure Ontology and Annotation have access to the resources they need to intiate the new project.

- What region is the Customer uploading from? (this may not be necessary, but something to keep in mind)
- Request expected date of upload
- Request Customer SSH Key - rsa format
- Ask for approximate number of files to expect
- Requst metadata with file upload, it should be in csv format
- Ask about customer redaction needs (specifically in terms of number heavy audio - ex FedEx)

Upload region:

Expected date of upload:

Customer public SSH key:

Expected Number of Files:

Metadata?:

Redaction Needs:

---

## Pre-Build

- Determine region/end point of SFTP server

- Add Customer to XSell's customer-designated SFTP DNS to Route-53 as **record** pointing to the transfer server/s3 bucket (currently sftp.xsell.io record is client.sftp.xsell.io and should we change this to simply $CUSTOMERNAME.sftp.xsell.io and then add the customer's name ex: verizon.sftp.xsell.io for each customer?)
![dns server](./assets/sftp.xsell.io.png)
client.sftp.xsell.io s-06bfeeacf19b45d0a
- Try to keep all customers within retail in one SFTP upload server using a designated home-folder per SFTP user/customer for  and one DNS - same for health

_sftp.xsell.io is already in use for internal products and other things._
**change client to customer or customer name**

- Create Customer s3 Bucket - with a name that is simple and obvious - for the specific customer's sftp upload server

- tag resource according to standard tagging policy found [here](https://xsell.atlassian.net/wiki/spaces/SECOPS/pages/1918926853/AWS+Naming+and+Tagging+Policy)

Tags to use: Customer: name of customer, env:dv, purpose:sftp-upload/customer-sftp/sftp-server, created_by:first.last,

- Create Customer 'User' in [AWS Transfer Family](https://console.aws.amazon.com/transfer/home?region=us-east-1#/) (SFTP)

![SFTP Server](./assets/SFTP.png)

- When creating a new user, [we need to make standard role for this]
    1. Enter user name - name of company or some obvious reference
    2. Select Role: s3-sftp-upload
    3. For Policy: none
    4. Select s3 bucket made in previous step
    5. Select the box that says 'restricted' to ensure customer only have access to their home directory
    6. Add Customer's SSH Public Key - if you don't have it yet, enter it once you have it. They will not be able to transfer without it.
    7. Select Create
    8. Test
    9. Tell point of contact that bucket is ready for the client to upload files.

Test by uploading a test.txt to the bucket via the CLI. Once the test passes - delete test.txt and tell the internal point of contact that sftp s3 bucket is ready for the customer and provide them with the customer's username and hosted-zone to upload to.

Region/end point of SFTP server:

SFTP DNS:

s3 bucket: (name and folder)

arn:

Customer User name in SFTP Server:

Added Customer's Public Key to SFTP Server:

Test:

Notify point of contact that sftp is ready for customer:

Once the Customer has uploaded their files - move on to the next step to convert and transcribe the files for further use.

Next Step: [Convert and Transcribe Customer Audio Files](https://xsell.atlassian.net/l/c/2wK01hLZ)
