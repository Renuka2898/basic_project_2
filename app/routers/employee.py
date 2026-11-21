from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.connection import get_db
from app.schemas.employee import EmployeeCreate, EmployeeUpdate, EmployeeResponse
from app.services import employee as employee_service


router = APIRouter(
    prefix="/employees",
    tags=["Employee CRUD"]
)


# CREATE
@router.post("/", response_model=EmployeeResponse)
def create_employee(
    employee: EmployeeCreate,
    db: Session = Depends(get_db)
):
    return employee_service.create_employee(db, employee)


# READ ALL
@router.get("/", response_model=list[EmployeeResponse])
def get_employees(db: Session = Depends(get_db)):
    return employee_service.get_employees(db)


# READ BY ID
@router.get("/{employee_id}", response_model=EmployeeResponse)
def get_employee(
    employee_id: int,
    db: Session = Depends(get_db)
):
    employee = employee_service.get_employee(db, employee_id)

    if employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")

    return employee


# UPDATE
@router.put("/{employee_id}", response_model=EmployeeResponse)
def update_employee(
    employee_id: int,
    employee: EmployeeUpdate,
    db: Session = Depends(get_db)
):
    updated_employee = employee_service.update_employee(
        db, employee_id, employee
    )

    if updated_employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")

    return updated_employee


# DELETE
@router.delete("/{employee_id}")
def delete_employee(
    employee_id: int,
    db: Session = Depends(get_db)
):
    deleted_employee = employee_service.delete_employee(db, employee_id)

    if deleted_employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")

    return {"message": "Employee deleted successfully"}