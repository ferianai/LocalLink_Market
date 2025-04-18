from models.user import Users
from instance.database import db
from shared import crono


def create_user(data, hashed_password):
    new_user = Users(
        username=data.username,
        first_name=data.first_name,
        last_name=data.last_name,
        email=data.email,
        phone=data.phone,
        password_hash=hashed_password,
        date_of_birth=data.date_of_birth,
        address=data.address,
        city=data.city,
        state=data.state,
        country=data.country,
        zip_code=data.zip_code,
        image_url=data.image_url,
        role=data.role,
        bank_account=data.bank_account,
        bank_name=data.bank_name,
        is_active=True,
        created_at=crono.now(),
        updated_at=crono.now(),
    )
    db.session.add(new_user)
    db.session.commit()
    return new_user
