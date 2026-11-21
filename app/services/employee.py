from sqlalchemy.orm import Session
from app.models.employee import Employee
from app.schemas.employee import EmployeeCreate, EmployeeUpdate


# CREATE
def create_employee(db: Session, employee: EmployeeCreate):

    db_employee = Employee(**employee.model_dump())

    db.add(db_employee)
    db.commit()
    db.refresh(db_employee)

    return db_employee


# READ ALL
def get_employees(db: Session):

    return db.query(Employee).all()


# READ BY ID
def get_employee(db: Session, employee_id: int):

    return db.query(Employee).filter(
        Employee.id == employee_id
    ).first()


# UPDATE
def update_employee(
    db: Session,
    employee_id: int,
    employee: EmployeeUpdate
):

    db_employee = get_employee(db, employee_id)

    if db_employee is None:
        return None

    for key, value in employee.model_dump().items():
        setattr(db_employee, key, value)

    db.commit()
    db.refresh(db_employee)

    return db_employee


# DELETE
def delete_employee(db: Session, employee_id: int):

    db_employee = get_employee(db, employee_id)

    if db_employee is None:
        return None

    db.delete(db_employee)
    db.commit()

    return db_employee