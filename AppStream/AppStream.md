
# AppStream

**xsell-health-accounts**
**xsell-retail-accounts**

## Customers

Optus (pre-implementation phase)

Anthem

FedEx

## Teams

- Ontology

- Annotation

- DataScience

---

## Users

Justin.Doyle

Jillian.Murphy

Alex.Perry

_A lot more that I need to add._

---

### Okta/AD/AppStream 2.0 & SAML 2.0 Integration Resources -

[AWS Docs](https://docs.aws.amazon.com/appstream2/latest/developerguide/external-identity-providers-further-info.html)

[Official Okta Q/A Help Center](https://support.okta.com/help/s/question/0D50Z00008GfxSX/okta-front-end-to-aws-appstram-20-configuration-instructions-please?language=en_US)

[Blog post April 2021](https://www.rapyder.com/blogs/amazon-aws-appstream-2-0-okta-saml-integration/)

[Okta: How to configure SAML 2.0 for AWS AppStream 2.0](https://saml-doc.okta.com/SAML_Docs/How-to-Configure-SAML-2.0-for-Amazon-AppStream-2-0.html)

---

Relay state endpoints for US West (Oregon)

https://appstream2.us-west-2.aws.amazon.com/saml

(FIPS)



## Active Directory

OU= ?

*Potential Groups To Create in AD**

- Annotation

- Ontology

- Data Scientist

---

### SFTP Upload-Server

ssh public key

- SSH key: requested public RSA key

s3 Bucket

- s3 bucket: name/Company-Upload

---

### SFTP AppStream-Server

ssh keys rsa

- SSH private key:

  - Currently built into AppStream image via Image Builder - saved to the windows AppStream Image so the solo user "Ontology" (that has the SSH public key configured) can be used by each Ontologist to access the customer's files via FileZilla.

- SSH public key:

- s3 bucket: name/homefolder-name

---

### Custom DNS for SFTP

>*I recently set up the DNS - Route 53

Hosted Zone: sftp.xsell.io

Record: client.sftp.xsell.io - **I'd like to change this**

for use by all new client uploads, since then we have changed the standard naming/tagging to use customer instead of client for referring to a new contract.

>_I need to change this - especially when we migrate to new accounts._

---

## Applications

There are a variaty of Windows applications that we use in AppStream to create the virtual desktop for the varying teams.

These Applictions include:

- **FileZilla** _Ontology, Annotation_

- **Jupyter_Notebook_(Anaconda3)** _Ontology, DataScience_

- **Scalc** _Ontology_

- **VLC** _Ontology, Annotation_

- **Chrome** _Ontology, Annotation, Data Science_

- **Audacity** _Ontology, Annotation, Data Science_

- **Drive Mapping** _Ontology, Annotation_

- **pgAdmin4** _Ontology, Data Science_

- **DBeaver** _Ontology_

- **LibreOffice 6.3** _Annotation, Data Science_

- **draw.io** _Data Science_

- **Powershell** _Data Science_

---

## Ontology

- FileZilla: server/username/password
- Jupyter_Notebook_(Anaconda3) Display: Jupyter Notebook (Anaconda3)
  - Launch Parameter: C:\ProgramData\Anaconda3\cwp.py C:\ProgramData\Anaconda3 C:\ProgramData\Anaconda3\python.exe C:\ProgramData\Anaconda3\Scripts\jupyter-notebook-script.py "%USERPROFILE%/"

-Scalc Display:

- OpenOffice Calc/LibreOffice

-VLC:

- VLC Media Player

-Chrome

-Audacity

-Drive_Mapping

-pgAdmin4

-DBeaver

- Display Name: DBeaverSQL

---

## Annotation

-Chrome

-VLC

-Audacity

-LibreOffice 6.3

-Drive_Mapping

---

## Data Science

-Chrome

-Audacity

-draw.io

-LibreOffice

-pgAdmin4

-Powershell

- Display Name: Start AutoML
- Launch Parameter: C:\scripts\start_jupyter_lab.ps1
- Python3/pip 

---

### Access Groups

??

What do we do with all the old sftp servers and uploaded data, especially accounts like verizon - we have 4 sftp servers set up for them in retail.


### Fixes

If a user in the userpool is not receiving invite emails to new stacks, run this command from the CLI.
_you cannot delete users from the userpool console_

  ➜  ~ aws appstream delete-user --user-name $FIRST.$LAST@xselltechnologies.com --authentication-type USERPOOL --region us-west-2

Make sure your profile in the CLI is set to the correct region.

