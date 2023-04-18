# AppStream Implementation

This document describes the process of building an AppStream environment for Ontology, Annotation, and DataScience.
We create an AppStream instance per client, with secure access to customer data for the Ontology team, access to the annotation tool via https and specific security groups.
The DataScience team has similar access to their tools through limited https.

Windows applications specified below are downloaded to the base image of an AppStream Instance.'
Currently we set up the AppStream environment from the aws console - but one is able to use script and the CLI to create a new image/fleet/stack.

This AppStream has been built for OPTUS, in the ap-southeast-2 region - as requested by the customer.

The Details

Customer: Optus

AWS Account: xsell-devops-shared-services/optus-staging

Region: Asian Pacific (Sydney) ap-southeast-2

## Setup

1. In the left side menu, select images and navigate to the Image Builder. Select the image that best supports the Ontology, Annotation, and DS needs. Next scroll to the bottom and select create.

>_when done building the image, make yout to 'stop' the image-builder instance! AWS charges by the hour for 'running' image-builders, even when not in use._
Image

**AppStream-WinServer2019-10-08-2021**
Platform: Microsoft Windows Server 2019 Base
Description: AppStream image for launching image builder instances
Display Name: AppStream-WinServer2019-10-08-2021
Visibility: Public
Owner: AWS
Instance Family: General Purpose, Compute Optimized, Memory Optimized
Apps Included : None
AppStream 2.0 agent version: 08-02-2021 ( LATEST )
Dynamic application providers: Disabled

Name: Optus-AppStream-Image-Builder-v1

Display Name: Optus-AppStream-Image-Builder-v1

Tags:

env:stage
customer:optus
created_by:sarah.rourke
product:hiper
application:appstream
component:
managed:false
description:Image:Image builder for the first version of optus appstream
expires:
purpose:desktop-environment

Instance Type: Compute Optimized - stream.compute.large

---

### Network

VPC:
  optus_staging_vpc
  vpc-*
CIDR: 

optus_stagin_private_subnet_0: subnet-*
IPv4: *.*.*.*/24

Security-group: xsdv-optus-appstream-annotation-access
Description: Allow AppStream Desktop to have access to Azure hosted Annotation tool
VPC: vpc-*

  inbound rules: DNS(TCP) port 53 source: **.**.**.***/32 annotation.az.hiper.io
<!-- appstream is not accessible for my role in devops-shared-services, will need to fill in this information at a later date. -->

### Applications

- Chrome
- FileZilla
- Powershell
  - Launch Parameter: C:\scripts\start_jupyter_lab.ps1
- Jupyter_Notebook_(Anaconda3)
- draw.io
- VLC
- Python3
  - pip
- dbeaver
- LibreOffice
- pgAdmin4
- Start AutoML
- Audacity
- Scalc (OpenOffice)