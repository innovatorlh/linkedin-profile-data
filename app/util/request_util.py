import requests

from util.env_properties_info import CONFIG_PERSONAL_EMAIL_API_ENDPOINT,CONFIG_PERSONAL_CONTACT_NUMBER_API_ENDPOINT,CONFIG_API_TOKEN


AUTH_HEADER = {'Authorization': 'Bearer ' + CONFIG_API_TOKEN}


def get_personal_email_data( linkedin_profile):
    params = {'email_validation': 'include', 'linkedin_profile_url': linkedin_profile, }
    emails_data = dict()
    response = requests.get(CONFIG_PERSONAL_EMAIL_API_ENDPOINT, params=params, headers=AUTH_HEADER)
    if response.status_code == 200:
        data = response.json()
        emails_data["emails"] = data["emails"]
    elif response.status_code == 404:
        emails_data["emails"] = []
    else:
        print("unable to process given emails request.profile_url=", linkedin_profile, " status code=", response.status_code)
    emails_data["api_status"] = response.status_code
    return emails_data


def get_personal_contact_number_data(lnkedin_profile):
    params = {'linkedin_profile_url': lnkedin_profile, }
    contact_numbers_data = dict()
    response = requests.get(CONFIG_PERSONAL_CONTACT_NUMBER_API_ENDPOINT, params=params, headers=AUTH_HEADER)
    if response.status_code == 200:
        data = response.json()
        contact_numbers_data["phone_numbers"] = data["numbers"]
    elif response.status_code == 404:
        contact_numbers_data["phone_numbers"] = []
    else:
        print("unable to process given phone numbers request. profile_url=", lnkedin_profile, " status code=",
              response.status_code)
    contact_numbers_data["api_status"] = response.status_code
    return contact_numbers_data

