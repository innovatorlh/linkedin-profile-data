
from util.request_util import get_personal_email_data, get_personal_contact_number_data


def get_personal_email_service(linkedin_profile):
    personal_email_data = get_personal_email_data(linkedin_profile)
    for i in range(3):
        print("api status is 429 hence retrying...")
        if personal_email_data["api_status"] != 429:
            break
    return personal_email_data


def get_personal_phone_number_service(linkedin_profile):
    personal_phone_number_data = get_personal_contact_number_data(linkedin_profile)
    for i in range(3):
        print("api status is 429 hence retrying...")
        if personal_phone_number_data["api_status"] != 429:
            break
    return personal_phone_number_data


def get_personal_email_phone_number_service(linkedin_profile):
    personal_email_data = get_personal_email_data(linkedin_profile)
    for i in range(3):
        print("api status is 429 hence retrying...")
        if personal_email_data["api_status"] != 429:
            break
    personal_phone_number_data = get_personal_contact_number_data(linkedin_profile)
    for i in range(3):
        print("api status is 429 hence retrying...")
        if personal_phone_number_data["api_status"] != 429:
            break
    return {
        "profile_url": linkedin_profile,
        "emaildata": personal_email_data,
        "phone_number_data": personal_phone_number_data,
    }
