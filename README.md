# Cisco Intersight

Cisco Intersight is a cloud operations platform that delivers intelligent visualization, optimization, and orchestration for applications and infrastructure across your hybrid environment. With Intersight, you get all of the benefits of SaaS delivery and full lifecycle management of distributed Intersight-connected servers and third-party storage across data centers, remote sites, branch offices, and edge environments. This empowers you to analyze, update, fix, and automate your environment in ways that were not possible with prior generations’ tools. As a result, your organization can achieve significant TCO savings and deliver applications faster in support of new business initiatives.

The Cisco Intersight API is a programmatic interface that uses the REST architecture to provide access to the Intersight Management Information Model. The Intersight Python SDK is generated based on the Cisco Intersight OpenAPI 3.x specification. The latest specification can be downloaded from [here](https://intersight.com/apidocs/downloads/). The Cisco Intersight Python SDK is updated frequently to be in sync with the OpenAPI version deployed at https://intersight.com




# Getting Started

1. [ Installation ](#installation)

    1.1. [ Requirements ](#requirements)

    1.2. [ Install ](#install)

2. [ Authentication ](#authentication)
3. [ Creating an Object ](#creating-an-object)
4. [ Creating an Object from JSON ](#creating-an-object-from-json)
5. [ Reading Objects ](#reading-an-object)

    5.1. [ Reading Objects Using a Filter ](#reading-an-object-using-a-filter)

6. [ Updating Objects ](#updating-an-object)
7. [ Deleting Objects ](#deleting-an-object)
8. [ Examples](#examples)

    8.1. [ Example - Server Configuration ](#server-configuration)

    8.2. [ Example - Firmware Upgrade ](#firmware-upgrade)

    8.3. [ Example - OS Install ](#os-install)

9. [ Targets ](#targets)

    9.1. [ Claiming a Target ](#claiming-a-target)

    9.2. [ Unclaiming a Target ](#unclaiming-a-target)

    9.3. [ Claiming an Appliance ](#claiming-an-appliance)

10. [ Triggering a Workflow ](#triggering-a-workflow)
11. [ Monitoring a Workflow ](#monitoring-a-workflow)
12. [ Debugging ](#debugging)





<a name="installation"></a>
## 1. Installation

<a name="requirements"></a>
### 1.1. Requirements

- Python >= 3.6

<a name="install"></a>
### 1.2. Install

- The latest intersight package can be installed using one of the following, 
    `pip install intersight`

    `pip install git+https://github.com/CiscoDevNet/intersight-python`

    `python setup.py install --user`

<a name="authentication"></a>

## 2. Authentication

- Start with creating an API Client object by specifying an API Key and an API Secret file path.
- This method also specifies which endpoint will the client connect to.
- There is no explicit login when using API Client and Secret. Every message carries the information required for authentication.

```python
import intersight
import re
import sys


def get_api_client(api_key_id, api_secret_file = None, private_key_string = None, proxy = None, endpoint="https://intersight.com"):
    if api_secret_file is None and private_key_string is None:
        print("Either api_secret_file or private_key_string is required to create api client")
        sys.exit(1)
    if api_secret_file is not None and private_key_string is not None:
        print("Please provide only one among api_secret_file or private_key_string")
        sys.exit(1)

    if api_secret_file is not None: 
        with open(api_secret_file, 'r') as f:
            api_key = f.read()
    else:
        api_key = private_key_string

    if re.search('BEGIN RSA PRIVATE KEY', api_key):
        # API Key v2 format
        signing_algorithm = intersight.signing.ALGORITHM_RSASSA_PKCS1v15
        
    elif re.search('BEGIN EC PRIVATE KEY', api_key):
        # API Key v3 format
        signing_algorithm = intersight.signing.ALGORITHM_ECDSA_MODE_DETERMINISTIC_RFC6979
    
    configuration = intersight.Configuration(
        host=endpoint,
        signing_info=intersight.signing.HttpSigningConfiguration(
            key_id=api_key_id,
            private_key_string = api_key,
            signing_scheme=intersight.signing.SCHEME_HS2019,
            signing_algorithm=signing_algorithm,
            hash_algorithm=intersight.signing.HASH_SHA256,
            signed_headers=[
                intersight.signing.HEADER_REQUEST_TARGET,
                intersight.signing.HEADER_HOST,
                intersight.signing.HEADER_DATE,
                intersight.signing.HEADER_DIGEST,
            ]
        )
    )
    # if you want to turn off certificate verification
    # configuration.verify_ssl = False

    # setting proxy
    if proxy is not None and proxy != "":
        configuration.proxy = proxy

    return intersight.ApiClient(configuration)
```

Once an API Client is created, it can be used to communicate with the Intersight server.
```python

from intersight.api import boot_api
from intersight.model.boot_precision_policy import BootPrecisionPolicy


api_client = get_api_client("api_key", "~/api_secret_file_path")

# Create an api instance of the correct API type
api_instance = boot_api.BootApi(api_client)

# Create an object locally and populate the object properties
boot_precision_policy = BootPrecisionPolicy()


# Create an object in Intersight
api_response = api_instance.create_boot_precision_policy(boot_precision_policy)    
```

Creating API Client with proxy and using it to communicate with the Intersight server.
```python
from intersight.api import boot_api
from intersight.model.boot_precision_policy import BootPrecisionPolicy

api_key_id = "your api_key_id"
api_secret_file = "path to your api secret file"
proxy = "your proxy"
# Creating API Client with proxy
api_client = get_api_client(api_key_id,
                            api_secret_file = api_secret_file
                            proxy = proxy)

# Create an api instance of the correct API type
api_instance = boot_api.BootApi(api_client)

# Create an object locally and populate the object properties
boot_precision_policy = BootPrecisionPolicy()


# Create an object in Intersight
api_response = api_instance.create_boot_precision_policy(boot_precision_policy)
```


<a name="creating-an-object"></a>
## 3. Creating an Object

This step helps user to create an object with the help of python intersight SDK.
In the below example we are going to create a boot precision policy.
First the instance of Model: BootPrecisionPolicy is created and then all the attributes
required to create the policy is set using the model object.

```python
from intersight.api import boot_api
from intersight.model.boot_precision_policy import BootPrecisionPolicy
from intersight.model.boot_device_base import BootDeviceBase
from intersight.model.organization_organization_relationship import OrganizationOrganizationRelationship
from pprint import pprint
import intersight

api_key = "api_key"
api_key_file = "~/api_key_file_path"

api_client = get_api_client(api_key, api_key_file)


def create_boot_local_cdd():
    # Creating an instance of boot_local_cdd
    boot_local_cdd = BootDeviceBase(class_id="boot.LocalCdd",
                                    object_type="boot.LocalCdd",
                                    name="local_cdd1",
                                    enabled=True)
    return boot_local_cdd


def create_boot_local_disk():
    # Creating an instance of boot_local_disk
    boot_local_disk = BootDeviceBase(class_id="boot.LocalDisk",
                                     object_type="boot.LocalDisk",
                                     name="local_disk1",
                                     enabled=True)
    return boot_local_disk


def create_organization():
    # Creating an instance of organization
    organization = OrganizationOrganizationRelationship(class_id="mo.MoRef",
                                                        object_type="organization.Organization")

    return organization


# Create an instance of the API class.
api_instance = boot_api.BootApi(api_client)

# Create an instance of local_cdd, local_disk, organization and list of boot_devices.
boot_local_cdd = create_boot_local_cdd()
boot_local_disk = create_boot_local_disk()
organization = create_organization()
boot_devices = [
    boot_local_disk,
    boot_local_cdd,
]

# BootPrecisionPolicy | The 'boot.PrecisionPolicy' resource to create.
boot_precision_policy = BootPrecisionPolicy()

# Setting all the attributes for boot_precison_policy instance.
boot_precision_policy.name = "sample_boot_policy1"
boot_precision_policy.description = "sample boot precision policy"
boot_precision_policy.boot_devices = boot_devices
boot_precision_policy.organization = organization

# example passing only required values which don't have defaults set
try:
    # Create a 'boot.PrecisionPolicy' resource.
    api_response = api_instance.create_boot_precision_policy(boot_precision_policy)
    pprint(api_response)
except intersight.ApiException as e:
    print("Exception when calling BootApi->create_boot_precision_policy: %s\n" % e)
```

<a name="creating-an-object-from-json"></a>
## 4. Creating an Object from JSON

This step helps user to create an object with the help of python intersight SDK.
In the below example we are going to create a boot precision policy.
The program will parse the input json file to fetch the json payload and use this data.
The instance of Model: BootPrecisionPolicy is created using parsed json data is as a keyword arguement.

Start with creating a json file contain the data which will be used to create boot precision policy.
Create a file data.json with the following content:

`data.json:`
```json
{
  "Name":"sample_boot_policy1",
  "ObjectType":"boot.PrecisionPolicy",
  "ClassId":"boot.PrecisionPolicy",
  "Description":"Create boot precision policy.",
  "BootDevices":[
     {
        "ClassId":"boot.LocalCdd",
        "ObjectType":"boot.LocalCdd",
        "Enabled":true,
        "Name":"local_cdd"
     },
     {
        "ClassId":"boot.LocalDisk",
        "ObjectType":"boot.LocalDisk",
        "Enabled":true,
        "Name":"local_disk"
     }
  ],
  "Organization":{
     "ObjectType":"organization.Organization",
     "ClassId":"mo.MoRef"
  }
}
```

```python
import json
from intersight.api import boot_api
from intersight.model.boot_precision_policy import BootPrecisionPolicy
from intersight.model.boot_device_base import BootDeviceBase
from intersight.model.organization_organization_relationship import OrganizationOrganizationRelationship
from pprint import pprint
import intersight

api_key = "api_key"
api_key_file = "~/api_key_file_path"

api_client = get_api_client(api_key, api_key_file)


# Create an instance of the API class.
api_instance = boot_api.BootApi(api_client)

data_json_file_path = "data.json"
with open(data_json_file_path, "r") as json_data_file:
    json_data = json_data_file.read()

# Loading the json objects into python dictionary.
data = json.loads(json_data)

# BootPrecisionPolicy | The 'boot.PrecisionPolicy' resource to create.
boot_precision_policy = BootPrecisionPolicy(**data, _spec_property_naming=True,
                                            _configuration=api_client.configuration)

# example passing only required values which don't have defaults set
try:
    # Create a 'boot.PrecisionPolicy' resource.
    api_response = api_instance.create_boot_precision_policy(boot_precision_policy)
    pprint(api_response)
except intersight.ApiException as e:
    print("Exception when calling BootApi->create_boot_precision_policy: %s\n" % e)
```

<a name="reading-an-object"></a>
## 5. Reading Objects

This step helps user to read an object with the help of python intersight SDK.
In the below example we are going to read all the results for boot precision policy.

```python
from intersight.api import boot_api
from pprint import pprint
import intersight

api_key = "api_key"
api_key_file = "~/api_key_file_path"

api_client = get_api_client(api_key, api_key_file)


# Create an instance of the API class
api_instance = boot_api.BootApi(api_client)

# example passing only required values which don't have defaults set
# and optional values
try:
    # Read a 'boot.PrecisionPolicy' resource.
    api_response = api_instance.get_boot_precision_policy_list()
    pprint(api_response)
except intersight.ApiException as e:
    print("Exception when calling BootApi->get_boot_precision_policy_list: %s\n" % e)
```

<a name="reading-an-object-using-a-filter"></a>
### 5.1. Reading Objects Using a Filter

Intersight supports oData query format to return a filtered list of objects.
An example is shown below. Here we filter devices that are in connected state.

```python
from intersight.api import asset_api

api_key = "api_key"
api_key_file = "~/api_key_file_path"

api_client = get_api_client(api_key, api_key_file)
asset_api = asset_api.AssetApi(api_client)
 
kwargs = dict(filter="ConnectionStatus eq 'Connected'")

# Get all device registration objects that are in connected state
api_result= api.get_asset_device_registration_list(**kwargs)
for device in api_result.results:
    print(device.device_ip_address[0])
```

<a name="updating-an-object"></a>
## 6. Updating Objects

This step helps user to update an object with the help of python intersight SDK.
In the below example we are going to update a boot precision policy.
First the instance of Model: BootPrecisionPolicy is created and then all the attributes
required to update the policy is set using the model object.

The read object operation is performed to fetch:
- Moid associated to boot precision policy.
- Moid associated to organization to update the appropriate fields.

In our example the first result of the response is updated i.e. first entry among all the entries for boot precision policy is updated.

```python
from intersight.api import boot_api
from intersight.model.boot_precision_policy import BootPrecisionPolicy
from intersight.model.boot_device_base import BootDeviceBase
from intersight.model.organization_organization_relationship import OrganizationOrganizationRelationship
from pprint import pprint
import intersight

api_key = "api_key"
api_key_file = "~/api_key_file_path"

api_client = get_api_client(api_key, api_key_file)


def create_boot_sdcard():
    # Creating an instance of boot_hdd_device
    boot_sdcard = BootDeviceBase(class_id="boot.SdCard",
                                 object_type="boot.SdCard",
                                 name="sdcard1",
                                 enabled=True)
    return boot_sdcard


def create_boot_iscsi():
    # Creating an instance of boot_iscsi
    boot_iscsi = BootDeviceBase(class_id="boot.Iscsi",
                                object_type="boot.Iscsi",
                                name="iscsi1",
                                enabled=True)
    return boot_iscsi


def create_boot_pxe():
    # Creating an instance of boot_pxe
    boot_pxe = BootDeviceBase(class_id="boot.Pxe",
                              object_type="boot.Pxe",
                              name="pxe1",
                              enabled=True,
                              interface_name="pxe1")
    return boot_pxe


def get_boot_precision_policy(api_client):
    # Enter a context with an instance of the API client
    with api_client:
        # Create an instance of the API class
        api_instance = boot_api.BootApi(api_client)

        # example passing only required values which don't have defaults set
        # and optional values
        try:
            # Read a 'boot.PrecisionPolicy' resource.
            api_response = api_instance.get_boot_precision_policy_list()
        except intersight.ApiException as e:
            print("Exception when calling BootApi->get_boot_precision_policy_list: %s\n" % e)
    return api_response


def create_organization(moid):
    # Creating an instance of organization
    organization = OrganizationOrganizationRelationship(class_id="mo.MoRef",
                                                        object_type="organization.Organization",
                                                        moid=moid)

    return organization


# Create an instance of the API class.
api_instance = boot_api.BootApi(api_client)

# Getting the response for existing object.
response = get_boot_precision_policy(api_client)

# Handling error scenario if get_boot_precision_policy does not return any entry.
if not response.results:
    raise NotFoundException(reason="The response does not contain any entry for boot precision policy. "
                                   "Please create a boot precision policy and then update it.")

# Fetch the organization Moid and boot precision policy moid from the Result's first entry.
organization_moid = response.results[0].organization['moid']
moid = response.results[0].moid

# Create an instance of hdd_device, iscsi, pxe, organization and list of boot_devices.
boot_hdd_device = create_boot_sdcard()
boot_iscsi = create_boot_iscsi()
boot_pxe = create_boot_pxe()
organization = create_organization(organization_moid)
boot_devices = [
    boot_hdd_device,
    boot_iscsi,
    boot_pxe,
]

# BootPrecisionPolicy | The 'boot.PrecisionPolicy' resource to create.
boot_precision_policy = BootPrecisionPolicy()

# Setting all the attributes for boot_precison_policy instance.
boot_precision_policy.name = "updated_boot_policy1"
boot_precision_policy.description = "Updated boot precision policy"
boot_precision_policy.boot_devices = boot_devices
boot_precision_policy.organization = organization

# example passing only required values which don't have defaults set
try:
    # Update a 'boot.PrecisionPolicy' resource.
    api_response = api_instance.update_boot_precision_policy(
        boot_precision_policy=boot_precision_policy,
        moid=moid)
    pprint(api_response)
except intersight.ApiException as e:
    print("Exception when calling BootApi->update_boot_precision_policy: %s\n" % e)
```

<a name="deleting-an-object"></a>
## 7. Deleting Objects

This step helps user to delete an object with the help of python intersight SDK.
In the below example we are going to delete a boot precision policy.
The read object operation is performed to fetch:
- Moid associated to boot precision policy.

In our example the first result of the response is deleted i.e. first entry among all the entries for boot precision policy is deleted.

```python
from intersight.api import boot_api
from intersight.exceptions import NotFoundException
from pprint import pprint
import intersight

api_key = "api_key"
api_key_file = "~/api_key_file_path"

api_client = get_api_client(api_key, api_key_file)


def get_boot_precision_policy(api_client):
    # Enter a context with an instance of the API client
    with api_client:
        # Create an instance of the API class
        api_instance = boot_api.BootApi(api_client)

        # example passing only required values which don't have defaults set
        # and optional values
        try:
            # Read a 'boot.PrecisionPolicy' resource.
            api_response = api_instance.get_boot_precision_policy_list()
        except intersight.ApiException as e:
            print("Exception when calling BootApi->get_boot_precision_policy_list: %s\n" % e)
    return api_response


# Create an instance of the API class
api_instance = boot_api.BootApi(api_client)

# Getting the response for existing object.
response = get_boot_precision_policy(api_client)

# Handling error scenario if get_boot_precision_policy does not return any entry.
if not response.results:
    raise NotFoundException(reason="The response does not contain any entry for boot precision policy. "
                                   "Please create a boot precision policy and then delete it.")

# Fetching the moid from the Result's first entry.
moid = response.results[0].moid

# example passing only required values which don't have defaults set
try:
    # Delete a 'boot.PrecisionPolicy' resource.
    api_instance.delete_boot_precision_policy(moid)
    print(f"Deletion for moid: %s was successful" % moid)
except intersight.ApiException as e:
    print("Exception when calling BootApi->delete_boot_precision_policy: %s\n" % e)
```

<a name="examples"></a>
## 8. Examples

<a name="server-configuration"></a>
### 8.1. Example: Server Configuration
Please refer [Server Configuration](https://github.com/cisco-intersight/intersight_python_examples/blob/main/examples/server_configuration/server_configuration.py)

<a name="firmware-upgrade"></a>
### 8.2. Example: Firmware Upgrade
Please refer [Direct Firmware Upgrade](https://github.com/cisco-intersight/intersight_python_examples/blob/main/examples/firmware_upgrade/firmware_upgrade_direct.py)

Please refer [Network Firmware Upgrade](https://github.com/cisco-intersight/intersight_python_examples/blob/main/examples/firmware_upgrade/firmware_upgrade_network.py)


<a name="os-install"></a>
### 8.3. Example: OS Install
Please refer [OS Install](https://github.com/cisco-intersight/intersight_python_examples/blob/main/examples/os_install/os_install.py)


<a name="targets"></a>
## 9. Targets

<a name="claiming-a-target"></a>
### 9.1. Claiming a Target

```python
from intersight.api import asset_api
from intersight.model.asset_device_claim import AssetDeviceClaim
from pprint import pprint
import intersight

api_key = "api_key"
api_key_file = "~/api_key_file_path"

api_client = get_api_client(api_key, api_key_file)

api_instance = asset_api.AssetApi(api_client)

# AssetTarget | The 'asset.Target' resource to create.
asset_target = AssetDeviceClaim()

# setting claim_code and device_id
asset_target.security_token = "2Nxxx-int"
asset_target.serial_number = "WZPxxxxxFMx"


# Post the above payload to claim a target
try:
    # Create a 'asset.Target' resource.
    claim_resp = api_instance.create_asset_device_claim(asset_target)
    pprint(claim_resp)
except intersight.ApiException as e:
    print("Exception when calling AssetApi->create_asset_device_claim: %s\n" % e)
```

<a name="unclaiming-a-target"></a>
### 9.2. Unclaiming a Target

```python
from intersight.api import asset_api
import intersight

api_key = "api_key"
api_key_file = "~/api_key_file_path"

api_client = get_api_client(api_key, api_key_file)

api_instance = asset_api.AssetApi(api_client)

# To find out all the connected devices.
kwargs = dict(filter="ConnectionStatus eq 'Connected'")

# Get all registered target.
api_result= api.get_asset_device_registration_list(**kwargs)

try:
    for device in api_result.results:
        # You need to provide the IP address of the target, you need to unclaim
        if "10.10.10.10" in device.device_ip_address:
            # Deleting the target as the same we do through api
            api_instance.delete_asset_device_claim(moid=device.device_claim.moid)
except intersight.ApiException as e:
    print("Exception when calling AssetApi->delete_asset_device_claim: %s\n" % e)
```

<a name="claiming-an-appliance"></a>
### 9.3. Claiming an Appliance

```python
from intersight.api import asset_api
from intersight.model.asset_target import AssetTarget
from pprint import pprint
import intersight

api_key = "api_key"
api_key_file = "~/api_key_file_path"

api_client = get_api_client(api_key, api_key_file)

api_instance = asset_api.AssetApi(api_client)

# ApplianceDeviceClaim | The 'appliance.DeviceClaim' resource to create.
appliance_device_claim = ApplianceDeviceClaim()

# setting claim_code and device_id
appliance_device_claim.username = "user1"
appliance_device_claim.password = "ChangeMe"
appliance_device_claim.hostname = "host1"
appliance_device_claim.platform_type = "UCSD"


# Post the above payload to claim a target
try:
    # Create a 'appliance.DeviceClaim' resource.
    claim_resp = api_instance.create_appliance_device_claim(appliance_device_claim)
    pprint(claim_resp)
except intersight.ApiException as e:
    print("Exception when calling AssetApi->create_appliance_device_claim: %s\n" % e)
```

<a name="triggering-a-workflow"></a>
## 10. Example : Triggering a Workflow
Please refer [Triggering a Workflow](https://github.com/cisco-intersight/intersight_python_examples/blob/main/examples/workflow/triggering_workflow.py)

<a name="monitoring-a-workflow"></a>
## 11. Example : Monitoring a Workflow
Please refer [Monitoring a Workflow](https://github.com/cisco-intersight/intersight_python_examples/blob/main/examples/workflow/monitoring_workflow.py)

<a name="debugging"></a>
## 12. Debugging

