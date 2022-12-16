from fastapi import FastAPI

from service.profile_service import get_personal_email_service, get_personal_phone_number_service, \
    get_personal_email_phone_number_service

app = FastAPI()


@app.get("/personalemail/{linkedin_profile}")
def get_personal_email(linkedin_profile: str):
    return get_personal_email_service(linkedin_profile)


@app.get("/personalphone/{linkedin_profile}")
def get_personal_phone_number(linkedin_profile: str):
    return get_personal_phone_number_service(linkedin_profile)


@app.get("/personalphoneemail/{linkedin_profile}")
def get_personal_email_phone_number(linkedin_profile: str):
    return get_personal_email_phone_number_service(linkedin_profile)
